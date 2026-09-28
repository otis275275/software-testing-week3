---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Phép tính Concatenate bị hoán đổi thành phép cộng số học Add và báo lỗi chuỗi (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-001
- **Requirement ID**: FR-CONCAT-01

## Description
Trên Build 2, khi chọn phép tính Concatenate với 2 chuỗi 'Hello' và 'World', hệ thống lại chạy phép Add và báo lỗi 'Number 1 is not a number'.

## Severity / Priority
- **Severity**: critical
- **Priority**: P0

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 2

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '2'.
2. Nhập 'Hello' vào First number, 'World' vào Second number.
3. Chọn Operation 'Concatenate' và nhấn 'Calculate'.

## Actual Result
Xuất hiện lỗi 'Number 1 is not a number' và không nối chuỗi.

## Expected Result
Trường Answer phải hiển thị chuỗi 'HelloWorld' không qua validate số.

## Evidence
- **Console Log / Error Text**: `Xuất hiện lỗi: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'HelloWorld'`
