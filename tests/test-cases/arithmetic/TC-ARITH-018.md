# TC-ARITH-018: Tích chọn "Integers only" để làm tròn/lấy phần nguyên kết quả phép chia

## Requirement ID
FR-ARITH-05

## Module / Test type / Technique
Arithmetic / Functional / Equivalence Partitioning

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 10    |
| Second number     | 3     |
| Operation         | Divide |
| Integers only     | Checked |

## Test steps
1. Nhập `10` vào trường "First number".
2. Nhập `3` vào trường "Second number".
3. Chọn phép tính `Divide` từ dropdown "Operation".
4. Tích chọn checkbox "Integers only".
5. Nhấn nút "Calculate".

## Expected result
- Trường "Answer" hiển thị giá trị nguyên `3` (thay vì số thập phân `3.3333333333333335`).
- Không có thông báo lỗi.

## Status / Related bugs
Not Run / None
