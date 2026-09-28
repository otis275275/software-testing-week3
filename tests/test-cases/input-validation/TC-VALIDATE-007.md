# TC-VALIDATE-007: Kiểm tra dữ liệu hợp lệ (Số nguyên và số thực)

## Requirement ID
FR-VAL-01

## Module / Test type / Technique
Input Validation / Functional / Equivalence Partitioning

## Preconditions
- Người dùng đã truy cập vào trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html).
- Đã chọn Build cần kiểm thử trên giao diện.

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 12.5 |
| Second number     | -3.5 |
| Operation         | Add |

## Test steps
1. Nhập `12.5` vào trường First number.
2. Nhập `-3.5` vào trường Second number.
3. Chọn `Add` tại danh sách chọn Operation.
4. Nhấn nút `Calculate`.

## Expected result
Hệ thống xác thực dữ liệu số hợp lệ thành công, không xuất hiện thông báo lỗi và tính kết quả `9` hiển thị ở ô Answer.

## Status / Related bugs
Not Run / None
