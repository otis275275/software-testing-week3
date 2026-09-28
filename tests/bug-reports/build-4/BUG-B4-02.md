---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Nhân hai số thập phân (Build 4)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-012
- **Requirement ID**: FR-ARITH-03

## Description
Trên Build 4, phát hiện lỗi khi thực thi test case `TC-ARITH-012` (Nhân hai số thập phân). Answer thực tế: '10', mong đợi: '10.5'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 4

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '4'.
2. Nhập '2.5' vào trường First number.
3. Nhập '4.2' vào trường Second number.
4. Chọn phép tính 'Multiply' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: '10', mong đợi: '10.5'

## Expected Result
Kết quả mong đợi: Answer='10.5'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '10', mong đợi: '10.5'`
