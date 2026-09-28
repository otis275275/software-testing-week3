# TC-CONCAT-002 — Nối hai giá trị số

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-002 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | High |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống nối hai giá trị số như chuỗi ký tự (không thực hiện phép cộng).

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | 12 |
| Second number | 34 |
| Operation | Concatenate |
| Integers only | Không áp dụng |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `12` vào First number | Giá trị hiển thị đúng |
| 2 | Nhập `34` vào Second number | Giá trị hiển thị đúng |
| 3 | Chọn Concatenate | Concatenate được chọn và Integers only không thể sử dụng |
| 4 | Nhấn Calculate | Answer hiển thị `1234` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `1234` (ghép chuỗi, không phải tổng `46`).

## Ghi chú

Phân biệt rõ hành vi nối chuỗi với phép tính cộng số học.
