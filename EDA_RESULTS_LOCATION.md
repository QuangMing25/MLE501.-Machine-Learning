# 📍 EDA Results - Vị trí lưu trữ
## Phase 1: Exploratory Data Analysis

**Date Completed**: 2026-03-10
**Author**: QuangMinh

---

## 📂 Cấu trúc thư mục kết quả EDA

```
Give Me Some Credit/
├── notebooks/
│   └── 01_EDA.ipynb ⭐⭐⭐⭐⭐          # Notebook EDA chi tiết (28KB)
│
├── reports/
│   ├── EDA_REPORT.md ⭐⭐⭐⭐          # Báo cáo EDA đầy đủ (14KB)
│   ├── summary_statistics.csv ⭐⭐⭐   # Thống kê mô tả (1.7KB)
│   ├── correlation_matrix.csv ⭐⭐⭐   # Ma trận tương quan (2.8KB)
│   ├── outlier_analysis.csv ⭐⭐      # Phân tích outliers (1.0KB)
│   ├── ttest_results.csv ⭐⭐         # Kết quả t-test (1.1KB)
│   │
│   └── figures/                       # Visualizations (7 files, 3.0MB)
│       ├── 01_missing_values.png ⭐⭐⭐⭐⭐
│       ├── 02_target_distribution.png ⭐⭐⭐⭐⭐
│       ├── 03_feature_distributions.png ⭐⭐⭐⭐⭐
│       ├── 04_boxplots_outliers.png ⭐⭐⭐⭐⭐
│       ├── 05_correlation_heatmap.png ⭐⭐⭐⭐⭐
│       ├── 06_target_correlation.png ⭐⭐⭐⭐⭐
│       └── 07_distributions_by_target.png ⭐⭐⭐⭐⭐
│
└── quick_eda.py ⭐⭐⭐                  # Script EDA nhanh (5.6KB)
```

---

## 📊 1. Notebook EDA (CHI TIẾT NHẤT)

### 📍 Vị trí:
```
notebooks/01_EDA.ipynb
```

### 📝 Nội dung:
Notebook Jupyter chi tiết với **10 sections**:

1. ✅ **Import Libraries** - Setup môi trường
2. ✅ **Load Data** - Load training & test data
3. ✅ **Data Overview** - Shape, info, columns
4. ✅ **Descriptive Statistics** - Mean, median, std, etc.
5. ✅ **Missing Values Analysis** - Phân tích giá trị thiếu
6. ✅ **Target Variable Analysis** - Class distribution & imbalance
7. ✅ **Feature Distributions** - Histograms & boxplots
8. ✅ **Outlier Analysis** - IQR method
9. ✅ **Correlation Analysis** - Heatmap & correlations
10. ✅ **Feature vs Target** - Distributions by class
11. ✅ **Statistical Tests** - T-tests
12. ✅ **Key Insights** - Tóm tắt findings
13. ✅ **Save Results** - Export to CSV

### 🚀 Cách mở:
```bash
cd "/Users/quangminh/QuangMinh/MSE35HN/Ky_[II]/[2.2] MLE501. Tri tue nhan tao 01_Hoc may/[4] Final Project/Give Me Some Credit"

# Option 1: Jupyter Notebook
jupyter notebook notebooks/01_EDA.ipynb

# Option 2: JupyterLab
jupyter lab notebooks/01_EDA.ipynb

# Option 3: VS Code
code notebooks/01_EDA.ipynb
```

### ⭐ Ưu điểm:
- Interactive (có thể chạy lại từng cell)
- Có visualizations đầy đủ
- Code + markdown + charts
- Chi tiết nhất

---

## 📄 2. EDA Report (BÁO CÁO VĂN BẢN)

### 📍 Vị trí:
```
reports/EDA_REPORT.md
```

### 📝 Nội dung:
Báo cáo markdown chi tiết **14KB** với 10 sections:

1. **Executive Summary** - Tóm tắt findings
2. **Dataset Overview** - Thông tin dataset
3. **Missing Values Analysis** - Phân tích missing values
4. **Target Variable Analysis** - Class distribution
5. **Descriptive Statistics** - Bảng thống kê
6. **Outlier Analysis** - IQR method results
7. **Correlation Analysis** - Correlations với target
8. **Key Insights** - Business understanding
9. **Recommendations** - Next steps chi tiết
10. **Conclusion** - Tổng kết

### 🚀 Cách xem:
```bash
# Option 1: VS Code (with Markdown Preview)
code reports/EDA_REPORT.md

# Option 2: Terminal (cat)
cat reports/EDA_REPORT.md

# Option 3: Any text editor
open reports/EDA_REPORT.md
```

### ⭐ Ưu điểm:
- Dễ đọc (markdown format)
- Có bảng biểu rõ ràng
- Recommendations chi tiết
- Không cần Python/Jupyter

---

## 🖼️ 3. Visualizations (CHARTS & GRAPHS)

### 📍 Vị trí:
```
reports/figures/
```

### 📊 7 Charts (Total: 3.0MB)

#### 1️⃣ **01_missing_values.png** (134KB)
- Missing values trong training & test sets
- Bar chart showing percentage missing
- **Key Insight**: MonthlyIncome (19.82%), NumberOfDependents (2.62%)

#### 2️⃣ **02_target_distribution.png** (190KB)
- Target class distribution
- Bar chart + Pie chart
- **Key Insight**: Imbalance 13.96:1 (93.32% vs 6.68%)

#### 3️⃣ **03_feature_distributions.png** (791KB)
- Histograms của tất cả 10 features
- 10 subplots với mean & median lines
- **Key Insight**: Nhiều features bị skewed

#### 4️⃣ **04_boxplots_outliers.png** (749KB)
- Boxplots cho outlier detection
- 10 subplots với outlier percentages
- **Key Insight**: DebtRatio (20.87%), Late payments (15.99%)

#### 5️⃣ **05_correlation_heatmap.png** (487KB)
- Correlation matrix heatmap
- All features + target
- **Key Insight**: Late payment features có correlation cao nhất

#### 6️⃣ **06_target_correlation.png** (212KB)
- Bar chart: Correlation of each feature với target
- Positive (green) & negative (red)
- **Key Insight**: NumberOfTime30-59Days (+0.1256), age (-0.1154)

#### 7️⃣ **07_distributions_by_target.png** (443KB)
- Feature distributions split by target class (0 vs 1)
- Top 6 most correlated features
- **Key Insight**: Clear separation in late payment features

### 🚀 Cách xem:
```bash
# Open figures folder
open reports/figures/

# View specific chart
open reports/figures/02_target_distribution.png

# View all at once (macOS)
open reports/figures/*.png
```

### ⭐ Ưu điểm:
- High resolution (300 DPI)
- Publication ready
- Rõ ràng, dễ hiểu
- Có thể dùng cho presentation

---

## 📈 4. CSV Data Files (DỮ LIỆU SỐ)

### 4.1 Summary Statistics

**📍 Vị trí**: `reports/summary_statistics.csv`

**📝 Nội dung**:
- Thống kê mô tả cho tất cả features
- Columns: dtype, count, missing, mean, std, min, q25, median, q75, max, skewness, kurtosis
- **Use case**: Import vào Excel/Python để phân tích thêm

```bash
# View in terminal
cat reports/summary_statistics.csv

# Open in Excel/Numbers
open reports/summary_statistics.csv
```

### 4.2 Correlation Matrix

**📍 Vị trí**: `reports/correlation_matrix.csv`

**📝 Nội dung**:
- Ma trận tương quan đầy đủ (11x11)
- All features + target
- **Use case**: Phát hiện multicollinearity, feature selection

```bash
cat reports/correlation_matrix.csv
```

### 4.3 Outlier Analysis

**📍 Vị trí**: `reports/outlier_analysis.csv`

**📝 Nội dung**:
- IQR bounds cho mỗi feature
- Outlier count & percentage
- **Use case**: Quyết định cách xử lý outliers

```bash
cat reports/outlier_analysis.csv
```

### 4.4 T-Test Results

**📍 Vị trí**: `reports/ttest_results.csv`

**📝 Nội dung**:
- T-test results cho mỗi feature (Class 0 vs Class 1)
- Mean của mỗi class, p-values
- **Use case**: Kiểm định statistical significance

```bash
cat reports/ttest_results.csv
```

---

## 🚀 5. Quick EDA Script (NHANH)

### 📍 Vị trí:
```
quick_eda.py
```

### 📝 Chức năng:
Script Python để chạy EDA nhanh trong terminal (không cần Jupyter)

**Output**:
- Dataset overview
- Missing values
- Target distribution
- Descriptive statistics
- Outliers
- Correlation with target
- Key insights & recommendations

### 🚀 Cách chạy:
```bash
cd "/Users/quangminh/QuangMinh/MSE35HN/Ky_[II]/[2.2] MLE501. Tri tue nhan tao 01_Hoc may/[4] Final Project/Give Me Some Credit"

python quick_eda.py
```

### ⏱️ Execution time: ~10-15 seconds

### ⭐ Ưu điểm:
- Cực nhanh
- Không cần Jupyter
- Output trực tiếp terminal
- Dễ share (text output)

---

## 📋 Tóm tắt theo Use Case

### 🎯 Bạn muốn gì?

#### **A. Xem tổng quan nhanh**
→ Chạy: `python quick_eda.py`
→ Time: 10 seconds

#### **B. Đọc báo cáo chi tiết**
→ Mở: `reports/EDA_REPORT.md`
→ Format: Markdown (dễ đọc)

#### **C. Xem charts/visualizations**
→ Mở folder: `reports/figures/`
→ 7 PNG files (high resolution)

#### **D. Phân tích interactive**
→ Mở: `notebooks/01_EDA.ipynb` trong Jupyter
→ Có thể chạy lại, modify code

#### **E. Export dữ liệu số**
→ CSV files trong: `reports/*.csv`
→ 4 files: statistics, correlation, outliers, ttests

#### **F. Presentation/Report**
→ Use: PNG charts từ `reports/figures/`
→ + Text insights từ `EDA_REPORT.md`

---

## 📊 Key Findings (Tóm tắt nhanh)

### 🎯 Dataset:
- **Training**: 150,000 samples
- **Test**: 101,503 samples
- **Features**: 10 numerical features

### ⚠️ Issues Found:
1. **Imbalanced Data**: 13.96:1 ratio (93.32% vs 6.68%)
2. **Missing Values**:
   - MonthlyIncome: 19.82%
   - NumberOfDependents: 2.62%
3. **Outliers**: 5 features với >5% outliers

### 📈 Top Predictors:
1. NumberOfTime30-59DaysPastDueNotWorse (+0.1256)
2. NumberOfTimes90DaysLate (+0.1172)
3. age (-0.1154)
4. NumberOfTime60-89DaysPastDueNotWorse (+0.1023)

### 💡 Recommendations:
1. Handle missing values (imputation)
2. Handle outliers (capping)
3. Handle imbalanced data (SMOTE)
4. Feature scaling (for Logistic & SVM)
5. Feature engineering (create new features)

---

## 🔄 Next Steps

### Immediate (Để xem kết quả):
```bash
# 1. Quick overview
python quick_eda.py

# 2. Open Jupyter notebook
jupyter notebook notebooks/01_EDA.ipynb

# 3. View visualizations
open reports/figures/

# 4. Read full report
open reports/EDA_REPORT.md
```

### After reviewing EDA:
→ **Phase 2**: Data Preprocessing
→ **Phase 3**: Feature Engineering
→ **Phase 4**: Model Building

---

## 📞 Files Summary

| File Type | Location | Size | Purpose |
|-----------|----------|------|---------|
| **Notebook** | notebooks/01_EDA.ipynb | 28KB | Interactive analysis |
| **Report** | reports/EDA_REPORT.md | 14KB | Full written report |
| **Charts** | reports/figures/*.png | 3.0MB | 7 visualizations |
| **CSV** | reports/*.csv | ~7KB | Raw analysis data |
| **Script** | quick_eda.py | 5.6KB | Quick terminal EDA |

**Total EDA Output**: ~3.1MB (excluding data)

---

## ✅ EDA Status: COMPLETED

**Completion Date**: 2026-03-10
**Next Phase**: Data Preprocessing

---

**Document Created**: 2026-03-10
**Last Updated**: 2026-03-10
