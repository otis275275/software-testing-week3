# TC-ARITH-004: Cộng với số 0 (Phần tử trung hòa)

## Requirement ID
FR-ARITH-01

## Module / Test type / Technique
Arithmetic / Functional / Boundary Value Analysis

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 0     |
| Second number     | 99    |
| Operation         | Add   |
| Integers only     | Unchecked |

## Test steps
1. Nhập `0` vào trường "First number".
2. Nhập `99` vào trường "Second number".
3. Chọn phép tính `Add` từ dropdown "Operation".
4. Nhấn nút "Calculate".

## Expected result
- Trường "Answer" hiển thị giá trị `99`.
- Không có thông báo lỗi.

## Status / Related bugs
Not Run / None
