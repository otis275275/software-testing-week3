---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Nối chuỗi có khoảng trắng (Build 7)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-007
- **Requirement ID**: FR-CONCAT-01

## Description
Trên Build 7, phát hiện lỗi khi thực thi test case `TC-CONCAT-007` (Nối chuỗi có khoảng trắng). Answer thực tế: 'Morning', mong đợi: 'Good Morning'.

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
2. Nhập 'Good ' vào trường First number.
3. Nhập 'Morning' vào trường Second number.
4. Chọn phép tính 'Concatenate' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: 'Morning', mong đợi: 'Good Morning'

## Expected Result
Kết quả mong đợi: Answer='Good Morning'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: 'Morning', mong đợi: 'Good Morning'`
