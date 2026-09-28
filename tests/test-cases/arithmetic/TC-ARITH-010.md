# TC-ARITH-010: Nhân số dương với số âm

## Requirement ID
FR-ARITH-03

## Module / Test type / Technique
Arithmetic / Functional / Equivalence Partitioning

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 7     |
| Second number     | -6    |
| Operation         | Multiply |
| Integers only     | Unchecked |

## Test steps
1. Nhập `7` vào trường "First number".
2. Nhập `-6` vào trường "Second number".
3. Chọn phép tính `Multiply` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Trường "Answer" hiển thị giá trị `-42`.
- Không có thông báo lỗi.

## Status / Related bugs
Not Run / None
