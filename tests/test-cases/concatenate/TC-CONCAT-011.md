# TC-CONCAT-011 — Nối hai chuỗi giống nhau

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CONCAT-011 |
| Chức năng | Concatenate |
| Mức độ ưu tiên | Low |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống nối đúng khi cả hai đầu vào có giá trị giống hệt nhau.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | abc |
| Second number | abc |
| Operation | Concatenate |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `abc` vào First number | Chuỗi hiển thị đúng |
| 2 | Nhập `abc` vào Second number | Chuỗi hiển thị đúng |
| 3 | Chọn Concatenate | Concatenate được chọn |
| 4 | Nhấn Calculate | Answer hiển thị `abcabc` |

## Kết quả mong đợi cuối cùng

Ô Answer hiển thị `abcabc` (hai chuỗi giống nhau được nối lại, không bị trùng lặp hay bỏ qua).

## Ghi chú

Kiểm tra hệ thống không áp dụng bất kỳ logic deduplication nào.
