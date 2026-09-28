# TC-VALIDATE-002 — Nhập dữ liệu không phải số

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-VALIDATE-002 |
| Chức năng | Input validation |
| Mức độ ưu tiên | High |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh các phép toán số từ chối dữ liệu không phải số.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.
- Nhấn **Clear**.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | abc |
| Second number | 5 |
| Operation | Add |
| Integers only | Unchecked |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập `abc` vào First number | Chuỗi được nhập vào trường |
| 2 | Nhập `5` vào Second number | Giá trị hiển thị đúng |
| 3 | Chọn Add và nhấn Calculate | Hệ thống hiển thị thông báo dữ liệu không hợp lệ |

## Kết quả mong đợi cuối cùng

Hệ thống không thực hiện phép cộng và yêu cầu nhập giá trị số.

## Ghi chú

Concatenate không thuộc phạm vi của test case này vì chức năng đó cho phép chuỗi.
