# TC-ARITH-020: Tích chọn "Integers only" với kết quả phép tính là số âm thập phân

## Requirement ID
FR-ARITH-05

## Module / Test type / Technique
Arithmetic / Functional / Boundary Value Analysis

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | -11   |
| Second number     | 2     |
| Operation         | Divide |
| Integers only     | Checked |

## Test steps
1. Nhập `-11` vào trường "First number".
2. Nhập `2` vào trường "Second number".
3. Chọn phép tính `Divide` từ dropdown "Operation".
4. Tích chọn checkbox "Integers only".
5. Nhấn nút "Calculate".

## Expected result
- Trường "Answer" hiển thị giá trị nguyên `-5` (lấy phần nguyên của `-5.5`).
- Không có thông báo lỗi.

## Status / Related bugs
Not Run / None
