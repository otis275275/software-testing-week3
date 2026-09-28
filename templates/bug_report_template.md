---
name: Bug Report
about: Báo cáo lỗi phát hiện từ quá trình kiểm thử
title: "[BUG][<Module>]: <Tóm tắt lỗi ngắn gọn>"
labels: ["type: bug", "status: new"]
assignees: ""
---

## Found by Test Case / Requirement
- **Found by Test Case ID**: TC-[MODULE]-[NUMBER] (Ví dụ: `TC-ARITH-015`)
- **Requirement ID**: FR-[MODULE]-[NUMBER] (Ví dụ: `FR-ARITH-04`)

## Description
[Mô tả ngắn gọn về hiện tượng lỗi phát sinh]

## Severity / Priority
- **Severity**: [blocker / critical / major / minor / trivial]
- **Priority**: [P0 / P1 / P2 / P3]

## Environment
- **Browser / Version**: [Ví dụ: Chrome 124, Firefox 125]
- **OS**: [Ví dụ: Windows 11, macOS Sonoma]
- **URL**: https://testsheepnz.github.io/BasicCalculator.html
- **Build / Version**: [Ví dụ: Build 1, Build 6, Build 8]

## Steps to Reproduce
1. Mở trang web ứng dụng và chọn Build `[Số Build]`.
2. Nhập `[Giá trị 1]` vào trường First number.
3. Nhập `[Giá trị 2]` vào trường Second number.
4. Chọn phép tính `[Tên phép tính]` tại Operation.
5. Nhấn nút **Calculate**.

## Actual Result
[Hệ thống đang hoạt động sai như thế nào? Ví dụ: Không kiểm tra số hợp lệ, kết quả tính toán ra NaN, vòng xoay loading bị treo vĩnh viễn...]

## Expected Result
[Hệ thống đúng phải hoạt động như thế nào theo yêu cầu nghiệp vụ / Test case?]

## Evidence
- **Screenshot / Video**: ![Mô tả ảnh](đường_dẫn_ảnh_hoặc_paste_trực_tiếp_vào_github_issue)
- **Console Log / Error Text**: `[Nội dung log lỗi hoặc text hiển thị sai]`
