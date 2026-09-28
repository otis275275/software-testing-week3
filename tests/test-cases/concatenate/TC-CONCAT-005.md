# TC-CONCAT-005: Cả hai đầu vào đều rỗng

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
| Second number     | (rỗng) |
| Operation         | Concatenate |

## Test steps
1. Để trống First number.
2. Để trống Second number.
3. Chọn **Concatenate** trong danh sách Operation.
4. Nhấn **Calculate**.

## Expected result
Ô Answer hiển thị chuỗi rỗng (hai chuỗi rỗng ghép lại) hoặc hệ thống hiển thị thông báo lỗi hợp lệ.

## Status / Related bugs
Not Run / None
