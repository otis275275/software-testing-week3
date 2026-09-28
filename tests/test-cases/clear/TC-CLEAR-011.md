# TC-CLEAR-011: Clear sau khi nhập số âm vào cả hai trường

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
| First Number      | -10   |
| Second Number     | -5    |
| Operation         | Multiply |
| Integers only     | Unchecked |

## Test steps
1. Nhập giá trị `-10` vào ô First Number
2. Nhập giá trị `-5` vào ô Second Number
3. Chọn phép tính `Multiply`
4. Nhấn nút **Calculate** → kết quả hiển thị `50`
5. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Ô Answer bị xóa trống
- Dropdown Operation trở về giá trị mặc định
- Trang sẵn sàng cho phép tính mới

## Status / Related bugs
Not Run / None
