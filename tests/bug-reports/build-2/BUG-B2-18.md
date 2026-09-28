---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Clear]: Tính toán lại sau khi Clear bị sai kết quả (Build 2)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CLEAR-010
- **Requirement ID**: FR-CLEAR-01

## Description
Sau khi bấm Clear và nhập '20 + 20', kết quả trả về '1' thay vì '40'.

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
2. Tính toán một phép tính bất kỳ và bấm Clear.
3. Nhập First number '20', Second number '20', chọn Add và bấm Calculate.

## Actual Result
Hiển thị kết quả '1'.

## Expected Result
Hiển thị kết quả '40'.

## Evidence
- **Console Log / Error Text**: `Answer='1', Error=''`
