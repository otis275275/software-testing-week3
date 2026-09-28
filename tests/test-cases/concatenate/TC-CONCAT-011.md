# TC-CONCAT-011: Nối hai chuỗi giống nhau

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
| First number      | abc |
| Second number     | abc |
| Operation         | Concatenate |

## Test steps
1. Nhập `abc` vào First number.
2. Nhập `abc` vào Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị `abcabc` (hai chuỗi giống nhau được nối lại, hệ thống không bỏ qua hay dedup).

## Status / Related bugs
Not Run / None
