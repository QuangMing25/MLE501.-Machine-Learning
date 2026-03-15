# Data Dictionary - Give Me Some Credit

## Tổng quan bài toán
**Mục tiêu**: Dự đoán xác suất một khách hàng sẽ gặp khó khăn tài chính nghiêm trọng trong vòng 2 năm tới.

**Loại bài toán**: Binary Classification (Phân loại nhị phân)

---

## Biến mục tiêu (Target Variable)

### 1. **SeriousDlqin2yrs**
- **Mô tả**: Người vay có gặp tình trạng chậm thanh toán 90 ngày trở lên hoặc tệ hơn hay không
- **Kiểu dữ liệu**: Binary (0/1 hoặc Y/N)
- **Ý nghĩa**:
  - `1` (Yes): Khách hàng có rủi ro cao, đã từng chậm thanh toán ≥ 90 ngày
  - `0` (No): Khách hàng thanh toán tốt
- **Vai trò**: Đây là biến mục tiêu cần dự đoán

---

## Các biến đặc trưng (Features)

### 2. **RevolvingUtilizationOfUnsecuredLines**
- **Mô tả**: Tỷ lệ sử dụng hạn mức tín dụng không có thế chấp
- **Công thức**: (Tổng dư nợ trên thẻ tín dụng + các khoản vay cá nhân không thế chấp) / Tổng hạn mức tín dụng
- **Kiểu dữ liệu**: Percentage (phần trăm, thường từ 0-1)
- **Ý nghĩa**:
  - Tỷ lệ cao (>0.8): Sử dụng gần hết hạn mức → Rủi ro cao
  - Tỷ lệ thấp (<0.3): Sử dụng hạn mức thận trọng → Rủi ro thấp
- **Lưu ý**: Không bao gồm bất động sản và các khoản trả góp như xe hơi

### 3. **age**
- **Mô tả**: Tuổi của người vay
- **Kiểu dữ liệu**: Integer (số nguyên, tính bằng năm)
- **Ý nghĩa**:
  - Người trẻ: Có thể ít kinh nghiệm tài chính
  - Người trung niên: Thường ổn định hơn
  - Người cao tuổi: Có thể có thu nhập hưu trí thấp

### 4. **NumberOfTime30-59DaysPastDueNotWorse**
- **Mô tả**: Số lần chậm thanh toán 30-59 ngày trong 2 năm qua
- **Kiểu dữ liệu**: Integer (số nguyên)
- **Ý nghĩa**:
  - 0: Không chậm thanh toán → Tín dụng tốt
  - 1-2: Có vài lần chậm nhẹ → Cần cảnh giác
  - ≥3: Chậm thường xuyên → Rủi ro cao

### 5. **DebtRatio**
- **Mô tả**: Tỷ lệ nợ trên thu nhập
- **Công thức**: (Các khoản nợ hàng tháng + cấp dưỡng + chi phí sinh hoạt) / Thu nhập gộp hàng tháng
- **Kiểu dữ liệu**: Percentage (phần trăm)
- **Ý nghĩa**:
  - <0.36: Tỷ lệ nợ an toàn
  - 0.36-0.43: Vùng cảnh báo
  - >0.43: Gánh nặng nợ cao → Rủi ro cao

### 6. **MonthlyIncome**
- **Mô tả**: Thu nhập hàng tháng
- **Kiểu dữ liệu**: Real (số thực, có thể có giá trị thập phân)
- **Đơn vị**: Tiền tệ (thường là USD)
- **Ý nghĩa**:
  - Thu nhập cao: Khả năng trả nợ tốt
  - Thu nhập thấp hoặc không ổn định: Rủi ro cao
- **Lưu ý**: Có thể có missing values

### 7. **NumberOfOpenCreditLinesAndLoans**
- **Mô tả**: Tổng số khoản vay và hạn mức tín dụng đang mở
- **Bao gồm**:
  - Khoản vay trả góp (xe hơi, nhà)
  - Thẻ tín dụng
- **Kiểu dữ liệu**: Integer
- **Ý nghĩa**:
  - Quá ít: Thiếu lịch sử tín dụng
  - Vừa phải (5-10): Quản lý tín dụng tốt
  - Quá nhiều (>15): Có thể đang gặp khó khăn tài chính

### 8. **NumberOfTimes90DaysLate**
- **Mô tả**: Số lần chậm thanh toán 90 ngày trở lên
- **Kiểu dữ liệu**: Integer
- **Ý nghĩa**:
  - 0: Thanh toán đúng hạn → Tốt
  - ≥1: Đã từng có nợ xấu nghiêm trọng → Rủi ro rất cao
- **Quan trọng**: Đây là chỉ số quan trọng nhất về rủi ro tín dụng

### 9. **NumberRealEstateLoansOrLines**
- **Mô tả**: Số lượng khoản vay bất động sản và thế chấp
- **Bao gồm**:
  - Khoản vay mua nhà
  - Vay thế chấp bất động sản
  - Home equity lines of credit
- **Kiểu dữ liệu**: Integer
- **Ý nghĩa**:
  - 0: Không có tài sản BĐS
  - 1-2: Có tài sản, ổn định
  - >3: Nhiều khoản vay BĐS → Cần xem xét kỹ

### 10. **NumberOfTime60-89DaysPastDueNotWorse**
- **Mô tả**: Số lần chậm thanh toán 60-89 ngày trong 2 năm qua
- **Kiểu dữ liệu**: Integer
- **Ý nghĩa**:
  - 0: Thanh toán tốt
  - ≥1: Có dấu hiệu rủi ro, nghiêm trọng hơn chậm 30-59 ngày

### 11. **NumberOfDependents**
- **Mô tả**: Số người phụ thuộc trong gia đình (không bao gồm bản thân)
- **Bao gồm**: Vợ/chồng, con cái, v.v.
- **Kiểu dữ liệu**: Integer
- **Ý nghĩa**:
  - Ít người phụ thuộc: Chi phí sinh hoạt thấp hơn
  - Nhiều người phụ thuộc: Gánh nặng tài chính lớn hơn
- **Lưu ý**: Có thể có missing values

---

## Tổng kết về Features

### Nhóm Features quan trọng:

1. **Lịch sử thanh toán** (Payment History):
   - NumberOfTimes90DaysLate ⭐⭐⭐ (Quan trọng nhất)
   - NumberOfTime60-89DaysPastDueNotWorse ⭐⭐
   - NumberOfTime30-59DaysPastDueNotWorse ⭐⭐

2. **Tỷ lệ sử dụng tín dụng** (Credit Utilization):
   - RevolvingUtilizationOfUnsecuredLines ⭐⭐⭐
   - DebtRatio ⭐⭐⭐

3. **Thông tin tài chính** (Financial Info):
   - MonthlyIncome ⭐⭐
   - NumberOfDependents ⭐

4. **Lịch sử tín dụng** (Credit History):
   - NumberOfOpenCreditLinesAndLoans ⭐⭐
   - NumberRealEstateLoansOrLines ⭐

5. **Thông tin nhân khẩu học** (Demographics):
   - age ⭐⭐

---

## Thông tin Dataset

- **Training set**: 150,000 mẫu
- **Test set**: ~100,000 mẫu
- **Tổng số features**: 11 features (10 features + 1 target)
- **Missing values**: Có thể có ở MonthlyIncome và NumberOfDependents

---

## Gợi ý xử lý dữ liệu

1. **Missing values**: Cần xử lý cho MonthlyIncome và NumberOfDependents
2. **Outliers**: Kiểm tra các giá trị bất thường (age < 18, DebtRatio > 10, v.v.)
3. **Feature Engineering**: Có thể tạo thêm features mới từ các features hiện có
4. **Imbalanced data**: Kiểm tra tỷ lệ class 0/1 của target variable
5. **Scaling**: Các features có scale khác nhau cần chuẩn hóa

---

**Lưu ý**: Đây là bài toán từ Kaggle Competition "Give Me Some Credit" - mục tiêu là giúp các tổ chức tín dụng đưa ra quyết định cho vay thông minh hơn.
