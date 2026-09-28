---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Concatenate hai số thập phân bị tính tổng thay vì nối chuỗi (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-009
- **Requirement ID**: FR-CONCAT-01

## Description
Nối chuỗi '3.14' và '2.71' bị tính tổng thành '5.85' thay vì '3.142.71'.

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
2. Nhập '3.14' vào First number, '2.71' vào Second number.
3. Chọn Operation 'Concatenate' và nhấn 'Calculate'.

## Actual Result
Trường Answer hiển thị '5.85'.

## Expected Result
Trường Answer phải hiển thị '3.142.71'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '5.85', mong đợi: '3.142.71'`
