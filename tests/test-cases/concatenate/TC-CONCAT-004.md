# TC-CONCAT-004 — First number có giá trị, Second number rỗng

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-004 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | Medium |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hành vi của hệ thống khi Second number bị bỏ trống và chỉ có First number có giá trị.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | Hello |
| Second number | (rỗng) |
| Operation | Concatenate |
| Integers only | Không áp dụng |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `Hello` vào First number | Giá trị hiển thị đúng |
| 2 | Để trống Second number | Ô Second number rỗng |
| 3 | Chọn Concatenate | Concatenate được chọn và Integers only không thể sử dụng |
| 4 | Nhấn Calculate | Answer hiển thị `Hello` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `Hello` (`Hello` ghép với chuỗi rỗng).

## Ghi chú

Kiểm tra trường hợp biên: một đầu vào rỗng.
