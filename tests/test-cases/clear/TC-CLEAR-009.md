# TC-CLEAR-009: Clear nhiều lần liên tiếp (nhấn Clear 2 lần trở lên)

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / State Transition

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang đang ở trạng thái mặc định

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First Number      | 15    |
| Second Number     | 3     |
| Operation         | Multiply |
| Integers only     | Unchecked |

## Test steps
1. Nhập giá trị `15` vào ô First Number
2. Nhập giá trị `3` vào ô Second Number
3. Chọn phép tính `Multiply`
4. Nhấn nút **Calculate** → kết quả hiển thị `45`
5. Nhấn nút **Clear** lần 1
6. Nhấn nút **Clear** lần 2
7. Nhấn nút **Clear** lần 3

## Expected result
- Sau lần Clear đầu tiên: tất cả trường được xóa / trở về mặc định
- Sau lần Clear thứ 2 và 3: không có lỗi xảy ra, trang vẫn ổn định
- Không xuất hiện lỗi JavaScript hay crash trình duyệt

## Status / Related bugs
Not Run / None
