---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Cộng với số 0 bị nối chuỗi (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-004
- **Requirement ID**: FR-ARITH-01

## Description
Phép cộng '0 + 99' bị nối chuỗi thành '099' thay vì '99'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 2

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '2'.
2. Nhập '0' vào First number, '99' vào Second number.
3. Chọn Operation 'Add' và nhấn 'Calculate'.

## Actual Result
Trường Answer hiển thị '099'.

## Expected Result
Trường Answer phải hiển thị '99'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '099', mong đợi: '99'`
