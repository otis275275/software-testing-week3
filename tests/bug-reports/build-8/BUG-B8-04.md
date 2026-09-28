---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Chia hết hai số nguyên dương (kết quả nguyên) (Build 8)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-013
- **Requirement ID**: FR-ARITH-04

## Description
Trên Build 8, phát hiện lỗi khi thực thi test case `TC-ARITH-013` (Chia hết hai số nguyên dương (kết quả nguyên)). Answer thực tế: '0.05', mong đợi: '20'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 8

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '8'.
2. Nhập '80' vào trường First number.
3. Nhập '4' vào trường Second number.
4. Chọn phép tính 'Divide' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: '0.05', mong đợi: '20'

## Expected Result
Kết quả mong đợi: Answer='20'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '0.05', mong đợi: '20'`
