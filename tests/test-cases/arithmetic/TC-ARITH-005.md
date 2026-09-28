# TC-ARITH-005: Trừ hai số nguyên dương cho kết quả dương

## Requirement ID
FR-ARITH-02

## Module / Test type / Technique
Arithmetic / Functional / Equivalence Partitioning

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 50    |
| Second number     | 20    |
| Operation         | Subtract |
| Integers only     | Unchecked |

## Test steps
1. Nhập `50` vào trường "First number".
2. Nhập `20` vào trường "Second number".
3. Chọn phép tính `Subtract` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Trường "Answer" hiển thị giá trị `30`.
- Không có thông báo lỗi.

## Status / Related bugs
Not Run / None
