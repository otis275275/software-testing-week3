---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Concatenate chuỗi với First number là chữ bị báo lỗi Number 1 (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-004
- **Requirement ID**: FR-CONCAT-01

## Description
First number là 'Hello', Second number rỗng khi Concatenate bị báo lỗi 'Number 1 is not a number'.

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
2. Nhập 'Hello' vào First number, để trống Second number.
3. Chọn Operation 'Concatenate' và nhấn 'Calculate'.

## Actual Result
Báo lỗi 'Number 1 is not a number'.

## Expected Result
Hiển thị chuỗi 'Hello'.

## Evidence
- **Console Log / Error Text**: `Lỗi: 'Number 1 is not a number'`
