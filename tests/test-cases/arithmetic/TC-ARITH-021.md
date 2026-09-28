# TC-ARITH-021: First number chứa ký tự không phải số trong phép tính số học

## Requirement ID
FR-ARITH-06

## Module / Test type / Technique
Arithmetic / Functional / Error Guessing & Equivalence Partitioning

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | abc   |
| Second number     | 10    |
| Operation         | Add   |
| Integers only     | Unchecked |

## Test steps
1. Nhập `abc` vào trường "First number".
2. Nhập `10` vào trường "Second number".
3. Chọn phép tính `Add` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Hệ thống hiển thị thông báo lỗi màu đỏ: `Number 1 is not a number`.
- Không thực hiện tính toán và trường "Answer" không hiển thị kết quả.

## Status / Related bugs
Not Run / None
