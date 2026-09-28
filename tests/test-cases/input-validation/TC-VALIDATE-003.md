# TC-VALIDATE-003: Bỏ trống trường Second number khi thực hiện phép tính số học

## Requirement ID
FR-VAL-01

## Module / Test type / Technique
Input Validation / Functional / Boundary Value Analysis

## Preconditions
- Người dùng đã truy cập vào trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html).
- Đã chọn Build cần kiểm thử trên giao diện.

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | 10 |
| Second number     | (Trống) |
| Operation         | Add |

## Test steps
1. Nhập `10` vào trường First number.
2. Để trống trường Second number.
3. Chọn `Add` tại danh sách chọn Operation.
4. Nhấn nút `Calculate`.

## Expected result
Hệ thống không tính toán và hiển thị thông báo lỗi kiểm tra dữ liệu đối với Second number (ví dụ: "Number 2 is not a number").

## Status / Related bugs
Not Run / None
