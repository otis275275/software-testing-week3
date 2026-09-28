---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Clear]: Clear khi tất cả các trường đang trống (Build 5)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CLEAR-004
- **Requirement ID**: FR-CLEAR-01

## Description
Trên Build 5, phát hiện lỗi khi thực thi test case `TC-CLEAR-004` (Clear khi tất cả các trường đang trống). Clear button bị disabled (không thể bấm).

## Severity / Priority
- **Severity**: critical
- **Priority**: P0

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 5

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '5'.
2. Để trống trường First number.
3. Để trống trường Second number.
4. Chọn phép tính 'Add' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Clear button bị disabled (không thể bấm)

## Expected Result


## Evidence
- **Console Log / Error Text**: `Clear button bị disabled (không thể bấm)`
