---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Không báo lỗi khi để trống trường Second number (Build 1)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-003
- **Requirement ID**: FR-VAL-01

## Description
Khi nhập First number = 10 và để trống Second number với phép cộng, hệ thống không bắt lỗi Second number trống.

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
2. Nhập '10' vào First number, để trống Second number.
3. Chọn Operation 'Add' và nhấn 'Calculate'.

## Actual Result
Không xuất hiện lỗi 'Number 2 is not a number'.

## Expected Result
Hệ thống phải thông báo lỗi 'Number 2 is not a number'.

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 2 is not a number'`
