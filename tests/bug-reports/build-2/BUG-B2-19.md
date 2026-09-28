---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Input Validation]: Không hiển thị lỗi khi để trống cả hai trường số ở phép Add (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-VALIDATE-001
- **Requirement ID**: FR-VAL-01

## Description
Do phép Add bị chạy theo cơ chế Concatenate trong Build 2, để trống 2 ô số không bị bắt lỗi.

## Severity / Priority
- **Severity**: minor
- **Priority**: P2

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 2

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '2'.
2. Để trống cả 2 ô số, chọn Add và nhấn Calculate.

## Actual Result
Không xuất hiện thông báo lỗi.

## Expected Result
Hệ thống phải báo lỗi 'Number 1 is not a number'.

## Evidence
- **Console Log / Error Text**: `Lỗi thực tế: '', mong đợi: 'Number 1 is not a number'`
