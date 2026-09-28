# TC-CONCAT-008: Nối chuỗi chữ hoa và chữ thường

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
| First number      | HELLO |
| Second number     | world |
| Operation         | Concatenate |

## Test steps
1. Nhập `HELLO` vào First number.
2. Nhập `world` vào Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị `HELLOworld` (giữ nguyên chữ hoa/thường, hệ thống không tự động chuyển đổi case).

## Status / Related bugs
Not Run / None
