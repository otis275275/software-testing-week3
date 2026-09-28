# TC-CONCAT-001 — Nối hai chuỗi

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-001 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | High |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống nối hai đầu vào như chuỗi và không kiểm tra kiểu số.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | Hello |
| Second number | World |
| Operation | Concatenate |
| Integers only | Không áp dụng |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `Hello` vào First number | Chuỗi hiển thị đúng |
| 2 | Nhập `World` vào Second number | Chuỗi hiển thị đúng |
| 3 | Chọn Concatenate | Concatenate được chọn và Integers only không thể sử dụng |
| 4 | Nhấn Calculate | Answer hiển thị `HelloWorld` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `HelloWorld`.

## Ghi chú

Không áp dụng kiểm tra dữ liệu số cho phép nối chuỗi.
