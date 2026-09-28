---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Concatenate]: Nối hai số thập phân dạng chuỗi (Build 8)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CONCAT-009
- **Requirement ID**: FR-CONCAT-01

## Description
Trên Build 8, phát hiện lỗi khi thực thi test case `TC-CONCAT-009` (Nối hai số thập phân dạng chuỗi). Answer thực tế: '2.713.14', mong đợi: '3.142.71'.

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
2. Nhập '3.14' vào trường First number.
3. Nhập '2.71' vào trường Second number.
4. Chọn phép tính 'Concatenate' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer thực tế: '2.713.14', mong đợi: '3.142.71'

## Expected Result
Kết quả mong đợi: Answer='3.142.71'

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '2.713.14', mong đợi: '3.142.71'`
