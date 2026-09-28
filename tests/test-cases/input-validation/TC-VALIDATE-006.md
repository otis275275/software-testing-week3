# TC-VALIDATE-006: Nhập chuỗi chỉ chứa khoảng trắng vào trường số

## Requirement ID
FR-VAL-02

## Module / Test type / Technique
Input Validation / Functional / Boundary Value Analysis

## Preconditions
- Người dùng đã truy cập vào trang web Basic Calculator (https://testsheepnz.github.io/BasicCalculator.html).
- Đã chọn Build cần kiểm thử trên giao diện.

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First number      | `   ` (chỉ chứa khoảng trắng) |
| Second number     | 5 |
| Operation         | Divide |

## Test steps
1. Nhập chuỗi khoảng trắng `   ` vào trường First number.
2. Nhập `5` vào trường Second number.
3. Chọn `Divide` tại danh sách chọn Operation.
4. Nhấn nút `Calculate`.

## Expected result
Hệ thống hiển thị thông báo lỗi "Number 1 is not a number" và không cho phép thực hiện phép chia.

## Status / Related bugs
Not Run / None
