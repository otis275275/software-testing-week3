# TC-VALIDATE-005: Nhập ký tự đặc biệt vào trường số

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
| First number      | 100 |
| Second number     | @#$% |
| Operation         | Subtract |

## Test steps
1. Nhập `100` vào trường First number.
2. Nhập `@#$%` vào trường Second number.
3. Chọn `Subtract` tại danh sách chọn Operation.
4. Nhấn nút `Calculate`.

## Expected result
Hệ thống từ chối tính toán và hiển thị thông báo lỗi "Number 2 is not a number".

## Status / Related bugs
Not Run / None
