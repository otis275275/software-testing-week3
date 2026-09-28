---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Clear]: Nút Clear bị vô hiệu hóa sau phép chia cho 0 (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CLEAR-006
- **Requirement ID**: FR-CLEAR-01

## Description
Tương tự Build 1, sau khi thực hiện phép chia cho 0 trên Build 2, nút Clear bị khóa (disabled).

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
2. Nhập '10' vào First number, '0' vào Second number.
3. Chọn Operation 'Divide' và nhấn 'Calculate'.

## Actual Result
Nút Clear bị disabled, không thể bấm.

## Expected Result
Nút Clear phải nhấn được bình thường.

## Evidence
- **Console Log / Error Text**: `Clear button bị disabled sau khi tính toán`
