---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Concatenate chuỗi có khoảng trắng bị báo lỗi số (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-007
- **Requirement ID**: FR-CONCAT-01

## Description
Nối chuỗi 'Good ' và 'Morning' bị hệ thống bắt lỗi số.

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
2. Nhập 'Good ' vào First number, 'Morning' vào Second number.
3. Chọn Operation 'Concatenate' và nhấn 'Calculate'.

## Actual Result
Báo lỗi 'Number 1 is not a number'.

## Expected Result
Hiển thị 'Good Morning'.

## Evidence
- **Console Log / Error Text**: `Lỗi: 'Number 1 is not a number'`
