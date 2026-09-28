---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Hệ thống không kiểm tra tính hợp lệ của First number khi nhập chữ cái (Build 1)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-021
- **Requirement ID**: FR-ARITH-06

## Description
Trên Build 1, khi thực hiện phép tính số học (Add) với First number là chuỗi ký tự chữ ('abc') và Second number là số ('10'), hệ thống không kiểm tra và không hiển thị thông báo lỗi 'Number 1 is not a number'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 1

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '1'.
2. Nhập 'abc' vào trường First number.
3. Nhập '10' vào trường Second number.
4. Chọn phép tính 'Add' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống không hiển thị thông báo lỗi 'Number 1 is not a number'. Ô Answer không có kết quả hợp lệ hoặc bị tính sai.

## Expected Result
Hệ thống phải hiển thị thông báo lỗi màu đỏ 'Number 1 is not a number' và không thực hiện tính toán.

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'`
