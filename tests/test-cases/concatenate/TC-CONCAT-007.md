# TC-CONCAT-007 — Nối chuỗi có khoảng trắng

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-007 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | Low |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống giữ nguyên khoảng trắng khi nối chuỗi (không tự động trim hoặc thêm khoảng trắng).

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | Hello |
| Second number | (khoảng trắng)World |
| Operation | Concatenate |
| Integers only | Không áp dụng |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `Hello` vào First number | Chuỗi hiển thị đúng |
| 2 | Nhập ` World` (có khoảng trắng đầu) vào Second number | Chuỗi hiển thị đúng |
| 3 | Chọn Concatenate | Concatenate được chọn và Integers only không thể sử dụng |
| 4 | Nhấn Calculate | Answer hiển thị `Hello World` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `Hello World` (khoảng trắng được giữ nguyên trong kết quả nối).

## Ghi chú

Kiểm tra xem hệ thống có tự động trim khoảng trắng đầu/cuối chuỗi hay không.
