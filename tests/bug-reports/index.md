# Danh mục Bug Reports (Tổng hợp các bản Build)

Tổng hợp tất cả các lỗi được phát hiện từ quá trình chạy kiểm thử tự động trên các bản Build.

---

## Danh sách lỗi trên Build 1 (Tổng: 10 lỗi)

| Bug ID | Test Case ID | Module | Tiêu đề lỗi | Severity | Priority | File chi tiết |
|---|---|---|---|---|---|---|
| **BUG-B1-01** | TC-ARITH-021 | Arithmetic | Hệ thống không kiểm tra tính hợp lệ của First number khi nhập chữ cái (Build 1) | `major` | `P1` | [BUG-B1-01.md](build-1/BUG-B1-01.md) |
| **BUG-B1-02** | TC-ARITH-022 | Arithmetic | Hệ thống không kiểm tra tính hợp lệ của Second number khi nhập ký tự đặc biệt (Build 1) | `major` | `P1` | [BUG-B1-02.md](build-1/BUG-B1-02.md) |
| **BUG-B1-03** | TC-CLEAR-006 | Clear | Nút Clear bị khóa/vô hiệu hóa sau khi thực hiện phép chia cho 0 (Build 1) | `critical` | `P0` | [BUG-B1-03.md](build-1/BUG-B1-03.md) |
| **BUG-B1-04** | TC-CLEAR-010 | Clear | Tính toán lại sau khi Clear bị sai kết quả (Build 1) | `major` | `P1` | [BUG-B1-04.md](build-1/BUG-B1-04.md) |
| **BUG-B1-05** | TC-VALIDATE-001 | Input Validation | Không hiển thị thông báo lỗi khi để trống cả hai trường số đầu vào (Build 1) | `minor` | `P2` | [BUG-B1-05.md](build-1/BUG-B1-05.md) |
| **BUG-B1-06** | TC-VALIDATE-002 | Input Validation | Không báo lỗi khi để trống trường First number (Build 1) | `minor` | `P2` | [BUG-B1-06.md](build-1/BUG-B1-06.md) |
| **BUG-B1-07** | TC-VALIDATE-003 | Input Validation | Không báo lỗi khi để trống trường Second number (Build 1) | `minor` | `P2` | [BUG-B1-07.md](build-1/BUG-B1-07.md) |
| **BUG-B1-08** | TC-VALIDATE-004 | Input Validation | Không kiểm tra định dạng số khi nhập ký tự chữ cái (Build 1) | `major` | `P1` | [BUG-B1-08.md](build-1/BUG-B1-08.md) |
| **BUG-B1-09** | TC-VALIDATE-005 | Input Validation | Không kiểm tra định dạng khi nhập ký tự đặc biệt vào Second number (Build 1) | `major` | `P1` | [BUG-B1-09.md](build-1/BUG-B1-09.md) |
| **BUG-B1-10** | TC-VALIDATE-006 | Input Validation | Không báo lỗi khi nhập chuỗi chỉ chứa khoảng trắng vào trường số (Build 1) | `minor` | `P2` | [BUG-B1-10.md](build-1/BUG-B1-10.md) |

---

## Danh sách lỗi trên Build 2 (Tổng: 23 lỗi)

| Bug ID | Test Case ID | Module | Tiêu đề lỗi | Severity | Priority | File chi tiết |
|---|---|---|---|---|---|---|
| **BUG-B2-01** | TC-ARITH-001 | Arithmetic | Phép tính Add bị hoán đổi thành phép nối chuỗi Concatenate (Build 2) | `critical` | `P0` | [BUG-B2-01.md](build-2/BUG-B2-01.md) |
| **BUG-B2-02** | TC-ARITH-002 | Arithmetic | Cộng số âm bị nối chuỗi thay vì tính toán số học (Build 2) | `critical` | `P0` | [BUG-B2-02.md](build-2/BUG-B2-02.md) |
| **BUG-B2-03** | TC-ARITH-003 | Arithmetic | Cộng hai số thập phân bị nối chuỗi (Build 2) | `critical` | `P0` | [BUG-B2-03.md](build-2/BUG-B2-03.md) |
| **BUG-B2-04** | TC-ARITH-004 | Arithmetic | Cộng với số 0 bị nối chuỗi (Build 2) | `major` | `P1` | [BUG-B2-04.md](build-2/BUG-B2-04.md) |
| **BUG-B2-05** | TC-ARITH-021 | Arithmetic | Không validate dữ liệu số khi chọn phép Add do bị đổi sang Concatenate (Build 2) | `major` | `P1` | [BUG-B2-05.md](build-2/BUG-B2-05.md) |
| **BUG-B2-06** | TC-ARITH-024 | Arithmetic | Cộng số 10 chữ số với 1 bị nối chuỗi (Build 2) | `major` | `P1` | [BUG-B2-06.md](build-2/BUG-B2-06.md) |
| **BUG-B2-07** | TC-CONCAT-001 | Concatenate | Phép tính Concatenate bị hoán đổi thành phép cộng số học Add và báo lỗi chuỗi (Build 2) | `critical` | `P0` | [BUG-B2-07.md](build-2/BUG-B2-07.md) |
| **BUG-B2-08** | TC-CONCAT-002 | Concatenate | Nối hai giá trị số bị tính tổng thay vì nối chuỗi (Build 2) | `critical` | `P0` | [BUG-B2-08.md](build-2/BUG-B2-08.md) |
| **BUG-B2-09** | TC-CONCAT-003 | Concatenate | Concatenate chuỗi với Second number là chữ bị báo lỗi Number 2 (Build 2) | `major` | `P1` | [BUG-B2-09.md](build-2/BUG-B2-09.md) |
| **BUG-B2-10** | TC-CONCAT-004 | Concatenate | Concatenate chuỗi với First number là chữ bị báo lỗi Number 1 (Build 2) | `major` | `P1` | [BUG-B2-10.md](build-2/BUG-B2-10.md) |
| **BUG-B2-11** | TC-CONCAT-006 | Concatenate | Concatenate chuỗi chứa ký tự đặc biệt bị báo lỗi số (Build 2) | `major` | `P1` | [BUG-B2-11.md](build-2/BUG-B2-11.md) |
| **BUG-B2-12** | TC-CONCAT-007 | Concatenate | Concatenate chuỗi có khoảng trắng bị báo lỗi số (Build 2) | `major` | `P1` | [BUG-B2-12.md](build-2/BUG-B2-12.md) |
| **BUG-B2-13** | TC-CONCAT-008 | Concatenate | Concatenate chuỗi chữ hoa và thường bị báo lỗi số (Build 2) | `major` | `P1` | [BUG-B2-13.md](build-2/BUG-B2-13.md) |
| **BUG-B2-14** | TC-CONCAT-009 | Concatenate | Concatenate hai số thập phân bị tính tổng thay vì nối chuỗi (Build 2) | `major` | `P1` | [BUG-B2-14.md](build-2/BUG-B2-14.md) |
| **BUG-B2-15** | TC-CONCAT-010 | Concatenate | Concatenate hai chuỗi số âm bị tính tổng thành '-70' (Build 2) | `major` | `P1` | [BUG-B2-15.md](build-2/BUG-B2-15.md) |
| **BUG-B2-16** | TC-CONCAT-011 | Concatenate | Concatenate hai chuỗi giống nhau bị báo lỗi số (Build 2) | `major` | `P1` | [BUG-B2-16.md](build-2/BUG-B2-16.md) |
| **BUG-B2-17** | TC-CLEAR-006 | Clear | Nút Clear bị vô hiệu hóa sau phép chia cho 0 (Build 2) | `critical` | `P0` | [BUG-B2-17.md](build-2/BUG-B2-17.md) |
| **BUG-B2-18** | TC-CLEAR-010 | Clear | Tính toán lại sau khi Clear bị sai kết quả (Build 2) | `major` | `P1` | [BUG-B2-18.md](build-2/BUG-B2-18.md) |
| **BUG-B2-19** | TC-VALIDATE-001 | Input Validation | Không hiển thị lỗi khi để trống cả hai trường số ở phép Add (Build 2) | `minor` | `P2` | [BUG-B2-19.md](build-2/BUG-B2-19.md) |
| **BUG-B2-20** | TC-VALIDATE-002 | Input Validation | Không hiển thị lỗi khi để trống First number ở phép Add (Build 2) | `minor` | `P2` | [BUG-B2-20.md](build-2/BUG-B2-20.md) |
| **BUG-B2-21** | TC-VALIDATE-003 | Input Validation | Không hiển thị lỗi khi để trống Second number ở phép Add (Build 2) | `minor` | `P2` | [BUG-B2-21.md](build-2/BUG-B2-21.md) |
| **BUG-B2-22** | TC-VALIDATE-006 | Input Validation | Nhập khoảng trắng vào First number không bị bắt lỗi ở phép Add (Build 2) | `minor` | `P2` | [BUG-B2-22.md](build-2/BUG-B2-22.md) |
| **BUG-B2-23** | TC-VALIDATE-007 | Input Validation | Cộng hai số thực hợp lệ bị nối chuỗi thành '12.52.5' (Build 2) | `critical` | `P0` | [BUG-B2-23.md](build-2/BUG-B2-23.md) |

---

## Danh sách lỗi trên Build 5 (Tổng: 9 lỗi)

| Bug ID | Test Case ID | Module | Tiêu đề lỗi | Severity | Priority | File chi tiết |
|---|---|---|---|---|---|---|
| **BUG-B5-01** | TC-CLEAR-002 | Clear | Clear khi chỉ nhập First Number (chưa tính toán) (Build 5) | `critical` | `P0` | [BUG-B5-01.md](build-5/BUG-B5-01.md) |
| **BUG-B5-02** | TC-CLEAR-003 | Clear | Clear khi chỉ nhập Second Number (chưa tính toán) (Build 5) | `critical` | `P0` | [BUG-B5-02.md](build-5/BUG-B5-02.md) |
| **BUG-B5-03** | TC-CLEAR-004 | Clear | Clear khi tất cả các trường đang trống (Build 5) | `critical` | `P0` | [BUG-B5-03.md](build-5/BUG-B5-03.md) |
| **BUG-B5-04** | TC-CLEAR-006 | Clear | Clear sau khi thực hiện phép chia cho 0 (Build 5) | `critical` | `P0` | [BUG-B5-04.md](build-5/BUG-B5-04.md) |
| **BUG-B5-05** | TC-CLEAR-010 | Clear | Clear sau khi tính toán xong, sau đó tính tiếp bình thường (Build 5) | `minor` | `P2` | [BUG-B5-05.md](build-5/BUG-B5-05.md) |
| **BUG-B5-06** | TC-VALIDATE-001 | Input Validation | Bỏ trống cả hai trường dữ liệu đầu vào (Build 5) | `minor` | `P2` | [BUG-B5-06.md](build-5/BUG-B5-06.md) |
| **BUG-B5-07** | TC-VALIDATE-002 | Input Validation | Bỏ trống trường First number khi thực hiện phép tính số học (Build 5) | `minor` | `P2` | [BUG-B5-07.md](build-5/BUG-B5-07.md) |
| **BUG-B5-08** | TC-VALIDATE-003 | Input Validation | Bỏ trống trường Second number khi thực hiện phép tính số học (Build 5) | `minor` | `P2` | [BUG-B5-08.md](build-5/BUG-B5-08.md) |
| **BUG-B5-09** | TC-VALIDATE-006 | Input Validation | Nhập chuỗi chỉ chứa khoảng trắng vào trường số (Build 5) | `minor` | `P2` | [BUG-B5-09.md](build-5/BUG-B5-09.md) |

---

## Danh sách lỗi trên Build 6 (Tổng: 6 lỗi)

| Bug ID | Test Case ID | Module | Tiêu đề lỗi | Severity | Priority | File chi tiết |
|---|---|---|---|---|---|---|
| **BUG-B6-01** | TC-ARITH-015 | Arithmetic | Chia cho số 0 (Xử lý lỗi Divide by zero) (Build 6) | `major` | `P1` | [BUG-B6-01.md](build-6/BUG-B6-01.md) |
| **BUG-B6-02** | TC-CLEAR-010 | Clear | Clear sau khi tính toán xong, sau đó tính tiếp bình thường (Build 6) | `minor` | `P2` | [BUG-B6-02.md](build-6/BUG-B6-02.md) |
| **BUG-B6-03** | TC-VALIDATE-001 | Input Validation | Bỏ trống cả hai trường dữ liệu đầu vào (Build 6) | `minor` | `P2` | [BUG-B6-03.md](build-6/BUG-B6-03.md) |
| **BUG-B6-04** | TC-VALIDATE-002 | Input Validation | Bỏ trống trường First number khi thực hiện phép tính số học (Build 6) | `minor` | `P2` | [BUG-B6-04.md](build-6/BUG-B6-04.md) |
| **BUG-B6-05** | TC-VALIDATE-003 | Input Validation | Bỏ trống trường Second number khi thực hiện phép tính số học (Build 6) | `minor` | `P2` | [BUG-B6-05.md](build-6/BUG-B6-05.md) |
| **BUG-B6-06** | TC-VALIDATE-006 | Input Validation | Nhập chuỗi chỉ chứa khoảng trắng vào trường số (Build 6) | `minor` | `P2` | [BUG-B6-06.md](build-6/BUG-B6-06.md) |

---

