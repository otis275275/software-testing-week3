# Test Run: Basic Calculator - Build 7

## Thông tin đợt thực thi (Run Information)
- **Sprint / Release**: Milestone 1 - Build Verification
- **Build Tested**: Build 7 (Uses previous answer as first operand)
- **Ngày thực thi (Execution Date)**: 2026-09-28
- **Tester**: Nguyễn Nhật Duy
- **Môi trường (Environment)**: Playwright Chromium (Automated), URL: https://testsheepnz.github.io/BasicCalculator.html

## Tóm tắt kết quả (Execution Summary)
- **Tổng số Test Cases**: 58
- **Passed**: 23 (39.7%)
- **Failed**: 35 (60.3%)
- **Blocked**: 0 (0.0%)

## Bảng kết quả thực thi chi tiết (Test Execution Table)

| Test Case ID | Module | Tester | Result | Related Bug | Note / Actual Result |
|--------------|--------|--------|--------|-------------|----------------------|
| TC-ARITH-001 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-01] | Answer thực tế: '15', mong đợi: '40' |
| TC-ARITH-002 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-02] | Answer thực tế: '18', mong đợi: '-12' |
| TC-ARITH-003 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-03] | Answer thực tế: '5.66', mong đợi: '18' |
| TC-ARITH-004 | Arithmetic | Nguyễn Nhật Duy | Pass | None | Answer=99 |
| TC-ARITH-005 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-04] | Answer thực tế: '-20', mong đợi: '30' |
| TC-ARITH-006 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-05] | Answer thực tế: '-40', mong đợi: '-25' |
| TC-ARITH-007 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-06] | Answer thực tế: '-3.25', mong đợi: '7.5' |
| TC-ARITH-008 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-07] | Answer thực tế: '-100', mong đợi: '0' |
| TC-ARITH-009 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-08] | Answer thực tế: '0', mong đợi: '96' |
| TC-ARITH-010 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-09] | Answer thực tế: '0', mong đợi: '-42' |
| TC-ARITH-011 | Arithmetic | Nguyễn Nhật Duy | Pass | None | Answer=0 |
| TC-ARITH-012 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-10] | Answer thực tế: '0', mong đợi: '10.5' |
| TC-ARITH-013 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-11] | Answer thực tế: '0', mong đợi: '20' |
| TC-ARITH-014 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-12] | Answer thực tế: '0', mong đợi: '3.5' |
| TC-ARITH-015 | Arithmetic | Nguyễn Nhật Duy | Pass | None | Answer= |
| TC-ARITH-016 | Arithmetic | Nguyễn Nhật Duy | Pass | None | Answer=0 |
| TC-ARITH-017 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-13] | Answer thực tế: '0', mong đợi: '10' |
| TC-ARITH-018 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-14] | Answer thực tế: '0', mong đợi: '3' |
| TC-ARITH-019 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-15] | Sau Toggle: Answer='0', Expected='3.5' |
| TC-ARITH-020 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-16] | Answer thực tế: '0', mong đợi: '-5' |
| TC-ARITH-021 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-17] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-ARITH-022 | Arithmetic | Nguyễn Nhật Duy | Pass | None | Answer= |
| TC-ARITH-023 | Arithmetic | Nguyễn Nhật Duy | Pass | None | Answer=0 |
| TC-ARITH-024 | Arithmetic | Nguyễn Nhật Duy | Fail | #[BUG-B7-18] | Answer thực tế: '1', mong đợi: '1234567891' |
| TC-ARITH-025 | Arithmetic | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CONCAT-001 | Concatenate | Nguyễn Nhật Duy | Fail | #[BUG-B7-19] | Answer thực tế: 'World', mong đợi: 'HelloWorld' |
| TC-CONCAT-002 | Concatenate | Nguyễn Nhật Duy | Fail | #[BUG-B7-20] | Answer thực tế: '456', mong đợi: '123456' |
| TC-CONCAT-003 | Concatenate | Nguyễn Nhật Duy | Pass | None | Answer=World |
| TC-CONCAT-004 | Concatenate | Nguyễn Nhật Duy | Fail | #[BUG-B7-21] | Answer thực tế: '', mong đợi: 'Hello' |
| TC-CONCAT-005 | Concatenate | Nguyễn Nhật Duy | Pass | None | Answer= |
| TC-CONCAT-006 | Concatenate | Nguyễn Nhật Duy | Fail | #[BUG-B7-22] | Answer thực tế: 'test.com', mong đợi: 'user@test.com' |
| TC-CONCAT-007 | Concatenate | Nguyễn Nhật Duy | Fail | #[BUG-B7-23] | Answer thực tế: 'Morning', mong đợi: 'Good Morning' |
| TC-CONCAT-008 | Concatenate | Nguyễn Nhật Duy | Fail | #[BUG-B7-24] | Answer thực tế: 'def', mong đợi: 'ABCdef' |
| TC-CONCAT-009 | Concatenate | Nguyễn Nhật Duy | Fail | #[BUG-B7-25] | Answer thực tế: '2.71', mong đợi: '3.142.71' |
| TC-CONCAT-010 | Concatenate | Nguyễn Nhật Duy | Fail | #[BUG-B7-26] | Answer thực tế: '-20', mong đợi: '-50-20' |
| TC-CONCAT-011 | Concatenate | Nguyễn Nhật Duy | Fail | #[BUG-B7-27] | Answer thực tế: 'Test', mong đợi: 'TestTest' |
| TC-CLEAR-001 | Clear | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-002 | Clear | Nguyễn Nhật Duy | Pass | None | Answer='', Error='' |
| TC-CLEAR-003 | Clear | Nguyễn Nhật Duy | Pass | None | Answer='', Error='' |
| TC-CLEAR-004 | Clear | Nguyễn Nhật Duy | Pass | None | Answer='', Error='' |
| TC-CLEAR-005 | Clear | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-006 | Clear | Nguyễn Nhật Duy | Fail | #[BUG-B7-28] | Clear button bị disabled sau khi tính toán |
| TC-CLEAR-007 | Clear | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-008 | Clear | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-009 | Clear | Nguyễn Nhật Duy | Pass | None | Answer='' |
| TC-CLEAR-010 | Clear | Nguyễn Nhật Duy | Fail | #[BUG-B7-29] | Answer='0', Error='' |
| TC-CLEAR-011 | Clear | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-012 | Clear | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-013 | Clear | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-014 | Clear | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-015 | Clear | Nguyễn Nhật Duy | Pass | None | Sau Clear: Answer='', Error='' |
| TC-VALIDATE-001 | Input Validation | Nguyễn Nhật Duy | Fail | #[BUG-B7-30] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-002 | Input Validation | Nguyễn Nhật Duy | Fail | #[BUG-B7-31] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-003 | Input Validation | Nguyễn Nhật Duy | Fail | #[BUG-B7-32] | Lỗi thực tế: '', mong đợi: 'Number 2 is not a number' |
| TC-VALIDATE-004 | Input Validation | Nguyễn Nhật Duy | Fail | #[BUG-B7-33] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-005 | Input Validation | Nguyễn Nhật Duy | Pass | None | Answer= |
| TC-VALIDATE-006 | Input Validation | Nguyễn Nhật Duy | Fail | #[BUG-B7-34] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-007 | Input Validation | Nguyễn Nhật Duy | Fail | #[BUG-B7-35] | Answer thực tế: '2.5', mong đợi: '15' |

> **Hướng dẫn ghi nhận Result:**
> - **Pass**: Test case thực thi thành công, Actual Result khớp Expected Result.
> - **Fail**: Test case thực thi thất bại, cần tạo GitHub Bug Issue và thay mã `#[BUG-...]` bằng Issue ID thực tế (ví dụ `#18`).
> - **Blocked**: Không thể thực thi test case do lỗi rào cản.
