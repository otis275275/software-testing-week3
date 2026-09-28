# Test Run: Basic Calculator - Build 3

## Thông tin đợt thực thi (Run Information)
- **Sprint / Release**: Milestone 1 - Build Verification
- **Build Tested**: Build 3 (Always treats like a number)
- **Ngày thực thi (Execution Date)**: 2026-09-28
- **Tester**: Huỳnh Đức Thịnh
- **Môi trường (Environment)**: Playwright Chromium (Automated), URL: https://testsheepnz.github.io/BasicCalculator.html

## Tóm tắt kết quả (Execution Summary)
- **Tổng số Test Cases**: 58
- **Passed**: 45 (77.6%)
- **Failed**: 13 (22.4%)
- **Blocked**: 0 (0.0%)

## Bảng kết quả thực thi chi tiết (Test Execution Table)

| Test Case ID | Module | Tester | Result | Related Bug | Note / Actual Result |
|--------------|--------|--------|--------|-------------|----------------------|
| TC-ARITH-001 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=40 |
| TC-ARITH-002 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=-12 |
| TC-ARITH-003 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=18 |
| TC-ARITH-004 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=99 |
| TC-ARITH-005 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=30 |
| TC-ARITH-006 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=-25 |
| TC-ARITH-007 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=7.5 |
| TC-ARITH-008 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=0 |
| TC-ARITH-009 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=96 |
| TC-ARITH-010 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=-42 |
| TC-ARITH-011 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=0 |
| TC-ARITH-012 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=10.5 |
| TC-ARITH-013 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=20 |
| TC-ARITH-014 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=3.5 |
| TC-ARITH-015 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer= |
| TC-ARITH-016 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=0 |
| TC-ARITH-017 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=10 |
| TC-ARITH-018 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=3 |
| TC-ARITH-019 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Sau Toggle: Answer='3.5', Expected='3.5' |
| TC-ARITH-020 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=-5 |
| TC-ARITH-021 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer= |
| TC-ARITH-022 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer= |
| TC-ARITH-023 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=0 |
| TC-ARITH-024 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Answer=1234567891 |
| TC-ARITH-025 | Arithmetic | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CONCAT-001 | Concatenate | Huỳnh Đức Thịnh | Fail | #[BUG-B3-01] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'HelloWorld' |
| TC-CONCAT-002 | Concatenate | Huỳnh Đức Thịnh | Pass | None | Answer=123456 |
| TC-CONCAT-003 | Concatenate | Huỳnh Đức Thịnh | Fail | #[BUG-B3-02] | Xuất hiện lỗi ngoài ý muốn: 'Number 2 is not a number'; Answer thực tế: '', mong đợi: 'World' |
| TC-CONCAT-004 | Concatenate | Huỳnh Đức Thịnh | Fail | #[BUG-B3-03] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'Hello' |
| TC-CONCAT-005 | Concatenate | Huỳnh Đức Thịnh | Pass | None | Answer= |
| TC-CONCAT-006 | Concatenate | Huỳnh Đức Thịnh | Fail | #[BUG-B3-04] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'user@test.com' |
| TC-CONCAT-007 | Concatenate | Huỳnh Đức Thịnh | Fail | #[BUG-B3-05] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'Good Morning' |
| TC-CONCAT-008 | Concatenate | Huỳnh Đức Thịnh | Fail | #[BUG-B3-06] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'ABCdef' |
| TC-CONCAT-009 | Concatenate | Huỳnh Đức Thịnh | Pass | None | Answer=3.142.71 |
| TC-CONCAT-010 | Concatenate | Huỳnh Đức Thịnh | Pass | None | Answer=-50-20 |
| TC-CONCAT-011 | Concatenate | Huỳnh Đức Thịnh | Fail | #[BUG-B3-07] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'TestTest' |
| TC-CLEAR-001 | Clear | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-002 | Clear | Huỳnh Đức Thịnh | Pass | None | Answer='', Error='' |
| TC-CLEAR-003 | Clear | Huỳnh Đức Thịnh | Pass | None | Answer='', Error='' |
| TC-CLEAR-004 | Clear | Huỳnh Đức Thịnh | Pass | None | Answer='', Error='' |
| TC-CLEAR-005 | Clear | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-006 | Clear | Huỳnh Đức Thịnh | Fail | #[BUG-B3-08] | Clear button bị disabled sau khi tính toán |
| TC-CLEAR-007 | Clear | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-008 | Clear | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-009 | Clear | Huỳnh Đức Thịnh | Pass | None | Answer='' |
| TC-CLEAR-010 | Clear | Huỳnh Đức Thịnh | Fail | #[BUG-B3-09] | Answer='1', Error='' |
| TC-CLEAR-011 | Clear | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-012 | Clear | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-013 | Clear | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-014 | Clear | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-015 | Clear | Huỳnh Đức Thịnh | Pass | None | Sau Clear: Answer='', Error='' |
| TC-VALIDATE-001 | Input Validation | Huỳnh Đức Thịnh | Fail | #[BUG-B3-10] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-002 | Input Validation | Huỳnh Đức Thịnh | Fail | #[BUG-B3-11] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-003 | Input Validation | Huỳnh Đức Thịnh | Fail | #[BUG-B3-12] | Lỗi thực tế: '', mong đợi: 'Number 2 is not a number' |
| TC-VALIDATE-004 | Input Validation | Huỳnh Đức Thịnh | Pass | None | Answer= |
| TC-VALIDATE-005 | Input Validation | Huỳnh Đức Thịnh | Pass | None | Answer= |
| TC-VALIDATE-006 | Input Validation | Huỳnh Đức Thịnh | Fail | #[BUG-B3-13] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-007 | Input Validation | Huỳnh Đức Thịnh | Pass | None | Answer=15 |

> **Hướng dẫn ghi nhận Result:**
> - **Pass**: Test case thực thi thành công, Actual Result khớp Expected Result.
> - **Fail**: Test case thực thi thất bại, cần tạo GitHub Bug Issue và thay mã `#[BUG-...]` bằng Issue ID thực tế (ví dụ `#18`).
> - **Blocked**: Không thể thực thi test case do lỗi rào cản.
