---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Bỏ trống cả hai trường dữ liệu đầu vào (Build 4)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-001
- **Requirement ID**: FR-VAL-01

## Description
Trên Build 4, phát hiện lỗi khi thực thi test case `TC-VALIDATE-001` (Bỏ trống cả hai trường dữ liệu đầu vào). Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'.

## Severity / Priority
- **Severity**: minor
- **Priority**: P2

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 4

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '4'.
2. Để trống trường First number.
3. Để trống trường Second number.
4. Chọn phép tính 'Add' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'

## Expected Result
, thông báo lỗi: 'Number 1 is not a number'

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'`
