---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Bỏ trống trường First number khi thực hiện phép tính số học (Build 7)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-002
- **Requirement ID**: FR-VAL-01

## Description
Trên Build 7, phát hiện lỗi khi thực thi test case `TC-VALIDATE-002` (Bỏ trống trường First number khi thực hiện phép tính số học). Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'.

## Severity / Priority
- **Severity**: minor
- **Priority**: P2

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 7

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '7'.
2. Để trống trường First number.
3. Nhập '10' vào trường Second number.
4. Chọn phép tính 'Add' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'

## Expected Result
, thông báo lỗi: 'Number 1 is not a number'

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'`
