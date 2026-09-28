# TC-ARITH-019: Chuyển đổi trạng thái (Toggle) checkbox "Integers only" trên kết quả đã có

## Requirement ID
FR-ARITH-05

## Module / Test type / Technique
Arithmetic / Functional / State Transition

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)
- Đã thực hiện phép tính `7 / 2` với checkbox "Integers only" được tích chọn (Answer đang hiển thị `3`)

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| Current Answer    | 3     |
| Integers only     | Toggle from Checked to Unchecked |

## Test steps
1. Nhấn bỏ tích chọn checkbox "Integers only".

## Expected result
- Trường "Answer" ngay lập tức cập nhật lại từ `3` thành số thực đầy đủ `3.5`.
- Không cần phải nhấn lại nút "Calculate".

## Status / Related bugs
Not Run / None
