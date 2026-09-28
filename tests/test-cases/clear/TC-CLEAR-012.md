# TC-CLEAR-012: Clear sau khi nhập số thập phân

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / Equivalence Partitioning

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang đang ở trạng thái mặc định

## Test data
| Field / Parameter | Value  |
|-------------------|--------|
| First Number      | 3.14   |
| Second Number     | 2.71   |
| Operation         | Add    |
| Integers only     | Unchecked |

## Test steps
1. Nhập giá trị `3.14` vào ô First Number
2. Nhập giá trị `2.71` vào ô Second Number
3. Chọn phép tính `Add`
4. Nhấn nút **Calculate** → kết quả hiển thị `5.85`
5. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Ô Answer bị xóa trống
- Dropdown Operation trở về giá trị mặc định
- Trang sẵn sàng cho phép tính mới

## Status / Related bugs
Not Run / None
