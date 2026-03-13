# [2] Kết quả Preprocessing
## Phase 2: Data Preprocessing

**Status**: ⏳ Pending
**Expected completion**: TBD

---

## 🎯 Mục tiêu Phase 2

Làm sạch và chuẩn bị dữ liệu cho modeling:

1. ✅ Handle missing values (imputation)
2. ✅ Handle outliers (capping/removal)
3. ✅ Feature scaling (StandardScaler)
4. ✅ Handle imbalanced data (SMOTE)
5. ✅ Train-validation split

---

## 📁 Files sẽ được lưu trong thư mục này

### 1. Notebook
- `02_Preprocessing.ipynb` - Jupyter notebook chi tiết

### 2. Processed Data
- `train_cleaned.csv` - Training data sau khi clean
- `test_cleaned.csv` - Test data sau khi clean
- `train_preprocessed.csv` - Data sau preprocessing hoàn chỉnh
- `X_train.csv`, `X_val.csv` - Features split
- `y_train.csv`, `y_val.csv` - Target split

### 3. Preprocessing Objects
- `scaler.pkl` - StandardScaler object
- `imputer_income.pkl` - Imputer for MonthlyIncome
- `imputer_dependents.pkl` - Imputer for NumberOfDependents
- `preprocessing_pipeline.pkl` - Complete pipeline

### 4. Reports
- `preprocessing_report.md` - Báo cáo chi tiết
- `missing_values_before_after.csv` - Before/after comparison
- `outliers_summary.csv` - Outlier treatment summary
- `data_quality_report.csv` - Data quality metrics

### 5. Visualizations
- `missing_values_comparison.png` - Before/after
- `outliers_before_after.png` - Boxplots comparison
- `distribution_after_preprocessing.png` - New distributions
- `class_balance_smote.png` - SMOTE effect

---

## 📊 Expected Outputs

### Data Quality Improvements:
- ❌ Missing values: 0%
- ✅ Outliers: Reduced to <2%
- ✅ All features scaled (mean=0, std=1)
- ✅ Class balance improved (from 13.96:1 to ~2:1 with SMOTE)

### Files Size Estimate:
- Cleaned data: ~30MB
- Preprocessing objects: ~1MB
- Reports: ~500KB
- Visualizations: ~2MB

**Total**: ~33MB

---

## 🔧 Tools & Methods

### Missing Values:
- **MonthlyIncome**: Median imputation
- **NumberOfDependents**: Median imputation

### Outliers:
- **Method**: IQR capping
- **Thresholds**:
  - age: 18-100
  - DebtRatio: 99th percentile
  - RevolvingUtilization: 2.0
  - Late payment features: Cap at 15

### Scaling:
- **Method**: StandardScaler
- **Features**: All numerical features
- **Note**: Only for Logistic Regression & SVM

### Imbalanced Data:
- **Method**: SMOTE
- **Ratio**: Increase minority to 50% of majority
- **Note**: Only on training set

---

## 📝 Checklist

- [ ] Handle missing values
- [ ] Handle outliers
- [ ] Feature scaling
- [ ] Handle imbalanced data
- [ ] Train-validation split
- [ ] Save processed data
- [ ] Save preprocessing objects
- [ ] Create visualizations
- [ ] Write report
- [ ] Verify data quality

---

**Created**: 2026-03-10
**Last updated**: TBD
