# TC-CLEAR-007: Clear sau khi thực hiện phép tính Concatenate

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
| First Number      | Hello |
| Second Number     | World |
| Operation         | Concatenate |
| Integers only     | Disabled (tự động) |

## Test steps
1. Nhập chuỗi `Hello` vào ô First Number
2. Nhập chuỗi `World` vào ô Second Number
3. Chọn phép tính `Concatenate` trong dropdown Operation
4. Xác nhận checkbox Integers only bị vô hiệu hóa
5. Nhấn nút **Calculate** → ghi nhận kết quả `HelloWorld`
6. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Ô Answer bị xóa trống
- Dropdown Operation trở về giá trị mặc định
- Checkbox Integers only trở về trạng thái mặc định (enabled và unchecked)

## Status / Related bugs
Not Run / None
