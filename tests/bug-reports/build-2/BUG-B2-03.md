---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Cộng hai số thập phân bị nối chuỗi (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-003
- **Requirement ID**: FR-ARITH-01

## Description
Phép cộng '12.34 + 5.66' bị nối chuỗi thành '12.345.66' thay vì tính ra '18'.

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
2. Nhập '12.34' vào First number, '5.66' vào Second number.
3. Chọn Operation 'Add' và nhấn 'Calculate'.

## Actual Result
Trường Answer hiển thị '12.345.66'.

## Expected Result
Trường Answer phải hiển thị '18'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '12.345.66', mong đợi: '18'`
