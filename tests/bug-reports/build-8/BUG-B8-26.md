---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Nhập ký tự đặc biệt vào trường số (Build 8)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-005
- **Requirement ID**: FR-VAL-02

## Description
Trên Build 8, phát hiện lỗi khi thực thi test case `TC-VALIDATE-005` (Nhập ký tự đặc biệt vào trường số). Lỗi thực tế: 'Number 1 is not a number', mong đợi: 'Number 2 is not a number'.

## Severity / Priority
- **Severity**: minor
- **Priority**: P2

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 8

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '8'.
2. Nhập '10' vào trường First number.
3. Nhập '@#$%' vào trường Second number.
4. Chọn phép tính 'Divide' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Lỗi thực tế: 'Number 1 is not a number', mong đợi: 'Number 2 is not a number'

## Expected Result
, thông báo lỗi: 'Number 2 is not a number'

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: 'Number 1 is not a number', mong đợi: 'Number 2 is not a number'`
