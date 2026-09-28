# TC-ARITH-022: Second number chứa ký tự không phải số trong phép tính số học

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
| First number      | 50    |
| Second number     | @#xyz |
| Operation         | Subtract |
| Integers only     | Unchecked |

## Test steps
1. Nhập `50` vào trường "First number".
2. Nhập `@#xyz` vào trường "Second number".
3. Chọn phép tính `Subtract` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Hệ thống hiển thị thông báo lỗi màu đỏ: `Number 2 is not a number`.
- Không thực hiện tính toán và trường "Answer" không hiển thị kết quả.

## Status / Related bugs
Not Run / None
