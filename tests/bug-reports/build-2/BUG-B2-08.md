---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Nối hai giá trị số bị tính tổng thay vì nối chuỗi (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-002
- **Requirement ID**: FR-CONCAT-01

## Description
Khi chọn Concatenate cho '123' và '456', hệ thống tính tổng ra '579' thay vì nối thành '123456'.

## Severity / Priority
- **Severity**: critical
- **Priority**: P0

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 2

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '2'.
2. Nhập '123' vào First number, '456' vào Second number.
3. Chọn Operation 'Concatenate' và nhấn 'Calculate'.

## Actual Result
Trường Answer hiển thị '579' (kết quả phép cộng).

## Expected Result
Trường Answer phải hiển thị '123456'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '579', mong đợi: '123456'`
