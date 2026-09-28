# TC-ARITH-024: Nhập số đạt giới hạn độ dài tối đa 10 ký tự (maxlength = 10)

## Requirement ID
FR-ARITH-06

## Module / Test type / Technique
Arithmetic / Functional / Boundary Value Analysis

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 1234567890 (10 chữ số) |
| Second number     | 1 |
| Operation         | Add |
| Integers only     | Unchecked |

## Test steps
1. Nhập `1234567890` (10 chữ số) vào trường "First number".
2. Cố gắng gõ thêm ký tự thứ 11 vào trường "First number".
3. Nhập `1` vào trường "Second number".
4. Chọn phép tính `Add` từ dropdown "Operation".
5. Nhấn nút "Calculate".

## Expected result
- Trường "First number" chỉ nhận tối đa 10 ký tự (không cho phép nhập ký tự thứ 11 do thuộc tính `maxlength="10"`).
- Trường "Answer" tính toán chính xác giá trị `1234567891`.

## Status / Related bugs
Not Run / None
