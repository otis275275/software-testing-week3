# TC-CONCAT-004: First number có giá trị, Second number rỗng

## Requirement ID
FR-CONCAT-02

## Module / Test type / Technique
Concatenate / Functional / BVA

## Preconditions
- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | Hello |
| Second number     | (rỗng) |
| Operation         | Concatenate |

## Test steps
1. Nhập `Hello` vào First number.
2. Để trống Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị `Hello` (`Hello` ghép với chuỗi rỗng).

## Status / Related bugs
Not Run / None
