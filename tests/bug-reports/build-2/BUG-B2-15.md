---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Concatenate hai chuỗi số âm bị tính tổng thành '-70' (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-010
- **Requirement ID**: FR-CONCAT-01

## Description
Nối chuỗi '-50' và '-20' bị tính tổng '-70' thay vì nối thành '-50-20'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 2

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '2'.
2. Nhập '-50' vào First number, '-20' vào Second number.
3. Chọn Operation 'Concatenate' và nhấn 'Calculate'.

## Actual Result
Trường Answer hiển thị '-70'.

## Expected Result
Trường Answer phải hiển thị '-50-20'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '-70', mong đợi: '-50-20'`
