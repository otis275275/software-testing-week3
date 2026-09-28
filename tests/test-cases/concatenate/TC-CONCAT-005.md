# TC-CONCAT-005 — Cả hai đầu vào đều rỗng

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-005 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | Medium |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hành vi của hệ thống khi cả hai đầu vào đều bị bỏ trống.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | (rỗng) |
| Second number | (rỗng) |
| Operation | Concatenate |
| Integers only | Không áp dụng |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Để trống First number | Ô First number rỗng |
| 2 | Để trống Second number | Ô Second number rỗng |
| 3 | Chọn Concatenate | Concatenate được chọn và Integers only không thể sử dụng |
| 4 | Nhấn Calculate | Answer hiển thị rỗng hoặc thông báo lỗi phù hợp |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị chuỗi rỗng (hai chuỗi rỗng ghép lại) hoặc hệ thống hiển thị thông báo lỗi hợp lệ.

## Ghi chú

Kiểm tra trường hợp biên cực đoan: cả hai đầu vào đều rỗng.
