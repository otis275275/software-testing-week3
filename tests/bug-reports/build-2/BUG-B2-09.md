---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Concatenate chuỗi với Second number là chữ bị báo lỗi Number 2 (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-003
- **Requirement ID**: FR-CONCAT-01

## Description
First number rỗng, Second number là 'World' khi Concatenate bị báo lỗi 'Number 2 is not a number'.

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
2. Để trống First number, nhập 'World' vào Second number.
3. Chọn Operation 'Concatenate' và nhấn 'Calculate'.

## Actual Result
Báo lỗi 'Number 2 is not a number'.

## Expected Result
Hiển thị chuỗi 'World'.

## Evidence
- **Console Log / Error Text**: `Lỗi: 'Number 2 is not a number'`
