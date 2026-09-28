# TC-CLEAR-013: Clear khi đang chọn Build khác Prototype (Build 1)

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / State Transition

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là **Build 1** (không phải Prototype)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| Build             | 1     |
| First Number      | 5     |
| Second Number     | 3     |
| Operation         | Add   |
| Integers only     | Unchecked |

## Test steps
1. Chọn `Build 1` trong dropdown Build
2. Nhập giá trị `5` vào ô First Number
3. Nhập giá trị `3` vào ô Second Number
4. Chọn phép tính `Add`
5. Nhấn nút **Calculate** → ghi nhận kết quả (có thể bị lỗi do Bug)
6. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Ô Answer bị xóa trống
- Dropdown Build **giữ nguyên là Build 1** (Clear không thay đổi Build)
- Dropdown Operation trở về giá trị mặc định

## Status / Related bugs
Not Run / None
