# Test Run: [Tên đợt test / Sprint / Release]

## Thông tin đợt thực thi (Run Information)
- **Sprint / Release**: [Ví dụ: Sprint 1 / Release v1.0]
- **Ngày thực thi (Execution Date)**: [YYYY-MM-DD]
- **Tester**: [Tên người thực thi]
- **Môi trường (Environment)**: [Browser, OS, URL, Build/Commit ID]

## Bảng kết quả thực thi (Test Execution Table)

| Test Case ID | Module | Tester | Result | Related Bug | Note |
|--------------|--------|--------|--------|-------------|------|
| TC-[MODULE]-001 | [Module Name] | [Tester Name] | Pass | None | [Ghi chú nếu có] |
| TC-[MODULE]-002 | [Module Name] | [Tester Name] | Fail | #18 | [Mô tả ngắn lý do lỗi] |
| TC-[MODULE]-003 | [Module Name] | [Tester Name] | Blocked | #19 | [Lý do bị chặn thực thi] |
| TC-[MODULE]-004 | [Module Name] | [Tester Name] | Not Run | None | [Chưa thực thi] |

> **Hướng dẫn ghi nhận Result:**
> - **Pass**: Test case thực thi thành công, Actual Result khớp Expected Result.
> - **Fail**: Test case thực thi thất bại, bắt buộc tạo Bug Issue và ghi rõ `Related Bug` (#IssueNumber).
> - **Blocked**: Không thể thực thi test case do bị ảnh hưởng bởi lỗi khác (phải link Bug Issue rào cản).
> - **Not Run**: Chưa thực thi test case.
