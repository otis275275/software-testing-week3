# Test Run: Basic Calculator - Build 6

## Thông tin đợt thực thi (Run Information)
- **Sprint / Release**: Milestone 1 - Build Verification
- **Build Tested**: Build 6 (Divide by zero not checked)
- **Ngày thực thi (Execution Date)**: 2026-09-28
- **Tester**: Lê Trung Thành Đạt
- **Môi trường (Environment)**: Playwright Chromium (Automated), URL: https://testsheepnz.github.io/BasicCalculator.html

## Tóm tắt kết quả (Execution Summary)
- **Tổng số Test Cases**: 58
- **Passed**: 52 (89.7%)
- **Failed**: 6 (10.3%)
- **Blocked**: 0 (0.0%)

## Bảng kết quả thực thi chi tiết (Test Execution Table)

| Test Case ID | Module | Tester | Result | Related Bug | Note / Actual Result |
|--------------|--------|--------|--------|-------------|----------------------|
| TC-ARITH-001 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=40 |
| TC-ARITH-002 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=-12 |
| TC-ARITH-003 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=18 |
| TC-ARITH-004 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=99 |
| TC-ARITH-005 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=30 |
| TC-ARITH-006 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=-25 |
| TC-ARITH-007 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=7.5 |
| TC-ARITH-008 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=0 |
| TC-ARITH-009 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=96 |
| TC-ARITH-010 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=-42 |
| TC-ARITH-011 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=0 |
| TC-ARITH-012 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=10.5 |
| TC-ARITH-013 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=20 |
| TC-ARITH-014 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=3.5 |
| TC-ARITH-015 | Arithmetic | Lê Trung Thành Đạt | Fail | #[BUG-B6-01] | Lỗi thực tế: '', mong đợi: 'Divide by zero error!' |
| TC-ARITH-016 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=0 |
| TC-ARITH-017 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=10 |
| TC-ARITH-018 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=3 |
| TC-ARITH-019 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Sau Toggle: Answer='3.5', Expected='3.5' |
| TC-ARITH-020 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=-5 |
| TC-ARITH-021 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer= |
| TC-ARITH-022 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer= |
| TC-ARITH-023 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=0 |
| TC-ARITH-024 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Answer=1234567891 |
| TC-ARITH-025 | Arithmetic | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CONCAT-001 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=HelloWorld |
| TC-CONCAT-002 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=123456 |
| TC-CONCAT-003 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=World |
| TC-CONCAT-004 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=Hello |
| TC-CONCAT-005 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer= |
| TC-CONCAT-006 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=user@test.com |
| TC-CONCAT-007 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=Good Morning |
| TC-CONCAT-008 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=ABCdef |
| TC-CONCAT-009 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=3.142.71 |
| TC-CONCAT-010 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=-50-20 |
| TC-CONCAT-011 | Concatenate | Lê Trung Thành Đạt | Pass | None | Answer=TestTest |
| TC-CLEAR-001 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-002 | Clear | Lê Trung Thành Đạt | Pass | None | Answer='', Error='' |
| TC-CLEAR-003 | Clear | Lê Trung Thành Đạt | Pass | None | Answer='', Error='' |
| TC-CLEAR-004 | Clear | Lê Trung Thành Đạt | Pass | None | Answer='', Error='' |
| TC-CLEAR-005 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-006 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-007 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-008 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-009 | Clear | Lê Trung Thành Đạt | Pass | None | Answer='' |
| TC-CLEAR-010 | Clear | Lê Trung Thành Đạt | Fail | #[BUG-B6-02] | Answer='1', Error='' |
| TC-CLEAR-011 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-012 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-013 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-014 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-CLEAR-015 | Clear | Lê Trung Thành Đạt | Pass | None | Sau Clear: Answer='', Error='' |
| TC-VALIDATE-001 | Input Validation | Lê Trung Thành Đạt | Fail | #[BUG-B6-03] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-002 | Input Validation | Lê Trung Thành Đạt | Fail | #[BUG-B6-04] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-003 | Input Validation | Lê Trung Thành Đạt | Fail | #[BUG-B6-05] | Lỗi thực tế: '', mong đợi: 'Number 2 is not a number' |
| TC-VALIDATE-004 | Input Validation | Lê Trung Thành Đạt | Pass | None | Answer= |
| TC-VALIDATE-005 | Input Validation | Lê Trung Thành Đạt | Pass | None | Answer= |
| TC-VALIDATE-006 | Input Validation | Lê Trung Thành Đạt | Fail | #[BUG-B6-06] | Lỗi thực tế: '', mong đợi: 'Number 1 is not a number' |
| TC-VALIDATE-007 | Input Validation | Lê Trung Thành Đạt | Pass | None | Answer=15 |

> **Hướng dẫn ghi nhận Result:**
> - **Pass**: Test case thực thi thành công, Actual Result khớp Expected Result.
> - **Fail**: Test case thực thi thất bại, cần tạo GitHub Bug Issue và thay mã `#[BUG-...]` bằng Issue ID thực tế (ví dụ `#18`).
> - **Blocked**: Không thể thực thi test case do lỗi rào cản.
