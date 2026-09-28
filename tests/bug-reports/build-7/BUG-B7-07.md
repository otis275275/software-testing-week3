---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Trừ hai số bằng nhau cho kết quả bằng 0 (Build 7)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-008
- **Requirement ID**: FR-ARITH-02

## Description
Trên Build 7, phát hiện lỗi khi thực thi test case `TC-ARITH-008` (Trừ hai số bằng nhau cho kết quả bằng 0). Answer thực tế: '-100', mong đợi: '0'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 7

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '7'.
2. Nhập '100' vào trường First number.
3. Nhập '100' vào trường Second number.
4. Chọn phép tính 'Subtract' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: '-100', mong đợi: '0'

## Expected Result
Kết quả mong đợi: Answer='0'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '-100', mong đợi: '0'`
