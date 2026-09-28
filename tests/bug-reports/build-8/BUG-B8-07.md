---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Chia số 0 cho một số khác 0 (Build 8)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-016
- **Requirement ID**: FR-ARITH-04

## Description
Trên Build 8, phát hiện lỗi khi thực thi test case `TC-ARITH-016` (Chia số 0 cho một số khác 0). Xuất hiện lỗi ngoài ý muốn: 'Divide by zero error!'; Answer thực tế: '', mong đợi: '0'.

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
2. Nhập '0' vào trường First number.
3. Nhập '25' vào trường Second number.
4. Chọn phép tính 'Divide' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Xuất hiện lỗi ngoài ý muốn: 'Divide by zero error!'; Answer thực tế: '', mong đợi: '0'

## Expected Result
Kết quả mong đợi: Answer='0'

## Evidence
- **Console Log / Error Text**: `Xuất hiện lỗi ngoài ý muốn: 'Divide by zero error!'; Answer thực tế: '', mong đợi: '0'`
