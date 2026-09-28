# Test Run: Basic Calculator - Build 2

## Thông tin đợt thực thi (Run Information)
- **Sprint / Release**: Milestone 1 - Build Verification
- **Build Tested**: Build 2 (Add and Concatenate swapped)
- **Ngày thực thi (Execution Date)**: 2026-09-28
- **Tester**: Trà Văn Sỹ
- **Môi trường (Environment)**: Playwright Chromium (Automated), URL: https://testsheepnz.github.io/BasicCalculator.html

## Tóm tắt kết quả (Execution Summary)
- **Tổng số Test Cases**: 58
- **Passed**: 35 (60.3%)
- **Failed**: 23 (39.7%)
- **Blocked**: 0 (0.0%)

## Bảng kết quả thực thi chi tiết (Test Execution Table)

| Test Case ID | Module | Tester | Result | Related Bug | Note / Actual Result |
|--------------|--------|--------|--------|-------------|----------------------|
| TC-ARITH-001 | Arithmetic | Trà Văn Sỹ | Fail | #[BUG-B2-01] | Answer thực tế: '2515', mong đợi: '40' |
| TC-ARITH-002 | Arithmetic | Trà Văn Sỹ | Fail | #[BUG-B2-02] | Answer thực tế: '-3018', mong đợi: '-12' |
| TC-ARITH-003 | Arithmetic | Trà Văn Sỹ | Fail | #[BUG-B2-03] | Answer thực tế: '12.345.66', mong đợi: '18' |
| TC-ARITH-004 | Arithmetic | Trà Văn Sỹ | Fail | #[BUG-B2-04] | Answer thực tế: '099', mong đợi: '99' |
| TC-ARITH-005 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=30 |
| TC-ARITH-006 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=-25 |
| TC-ARITH-007 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=7.5 |
| TC-ARITH-008 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=0 |
| TC-ARITH-009 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=96 |
| TC-ARITH-010 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=-42 |
| TC-ARITH-011 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=0 |
| TC-ARITH-012 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=10.5 |
| TC-ARITH-013 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=20 |
| TC-ARITH-014 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=3.5 |
| TC-ARITH-015 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer= |
| TC-ARITH-016 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=0 |
| TC-ARITH-017 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=10 |
| TC-ARITH-018 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=3 |
| TC-ARITH-019 | Arithmetic | Trà Văn Sỹ | Pass | None | Sau Toggle: Answer='3.5', Expected='3.5' |
| TC-ARITH-020 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=-5 |
| TC-ARITH-021 | Arithmetic | Trà Văn Sỹ | Fail | #[BUG-B2-05] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-ARITH-022 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer= |
| TC-ARITH-023 | Arithmetic | Trà Văn Sỹ | Pass | None | Answer=0 |
| TC-ARITH-024 | Arithmetic | Trà Văn Sỹ | Fail | #[BUG-B2-06] | Answer thực tế: '12345678901', mong đợi: '1234567891' |
| TC-ARITH-025 | Arithmetic | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CONCAT-001 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-07] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'HelloWorld' |
| TC-CONCAT-002 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-08] | Answer thực tế: '579', mong đợi: '123456' |
| TC-CONCAT-003 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-09] | Xuất hiện lỗi ngoài ý muốn: 'Number 2 is not a number'; Answer thực tế: '', mong đợi: 'World' |
| TC-CONCAT-004 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-10] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'Hello' |
| TC-CONCAT-005 | Concatenate | Trà Văn Sỹ | Pass | None | Answer=0 |
| TC-CONCAT-006 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-11] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'user@test.com' |
| TC-CONCAT-007 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-12] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'Good Morning' |
| TC-CONCAT-008 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-13] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'ABCdef' |
| TC-CONCAT-009 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-14] | Answer thực tế: '5.85', mong đợi: '3.142.71' |
| TC-CONCAT-010 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-15] | Answer thực tế: '-70', mong đợi: '-50-20' |
| TC-CONCAT-011 | Concatenate | Trà Văn Sỹ | Fail | #[BUG-B2-16] | Xuất hiện lỗi ngoài ý muốn: 'Number 1 is not a number'; Answer thực tế: '', mong đợi: 'TestTest' |
| TC-CLEAR-001 | Clear | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-002 | Clear | Trà Văn Sỹ | Pass | None | Answer='', Error='' |
| TC-CLEAR-003 | Clear | Trà Văn Sỹ | Pass | None | Answer='', Error='' |
| TC-CLEAR-004 | Clear | Trà Văn Sỹ | Pass | None | Answer='', Error='' |
| TC-CLEAR-005 | Clear | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-006 | Clear | Trà Văn Sỹ | Fail | #[BUG-B2-17] | Clear button bị disabled sau khi tính toán |
| TC-CLEAR-007 | Clear | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-008 | Clear | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-009 | Clear | Trà Văn Sỹ | Pass | None | Answer='' |
| TC-CLEAR-010 | Clear | Trà Văn Sỹ | Fail | #[BUG-B2-18] | Answer='1', Error='' |
| TC-CLEAR-011 | Clear | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-012 | Clear | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-013 | Clear | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-014 | Clear | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-015 | Clear | Trà Văn Sỹ | Pass | None | Sau Clear: Answer='', Error='' |
| TC-VALIDATE-001 | Input Validation | Trà Văn Sỹ | Fail | #[BUG-B2-19] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-002 | Input Validation | Trà Văn Sỹ | Fail | #[BUG-B2-20] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-003 | Input Validation | Trà Văn Sỹ | Fail | #[BUG-B2-21] | Lỗi thực tế: '', mong đợi: 'Number 2 is not a number' |
| TC-VALIDATE-004 | Input Validation | Trà Văn Sỹ | Pass | None | Answer= |
| TC-VALIDATE-005 | Input Validation | Trà Văn Sỹ | Pass | None | Answer= |
| TC-VALIDATE-006 | Input Validation | Trà Văn Sỹ | Fail | #[BUG-B2-22] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-007 | Input Validation | Trà Văn Sỹ | Fail | #[BUG-B2-23] | Answer thực tế: '12.52.5', mong đợi: '15' |

> **Hướng dẫn ghi nhận Result:**
> - **Pass**: Test case thực thi thành công, Actual Result khớp Expected Result.
> - **Fail**: Test case thực thi thất bại, cần tạo GitHub Bug Issue và thay mã `#[BUG-...]` bằng Issue ID thực tế (ví dụ `#18`).
> - **Blocked**: Không thể thực thi test case do lỗi rào cản.
