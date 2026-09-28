# TC-CONCAT-002: Nối hai giá trị số

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
| First number      | 12 |
| Second number     | 34 |
| Operation         | Concatenate |

## Test steps
1. Nhập `12` vào First number.
2. Nhập `34` vào Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị `1234` (ghép chuỗi, không phải tổng `46`).

## Status / Related bugs
Not Run / None
