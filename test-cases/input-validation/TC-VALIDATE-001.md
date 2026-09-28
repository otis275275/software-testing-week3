# TC-VALIDATE-001 — Bỏ trống dữ liệu đầu vào

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-VALIDATE-001 |
| Chức năng | Input validation |
| Mức độ ưu tiên | High |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh hệ thống xử lý khi các trường số bị bỏ trống.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | Trống |
| Second number | Trống |
| Operation | Add |
| Integers only | Unchecked |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Để trống hai trường đầu vào | Hai trường không có dữ liệu |
| 2 | Chọn Add | Add được chọn |
| 3 | Nhấn Calculate | Hệ thống hiển thị thông báo kiểm tra dữ liệu và không tính kết quả |

## Kết quả mong đợi cuối cùng

Hệ thống không thực hiện phép cộng với hai đầu vào trống.

## Ghi chú

Ghi chính xác nội dung thông báo thực tế trong test run.
