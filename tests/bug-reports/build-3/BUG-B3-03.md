---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: First number có giá trị, Second number rỗng (Build 3)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-004
- **Requirement ID**: FR-CONCAT-01

## Description
Trên Build 3, phát hiện lỗi khi thực thi test case `TC-CONCAT-004` (First number có giá trị, Second number rỗng). Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'Hello'.

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
2. Nhập 'Hello' vào trường First number.
3. Để trống trường Second number.
4. Chọn phép tính 'Concatenate' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'Hello'

## Expected Result
Kết quả mong đợi: Answer='Hello'

## Evidence
- **Console Log / Error Text**: `Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'Hello'`
