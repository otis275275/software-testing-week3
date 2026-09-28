---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Clear]: Tính toán lại sau khi Clear bị sai kết quả (Build 1)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CLEAR-010
- **Requirement ID**: FR-CLEAR-01

## Description
Sau khi tính toán xong và bấm Clear, người dùng nhập phép tính mới ('20 + 20') thì kết quả trả về sai ('1') thay vì '40'.

## Severity / Priority
- **Severity**: major
- **Priority**: P1

## Environment
- **Browser / Version**: Playwright Chromium / Chrome 124
- **OS**: Windows 11
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 1

## Steps to Reproduce
1. Mở trang web Basic Calculator, chọn Build '1'.
2. Nhập First number '10', Second number '20', chọn Add và bấm Calculate.
3. Bấm nút Clear.
4. Nhập First number '20', Second number '20', bấm Calculate.

## Actual Result
Ô Answer hiển thị giá trị '1'.

## Expected Result
Ô Answer phải hiển thị giá trị '40'.

## Evidence
- **Console Log / Error Text**: `Answer thực tế: '1', mong đợi: '40'`
