---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Nối chuỗi chữ hoa và chữ thường (Build 8)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-008
- **Requirement ID**: FR-CONCAT-01

## Description
Trên Build 8, phát hiện lỗi khi thực thi test case `TC-CONCAT-008` (Nối chuỗi chữ hoa và chữ thường). Answer thực tế: 'defABC', mong đợi: 'ABCdef'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 8

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '8'.
2. Nhập 'ABC' vào trường First number.
3. Nhập 'def' vào trường Second number.
4. Chọn phép tính 'Concatenate' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: 'defABC', mong đợi: 'ABCdef'

## Expected Result
Kết quả mong đợi: Answer='ABCdef'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: 'defABC', mong đợi: 'ABCdef'`
