# TC-ARITH-016: Chia số 0 cho một số khác 0

## Requirement ID
FR-ARITH-04

## Module / Test type / Technique
Arithmetic / Functional / Boundary Value Analysis

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 0     |
| Second number     | 25    |
| Operation         | Divide |
| Integers only     | Unchecked |

## Test steps
1. Nhập `0` vào trường "First number".
2. Nhập `25` vào trường "Second number".
3. Chọn phép tính `Divide` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Trường "Answer" hiển thị giá trị `0`.
- Không xuất hiện thông báo lỗi.

## Status / Related bugs
Not Run / None
