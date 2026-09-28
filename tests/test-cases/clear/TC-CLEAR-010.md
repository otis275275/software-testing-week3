# TC-CLEAR-010: Clear sau khi tính toán xong, sau đó có thể tính tiếp bình thường

## Requirement ID
FR-CLEAR-01

## Module / Test type / Technique
Clear / Functional / State Transition

## Preconditions
- Truy cập được trang https://testsheepnz.github.io/BasicCalculator.html
- Build đang chọn là Prototype
- Trang đang ở trạng thái mặc định

## Test data
| Field / Parameter | Value (Lần 1) | Value (Lần 2) |
|-------------------|---------------|---------------|
| First Number      | 8             | 20            |
| Second Number     | 4             | 5             |
| Operation         | Add           | Subtract      |
| Integers only     | Unchecked     | Unchecked     |

## Test steps
1. Nhập `8` vào First Number, `4` vào Second Number, chọn `Add`
2. Nhấn **Calculate** → kết quả: `12`
3. Nhấn nút **Clear**
4. Xác nhận tất cả trường đã được xóa
5. Nhập `20` vào First Number, `5` vào Second Number, chọn `Subtract`
6. Nhấn **Calculate**

## Expected result
- Sau bước 3: tất cả trường được xóa / trở về mặc định
- Sau bước 6: ô Answer hiển thị kết quả đúng là `15`
- Hệ thống hoạt động bình thường sau khi Clear, không bị ảnh hưởng bởi phép tính trước

## Status / Related bugs
Not Run / None
