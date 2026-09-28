# TC-ARITH-013: Chia hết hai số nguyên dương (kết quả nguyên)

## Requirement ID
FR-ARITH-04

## Module / Test type / Technique
Arithmetic / Functional / Equivalence Partitioning

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 80    |
| Second number     | 4     |
| Operation         | Divide |
| Integers only     | Unchecked |

## Test steps
1. Nhập `80` vào trường "First number".
2. Nhập `4` vào trường "Second number".
3. Chọn phép tính `Divide` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Trường "Answer" hiển thị giá trị `20`.
- Không có thông báo lỗi.

## Status / Related bugs
Not Run / None
