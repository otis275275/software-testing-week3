---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Cộng số âm bị nối chuỗi thay vì tính toán số học (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-002
- **Requirement ID**: FR-ARITH-01

## Description
Phép tính '-30 + 18' bị thực thi thành phép nối chuỗi '-3018' thay vì tính ra '-12'.

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
2. Nhập '-30' vào First number, '18' vào Second number.
3. Chọn Operation 'Add' và nhấn 'Calculate'.

## Actual Result
Trường Answer hiển thị '-3018'.

## Expected Result
Trường Answer phải hiển thị '-12'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '-3018', mong đợi: '-12'`
