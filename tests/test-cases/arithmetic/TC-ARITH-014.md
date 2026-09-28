# TC-ARITH-014: Chia không hết cho kết quả số thập phân (khi không chọn Integers only)

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
| First number      | 7     |
| Second number     | 2     |
| Operation         | Divide |
| Integers only     | Unchecked |

## Test steps
1. Nhập `7` vào trường "First number".
2. Nhập `2` vào trường "Second number".
3. Chọn phép tính `Divide` từ dropdown "Operation".
4. Đảm bảo checkbox "Integers only" KHÔNG được tích chọn.
5. Nhấn nút "Calculate".

## Expected result
- Trường "Answer" hiển thị giá trị số thực `3.5`.
- Không có thông báo lỗi.

## Status / Related bugs
Not Run / None
