# TC-CONCAT-006: Nối chuỗi chứa ký tự đặc biệt

## Requirement ID
FR-CONCAT-03

## Module / Test type / Technique
Concatenate / Functional / Equivalence Partitioning

## Preconditions
- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | Hello@ |
| Second number     | #World! |
| Operation         | Concatenate |

## Test steps
1. Nhập `Hello@` vào First number.
2. Nhập `#World!` vào Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị `Hello@#World!` (nối nguyên vẹn bao gồm các ký tự đặc biệt, không bị escape hay bỏ qua).

## Status / Related bugs
Not Run / None
