---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Nối hai chuỗi giống nhau (Build 7)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-011
- **Requirement ID**: FR-CONCAT-01

## Description
Trên Build 7, phát hiện lỗi khi thực thi test case `TC-CONCAT-011` (Nối hai chuỗi giống nhau). Answer thực tế: 'Test', mong đợi: 'TestTest'.

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
2. Nhập 'Test' vào trường First number.
3. Nhập 'Test' vào trường Second number.
4. Chọn phép tính 'Concatenate' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: 'Test', mong đợi: 'TestTest'

## Expected Result
Kết quả mong đợi: Answer='TestTest'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: 'Test', mong đợi: 'TestTest'`
