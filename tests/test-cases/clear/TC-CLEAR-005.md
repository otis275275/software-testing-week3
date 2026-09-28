# TC-CLEAR-005: Clear sau khi nhập input không hợp lệ (chữ cái thay vì số)

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / Equivalence Partitioning

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang đang ở trạng thái mặc định

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First Number      | abc   |
| Second Number     | xyz   |
| Operation         | Add   |
| Integers only     | Unchecked |

## Test steps
1. Nhập chuỗi `abc` vào ô First Number
2. Nhập chuỗi `xyz` vào ô Second Number
3. Chọn phép tính `Add`
4. Nhấn nút **Calculate** → hệ thống hiển thị thông báo lỗi
5. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Thông báo lỗi biến mất (nếu có)
- Ô Answer bị xóa trống
- Trang trở về trạng thái mặc định, sẵn sàng nhập lại

## Status / Related bugs
Not Run / None
