---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Không báo lỗi khi nhập chuỗi chỉ chứa khoảng trắng vào trường số (Build 1)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-006
- **Requirement ID**: FR-VAL-02

## Description
Nhập '   ' (3 dấu cách) vào First number và '20' vào Second number với phép Subtract, hệ thống không báo lỗi ký tự không hợp lệ.

## Severity / Priority
- **Severity**: minor
- **Priority**: P2

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 1

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '1'.
2. Nhập '   ' vào First number, '20' vào Second number.
3. Chọn Operation 'Subtract' và nhấn 'Calculate'.

## Actual Result
Không xuất hiện thông báo lỗi 'Number 1 is not a number'.

## Expected Result
Hệ thống phải thông báo lỗi 'Number 1 is not a number'.

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'`
