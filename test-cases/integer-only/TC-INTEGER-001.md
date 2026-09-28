# TC-INTEGER-001 — Trả về kết quả số nguyên

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-INTEGER-001 |
| Chức năng | Integers only |
| Mức độ ưu tiên | High |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh tùy chọn Integers only chuyển kết quả phép tính thành số nguyên.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | 10 |
| Second number | 4 |
| Operation | Divide |
| Integers only | Checked |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `10` và `4` | Hai giá trị hiển thị đúng |
| 2 | Chọn Divide | Divide được chọn |
| 3 | Chọn Integers only | Checkbox ở trạng thái checked |
| 4 | Nhấn Calculate | Answer hiển thị kết quả dạng số nguyên |

## Kết quả mong đợi cuối cùng

Answer không chứa phần thập phân; ghi lại giá trị thực tế để xác nhận quy tắc chuyển đổi.

## Ghi chú

Nếu đặc tả quy định rõ làm tròn hay cắt phần thập phân, cập nhật giá trị mong đợi tương ứng.
