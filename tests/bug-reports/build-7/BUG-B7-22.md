---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Nối chuỗi chứa ký tự đặc biệt (Build 7)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-006
- **Requirement ID**: FR-CONCAT-01

## Description
Trên Build 7, phát hiện lỗi khi thực thi test case `TC-CONCAT-006` (Nối chuỗi chứa ký tự đặc biệt). Answer thực tế: 'test.com', mong đợi: 'user@test.com'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 7

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '7'.
2. Nhập 'user@' vào trường First number.
3. Nhập 'test.com' vào trường Second number.
4. Chọn phép tính 'Concatenate' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: 'test.com', mong đợi: 'user@test.com'

## Expected Result
Kết quả mong đợi: Answer='user@test.com'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: 'test.com', mong đợi: 'user@test.com'`
