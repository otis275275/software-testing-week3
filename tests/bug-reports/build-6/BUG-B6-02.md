---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][Clear]: Clear sau khi tính toán xong, sau đó tính tiếp bình thường (Build 6)"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-CLEAR-010
- **Requirement ID**: FR-CLEAR-01

## Description
Trên Build 6, phát hiện lỗi khi thực thi test case `TC-CLEAR-010` (Clear sau khi tính toán xong, sau đó tính tiếp bình thường). Answer='1', Error=''.

## Severity / Priority
- **Severity**: minor
- **Priority**: P2

## Environment
- **Browser / Version**: Playwright Chromium / Chrome
- **OS**: Windows / macOS
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: Build 6

## Steps to Reproduce
1. Mở trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html) và chọn Build '6'.
2. Nhập '10' vào trường First number.
3. Nhập '20' vào trường Second number.
4. Chọn phép tính 'Add' tại dropdown Operation.
5. Nhấn nút 'Calculate'.

## Actual Result
Hệ thống hoạt động không đúng: Answer='1', Error=''

## Expected Result
Kết quả mong đợi: Answer='40'

## Evidence
- **Console Log / Error Text**: `Answer='1', Error=''`
