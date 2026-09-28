---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Không validate dữ liệu số khi chọn phép Add do bị đổi sang Concatenate (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-021
- **Requirement ID**: FR-ARITH-06

## Description
Do phép Add bị đổi thành Concatenate trong Build 2, hệ thống xem 'abc' là chuỗi hợp lệ và không báo lỗi 'Number 1 is not a number'.

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
2. Nhập 'abc' vào First number, '10' vào Second number.
3. Chọn Operation 'Add' và nhấn 'Calculate'.

## Actual Result
Không hiển thị lỗi 'Number 1 is not a number'.

## Expected Result
Phép toán Add phải bắt buộc kiểm tra tính hợp lệ của số.

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'`
