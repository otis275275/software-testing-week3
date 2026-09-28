# TC-CONCAT-010 — Nối chuỗi chứa số âm

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-010 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | Low |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống giữ nguyên dấu âm khi nối chuỗi chứa số âm.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | -10 |
| Second number | 5 |
| Operation | Concatenate |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `-10` vào First number | Giá trị hiển thị đúng |
| 2 | Nhập `5` vào Second number | Giá trị hiển thị đúng |
| 3 | Chọn Concatenate | Concatenate được chọn |
| 4 | Nhấn Calculate | Answer hiển thị `-105` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `-105` (dấu âm được giữ nguyên, không bị bỏ qua).

## Ghi chú

Kiểm tra xem ký tự `-` trong đầu vào có bị hệ thống xử lý đặc biệt hay không.
