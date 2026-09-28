---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Nối chuỗi chứa ký tự đặc biệt (Build 3)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-006
- **Requirement ID**: FR-CONCAT-01

## Description
Trên Build 3, phát hiện lỗi khi thực thi test case `TC-CONCAT-006` (Nối chuỗi chứa ký tự đặc biệt). Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'user@test.com'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 3

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '3'.
2. Nhập 'user@' vào trường First number.
3. Nhập 'test.com' vào trường Second number.
4. Chọn phép tính 'Concatenate' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'user@test.com'

## Expected Result
Kết quả mong đợi: Answer='user@test.com'

## Evidence
- **Console Log / Error Text**: `Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'user@test.com'`
