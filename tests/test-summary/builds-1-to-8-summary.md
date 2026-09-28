# Test Summary Report — Basic Calculator (Builds 1 – 8)

## 1. Thông tin chung & Bảng chỉ số tổng quan (Executive Test Metrics)

| Tiêu chí (Metric) | Nội dung / Giá trị thực tế | Ghi chú |
|---|---|---|
| **Project / Product** | Basic Calculator Web Application ([TestSheepNZ](https://testsheepnz.github.io/BasicCalculator.html)) | Ứng dụng web máy tính cơ bản |
| **Test Scope** | Kiểm thử tự động toàn diện từ **Build 1 đến Build 8** | 4 Modules: Arithmetic, Concatenate, Clear, Validation |
| **Test Environment** | • **OS**: Windows 11 / macOS<br>• **Browser**: Chromium (Playwright v1.40+ / Chrome v130+)<br>• **Runtime**: Node.js v20+, Python 3.13<br>• **Device / Viewport**: Desktop PC (1280 × 720) | Môi trường kiểm thử tự động (Automated Testing) |
| **Execution Date** | 2026-09-28 | Đợt kiểm thử Milestone 1 |
| **Total Test Cases** | **58** kịch bản kiểm thử độc lập | Arithmetic: 25, Concatenate: 11, Clear: 15, Validation: 7 |
| **Total Test Runs** | **464** lượt thực thi kiểm thử | 58 Test Cases × 8 Bản Build |
| **Passed** | **331** lượt Pass | Tỷ lệ thành công: **71.3%** |
| **Failed** | **133** lượt Fail | Tỷ lệ lỗi: **28.7%** |
| **Blocked / Skipped** | **0** (0.0%) | Không có ca kiểm thử nào bị chặn hoặc bỏ qua |
| **Not Executed** | **0** (0.0%) | Đã chạy phủ 100% kịch bản trên toàn bộ 8 build |
| **Pass Rate** | **71.3%** toàn hệ thống | Công thức: `(331 / 464) × 100%` |
| **Defects Found** | **133** lỗi được phát hiện và lập báo cáo chi tiết | Đầy đủ file tại thư mục `tests/bug-reports/` |
| **Defect Severity** | • **Critical (P0 / Blocker)**: 14 lỗi (10.5%)<br>• **High / Major (P1)**: 83 lỗi (62.4%)<br>• **Medium / Low / Minor (P2)**: 36 lỗi (27.1%) | Phân loại theo mức độ ảnh hưởng nghiệp vụ |
| **Outstanding Issues** | **133 bugs đang Open** (Chưa được sửa lỗi trên các build) | Trong đó có 14 lỗi Critical cản trở nghiêm trọng luồng sử dụng |
| **Conclusion / Verdict** | **Chưa đạt chuẩn phát hành (Not Ready for Release)** | Build 6 ổn định nhất (89.7%), Build 7 và 8 lỗi logic nặng nhất |
| **Tổng số thành viên** | 5 thành viên (4 Tester chính phụ trách build, 1 Cross-tester) | Người tổng hợp báo cáo: Huỳnh Đức Thịnh |

---

## 2. Phân công kiểm thử

| Thành viên | Build phụ trách | Vai trò & Đóng góp |
|---|---|---|
| **Trà Văn Sỹ** | Build 1, Build 2 | Thực thi 116 lượt test, phát hiện và lập 33 bug reports |
| **Huỳnh Đức Thịnh** | Build 3, Build 4 | Thực thi 116 lượt test, phát hiện và lập 23 bug reports |
| **Lê Trung Thành Đạt** | Build 5, Build 6 | Thực thi 116 lượt test, phát hiện và lập 15 bug reports |
| **Lê Công Phúc** | Build 7, Build 8 | Thực thi 116 lượt test, phát hiện và lập 62 bug reports |
| **Nguyễn Nhật Duy** | Kiểm thử chéo Build 2, Build 7 | Thực hiện kiểm thử độc lập, đối soát kết quả các build phức tạp |

---

## 3. Kết quả theo build

| Build | Tester chính | Pass | Fail | Blocked | Not Run | Tổng | Tỷ lệ Pass | Đánh giá |
|:---:|---|---:|---:|---:|---:|---:|:---:|---|
| **Build 1** | Trà Văn Sỹ | 48 | 10 | 0 | 0 | 58 | **82.8%** | **Chấp nhận có điều kiện** (Lỗi thiếu validation ký tự/khoảng trắng) |
| **Build 2** | Trà Văn Sỹ, Nguyễn Nhật Duy | 35 | 23 | 0 | 0 | 58 | **60.3%** | **Không đạt** (Lỗi hoán đổi nghiêm trọng Add và Concatenate) |
| **Build 3** | Huỳnh Đức Thịnh | 45 | 13 | 0 | 0 | 58 | **77.6%** | **Không đạt** (Lỗi ép kiểu số khi thực hiện nối chuỗi ký tự) |
| **Build 4** | Huỳnh Đức Thịnh | 48 | 10 | 0 | 0 | 58 | **82.8%** | **Không đạt** (Lỗi khóa cứng Integers only, tính sai số thực) |
| **Build 5** | Lê Trung Thành Đạt | 49 | 9 | 0 | 0 | 58 | **84.5%** | **Không đạt** (Lỗi nút Clear bị vô hiệu hóa/không bấm được) |
| **Build 6** | Lê Trung Thành Đạt | 52 | 6 | 0 | 0 | 58 | **89.7%** | **Ổn định nhất** (Không bắt lỗi ngoại lệ chia cho 0) |
| **Build 7** | Lê Công Phúc, Nguyễn Nhật Duy | 23 | 35 | 0 | 0 | 58 | **39.7%** | **Cực kỳ kém** (Lấy kết quả trước đó làm toán hạng thứ nhất) |
| **Build 8** | Lê Công Phúc | 31 | 27 | 0 | 0 | 58 | **53.4%** | **Rất kém** (Đảo ngược vị trí Number 1 và Number 2) |
| **TỔNG CỘNG** | **Cả nhóm** | **331** | **133** | **0** | **0** | **464** | **71.3%** | **28.7% tổng số lượt kiểm thử ghi nhận lỗi** |

---

## 4. So sánh các build (Ma trận chức năng)

> **Quy ước**:
> - `Pass`: Chức năng hoạt động chính xác theo đúng đặc tả yêu cầu.
> - `Fail`: Phát hiện sai lệch kết quả, lỗi logic tính toán hoặc lỗi giao diện.
> - `Partial`: Đạt các ca kiểm thử cơ bản nhưng trượt các ca kiểm thử biên/ngoại lệ.

| Chức năng | Build 1 | Build 2 | Build 3 | Build 4 | Build 5 | Build 6 | Build 7 | Build 8 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Phép Cộng (Add)** | Pass | **Fail** | Pass | Pass | Pass | Pass | **Fail** | Pass |
| **Phép Trừ (Subtract)** | Pass | Pass | Pass | **Partial** | Pass | Pass | **Fail** | **Fail** |
| **Phép Nhân (Multiply)** | Pass | Pass | Pass | **Partial** | Pass | Pass | **Fail** | Pass |
| **Phép Chia (Divide)** | Pass | Pass | Pass | **Partial** | Pass | **Fail** | **Fail** | **Fail** |
| **Nối chuỗi (Concatenate)** | Pass | **Fail** | **Fail** | Pass | Pass | Pass | **Fail** | **Fail** |
| **Lấy số nguyên (Integers only)** | Pass | Pass | Pass | **Fail** | Pass | Pass | **Fail** | **Fail** |
| **Nút Xóa (Clear)** | **Partial** | **Partial** | **Partial** | **Partial** | **Fail** | **Partial** | **Partial** | **Partial** |
| **Kiểm tra dữ liệu (Validation)** | **Fail** | **Fail** | **Fail** | **Fail** | **Fail** | **Fail** | **Fail** | **Fail** |

### Chi tiết các sai lệch chức năng đặc thù:
- **Build 2**: Hoán đổi phép `Add` và `Concatenate` (`25 + 15` cho kết quả `2515`; nối `"Hello" + "World"` báo lỗi yêu cầu số).
- **Build 4**: Khóa cứng chế độ số nguyên (`Integers only`). Mọi phép trừ, nhân, chia ra số thực đều bị cắt phần thập phân dù bỏ tick checkbox.
- **Build 6**: Bỏ qua kiểm tra phép chia cho 0, trả về ô kết quả rỗng thay vì hiển thị thông báo lỗi `Divide by zero`.
- **Build 7**: Tự động lấy kết quả tính toán trước đó làm `First number`, làm hỏng toàn bộ chuỗi tính toán liên tiếp.
- **Build 8**: Đảo ngược toán hạng `Number 1` và `Number 2`. Phép cộng và nhân có tính giao hoán nên vẫn `Pass`; các phép toán không giao hoán (Trừ, Chia, Ghép chuỗi) bị đảo ngược hoàn toàn kết quả (`Fail`).

---

## 5. Thống kê và Danh sách lỗi

Tổng cộng có **133 lỗi** được phát hiện và lập tài liệu chi tiết tại [`tests/bug-reports`](../bug-reports/).

### 5.1. Thống kê theo mức độ nghiêm trọng (Severity & Priority)

| Mức độ nghiêm trọng (Severity) | Phân loại tương đương | Độ ưu tiên | Số lượng lỗi | Tỷ lệ (%) | Đặc điểm tác động |
|---|---|:---:|:---:|:---:|---|
| **Critical** | **Critical / Blocker** | `P0` | **14** | 10.5% | Gây tắc nghẽn hoặc sai hoàn toàn tính năng chính (Hoán đổi Add/Concat B2, khóa nút Clear B5, hỏng nút Clear sau chia 0). |
| **Major** | **High** | `P1` | **83** | 62.4% | Tính toán sai số học, lỗi ép kiểu dữ liệu (B3, B4), đảo toán hạng (B7, B8). |
| **Minor** | **Medium / Low** | `P2` | **36** | 27.1% | Không báo lỗi khi để trống trường, không bắt lỗi chuỗi khoảng trắng. |
| **Tổng cộng** | | | **133** | **100%** | |

### 5.2. Các lỗi hệ thống lặp lại trên mọi Build (Systemic Bugs)
1. **Lỗi Input Validation khi để trống trường (`TC-VALIDATE-001`, `002`, `003`)**: Toàn bộ 8 build đều không hiển thị thông báo lỗi khi người dùng nhấn Calculate với trường dữ liệu để trống.
2. **Lỗi chuỗi khoảng trắng (`TC-VALIDATE-006`)**: Nhập khoảng trắng vào trường số không bị hệ thống bắt lỗi (thiếu hàm `trim()`).
3. **Lỗi tính toán lại sau Clear (`TC-CLEAR-010`)**: Sau khi Clear và nhập số mới, hệ thống vẫn lưu cache hoặc xử lý không đúng kết quả.
4. **Lỗi nút Clear sau khi chia cho 0 (`TC-CLEAR-006`)**: Xuất hiện từ Build 1 đến Build 5 và Build 7 (nút Clear bị khóa/vô hiệu sau lỗi chia cho 0).

---

## 6. Phân tích nguyên nhân (Root Cause Analysis - RCA)

1. **Lỗi biến dị có chủ đích trong mã nguồn (Injected Mutations)**:
   - **Build 2**: Nhầm lẫn chỉ số/giá trị trong bộ xử lý sự kiện dropdown phép tính (`value="0"` và `value="4"`).
   - **Build 3**: Ép kiểu cưỡng bức `Number(val)` trước khi truyền vào hàm xử lý chuỗi.
   - **Build 4**: Biến cờ `integersOnly` bị gán cố định `true` trong logic xử lý sau tính toán.
   - **Build 5**: Nút `Clear` bị gán thuộc tính `disabled` vĩnh viễn hoặc thiếu event listener.
   - **Build 7**: Biến lưu trữ `previousAnswer` ghi đè giá trị tham số `number1`.
   - **Build 8**: Thứ tự tham số truyền vào hàm tính toán bị hoán đổi: `calc(num2, num1)`.
2. **Lỗi kiến trúc cốt lõi**:
   - Thiếu tầng xác thực dữ liệu đầu vào (Input Validation Layer) ở phía client trước khi gửi dữ liệu tính toán.
   - Thiếu cơ chế đồng bộ và khôi phục trạng thái (State Reset) của form khi người dùng thao tác nút `Clear`.

---

## 7. Các vấn đề tồn đọng (Outstanding Issues)

Toàn bộ **133 lỗi** phát hiện được hiện đều đang ở trạng thái **Open (Chưa được xử lý)** do bản chất các bản Build 1–8 là các phiên bản thử nghiệm có lỗi chủ đích. Các vấn đề trọng yếu cần đội ngũ phát triển giải quyết gồm:

1. **Nhóm lỗi nghiêm trọng (Critical / Blocker - 14 lỗi)**:
   - Sửa lỗi kẹt vòng xoay loading và mở khóa thuộc tính `disabled` của nút Clear sau khi chia cho 0 (`BUG-B1-03`, `BUG-B2-17`, `BUG-B3-08`, `BUG-B4-05`, `BUG-B5-04`, `BUG-B7-28`).
   - Sửa triệt để lỗi hoán đổi logic giữa phép `Add` và `Concatenate` trên Build 2 (`BUG-B2-01`, `BUG-B2-02`, `BUG-B2-03`, `BUG-B2-07`, `BUG-B2-08`, `BUG-B2-23`).
   - Gỡ bỏ trạng thái khóa cứng vô hiệu hóa nút Clear trên Build 5 (`BUG-B5-01`, `BUG-B5-02`, `BUG-B5-03`).
2. **Nhóm lỗi sai lệch logic nghiệp vụ (High / Major - 83 lỗi)**:
   - Loại bỏ cơ chế tự động lấy `previousAnswer` làm toán hạng thứ nhất trên Build 7 (gây hỏng 35 ca kiểm thử).
   - Đảo lại đúng thứ tự truyền tham số `First number` và `Second number` trên Build 8 (gây hỏng 27 ca kiểm thử).
   - Cho phép nối chuỗi ký tự tự do trong phép Concatenate trên Build 3 mà không ép kiểu sang số.
   - Mở khóa trạng thái checkbox `Integers only` trên Build 4 để hỗ trợ hiển thị kết quả số thực.
3. **Nhóm lỗi chuẩn hóa dữ liệu đầu vào (Medium / Low / Minor - 36 lỗi)**:
   - Bổ sung hàm `trim()` loại bỏ khoảng trắng trước khi kiểm tra dữ liệu số (`TC-VALIDATE-006`).
   - Bắt buộc hiển thị thông báo lỗi khi người dùng để trống một hoặc cả hai trường số đầu vào (`TC-VALIDATE-001`, `002`, `003`).

---

## 8. Rủi ro và giới hạn

- **Phạm vi trình duyệt**: Kiểm thử tự động mới chỉ được thực hiện trên trình duyệt Chromium thông qua Playwright; chưa kiểm thử chéo trên Firefox, Safari (WebKit) hoặc trình duyệt di động.
- **Kiểm thử tải và hiệu năng**: Chưa thực hiện kiểm thử với các phép tính chuỗi quá dài hoặc số nguyên vượt giới hạn `Number.MAX_SAFE_INTEGER`.
- **Trạng thái lưu trữ ngầm**: Build 7 cho thấy rủi ro lớn về biến toàn cục lưu trạng thái tính toán cũ, dễ phát sinh lỗi rò rỉ bộ nhớ hoặc sai lệch dữ liệu người dùng tiếp theo.

---

## 9. Kết luận chung & Đánh giá (Conclusion & Verdict)

- **Tổng số test cases**: 58 kịch bản kiểm thử (464 lượt chạy thực tế qua 8 build).
- **Tổng số Pass**: 331 (71.3%).
- **Tổng số Fail**: 133 (28.7%).
- **Tổng số Blocked**: 0 (0.0%).
- **Tổng số Not Run**: 0 (0.0%).
- **Build ổn định nhất**: **Build 6** (Tỷ lệ pass **89.7%**, 6 lỗi, 0 lỗi Critical).
- **Build có nhiều lỗi nhất**: **Build 7** (Tỷ lệ fail **60.3%**, 35 lỗi) và **Build 8** (Tỷ lệ fail **46.6%**, 27 lỗi).
- **Đánh giá kết luận cuối cùng (Final Verdict)**: 
  - Ứng dụng **chưa đủ điều kiện phát hành (NOT READY FOR PRODUCTION)** trên tất cả các phiên bản do còn tồn tại 14 lỗi mức độ Critical và tỷ lệ lỗi tổng thể lên đến 28.7%.
  - Bộ kịch bản kiểm thử (58 Test Cases) đạt độ bao phủ xuất sắc, phân biệt rõ ràng các dạng lỗi đột biến nghiệp vụ giữa 8 phiên bản build.
  - Các lỗi nền tảng (validation rỗng, nút Clear sau lỗi, khoảng trắng) cần được chuẩn hóa và sửa dứt điểm trước khi bàn giao sản phẩm hoàn thiện.

---

## 10. Quy ước trạng thái

- `Pass`: Kết quả thực tế khớp chính xác với kết quả mong đợi trong kịch bản kiểm thử.
- `Fail`: Kết quả thực tế sai khác kết quả mong đợi (sai logic, văng lỗi ngoài ý muốn hoặc không hiển thị thông báo hợp lệ).
- `Blocked`: Ca kiểm thử không thể tiếp tục thực thi do có lỗi chắn trước đó.
- `Not Run`: Ca kiểm thử chưa được thực hiện.
