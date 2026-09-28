# -*- coding: utf-8 -*-
"""
Script đọc file Test Run (tests/test-runs/build-X-test-run.md)
và xuất toàn bộ Bug Report vào thư mục tests/bug-reports/build-X/.

Cách chạy:
  python tests/test-scripts/generate_bug_reports.py 1
  python tests/test-scripts/generate_bug_reports.py 2
  python tests/test-scripts/generate_bug_reports.py 3
  python tests/test-scripts/generate_bug_reports.py all
"""

import os
import re
import sys
import glob

# Đảm bảo đường dẫn import
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TESTS_DIR = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
sys.path.append(CURRENT_DIR)

from test_data import ALL_TEST_CASES

TC_LOOKUP = {tc["id"]: tc for tc in ALL_TEST_CASES}

REQ_LOOKUP = {
    "TC-ARITH-001": "FR-ARITH-01", "TC-ARITH-002": "FR-ARITH-01", "TC-ARITH-003": "FR-ARITH-01", "TC-ARITH-004": "FR-ARITH-01",
    "TC-ARITH-005": "FR-ARITH-02", "TC-ARITH-006": "FR-ARITH-02", "TC-ARITH-007": "FR-ARITH-02", "TC-ARITH-008": "FR-ARITH-02",
    "TC-ARITH-009": "FR-ARITH-03", "TC-ARITH-010": "FR-ARITH-03", "TC-ARITH-011": "FR-ARITH-03", "TC-ARITH-012": "FR-ARITH-03",
    "TC-ARITH-013": "FR-ARITH-04", "TC-ARITH-014": "FR-ARITH-04", "TC-ARITH-015": "FR-ARITH-04", "TC-ARITH-016": "FR-ARITH-04", "TC-ARITH-017": "FR-ARITH-04",
    "TC-ARITH-018": "FR-ARITH-05", "TC-ARITH-019": "FR-ARITH-05", "TC-ARITH-020": "FR-ARITH-05",
    "TC-ARITH-021": "FR-ARITH-06", "TC-ARITH-022": "FR-ARITH-06", "TC-ARITH-023": "FR-ARITH-06", "TC-ARITH-024": "FR-ARITH-06",
    "TC-ARITH-025": "FR-ARITH-07",
    "TC-VALIDATE-001": "FR-VAL-01", "TC-VALIDATE-002": "FR-VAL-01", "TC-VALIDATE-003": "FR-VAL-01",
    "TC-VALIDATE-004": "FR-VAL-02", "TC-VALIDATE-005": "FR-VAL-02", "TC-VALIDATE-006": "FR-VAL-02", "TC-VALIDATE-007": "FR-VAL-02",
}

def get_req_id(tc_id):
    if tc_id in REQ_LOOKUP:
        return REQ_LOOKUP[tc_id]
    if tc_id.startswith("TC-CONCAT"): return "FR-CONCAT-01"
    if tc_id.startswith("TC-CLEAR"): return "FR-CLEAR-01"
    if tc_id.startswith("TC-VALIDATE"): return "FR-VAL-01"
    return "FR-GEN-01"

def determine_severity_priority(module, note):
    note_lower = note.lower()
    if "disabled" in note_lower or "crash" in note_lower or "blocked" in note_lower:
        return "critical", "P0"
    if module in ["Arithmetic", "Concatenate"]:
        return "major", "P1"
    return "minor", "P2"

def parse_test_run_file(test_run_path):
    failed_cases = []
    if not os.path.exists(test_run_path):
        return failed_cases

    with open(test_run_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line_str = line.strip()
        if not line_str.startswith("|"):
            continue
        parts = [p.strip() for p in line_str.split("|")[1:-1]]
        if len(parts) >= 6:
            tc_id, module, tester, result, bug_id, note = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
            if result.lower() == "fail":
                failed_cases.append({
                    "tc_id": tc_id,
                    "module": module,
                    "tester": tester,
                    "result": result,
                    "raw_bug_id": bug_id,
                    "note": note
                })
    return failed_cases

def generate_bugs_for_build(build_num):
    test_run_path = os.path.join(TESTS_DIR, "test-runs", f"build-{build_num}-test-run.md")
    
    if not os.path.exists(test_run_path):
        print(f"⚠️  Không tìm thấy file: {test_run_path}")
        return []

    failed_cases = parse_test_run_file(test_run_path)
    if not failed_cases:
        print(f"ℹ️  Build {build_num} không có test case nào bị Fail.")
        return []

    build_dir = os.path.join(TESTS_DIR, "bug-reports", f"build-{build_num}")
    os.makedirs(build_dir, exist_ok=True)

    generated_bugs = []
    for idx, item in enumerate(failed_cases, start=1):
        bug_id = f"BUG-B{build_num}-{idx:02d}"
        tc_id = item["tc_id"]
        tc_info = TC_LOOKUP.get(tc_id, {})
        title_base = tc_info.get("title", f"Lỗi tại {tc_id}")
        module = item["module"]
        note = item["note"]
        req_id = get_req_id(tc_id)
        severity, priority = determine_severity_priority(module, note)

        num1 = tc_info.get("num1", "")
        num2 = tc_info.get("num2", "")
        op = tc_info.get("operation", "Add")
        exp_ans = tc_info.get("expected_answer", "")
        exp_err = tc_info.get("expected_error", "")

        steps_md = f"1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '{build_num}'.\n"
        if num1: steps_md += f"2. Nhập '{num1}' vào trường First number.\n"
        else: steps_md += f"2. Để trống trường First number.\n"
        if num2: steps_md += f"3. Nhập '{num2}' vào trường Second number.\n"
        else: steps_md += f"3. Để trống trường Second number.\n"
        steps_md += f"4. Chọn phép tính '{op}' tại dropdown Operation.\n"
        steps_md += f"5. Nhấn nút 'Calculate'."

        expected_text = f"Kết quả mong đợi: Answer='{exp_ans}'" if exp_ans else ""
        if exp_err:
            expected_text += f", thông báo lỗi: '{exp_err}'"

        actual_text = f"Hệ thống hoạt động không đúng: {note}"

        content = f"""---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][{module}]: {title_base} (Build {build_num})"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: {tc_id}
- **Requirement ID**: {req_id}

## Description
Trên Build {build_num}, phát hiện lỗi khi thực thi test case `{tc_id}` ({title_base}). {note}.

## Severity / Priority
- **Severity**: {severity}
- **Priority**: {priority}

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build {build_num}

## Steps to Reproduce
{steps_md}

## Actual Result
{actual_text}

## Expected Result
{expected_text}

## Evidence
- **Console Log / Error Text**: `{note}`
"""
        bug_file = os.path.join(build_dir, f"{bug_id}.md")
        with open(bug_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        generated_bugs.append({
            "bug_id": bug_id,
            "tc_id": tc_id,
            "module": module,
            "title": f"{title_base} (Build {build_num})",
            "severity": severity,
            "priority": priority,
        })

    print(f"✅ Đã tạo {len(generated_bugs)} file bug report trong thư mục: tests/bug-reports/build-{build_num}/")
    return generated_bugs

def update_global_index():
    bug_reports_dir = os.path.join(TESTS_DIR, "bug-reports")
    os.makedirs(bug_reports_dir, exist_ok=True)

    build_subdirs = sorted([d for d in os.listdir(bug_reports_dir) if os.path.isdir(os.path.join(bug_reports_dir, d)) and d.startswith("build-")])
    
    index_content = "# Danh mục Bug Reports (Tổng hợp các bản Build)\n\n"
    index_content += "Tổng hợp tất cả các lỗi được phát hiện từ quá trình chạy kiểm thử tự động trên các bản Build.\n\n---\n\n"

    total_all_bugs = 0

    for b_dir in build_subdirs:
        b_num = b_dir.replace("build-", "")
        b_path = os.path.join(bug_reports_dir, b_dir)
        bug_files = sorted(glob.glob(os.path.join(b_path, "BUG-*.md")))
        total_all_bugs += len(bug_files)

        index_content += f"## Danh sách lỗi trên Build {b_num} (Tổng: {len(bug_files)} lỗi)\n\n"
        index_content += "| Bug ID | Test Case ID | Module | Tiêu đề lỗi | Severity | Priority | File chi tiết |\n"
        index_content += "|---|---|---|---|---|---|---|\n"

        for bf in bug_files:
            bug_name = os.path.basename(bf).replace(".md", "")
            with open(bf, "r", encoding="utf-8") as f:
                txt = f.read()
            
            tc_match = re.search(r"\*\*Found by Test Case ID\*\*:\s*([^\n\r]+)", txt)
            tc_id = tc_match.group(1).strip() if tc_match else "N/A"
            
            title_match = re.search(r"title:\s*\"\[BUG\]\[([^\]]+)\]:\s*([^\"]+)\"", txt)
            if title_match:
                module = title_match.group(1).strip()
                title = title_match.group(2).strip()
            else:
                module = "General"
                title = bug_name

            sev_match = re.search(r"\*\*Severity\*\*:\s*([^\n\r]+)", txt)
            sev = sev_match.group(1).strip() if sev_match else "major"

            pri_match = re.search(r"\*\*Priority\*\*:\s*([^\n\r]+)", txt)
            pri = pri_match.group(1).strip() if pri_match else "P1"

            index_content += f"| **{bug_name}** | {tc_id} | {module} | {title} | `{sev}` | `{pri}` | [{bug_name}.md]({b_dir}/{bug_name}.md) |\n"

        index_content += "\n---\n\n"

    index_file = os.path.join(bug_reports_dir, "index.md")
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print(f"📑 Đã cập nhật file tổng hợp: tests/bug-reports/index.md (Tổng cộng {total_all_bugs} lỗi)")

def main():
    # Lấy tham số dòng lệnh nếu có (ví dụ: python generate_bug_reports.py 1 hoặc python generate_bug_reports.py --build 1)
    args = sys.argv[1:]
    build_choice = ""

    if len(args) == 1 and not args[0].startswith("-"):
        build_choice = args[0].strip()
    elif "--build" in args:
        idx = args.index("--build")
        if idx + 1 < len(args):
            build_choice = args[idx + 1].strip()
    elif "--all" in args or "all" in [a.lower() for a in args]:
        build_choice = "all"

    if not build_choice:
        test_runs_dir = os.path.join(TESTS_DIR, "test-runs")
        existing_runs = sorted(glob.glob(os.path.join(test_runs_dir, "build-*-test-run.md")))
        print("=" * 60)
        print("   TOOL TỰ ĐỘNG TẠO BUG REPORTS TỪ KẾT QUẢ TEST RUN")
        print("=" * 60)
        print("Các file Test Run đang có sẵn trong tests/test-runs/:")
        for rf in existing_runs:
            m = re.search(r"build-(\d+)-test-run\.md", os.path.basename(rf))
            if m:
                print(f"  - Build {m.group(1)}: {os.path.basename(rf)}")
        print("-" * 60)
        build_choice = input("👉 Nhập số build cần tạo Bug Report (ví dụ: 1, 2, 3... hoặc 'all'): ").strip()

    if build_choice.lower() == "all":
        test_runs_dir = os.path.join(TESTS_DIR, "test-runs")
        existing_runs = sorted(glob.glob(os.path.join(test_runs_dir, "build-*-test-run.md")))
        for trf in existing_runs:
            match = re.search(r"build-(\d+)-test-run\.md", os.path.basename(trf))
            if match:
                generate_bugs_for_build(match.group(1))
        update_global_index()
    elif build_choice:
        for b in build_choice.split(","):
            generate_bugs_for_build(b.strip())
        update_global_index()

if __name__ == "__main__":
    main()
