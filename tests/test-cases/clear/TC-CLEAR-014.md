# TC-CLEAR-014: Clear sau khi nhập số rất lớn (giá trị biên trên)

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / Boundary Value Analysis

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang đang ở trạng thái mặc định

## Test data
| Field / Parameter | Value         |
|-------------------|---------------|
| First Number      | 999999999     |
| Second Number     | 999999999     |
| Operation         | Add           |
| Integers only     | Unchecked     |

## Test steps
1. Nhập giá trị `999999999` vào ô First Number
2. Nhập giá trị `999999999` vào ô Second Number
3. Chọn phép tính `Add`
4. Nhấn nút **Calculate** → ghi nhận kết quả
5. Nhấn nút **Clear**

## Expected result
- Ô First Number bị xóa trống
- Ô Second Number bị xóa trống
- Ô Answer bị xóa trống
- Trang không bị lỗi hiển thị hay crash sau khi Clear số lớn

## Status / Related bugs
Not Run / None
