# TC-ARITH-025: Nhấn nút "Clear" để xóa kết quả phép tính và đặt lại trạng thái

## Requirement ID
FR-ARITH-07

## Module / Test type / Technique
Arithmetic / Functional / State Transition

## Preconditions
- Trình duyệt đã mở trang Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html)
- Dropdown Build đang chọn "Prototype" (Build 0)
- Đã thực hiện xong một phép tính, trường "Answer" đang có giá trị `50`, checkbox "Integers only" đang được tích chọn.

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| Action            | Click nút "Clear" |

## Test steps
1. Nhấn nút "Clear".

## Expected result
- Trường "Answer" bị xóa rỗng giá trị.
- Checkbox "Integers only" được uncheck (bỏ chọn).
- Thông báo lỗi (nếu có trước đó) được xóa sạch.

## Status / Related bugs
Not Run / None
