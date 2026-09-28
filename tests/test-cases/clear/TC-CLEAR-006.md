# TC-CLEAR-006: Clear sau khi thực hiện phép chia cho 0

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / Boundary Value Analysis

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang đang ở trạng thái mặc định

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First Number      | 10    |
| Second Number     | 0     |
| Operation         | Divide |
| Integers only     | Unchecked |

## Test steps
1. Nhập giá trị `10` vào ô First Number
2. Nhập giá trị `0` vào ô Second Number
3. Chọn phép tính `Divide`
4. Nhấn nút **Calculate** → ghi nhận kết quả / thông báo lỗi chia cho 0
5. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Ô Answer bị xóa trống (hoặc thông báo lỗi biến mất)
- Dropdown Operation trở về giá trị mặc định
- Trang không bị lỗi sau khi Clear

## Status / Related bugs
Not Run / None
