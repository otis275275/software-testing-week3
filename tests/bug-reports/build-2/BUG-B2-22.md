---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Nhập khoảng trắng vào First number không bị bắt lỗi ở phép Add (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-006
- **Requirement ID**: FR-VAL-02

## Description
Nhập chuỗi khoảng trắng vào First number trong phép Add bị xem là chuỗi hợp lệ.

## Severity / Priority
- **Severity**: minor
- **Priority**: P2

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 2

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '2'.
2. Nhập '   ' vào First number, '20' vào Second number, chọn Add và nhấn Calculate.

## Actual Result
Không xuất hiện thông báo lỗi.

## Expected Result
Báo lỗi 'Number 1 is not a number'.

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'`
