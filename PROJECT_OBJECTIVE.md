# Mục tiêu dự án - Credit Scoring

## 🎯 Tổng quan bài toán

**Bài toán**: Dự đoán xác suất khách hàng gặp khó khăn tài chính nghiêm trọng (nợ xấu) trong vòng 2 năm tới

**Loại bài toán**: Binary Classification (Phân loại nhị phân)

---

## 📥 INPUT - Dữ liệu đầu vào (10 features)

### 1. **RevolvingUtilizationOfUnsecuredLines**
- Tỷ lệ sử dụng hạn mức tín dụng không thế chấp
- Kiểu: Percentage (0-1 hoặc có thể >1)

### 2. **age**
- Tuổi của khách hàng
- Kiểu: Integer (năm)

### 3. **NumberOfTime30-59DaysPastDueNotWorse**
- Số lần chậm thanh toán 30-59 ngày trong 2 năm qua
- Kiểu: Integer

### 4. **DebtRatio**
- Tỷ lệ nợ/thu nhập hàng tháng
- Kiểu: Percentage

### 5. **MonthlyIncome**
- Thu nhập hàng tháng
- Kiểu: Real (số thực)
- ⚠️ Có thể có missing values

### 6. **NumberOfOpenCreditLinesAndLoans**
- Số lượng khoản vay và thẻ tín dụng đang mở
- Kiểu: Integer

### 7. **NumberOfTimes90DaysLate**
- Số lần chậm thanh toán ≥90 ngày
- Kiểu: Integer
- ⭐ Feature quan trọng nhất

### 8. **NumberRealEstateLoansOrLines**
- Số lượng khoản vay bất động sản
- Kiểu: Integer

### 9. **NumberOfTime60-89DaysPastDueNotWorse**
- Số lần chậm thanh toán 60-89 ngày trong 2 năm qua
- Kiểu: Integer

### 10. **NumberOfDependents**
- Số người phụ thuộc trong gia đình
- Kiểu: Integer
- ⚠️ Có thể có missing values

---

## 📤 OUTPUT - Dự đoán (Target Variable)

### **SeriousDlqin2yrs**
- **Kiểu dữ liệu**: Binary (0/1)
- **Ý nghĩa**: Khách hàng có gặp khó khăn tài chính nghiêm trọng (nợ xấu) trong vòng 2 năm tới hay không?

#### Giá trị:
- **0** → Khách hàng tốt (không vỡ nợ)
  - Thanh toán đúng hạn
  - Rủi ro tín dụng thấp
  - ✅ Có thể cho vay

- **1** → Khách hàng xấu (vỡ nợ / nợ xấu)
  - Có khả năng chậm thanh toán ≥90 ngày
  - Rủi ro tín dụng cao
  - ❌ Cần cân nhắc kỹ trước khi cho vay

---

## 🎲 Công thức tổng quát

```
f: X → Y

Trong đó:
- X = (x₁, x₂, ..., x₁₀) : Vector 10 features đầu vào
- Y ∈ {0, 1}            : Nhãn phân loại nhị phân
- f                      : Mô hình Machine Learning cần xây dựng
```

### Cụ thể:

```
Input (X):
┌─────────────────────────────────────────────────┐
│ 1. RevolvingUtilizationOfUnsecuredLines         │
│ 2. age                                          │
│ 3. NumberOfTime30-59DaysPastDueNotWorse         │
│ 4. DebtRatio                                    │
│ 5. MonthlyIncome                                │
│ 6. NumberOfOpenCreditLinesAndLoans              │
│ 7. NumberOfTimes90DaysLate                      │
│ 8. NumberRealEstateLoansOrLines                 │
│ 9. NumberOfTime60-89DaysPastDueNotWorse         │
│ 10. NumberOfDependents                          │
└─────────────────────────────────────────────────┘
                    ↓
            [ML Model (f)]
                    ↓
Output (Y):
┌─────────────────────────────────────────────────┐
│ SeriousDlqin2yrs ∈ {0, 1}                      │
│                                                 │
│ 0 = Khách hàng tốt (không vỡ nợ)               │
│ 1 = Khách hàng xấu (vỡ nợ)                     │
└─────────────────────────────────────────────────┘
```

---

## 📊 Thông tin Dataset

- **Training set**: 150,000 mẫu dữ liệu
- **Test set**: ~100,000 mẫu dữ liệu
- **Số features**: 10 features đầu vào
- **Target**: 1 biến nhị phân (SeriousDlqin2yrs)

---

## 🚀 Pipeline dự kiến

```
1. Data Loading & Exploration
   ↓
2. Data Preprocessing
   - Handle missing values (MonthlyIncome, NumberOfDependents)
   - Handle outliers
   - Feature scaling/normalization
   ↓
3. Exploratory Data Analysis (EDA)
   - Phân tích phân phối dữ liệu
   - Kiểm tra imbalanced data
   - Phân tích tương quan giữa các features
   ↓
4. Feature Engineering
   - Tạo features mới từ features hiện có
   - Feature selection
   ↓
5. Model Building
   - Thử nghiệm nhiều mô hình ML
   - Hyperparameter tuning
   - Cross-validation
   ↓
6. Model Evaluation
   - Accuracy, Precision, Recall, F1-Score
   - ROC-AUC Score
   - Confusion Matrix
   ↓
7. Model Deployment & Prediction
   - Dự đoán trên test set
   - Tạo submission file
```

---

## 📝 Ghi chú quan trọng

### Đặc điểm của bài toán:
1. **Binary Classification**: Phân loại 2 class (tốt/xấu)
2. **Imbalanced Data**: Thường số khách hàng tốt >> khách hàng xấu
3. **Missing Values**: Có missing values cần xử lý
4. **High Stakes**: Quyết định cho vay có ảnh hưởng tài chính lớn

### Metrics quan trọng:
- **ROC-AUC**: Đánh giá tổng thể khả năng phân loại
- **Recall (Sensitivity)**: Quan trọng để không bỏ sót khách hàng xấu
- **Precision**: Tránh từ chối nhầm khách hàng tốt
- **F1-Score**: Cân bằng giữa Precision và Recall

### Business Impact:
- **False Positive** (dự đoán xấu nhưng thực tế tốt): Mất cơ hội kinh doanh
- **False Negative** (dự đoán tốt nhưng thực tế xấu): Tổn thất tài chính do nợ xấu

---

## 🔄 Lịch sử cuộc trò chuyện

### Phiên làm việc ngày 2026-03-09

1. ✅ **Khám phá cấu trúc dự án**
   - Xác định thư mục làm việc: "Give Me Some Credit"
   - Phát hiện dataset: cs-training.csv, cs-test.csv, Data Dictionary.xls

2. ✅ **Đọc Data Dictionary**
   - Cài đặt thư viện: xlrd, openpyxl
   - Tạo script đọc Data Dictionary: `read_data_dictionary.py`
   - Tạo tài liệu: `DATA_DICTIONARY.md`

3. ✅ **Xác định mục tiêu dự án**
   - Input: 10 features
   - Output: SeriousDlqin2yrs (0/1)
   - Tạo tài liệu: `PROJECT_OBJECTIVE.md` (file này)

### Tiếp theo cần làm:
- [ ] Exploratory Data Analysis (EDA)
- [ ] Data Preprocessing
- [ ] Feature Engineering
- [ ] Model Building
- [ ] Model Evaluation

---

**Cập nhật lần cuối**: 2026-03-09
**Người thực hiện**: QuangMinh
**Môn học**: MLE501 - Trí tuệ nhân tạo 01 - Học máy
**Dự án**: Final Project - Credit Scoring
