---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Chia cho số 0 (Xử lý lỗi Divide by zero) (Build 6)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-015
- **Requirement ID**: FR-ARITH-04

## Description
Trên Build 6, phát hiện lỗi khi thực thi test case `TC-ARITH-015` (Chia cho số 0 (Xử lý lỗi Divide by zero)). Lỗi thực tế: '', mong đợi: 'Divide by zero error!'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 6

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '6'.
2. Nhập '100' vào trường First number.
3. Nhập '0' vào trường Second number.
4. Chọn phép tính 'Divide' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Lỗi thực tế: '', mong đợi: 'Divide by zero error!'

## Expected Result
, thông báo lỗi: 'Divide by zero error!'

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Divide by zero error!'`
