# TC-CONCAT-009: Nối hai số thập phân dạng chuỗi

## Requirement ID
FR-CONCAT-01

## Module / Test type / Technique
Concatenate / Functional / Equivalence Partitioning

## Preconditions
- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 1.5 |
| Second number     | 2.5 |
| Operation         | Concatenate |

## Test steps
1. Nhập `1.5` vào First number.
2. Nhập `2.5` vào Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị `1.52.5` (ghép chuỗi, không phải tổng `4`).

## Status / Related bugs
Not Run / None
