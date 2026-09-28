# TC-DIV-001 — Chia hai số hợp lệ

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-DIV-001 |
| Chức năng | Divide |
| Mức độ ưu tiên | High |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống chia chính xác hai giá trị số hợp lệ.

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
| Integers only | Unchecked |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `10` vào First number | Giá trị hiển thị đúng |
| 2 | Nhập `4` vào Second number | Giá trị hiển thị đúng |
| 3 | Chọn Divide | Divide được chọn |
| 4 | Nhấn Calculate | Answer hiển thị `2.5` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `2.5`.

## Ghi chú

Trường hợp chia cho 0 nên được viết thành test case riêng.
