---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Arithmetic]: Phép tính Add bị hoán đổi thành phép nối chuỗi Concatenate (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-ARITH-001
- **Requirement ID**: FR-ARITH-01

## Description
Trên Build 2, khi chọn phép tính Add giữa 2 số '25' và '15', hệ thống lại thực hiện phép nối chuỗi và trả về '2515' thay vì '40'.

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
2. Nhập '25' vào First number, '15' vào Second number.
3. Chọn Operation 'Add' và nhấn 'Calculate'.

## Actual Result
Trường Answer hiển thị chuỗi ghép '2515'.

## Expected Result
Trường Answer phải hiển thị kết quả tổng '40'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '2515', mong đợi: '40'`
