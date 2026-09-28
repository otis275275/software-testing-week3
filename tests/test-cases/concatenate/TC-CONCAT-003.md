# TC-CONCAT-003 — First number rỗng, Second number có giá trị

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-003 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | Medium |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hành vi của hệ thống khi First number bị bỏ trống và chỉ có Second number có giá trị.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | (rỗng) |
| Second number | World |
| Operation | Concatenate |
| Integers only | Không áp dụng |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Để trống First number | Ô First number rỗng |
| 2 | Nhập `World` vào Second number | Giá trị hiển thị đúng |
| 3 | Chọn Concatenate | Concatenate được chọn và Integers only không thể sử dụng |
| 4 | Nhấn Calculate | Answer hiển thị `World` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `World` (chuỗi rỗng ghép với `World`).

## Ghi chú

Kiểm tra trường hợp biên: một đầu vào rỗng.
