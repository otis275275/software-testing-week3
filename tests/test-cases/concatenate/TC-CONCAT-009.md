# TC-CONCAT-009 — Nối hai số thập phân dạng chuỗi

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-009 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | Medium |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống nối đúng hai chuỗi chứa số thập phân mà không thực hiện phép tính số học.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | 1.5 |
| Second number | 2.5 |
| Operation | Concatenate |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `1.5` vào First number | Giá trị hiển thị đúng |
| 2 | Nhập `2.5` vào Second number | Giá trị hiển thị đúng |
| 3 | Chọn Concatenate | Concatenate được chọn |
| 4 | Nhấn Calculate | Answer hiển thị `1.52.5` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `1.52.5` (ghép chuỗi, không phải tổng `4`).

## Ghi chú

Phân biệt rõ hành vi nối chuỗi với phép tính cộng số thập phân.
