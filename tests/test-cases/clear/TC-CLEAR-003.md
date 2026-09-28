# TC-CLEAR-003: Clear khi chỉ nhập Second Number (chưa tính toán)

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
| First Number      | (để trống) |
| Second Number     | 99    |
| Operation         | (mặc định) |
| Integers only     | (mặc định) |

## Test steps
1. Để trống ô First Number
2. Nhập giá trị `99` vào ô Second Number
3. Không chọn Operation
4. Nhấn nút **Clear**

## Expected result
- Ô First Number vẫn trống
- Ô Second Number bị xóa trống
- Ô Answer vẫn trống
- Trang trở về trạng thái mặc định ban đầu

## Status / Related bugs
Not Run / None
