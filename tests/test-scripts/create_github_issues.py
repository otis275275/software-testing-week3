# -*- coding: utf-8 -*-
"""
Script tạo tự động các GitHub Issues lên repository GitHub thông qua GitHub REST API.
Cấu trúc Issue tuân thủ đúng template yêu cầu:
- Tiêu đề Section bằng Tiếng Anh (## Summary, ## Precondition, ## Steps to Reproduce, ...)
- Nội dung chi tiết bằng Tiếng Việt
"""

import os
import sys
import requests

REPO = "otis275275/software-testing-week3"
API_URL = f"https://api.github.com/repos/{REPO}/issues"

ROOT_CAUSE_BUGS = [
    {
        "title": "[BUG][Build 1][Validation]: Hệ thống không kiểm tra tính hợp lệ của dữ liệu số",
        "labels": ["type: bug", "module: input-validation", "severity: major", "priority: P1", "status: new"],
        "body": """## Summary
Hệ thống bỏ qua bước kiểm tra kiểu số đối với First number và Second number. Khi nhập chữ cái, ký tự đặc biệt, để trống hoặc nhập khoảng trắng vào các phép tính số học (Add, Subtract, Multiply, Divide), hệ thống không hiển thị thông báo lỗi 'Number 1 is not a number' hay 'Number 2 is not a number' mà vẫn tiếp tục tính toán hoặc trả về kết quả sai (NaN).

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build 1.

## Steps to Reproduce
1. Mở trang Basic Calculator và chọn Build 1.
2. Nhập `abc` vào ô First number.
3. Nhập `10` vào ô Second number.
4. Chọn phép tính `Add` tại danh sách Operation.
5. Nhấn nút `Calculate`.

## Expected Result
Hệ thống phải chặn phép tính và hiển thị thông báo lỗi bằng chữ đỏ:
"Number 1 is not a number"

## Actual Result
Hệ thống không hiển thị thông báo lỗi 'Number 1 is not a number', vẫn thực thi phép tính và hiển thị giá trị `NaN` tại ô Answer.

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 1

## Severity
Major

## Priority
P1

## Evidence
- Test Cases liên quan: `TC-ARITH-021`, `TC-ARITH-022`, `TC-VALIDATE-001` đến `TC-VALIDATE-006`
- Lỗi ghi nhận: Bỏ qua hàm `isNaN()`, không xuất hiện thông báo lỗi `errorMsgField`."""
    },
    {
        "title": "[BUG][Build 2][Core]: Phép toán Add và Concatenate bị hoán đổi logic cho nhau",
        "labels": ["type: bug", "module: core", "severity: critical", "priority: P0", "status: new"],
        "body": """## Summary
Logic của hai phép toán Add và Concatenate bị đảo ngược: Khi chọn Add (cộng số học) hệ thống lại thực hiện nối chuỗi, và khi chọn Concatenate (nối chuỗi) hệ thống lại thực hiện phép tính cộng số học kèm theo việc ép kiểm tra kiểu số.

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build 2.

## Steps to Reproduce
1. Mở trang Basic Calculator và chọn Build 2.
2. Nhập `25` vào First number, `15` vào Second number, chọn Operation `Add` -> Nhấn `Calculate`.
3. Nhập `Hello` vào First number, `World` vào Second number, chọn Operation `Concatenate` -> Nhấn `Calculate`.

## Expected Result
- Phép tính Add: Kết quả hiển thị `40` (tổng số học).
- Phép tính Concatenate: Kết quả hiển thị `HelloWorld` (nối chuỗi văn bản không qua kiểm tra số).

## Actual Result
- Phép tính Add trả về `2515` (nối chuỗi).
- Phép tính Concatenate báo lỗi `Number 1 is not a number` do bị chạy nhầm vào logic phép cộng.

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 2

## Severity
Critical

## Priority
P0

## Evidence
- Test Cases liên quan: `TC-ARITH-001` đến `TC-ARITH-004`, `TC-CONCAT-001` đến `TC-CONCAT-011`
- Lỗi ghi nhận: Add trả về chuỗi ghép, Concatenate bị chặn bởi validation số."""
    },
    {
        "title": "[BUG][Build 3][Concatenate]: Phép Concatenate bị ép kiểm tra kiểu số khiến không nối được chuỗi chữ",
        "labels": ["type: bug", "module: concatenate", "severity: major", "priority: P1", "status: new"],
        "body": """## Summary
Khi người dùng chọn phép toán Concatenate để nối các chuỗi văn bản thông thường, hệ thống luôn ép kiểm tra kiểu số và báo lỗi 'Number 1 is not a number', khiến tính năng nối chuỗi văn bản bị vô hiệu hóa hoàn toàn.

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build 3.

## Steps to Reproduce
1. Mở trang Basic Calculator và chọn Build 3.
2. Nhập `Hello` vào ô First number.
3. Nhập `World` vào ô Second number.
4. Chọn Operation là `Concatenate`.
5. Nhấn nút `Calculate`.

## Expected Result
Hệ thống phải nối hai chuỗi và hiển thị kết quả:
"HelloWorld"

## Actual Result
Hệ thống hiển thị thông báo lỗi màu đỏ "Number 1 is not a number" và không trả về kết quả nối chuỗi.

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 3

## Severity
Major

## Priority
P1

## Evidence
- Test Cases liên quan: `TC-CONCAT-001`, `TC-CONCAT-003`, `TC-CONCAT-004`, `TC-CONCAT-006` đến `TC-CONCAT-008`, `TC-CONCAT-011`
- Lỗi ghi nhận: Biến `isNumber` luôn bị gán `true` ngay cả khi chọn Concatenate."""
    },
    {
        "title": "[BUG][Build 4][UI/State]: Checkbox Integers only bị khóa cố định không thể bỏ chọn",
        "labels": ["type: bug", "module: ui", "severity: major", "priority: P1", "status: new"],
        "body": """## Summary
Checkbox tùy chọn 'Integers only' luôn bị tích chọn sẵn và bị vô hiệu hóa (disabled). Người dùng không thể tắt tùy chọn này để xem kết quả số thực/thập phân chính xác cho các phép chia hoặc phép tính phân số.

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build 4.

## Steps to Reproduce
1. Mở trang Basic Calculator và chọn Build 4.
2. Quan sát ô checkbox 'Integers only'.
3. Nhập `7` vào First number, `2` vào Second number.
4. Chọn Operation `Divide` và nhấn `Calculate`.

## Expected Result
- Người dùng có thể tự do tích hoặc bỏ tích chọn checkbox 'Integers only'.
- Khi bỏ chọn, phép chia `7 / 2` phải hiển thị đầy đủ là `3.5`.

## Actual Result
- Checkbox 'Integers only' bị disable và luôn bị ép chọn.
- Kết quả phép chia `7 / 2` luôn bị ép lấy phần nguyên là `3`.

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 4

## Severity
Major

## Priority
P1

## Evidence
- Test Cases liên quan: `TC-ARITH-003`, `TC-ARITH-007`, `TC-ARITH-012`, `TC-ARITH-014`, `TC-ARITH-019`, `TC-CLEAR-015`
- Lỗi ghi nhận: Thuộc tính `integerSelect.disabled = true` và `checked = true` bị khóa cứng."""
    },
    {
        "title": "[BUG][Build 5][Clear]: Nút Clear bị vô hiệu hóa hoàn toàn",
        "labels": ["type: bug", "module: clear", "severity: critical", "priority: P0", "status: new"],
        "body": """## Summary
Nút chức năng 'Clear' bị vô hiệu hóa (disabled = true) ngay từ khi mở Build 5 và trong suốt quá trình sử dụng, khiến người dùng không thể xóa dữ liệu hay làm mới màn hình sau khi tính toán.

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build 5.

## Steps to Reproduce
1. Mở trang Basic Calculator và chọn Build 5.
2. Nhập số vào First number và Second number, thực hiện phép tính bất kỳ.
3. Nhấn nút `Clear`.

## Expected Result
Nút Clear phải ở trạng thái hoạt động (enabled) và khi nhấn vào sẽ xóa trống ô Answer, bỏ chọn checkbox Integers only và xóa thông báo lỗi.

## Actual Result
Nút Clear bị vô hiệu hóa hoàn toàn (mờ đi và không thể click).

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 5

## Severity
Critical

## Priority
P0

## Evidence
- Test Cases liên quan: Toàn bộ 15 test case module Clear (`TC-CLEAR-001` đến `TC-CLEAR-015`) và `TC-ARITH-025`
- Lỗi ghi nhận: Hàm `buildChanged()` thiết lập `clearButton.disabled = true`."""
    },
    {
        "title": "[BUG][Build 6][Arithmetic]: Không kiểm tra phép chia cho 0 khiến ứng dụng hiển thị Infinity",
        "labels": ["type: bug", "module: arithmetic", "severity: critical", "priority: P0", "status: new"],
        "body": """## Summary
Hệ thống không kiểm tra điều kiện chia cho 0 trong phép tính Divide, dẫn đến việc trình duyệt tự tính toán ra giá trị vô cực 'Infinity' thay vì hiển thị thông báo lỗi bảo vệ người dùng.

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build 6.

## Steps to Reproduce
1. Mở trang Basic Calculator và chọn Build 6.
2. Nhập `100` vào First number.
3. Nhập `0` vào Second number.
4. Chọn Operation `Divide`.
5. Nhấn nút `Calculate`.

## Expected Result
Hệ thống phải chặn phép tính và hiển thị thông báo lỗi màu đỏ:
"Divide by zero error!"

## Actual Result
Ô Answer hiển thị giá trị `Infinity` và không xuất hiện thông báo lỗi.

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 6

## Severity
Critical

## Priority
P0

## Evidence
- Test Cases liên quan: `TC-ARITH-015`
- Lỗi ghi nhận: Bỏ qua điều kiện kiểm tra `if(num2 == 0)` trên Build 6."""
    },
    {
        "title": "[BUG][Build 7][Core]: Hệ thống lấy giá trị Answer cũ làm toán hạng đầu tiên thay vì First number",
        "labels": ["type: bug", "module: core", "severity: critical", "priority: P0", "status: new"],
        "body": """## Summary
Khi thực hiện tính toán, hệ thống bỏ qua giá trị người dùng nhập tại ô First number mà tự động thay thế bằng giá trị đang hiển thị trong ô Answer từ lần tính trước, gây sai lệch toàn bộ kết quả.

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build 7.

## Steps to Reproduce
1. Mở trang Basic Calculator và chọn Build 7.
2. Nhập `25` vào First number, `15` vào Second number.
3. Chọn Operation `Add` và nhấn `Calculate`.

## Expected Result
Hệ thống phải lấy giá trị `25` từ ô First number và tính `25 + 15 = 40`.

## Actual Result
Do ô Answer ban đầu chưa có giá trị (`""` tương đương 0), hệ thống tính `0 + 15` và trả về kết quả sai là `15`.

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 7

## Severity
Critical

## Priority
P0

## Evidence
- Test Cases liên quan: `TC-ARITH-001` đến `TC-ARITH-003`, `TC-ARITH-005` đến `TC-ARITH-010`, `TC-CONCAT-001`, `TC-CONCAT-002`, `TC-VALIDATE-007`
- Lỗi ghi nhận: Dòng mã `if (selectedBuild == 7) num1 = answer;` ghi đè giá trị đầu vào."""
    },
    {
        "title": "[BUG][Build 8][Core]: Hoán đổi vị trí First number và Second number khi tính toán",
        "labels": ["type: bug", "module: core", "severity: critical", "priority: P0", "status: new"],
        "body": """## Summary
Hệ thống tự động tráo đổi vị trí của hai toán hạng First number và Second number trước khi tính toán, dẫn đến kết quả bị sai đối với tất cả các phép toán không có tính giao hoán (phép trừ, phép chia, phép nối chuỗi).

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build 8.

## Steps to Reproduce
1. Mở trang Basic Calculator và chọn Build 8.
2. Nhập `50` vào First number, `20` vào Second number.
3. Chọn Operation `Subtract` và nhấn `Calculate`.

## Expected Result
Phép tính `50 - 20` phải cho kết quả là `30`.

## Actual Result
Hệ thống tráo đổi vị trí thành `20 - 50` và trả về kết quả sai là `-30`.

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 8

## Severity
Critical

## Priority
P0

## Evidence
- Test Cases liên quan: `TC-ARITH-005`, `TC-ARITH-006`, `TC-ARITH-007`, `TC-ARITH-013`, `TC-ARITH-014`, `TC-CONCAT-001`, `TC-CONCAT-003`, `TC-CONCAT-004`
- Lỗi ghi nhận: Đoạn mã `var temp = num1; num1 = num2; num2 = temp;` hoán vị biến."""
    },
    {
        "title": "[BUG][UI/State]: Vòng xoay Calculating và nút Clear bị kẹt vĩnh viễn khi gặp lỗi chia cho 0",
        "labels": ["type: bug", "module: ui", "severity: major", "priority: P1", "status: new"],
        "body": """## Summary
Khi phát sinh lỗi chia cho 0, hệ thống hiển thị thông báo lỗi nhưng quên gọi hàm mở khóa giao diện `unlockCalculate()`, khiến vòng xoay loading 'Calculating...' tiếp tục quay mãi mãi và nút Calculate / Clear bị khóa không thể thao tác tiếp.

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) trên bất kỳ Build nào có kiểm tra chia cho 0 (Build 0-5, 7-8).

## Steps to Reproduce
1. Nhập `10` vào First number, `0` vào Second number.
2. Chọn Operation `Divide` và nhấn `Calculate`.
3. Quan sát giao diện và thử nhấn nút `Clear`.

## Expected Result
Sau khi hiển thị thông báo lỗi `Divide by zero error!`, vòng xoay loading phải biến mất và nút Calculate / Clear phải được mở khóa để người dùng thao tác tiếp.

## Actual Result
Vòng xoay spinner tiếp tục xoay vĩnh viễn, nút Calculate và nút Clear bị vô hiệu hóa hoàn toàn.

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 0-5, 7-8

## Severity
Major

## Priority
P1

## Evidence
- Test Cases liên quan: `TC-CLEAR-006`, `TC-CLEAR-010`
- Lỗi ghi nhận: Hàm `calculate()` return ngay trong nhánh `case 3 (num2 == 0)` mà không gọi `unlockCalculate()`."""
    },
    {
        "title": "[BUG][Build 9][UI]: Trường Second number và nút Calculate bị biến mất hoàn toàn khỏi giao diện (Elements Vanish)",
        "labels": ["type: bug", "module: ui", "severity: blocker", "priority: P0", "status: new"],
        "body": """## Summary
Khi người dùng chuyển sang Build 9, trường nhập liệu Second number và nút bấm Calculate bị ẩn (hidden) và vô hiệu hóa (disabled) hoàn toàn khỏi giao diện người dùng, khiến người dùng không thể nhập số thứ hai và không thể bấm nút để thực hiện bất kỳ phép tính toán nào.

## Precondition
Người dùng đã truy cập trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build 9.

## Steps to Reproduce
1. Mở trang Basic Calculator.
2. Tại danh sách dropdown Build, chọn `9`.
3. Quan sát giao diện các trường nhập liệu và nút bấm.

## Expected Result
Trường Second number và nút Calculate phải luôn hiển thị đầy đủ, rõ ràng trên giao diện để người dùng có thể nhập số thứ hai và bấm nút tính toán.

## Actual Result
- Trường Second number bị ẩn hoàn toàn (`hidden = true`, `disabled = true`).
- Nút bấm Calculate bị biến mất khỏi giao diện (`hidden = true`, `disabled = true`).
- Ứng dụng bị vô hiệu hóa hoàn toàn khả năng tính toán.

## Environment
- OS: Windows 11
- Browser: Chrome 124 / Playwright Chromium
- Application: Basic Calculator
- Build: Build 9

## Severity
Blocker

## Priority
P0

## Evidence
- Thuộc tính DOM ghi nhận trong hàm `buildChanged()`:
  - `document.getElementById('number2Field').hidden = true`
  - `document.getElementById('number2Field').disabled = true`
  - `document.getElementById('calculateButton').hidden = true`
  - `document.getElementById('calculateButton').disabled = true`"""
    }
]

def create_issue(token, bug):
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": bug["title"],
        "body": bug["body"],
        "labels": bug["labels"]
    }
    res = requests.post(API_URL, json=payload, headers=headers)
    if res.status_code == 201:
        data = res.json()
        print(f"✅ Đã tạo thành công Issue #{data['number']}: {bug['title']}")
        return data['number']
    else:
        print(f"❌ Lỗi khi tạo issue '{bug['title']}': HTTP {res.status_code} - {res.text}")
        return None

def main():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or os.environ.get("PAT")
    
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        token = sys.argv[1].strip()

    if not token:
        print("=" * 60)
        print("      TỰ ĐỘNG TẠO 10 ISSUES LÊN GITHUB REPO      ")
        print(f"      Repository: {REPO}")
        print("=" * 60)
        token = input("👉 Nhập GitHub Personal Access Token (PAT) của bạn: ").strip()

    if not token:
        print("⚠️ Chưa có PAT. Hủy thao tác.")
        return

    print(f"\n🚀 Đang kết nối tới GitHub API repo '{REPO}' để tạo 10 Issues...\n")
    created_count = 0
    for bug in ROOT_CAUSE_BUGS:
        num = create_issue(token, bug)
        if num:
            created_count += 1

    print(f"\n🎉 Hoàn tất! Đã tạo thành công {created_count}/{len(ROOT_CAUSE_BUGS)} Issues trên GitHub.")

if __name__ == "__main__":
    main()
