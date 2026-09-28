# TC-ARITH-003: Cộng hai số thập phân (số thực)

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
| First number      | 12.34 |
| Second number     | 5.66  |
| Operation         | Add   |
| Integers only     | Unchecked |

## Test steps
1. Nhập `12.34` vào trường "First number".
2. Nhập `5.66` vào trường "Second number".
3. Chọn phép tính `Add` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Trường "Answer" hiển thị giá trị `18`.
- Không có thông báo lỗi.

## Status / Related bugs
Not Run / None
