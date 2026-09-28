---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Không kiểm tra định dạng số khi nhập ký tự chữ cái (Build 1)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-004
- **Requirement ID**: FR-VAL-02

## Description
Nhập 'abc' vào First number và '15' vào Second number với phép Multiply, hệ thống không báo lỗi định dạng số.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 1

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '1'.
2. Nhập 'abc' vào First number, '15' vào Second number.
3. Chọn Operation 'Multiply' và nhấn 'Calculate'.

## Actual Result
Không hiển thị lỗi 'Number 1 is not a number'.

## Expected Result
Hiển thị thông báo lỗi 'Number 1 is not a number'.

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'`
