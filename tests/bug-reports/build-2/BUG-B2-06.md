---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Cộng số 10 chữ số với 1 bị nối chuỗi (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-024
- **Requirement ID**: FR-ARITH-06

## Description
Phép tính '1234567890 + 1' trả về '12345678901' thay vì '1234567891'.

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
2. Nhập '1234567890' vào First number, '1' vào Second number.
3. Chọn Operation 'Add' và nhấn 'Calculate'.

## Actual Result
Trường Answer hiển thị '12345678901'.

## Expected Result
Trường Answer phải hiển thị '1234567891'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '12345678901', mong đợi: '1234567891'`
