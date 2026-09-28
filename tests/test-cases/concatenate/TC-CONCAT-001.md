# TC-CONCAT-001: Nối hai chuỗi chữ thông thường

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
| First number      | Hello |
| Second number     | World |
| Operation         | Concatenate |

## Test steps
1. Nhập `Hello` vào First number.
2. Nhập `World` vào Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị `HelloWorld` (nối hai chuỗi, không kiểm tra kiểu số, Integers only bị vô hiệu hóa).

## Status / Related bugs
Not Run / None
