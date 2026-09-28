# TC-ARITH-001: Cộng hai số nguyên dương

## Requirement ID
FR-ARITH-01

## Module / Test type / Technique
Arithmetic / Functional / Equivalence Partitioning

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 25    |
| Second number     | 15    |
| Operation         | Add   |
| Integers only     | Unchecked |

## Test steps
1. Nhập `25` vào trường "First number".
2. Nhập `15` vào trường "Second number".
3. Chọn phép tính `Add` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Trạng thái "Calculating ..." hiển thị trong giây lát.
- Trường "Answer" hiển thị giá trị `40`.
- Không xuất hiện thông báo lỗi.

## Status / Related bugs
Not Run / None
