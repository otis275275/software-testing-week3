# TC-CLEAR-008: Clear khi checkbox Integers only đang được bật

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / State Transition

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang đang ở trạng thái mặc định

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First Number      | 7     |
| Second Number     | 2     |
| Operation         | Divide |
| Integers only     | Checked |

## Test steps
1. Nhập giá trị `7` vào ô First Number
2. Nhập giá trị `2` vào ô Second Number
3. Chọn phép tính `Divide`
4. Tích chọn checkbox `Integers only`
5. Nhấn nút **Calculate** → kết quả hiển thị `3` (số nguyên)
6. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Ô Answer bị xóa trống
- Checkbox `Integers only` trở về trạng thái **unchecked** (mặc định)
- Dropdown Operation trở về giá trị mặc định

## Status / Related bugs
Not Run / None
