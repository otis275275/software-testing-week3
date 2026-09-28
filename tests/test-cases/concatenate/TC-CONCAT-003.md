# TC-CONCAT-003: First number rỗng, Second number có giá trị

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
| First number      | (rỗng) |
| Second number     | World |
| Operation         | Concatenate |

## Test steps
1. Để trống First number.
2. Nhập `World` vào Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị `World` (chuỗi rỗng ghép với `World`).

## Status / Related bugs
Not Run / None
