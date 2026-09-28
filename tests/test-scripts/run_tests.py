import os
import sys
import time
import argparse
from datetime import datetime

# Cho phép chạy script từ bất kỳ thư mục nào
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from playwright.sync_api import sync_playwright
from test_data import ALL_TEST_CASES

BUILD_DESCRIPTIONS = {
    "0": "Prototype (Works perfectly)",
    "1": "Build 1 (Doesn't check for valid numbers)",
    "2": "Build 2 (Add and Concatenate swapped)",
    "3": "Build 3 (Always treats like a number)",
    "4": "Build 4 (Locked on integer)",
    "5": "Build 5 (Clear button unavailable)",
    "6": "Build 6 (Divide by zero not checked)",
    "7": "Build 7 (Uses previous answer as first operand)",
    "8": "Build 8 (Switches number 1 and 2 around)",
}

OP_MAP = {
    "Add": "0",
    "Subtract": "1",
    "Multiply": "2",
    "Divide": "3",
    "Concatenate": "4",
}

def wait_for_calculation(page, max_wait_ms=2000):
    """Đợi quá trình calculating hoàn tất hoặc có thông báo lỗi xuất hiện"""
    start_time = time.time()
    while (time.time() - start_time) * 1000 < max_wait_ms:
        # Nếu có thông báo lỗi hiển thị (ví dụ Divide by zero error!) thì dừng đợi ngay
        err = page.inner_text("#errorMsgField").strip()
        if err:
            break
        # Nếu nút Calculate đã active trở lại và calculatingForm đã ẩn
        is_disabled = page.is_disabled("#calculateButton")
        is_calc_hidden = page.is_hidden("#calculatingForm")
        if not is_disabled and is_calc_hidden:
            break
        page.wait_for_timeout(100)
    page.wait_for_timeout(200)

def run_single_test(page, tc):
    """Thực thi một test case cụ thể trên giao diện"""
    action = tc.get("action", "calculate")
    num1 = tc.get("num1", "")
    num2 = tc.get("num2", "")
    op_name = tc.get("operation", "Add")
    op_val = OP_MAP.get(op_name, "0")
    int_only = tc.get("integers_only", False)
    expected_ans = str(tc.get("expected_answer", ""))
    expected_err = str(tc.get("expected_error", ""))

    try:
        # 1. Đặt lại form về trạng thái sạch trước khi test
        # QUAN TRỌNG: Web app có bug ở case divide by zero không gọi unlockCalculate(), khiến spinner xoay mãi mãi.
        # Ta ép gọi unlockCalculate() để mở khóa giao diện cho test case tiếp theo.
        page.evaluate("""() => {
            if (typeof unlockCalculate === 'function') unlockCalculate();
            if (typeof clearAnswer === 'function') clearAnswer();
            if (typeof selectedBuild !== 'undefined' && selectedBuild == 5) {
                var cb = document.getElementById('clearButton');
                if (cb) cb.disabled = true;
            }
        }""")
        page.fill("#number1Field", "")
        page.fill("#number2Field", "")

        # 2. Xử lý theo từng loại action
        if action == "just_clear":
            if num1: page.fill("#number1Field", str(num1))
            if num2: page.fill("#number2Field", str(num2))
            is_disabled = page.is_disabled("#clearButton")
            if is_disabled:
                return {
                    "result": "Fail",
                    "note": "Clear button bị disabled (không thể bấm)",
                    "actual_answer": "",
                    "actual_error": "Clear button disabled",
                }
            page.click("#clearButton", timeout=3000)
            ans = page.input_value("#numberAnswerField")
            err = page.inner_text("#errorMsgField").strip()
            passed = (ans == expected_ans) and (expected_err in err if expected_err else not err)
            return {
                "result": "Pass" if passed else "Fail",
                "note": f"Answer='{ans}', Error='{err}'",
                "actual_answer": ans,
                "actual_error": err,
            }

        elif action == "calculate_then_clear":
            page.select_option("#selectOperationDropdown", op_val)
            if page.is_visible("#integerSelect") and not page.is_disabled("#integerSelect"):
                page.set_checked("#integerSelect", int_only)
            page.fill("#number1Field", str(num1))
            page.fill("#number2Field", str(num2))
            page.click("#calculateButton", timeout=3000)
            wait_for_calculation(page)
            if page.is_disabled("#clearButton"):
                return {
                    "result": "Fail",
                    "note": "Clear button bị disabled sau khi tính toán",
                    "actual_answer": page.input_value("#numberAnswerField"),
                    "actual_error": page.inner_text("#errorMsgField").strip(),
                }
            page.click("#clearButton", timeout=3000)
            ans = page.input_value("#numberAnswerField")
            err = page.inner_text("#errorMsgField").strip()
            passed = (ans == expected_ans) and (expected_err in err if expected_err else not err)
            return {
                "result": "Pass" if passed else "Fail",
                "note": f"Sau Clear: Answer='{ans}', Error='{err}'",
                "actual_answer": ans,
                "actual_error": err,
            }

        elif action == "clear_multiple_times":
            page.fill("#number1Field", str(num1))
            page.fill("#number2Field", str(num2))
            page.click("#calculateButton", timeout=3000)
            wait_for_calculation(page)
            if page.is_disabled("#clearButton"):
                return {"result": "Fail", "note": "Clear button bị disabled", "actual_answer": "", "actual_error": "Clear disabled"}
            page.click("#clearButton", timeout=3000)
            page.click("#clearButton", timeout=3000)
            ans = page.input_value("#numberAnswerField")
            err = page.inner_text("#errorMsgField").strip()
            return {"result": "Pass" if ans == "" else "Fail", "note": f"Answer='{ans}'", "actual_answer": ans, "actual_error": err}

        elif action == "clear_then_recalculate":
            page.fill("#number1Field", str(num1))
            page.fill("#number2Field", str(num2))
            page.click("#calculateButton", timeout=3000)
            wait_for_calculation(page)
            if not page.is_disabled("#clearButton"):
                page.click("#clearButton", timeout=3000)
            page.fill("#number1Field", "20")
            page.fill("#number2Field", "20")
            page.click("#calculateButton", timeout=3000)
            wait_for_calculation(page)
            ans = page.input_value("#numberAnswerField")
            err = page.inner_text("#errorMsgField").strip()
            passed = (ans == "40")
            return {"result": "Pass" if passed else "Fail", "note": f"Answer='{ans}', Error='{err}'", "actual_answer": ans, "actual_error": err}

        elif action == "toggle_int_after":
            page.select_option("#selectOperationDropdown", op_val)
            if page.is_visible("#integerSelect") and not page.is_disabled("#integerSelect"):
                page.set_checked("#integerSelect", True)
            page.fill("#number1Field", str(num1))
            page.fill("#number2Field", str(num2))
            page.click("#calculateButton", timeout=3000)
            wait_for_calculation(page)
            # Giờ bỏ tích chọn
            if page.is_visible("#integerSelect") and not page.is_disabled("#integerSelect"):
                page.set_checked("#integerSelect", False)
                page.dispatch_event("#integerSelect", "change")
            ans = page.input_value("#numberAnswerField")
            err = page.inner_text("#errorMsgField").strip()
            passed = (ans == expected_ans)
            return {"result": "Pass" if passed else "Fail", "note": f"Sau Toggle: Answer='{ans}', Expected='{expected_ans}'", "actual_answer": ans, "actual_error": err}

        else: # Standard calculate
            page.select_option("#selectOperationDropdown", op_val)
            if page.is_visible("#integerSelect") and not page.is_disabled("#integerSelect"):
                page.set_checked("#integerSelect", int_only)
            page.fill("#number1Field", str(num1))
            page.fill("#number2Field", str(num2))
            page.click("#calculateButton", timeout=3000)
            wait_for_calculation(page)

            ans = page.input_value("#numberAnswerField")
            err = page.inner_text("#errorMsgField").strip()

            passed = True
            mismatch_reasons = []

            if expected_err:
                if expected_err not in err:
                    passed = False
                    mismatch_reasons.append(f"Lỗi thực tế: '{err}', mong đợi: '{expected_err}'")
            else:
                if err:
                    passed = False
                    mismatch_reasons.append(f"Xuất hiện lỗi ngoài ý muốn: '{err}'")
                if expected_ans != "" and ans != expected_ans:
                    passed = False
                    mismatch_reasons.append(f"Answer thực tế: '{ans}', mong đợi: '{expected_ans}'")

            note = "; ".join(mismatch_reasons) if mismatch_reasons else f"Answer={ans}"
            return {
                "result": "Pass" if passed else "Fail",
                "note": note,
                "actual_answer": ans,
                "actual_error": err,
            }

    except Exception as e:
        return {
            "result": "Blocked",
            "note": f"Exception: {str(e)}",
            "actual_answer": "",
            "actual_error": str(e),
        }

def run_build_test_suite(build_num, headed=True, tester_name="Automated QA"):
    """Chạy toàn bộ test cases cho một build cụ thể và xuất báo cáo markdown"""
    build_str = str(build_num)
    build_desc = BUILD_DESCRIPTIONS.get(build_str, f"Build {build_str}")

    print(f"\n=======================================================")
    print(f"🚀 BẮT ĐẦU CHẠY TEST SUITE TRÊN {build_desc.upper()}")
    print(f"=======================================================")

    results = []
    pass_count = 0
    fail_count = 0
    blocked_count = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed, slow_mo=50 if headed else 0)
        page = browser.new_page()
        page.goto("https://testsheepnz.github.io/BasicCalculator.html")

        # Chọn Build trên dropdown
        page.select_option("#selectBuild", build_str)
        page.dispatch_event("#selectBuild", "change")
        time.sleep(0.5)

        total_tcs = len(ALL_TEST_CASES)
        for idx, tc in enumerate(ALL_TEST_CASES, start=1):
            res = run_single_test(page, tc)
            res_status = res["result"]
            if res_status == "Pass":
                pass_count += 1
                symbol = "✅ PASS"
            elif res_status == "Fail":
                fail_count += 1
                symbol = "❌ FAIL"
            else:
                blocked_count += 1
                symbol = "⚠️ BLOCKED"

            print(f"[{idx:02d}/{total_tcs}] {tc['id']} ({tc['module']}): {symbol} -> {res['note']}")
            results.append({
                "tc": tc,
                "result": res_status,
                "note": res["note"],
                "actual_answer": res["actual_answer"],
                "actual_error": res["actual_error"],
            })

        browser.close()

    print(f"\n-------------------------------------------------------")
    print(f"📊 KẾT QUẢ BUILD {build_str}: Tổng {total_tcs} | Pass: {pass_count} | Fail: {fail_count} | Blocked: {blocked_count}")
    print(f"-------------------------------------------------------")

    # Xuất file Test Run Markdown
    export_markdown_report(build_str, build_desc, tester_name, results, pass_count, fail_count, blocked_count)
    return results

def export_markdown_report(build_str, build_desc, tester_name, results, pass_count, fail_count, blocked_count):
    """Xuất file Test Run theo format chuẩn trong tests/test-runs/"""
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test-runs"))
    os.makedirs(output_dir, exist_ok=True)
    report_file = os.path.join(output_dir, f"build-{build_str}-test-run.md")

    today_str = datetime.now().strftime("%Y-%m-%d")
    total = len(results)

    content = f"""# Test Run: Basic Calculator - Build {build_str}

## Thông tin đợt thực thi (Run Information)
- **Sprint / Release**: Milestone 1 - Build Verification
- **Build Tested**: {build_desc}
- **Ngày thực thi (Execution Date)**: {today_str}
- **Tester**: {tester_name}
- **Môi trường (Environment)**: Playwright Chromium (Automated), URL: https://testsheepnz.github.io/BasicCalculator.html

## Tóm tắt kết quả (Execution Summary)
- **Tổng số Test Cases**: {total}
- **Passed**: {pass_count} ({pass_count/total*100:.1f}%)
- **Failed**: {fail_count} ({fail_count/total*100:.1f}%)
- **Blocked**: {blocked_count} ({blocked_count/total*100:.1f}%)

## Bảng kết quả thực thi chi tiết (Test Execution Table)

| Test Case ID | Module | Tester | Result | Related Bug | Note / Actual Result |
|--------------|--------|--------|--------|-------------|----------------------|
"""
    bug_counter = 1
    for item in results:
        tc = item["tc"]
        res = item["result"]
        note = item["note"].replace("|", "\\|")
        related_bug = "None"
        if res == "Fail":
            related_bug = f"#[BUG-B{build_str}-{bug_counter:02d}]"
            bug_counter += 1
        elif res == "Blocked":
            related_bug = "Blocked"

        content += f"| {tc['id']} | {tc['module']} | {tester_name} | {res} | {related_bug} | {note} |\n"

    content += """
> **Hướng dẫn ghi nhận Result:**
> - **Pass**: Test case thực thi thành công, Actual Result khớp Expected Result.
> - **Fail**: Test case thực thi thất bại, cần tạo GitHub Bug Issue và thay mã `#[BUG-...]` bằng Issue ID thực tế (ví dụ `#18`).
> - **Blocked**: Không thể thực thi test case do lỗi rào cản.
"""

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"📄 Đã tự động tạo báo cáo Test Run: {report_file}")

def main():
    parser = argparse.ArgumentParser(description="Chạy bộ kiểm thử tự động Basic Calculator")
    parser.add_argument("--build", type=str, default="", help="Số build cần test (0 đến 8, hoặc 'all', hoặc '1,2')")
    parser.add_argument("--headless", action="store_true", help="Chạy ẩn trình duyệt (mặc định mở trình duyệt)")
    parser.add_argument("--tester", type=str, default="QA Tester", help="Tên người thực thi test")
    args = parser.parse_args()

    build_input = args.build.strip()
    if not build_input:
        print("=======================================================")
        print("   BASIC CALCULATOR AUTOMATION TEST SUITE (PLAYWRIGHT)  ")
        print("=======================================================")
        print("Danh sách build:")
        for k, v in BUILD_DESCRIPTIONS.items():
            print(f"  [{k}] {v}")
        print("  [all] Chạy qua tất cả các build từ 1 đến 8")
        build_input = input("\n👉 Nhập build bạn muốn chạy (0-8 hoặc 'all' hoặc '1,2'): ").strip()

    if not build_input:
        build_input = "1"

    builds_to_run = []
    if build_input.lower() == "all":
        builds_to_run = [str(i) for i in range(1, 9)]
    elif "," in build_input:
        builds_to_run = [b.strip() for b in build_input.split(",")]
    else:
        builds_to_run = [build_input]

    is_headed = not args.headless

    for b in builds_to_run:
        if b in BUILD_DESCRIPTIONS:
            run_build_test_suite(b, headed=is_headed, tester_name=args.tester)
        else:
            print(f"⚠️ Build '{b}' không hợp lệ. Vui lòng chọn từ 0 đến 8.")

if __name__ == "__main__":
    main()
