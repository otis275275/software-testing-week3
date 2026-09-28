# TC-CONCAT-010: Nối chuỗi chứa số âm

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
| First number      | -10 |
| Second number     | 5 |
| Operation         | Concatenate |

## Test steps
1. Nhập `-10` vào First number.
2. Nhập `5` vào Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị `-105` (dấu âm được giữ nguyên, không bị bỏ qua hay xử lý đặc biệt).

## Status / Related bugs
Not Run / None
