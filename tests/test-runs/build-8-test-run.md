# Test Run: Basic Calculator - Build 8

## Thông tin đợt thực thi (Run Information)
- **Sprint / Release**: Milestone 1 - Build Verification
- **Build Tested**: Build 8 (Switches number 1 and 2 around)
- **Ngày thực thi (Execution Date)**: 2026-09-28
- **Tester**: Lê Công Phúc
- **Môi trường (Environment)**: Playwright Chromium (Automated), URL: https://testsheepnz.github.io/BasicCalculator.html

## Tóm tắt kết quả (Execution Summary)
- **Tổng số Test Cases**: 58
- **Passed**: 31 (53.4%)
- **Failed**: 27 (46.6%)
- **Blocked**: 0 (0.0%)

## Bảng kết quả thực thi chi tiết (Test Execution Table)

| Test Case ID | Module | Tester | Result | Related Bug | Note / Actual Result |
|--------------|--------|--------|--------|-------------|----------------------|
| TC-ARITH-001 | Arithmetic | Lê Công Phúc | Pass | None | Answer=40 |
| TC-ARITH-002 | Arithmetic | Lê Công Phúc | Pass | None | Answer=-12 |
| TC-ARITH-003 | Arithmetic | Lê Công Phúc | Pass | None | Answer=18 |
| TC-ARITH-004 | Arithmetic | Lê Công Phúc | Pass | None | Answer=99 |
| TC-ARITH-005 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-01] | Answer thực tế: '-30', mong đợi: '30' |
| TC-ARITH-006 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-02] | Answer thực tế: '25', mong đợi: '-25' |
| TC-ARITH-007 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-03] | Answer thực tế: '-7.5', mong đợi: '7.5' |
| TC-ARITH-008 | Arithmetic | Lê Công Phúc | Pass | None | Answer=0 |
| TC-ARITH-009 | Arithmetic | Lê Công Phúc | Pass | None | Answer=96 |
| TC-ARITH-010 | Arithmetic | Lê Công Phúc | Pass | None | Answer=-42 |
| TC-ARITH-011 | Arithmetic | Lê Công Phúc | Pass | None | Answer=0 |
| TC-ARITH-012 | Arithmetic | Lê Công Phúc | Pass | None | Answer=10.5 |
| TC-ARITH-013 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-04] | Answer thực tế: '0.05', mong đợi: '20' |
| TC-ARITH-014 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-05] | Answer thực tế: '0.2857142857142857', mong đợi: '3.5' |
| TC-ARITH-015 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-06] | Lỗi thực tế: '', mong đợi: 'Divide by zero error!' |
| TC-ARITH-016 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-07] | Xuất hiện lỗi ngoài ý muốn: 'Divide by zero error!'; Answer thực tế: '', mong đợi: '0' |
| TC-ARITH-017 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-08] | Answer thực tế: '0.1', mong đợi: '10' |
| TC-ARITH-018 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-09] | Answer thực tế: '0', mong đợi: '3' |
| TC-ARITH-019 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-10] | Sau Toggle: Answer='0.2857142857142857', Expected='3.5' |
| TC-ARITH-020 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-11] | Answer thực tế: '0', mong đợi: '-5' |
| TC-ARITH-021 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-12] | Lỗi thực tế: 'Number 2 is not a number', mong đợi: 'Number 1 is not a number' |
| TC-ARITH-022 | Arithmetic | Lê Công Phúc | Fail | #[BUG-B8-13] | Lỗi thực tế: 'Number 1 is not a number', mong đợi: 'Number 2 is not a number' |
| TC-ARITH-023 | Arithmetic | Lê Công Phúc | Pass | None | Answer=0 |
| TC-ARITH-024 | Arithmetic | Lê Công Phúc | Pass | None | Answer=1234567891 |
| TC-ARITH-025 | Arithmetic | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CONCAT-001 | Concatenate | Lê Công Phúc | Fail | #[BUG-B8-14] | Answer thực tế: 'WorldHello', mong đợi: 'HelloWorld' |
| TC-CONCAT-002 | Concatenate | Lê Công Phúc | Fail | #[BUG-B8-15] | Answer thực tế: '456123', mong đợi: '123456' |
| TC-CONCAT-003 | Concatenate | Lê Công Phúc | Pass | None | Answer=World |
| TC-CONCAT-004 | Concatenate | Lê Công Phúc | Pass | None | Answer=Hello |
| TC-CONCAT-005 | Concatenate | Lê Công Phúc | Pass | None | Answer= |
| TC-CONCAT-006 | Concatenate | Lê Công Phúc | Fail | #[BUG-B8-16] | Answer thực tế: 'test.comuser@', mong đợi: 'user@test.com' |
| TC-CONCAT-007 | Concatenate | Lê Công Phúc | Fail | #[BUG-B8-17] | Answer thực tế: 'MorningGood ', mong đợi: 'Good Morning' |
| TC-CONCAT-008 | Concatenate | Lê Công Phúc | Fail | #[BUG-B8-18] | Answer thực tế: 'defABC', mong đợi: 'ABCdef' |
| TC-CONCAT-009 | Concatenate | Lê Công Phúc | Fail | #[BUG-B8-19] | Answer thực tế: '2.713.14', mong đợi: '3.142.71' |
| TC-CONCAT-010 | Concatenate | Lê Công Phúc | Fail | #[BUG-B8-20] | Answer thực tế: '-20-50', mong đợi: '-50-20' |
| TC-CONCAT-011 | Concatenate | Lê Công Phúc | Pass | None | Answer=TestTest |
| TC-CLEAR-001 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-002 | Clear | Lê Công Phúc | Pass | None | Answer='', Error='' |
| TC-CLEAR-003 | Clear | Lê Công Phúc | Pass | None | Answer='', Error='' |
| TC-CLEAR-004 | Clear | Lê Công Phúc | Pass | None | Answer='', Error='' |
| TC-CLEAR-005 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-006 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-007 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-008 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-009 | Clear | Lê Công Phúc | Pass | None | Answer='' |
| TC-CLEAR-010 | Clear | Lê Công Phúc | Fail | #[BUG-B8-21] | Answer='1', Error='' |
| TC-CLEAR-011 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-012 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-013 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-014 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-015 | Clear | Lê Công Phúc | Pass | None | Sau Clear: Answer='', Error='' |
| TC-VALIDATE-001 | Input Validation | Lê Công Phúc | Fail | #[BUG-B8-22] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-002 | Input Validation | Lê Công Phúc | Fail | #[BUG-B8-23] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-003 | Input Validation | Lê Công Phúc | Fail | #[BUG-B8-24] | Lỗi thực tế: '', mong đợi: 'Number 2 is not a number' |
| TC-VALIDATE-004 | Input Validation | Lê Công Phúc | Fail | #[BUG-B8-25] | Lỗi thực tế: 'Number 2 is not a number', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-005 | Input Validation | Lê Công Phúc | Fail | #[BUG-B8-26] | Lỗi thực tế: 'Number 1 is not a number', mong đợi: 'Number 2 is not a number' |
| TC-VALIDATE-006 | Input Validation | Lê Công Phúc | Fail | #[BUG-B8-27] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-007 | Input Validation | Lê Công Phúc | Pass | None | Answer=15 |

> **Hướng dẫn ghi nhận Result:**
> - **Pass**: Test case thực thi thành công, Actual Result khớp Expected Result.
> - **Fail**: Test case thực thi thất bại, cần tạo GitHub Bug Issue và thay mã `#[BUG-...]` bằng Issue ID thực tế (ví dụ `#18`).
> - **Blocked**: Không thể thực thi test case do lỗi rào cản.
