# TC-CLEAR-002: Clear khi chỉ nhập First Number (chưa tính toán)

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
| First Number      | 42    |
| Second Number     | (để trống) |
| Operation         | (mặc định) |
| Integers only     | (mặc định) |

## Test steps
1. Nhập giá trị `42` vào ô First Number
2. Không nhập gì vào ô Second Number
3. Không chọn Operation
4. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number vẫn trống
- Ô Answer vẫn trống
- Trang trở về trạng thái mặc định ban đầu

## Status / Related bugs
Not Run / None
