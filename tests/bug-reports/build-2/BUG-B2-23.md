---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Cộng hai số thực hợp lệ bị nối chuỗi thành '12.52.5' (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-007
- **Requirement ID**: FR-VAL-02

## Description
Nhập 12.5 và 2.5 với phép Add bị nối chuỗi thành '12.52.5' thay vì '15'.

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
2. Nhập '12.5' vào First number, '2.5' vào Second number.
3. Chọn Operation 'Add' và nhấn 'Calculate'.

## Actual Result
Trường Answer hiển thị '12.52.5'.

## Expected Result
Trường Answer phải hiển thị '15'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '12.52.5', mong đợi: '15'`
