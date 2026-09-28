---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Nhập số đạt giới hạn độ dài tối đa 10 ký tự (Build 7)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-024
- **Requirement ID**: FR-ARITH-06

## Description
Trên Build 7, phát hiện lỗi khi thực thi test case `TC-ARITH-024` (Nhập số đạt giới hạn độ dài tối đa 10 ký tự). Answer thực tế: '1', mong đợi: '1234567891'.

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
2. Nhập '1234567890' vào trường First number.
3. Nhập '1' vào trường Second number.
4. Chọn phép tính 'Add' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: '1', mong đợi: '1234567891'

## Expected Result
Kết quả mong đợi: Answer='1234567891'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '1', mong đợi: '1234567891'`
