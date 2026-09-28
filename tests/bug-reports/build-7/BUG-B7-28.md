---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Clear]: Clear sau khi thực hiện phép chia cho 0 (Build 7)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CLEAR-006
- **Requirement ID**: FR-CLEAR-01

## Description
Trên Build 7, phát hiện lỗi khi thực thi test case `TC-CLEAR-006` (Clear sau khi thực hiện phép chia cho 0). Clear button bị disabled sau khi tính toán.

## Severity / Priority
- **Severity**: critical
- **Priority**: P0

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 7

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '7'.
2. Nhập '10' vào trường First number.
3. Nhập '0' vào trường Second number.
4. Chọn phép tính 'Divide' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Clear button bị disabled sau khi tính toán

## Expected Result


## Evidence
- **Console Log / Error Text**: `Clear button bị disabled sau khi tính toán`
