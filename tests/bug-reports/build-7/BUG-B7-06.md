---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Trừ hai số thập phân (Build 7)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-007
- **Requirement ID**: FR-ARITH-02

## Description
Trên Build 7, phát hiện lỗi khi thực thi test case `TC-ARITH-007` (Trừ hai số thập phân). Answer thực tế: '-3.25', mong đợi: '7.5'.

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
2. Nhập '10.75' vào trường First number.
3. Nhập '3.25' vào trường Second number.
4. Chọn phép tính 'Subtract' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: '-3.25', mong đợi: '7.5'

## Expected Result
Kết quả mong đợi: Answer='7.5'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '-3.25', mong đợi: '7.5'`
