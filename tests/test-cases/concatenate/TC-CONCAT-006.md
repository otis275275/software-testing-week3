# TC-CONCAT-006 — Nối chuỗi chứa ký tự đặc biệt

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-006 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | Low |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống xử lý và nối đúng các chuỗi có chứa ký tự đặc biệt.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | Hello@ |
| Second number | #World! |
| Operation | Concatenate |
| Integers only | Không áp dụng |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `Hello@` vào First number | Chuỗi hiển thị đúng |
| 2 | Nhập `#World!` vào Second number | Chuỗi hiển thị đúng |
| 3 | Chọn Concatenate | Concatenate được chọn và Integers only không thể sử dụng |
| 4 | Nhấn Calculate | Answer hiển thị `Hello@#World!` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `Hello@#World!` (nối nguyên vẹn bao gồm ký tự đặc biệt).

## Ghi chú

Kiểm tra xem hệ thống có escape hoặc bỏ qua ký tự đặc biệt hay không.
