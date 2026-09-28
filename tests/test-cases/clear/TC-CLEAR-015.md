# TC-CLEAR-015: Clear khi ô Answer đang hiển thị kết quả thập phân với Integers only đang tắt

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / Equivalence Partitioning

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang đang ở trạng thái mặc định

## Test data
| Field / Parameter | Value   |
|-------------------|---------|
| First Number      | 10      |
| Second Number     | 3       |
| Operation         | Divide  |
| Integers only     | Unchecked |

## Test steps
1. Nhập giá trị `10` vào ô First Number
2. Nhập giá trị `3` vào ô Second Number
3. Chọn phép tính `Divide`
4. Đảm bảo checkbox `Integers only` **không được tích**
5. Nhấn nút **Calculate** → kết quả hiển thị số thập phân (ví dụ: `3.3333...`)
6. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Ô Answer bị xóa trống (kết quả thập phân bị xóa hoàn toàn)
- Checkbox `Integers only` vẫn ở trạng thái unchecked (mặc định)
- Dropdown Operation trở về giá trị mặc định

## Status / Related bugs
Not Run / None
