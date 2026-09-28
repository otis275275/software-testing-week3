# TC-CLEAR-001: Clear sau khi nhập đầy đủ dữ liệu và tính toán

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / Equivalence Partitioning

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang đang ở trạng thái mặc định (chưa nhập gì)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First Number      | 10    |
| Second Number     | 5     |
| Operation         | Add   |
| Integers only     | Checked |

## Test steps
1. Nhập giá trị `10` vào ô First Number
2. Nhập giá trị `5` vào ô Second Number
3. Chọn phép tính `Add` trong dropdown Operation
4. Tích vào checkbox `Integers only`
5. Nhấn nút **Calculate** → ghi nhận kết quả ở ô Answer
6. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Ô Answer bị xóa trống
- Dropdown Operation trở về giá trị mặc định (Add)
- Checkbox Integers only trở về trạng thái mặc định (unchecked)
- Trang sẵn sàng để nhập phép tính mới

## Status / Related bugs
Not Run / None
