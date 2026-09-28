# TC-ARITH-015: Chia cho số 0 (Xử lý lỗi Divide by zero)

## Requirement ID
FR-ARITH-04

## Module / Test type / Technique
Arithmetic / Functional / Boundary Value Analysis & Error Guessing

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 100   |
| Second number     | 0     |
| Operation         | Divide |
| Integers only     | Unchecked |

## Test steps
1. Nhập `100` vào trường "First number".
2. Nhập `0` vào trường "Second number".
3. Chọn phép tính `Divide` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Hệ thống chặn phép chia và hiển thị thông báo lỗi bằng chữ màu đỏ: `Divide by zero error!`.
- Không hiển thị kết quả vô cực (`Infinity`) hoặc NaN trong trường "Answer".

## Status / Related bugs
Not Run / None
