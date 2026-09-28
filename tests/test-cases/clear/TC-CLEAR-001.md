# TC-CLEAR-001 — Xóa dữ liệu máy tính

## Thông tin chung

| Thuộc tính | Nội dung |
|---|---|
| Test Case ID | TC-CLEAR-001 |
| Chức năng | Clear |
| Mức độ ưu tiên | Medium |
| Người tạo | [Tên thành viên] |
| Ngày tạo | YYYY-MM-DD |

## Mục tiêu

Xác minh nút Clear đưa biểu mẫu về trạng thái ban đầu.

## Điều kiện tiên quyết

- Truy cập được trang Basic Calculator.
- Chọn build cần kiểm thử.

## Dữ liệu kiểm thử

| Trường | Giá trị |
|---|---|
| First number | 10 |
| Second number | 5 |
| Operation | Add |
| Integers only | Checked |

## Các bước thực hiện

| Bước | Thao tác | Kết quả mong đợi |
|---:|---|---|
| 1 | Nhập dữ liệu và thực hiện phép tính | Answer có kết quả |
| 2 | Nhấn Clear | Dữ liệu nhập và Answer được xóa |
| 3 | Kiểm tra Operation và Integers only | Các điều khiển trở về trạng thái mặc định |

## Kết quả mong đợi cuối cùng

Biểu mẫu trở về trạng thái ban đầu và sẵn sàng cho phép tính mới.

## Ghi chú

Ghi lại bất kỳ trường hoặc lựa chọn nào không được reset.
