---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Không hiển thị thông báo lỗi khi để trống cả hai trường số đầu vào (Build 1)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-001
- **Requirement ID**: FR-VAL-01

## Description
Khi người dùng để trống cả First number và Second number rồi bấm Calculate với phép cộng, hệ thống không báo lỗi dữ liệu đầu vào.

## Severity / Priority
- **Severity**: minor
- **Priority**: P2

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 1

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '1'.
2. Để trống trường First number và Second number.
3. Chọn phép tính 'Add' và nhấn 'Calculate'.

## Actual Result
Không có thông báo lỗi 'Number 1 is not a number' hiển thị.

## Expected Result
Hệ thống phải hiển thị thông báo lỗi yêu cầu nhập số hợp lệ.

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'`
