---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Kiểm tra dữ liệu hợp lệ (Số nguyên và số thực) (Build 7)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-007
- **Requirement ID**: FR-VAL-02

## Description
Trên Build 7, phát hiện lỗi khi thực thi test case `TC-VALIDATE-007` (Kiểm tra dữ liệu hợp lệ (Số nguyên và số thực)). Answer thực tế: '2.5', mong đợi: '15'.

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
2. Nhập '12.5' vào trường First number.
3. Nhập '2.5' vào trường Second number.
4. Chọn phép tính 'Add' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: '2.5', mong đợi: '15'

## Expected Result
Kết quả mong đợi: Answer='15'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '2.5', mong đợi: '15'`
