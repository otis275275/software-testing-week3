# TC-CONCAT-008 — Nối chuỗi chữ hoa và chữ thường

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-008 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | Medium |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống giữ nguyên chữ hoa/thường khi nối chuỗi (không tự động chuyển đổi case).

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | HELLO |
| Second number | world |
| Operation | Concatenate |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `HELLO` vào First number | Chuỗi hiển thị đúng |
| 2 | Nhập `world` vào Second number | Chuỗi hiển thị đúng |
| 3 | Chọn Concatenate | Concatenate được chọn |
| 4 | Nhấn Calculate | Answer hiển thị `HELLOworld` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `HELLOworld` (giữ nguyên chữ hoa/thường, không bị chuyển đổi).

## Ghi chú

Kiểm tra tính case-sensitive của chức năng nối chuỗi.
