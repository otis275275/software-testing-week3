# TC-VALIDATE-004: Nhập chữ cái (Alphabet) vào trường số

## Requirement ID
FR-VAL-02

## Module / Test type / Technique
Input Validation / Functional / Equivalence Partitioning

## Preconditions
- Người dùng đã truy cập vào trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html).
- Đã chọn Build cần kiểm thử trên giao diện.

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | abc |
| Second number     | 15 |
| Operation         | Multiply |

## Test steps
1. Nhập `abc` vào trường First number.
2. Nhập `15` vào trường Second number.
3. Chọn `Multiply` tại danh sách chọn Operation.
4. Nhấn nút `Calculate`.

## Expected result
Hệ thống từ chối tính toán và hiển thị thông báo lỗi "Number 1 is not a number".

## Status / Related bugs
Not Run / None
