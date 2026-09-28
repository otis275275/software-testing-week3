# TC-CLEAR-004: Clear khi tất cả các trường đang trống (trang mới mở)

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / Equivalence Partitioning

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang vừa được tải lại, tất cả trường đang trống

## Test data
| Field / Parameter | Value |
|-------------------|-------|
| First Number      | (để trống) |
| Second Number     | (để trống) |
| Operation         | (mặc định) |
| Integers only     | (mặc định) |

## Test steps
1. Không nhập gì vào bất kỳ ô nào
2. Nhấn nút **Clear**

## Expected result
- Không có lỗi xảy ra
- Tất cả ô vẫn ở trạng thái trống / mặc định
- Ô Answer vẫn trống
- Trang không bị crash hay reload

## Status / Related bugs
Not Run / None
