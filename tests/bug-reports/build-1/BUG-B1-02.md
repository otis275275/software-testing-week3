---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Hệ thống không kiểm tra tính hợp lệ của Second number khi nhập ký tự đặc biệt (Build 1)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-022
- **Requirement ID**: FR-ARITH-06

## Description
Trên Build 1, khi thực hiện phép tính Subtract với Second number chứa ký tự đặc biệt ('@#xyz'), hệ thống bỏ qua kiểm tra số hợp lệ và không báo lỗi.

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
2. Nhập '50' vào trường First number.
3. Nhập '@#xyz' vào trường Second number.
4. Chọn phép tính 'Subtract' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Không xuất hiện thông báo lỗi 'Number 2 is not a number'.

## Expected Result
Hệ thống phải chặn tính toán và hiển thị thông báo lỗi 'Number 2 is not a number'.

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 2 is not a number'`
