# TC-ARITH-023: Để trống cả hai trường số khi thực hiện phép tính số học

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
| First number      | (để trống) |
| Second number     | (để trống) |
| Operation         | Multiply |
| Integers only     | Unchecked |

## Test steps
1. Để trống trường "First number".
2. Để trống trường "Second number".
3. Chọn phép tính `Multiply` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Hệ thống coi giá trị rỗng là `0` hoặc không gây crash trang web; thực hiện phép tính nhân `0 * 0 = 0` hoặc hiển thị giá trị kết quả `0` an toàn.
- Không xuất hiện lỗi JavaScript trên Console.

## Status / Related bugs
Not Run / None
