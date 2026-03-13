# 📊 Exploratory Data Analysis Report
## Credit Scoring - Give Me Some Credit

**Date**: 2026-03-09
**Author**: QuangMinh
**Course**: MLE501 - AI & Machine Learning

---

## 🎯 Executive Summary

Exploratory Data Analysis (EDA) đã được thực hiện trên dataset "Give Me Some Credit" để hiểu rõ cấu trúc dữ liệu, phát hiện các vấn đề cần xử lý, và đưa ra insights cho các bước tiếp theo.

### Key Findings:
- ✅ Dataset lớn với **150,000 mẫu training** và **101,503 mẫu test**
- ⚠️ **Imbalanced data**: Tỷ lệ class 0:1 là **13.96:1** (93.32% vs 6.68%)
- ⚠️ **Missing values**: 2 features có missing (MonthlyIncome: 19.82%, NumberOfDependents: 2.62%)
- ⚠️ **Outliers**: 5 features có >5% outliers
- 📈 **Top correlated features**: NumberOfTime30-59DaysPastDueNotWorse, NumberOfTimes90DaysLate, age

---

## 1️⃣ Dataset Overview

### Dataset Size
| Dataset | Samples | Features | Target |
|---------|---------|----------|--------|
| Training | 150,000 | 10 | SeriousDlqin2yrs |
| Test | 101,503 | 10 | To predict |

### Features List
| # | Feature Name | Data Type | Description |
|---|--------------|-----------|-------------|
| 1 | RevolvingUtilizationOfUnsecuredLines | float64 | Tỷ lệ sử dụng hạn mức tín dụng |
| 2 | age | int64 | Tuổi khách hàng |
| 3 | NumberOfTime30-59DaysPastDueNotWorse | int64 | Số lần chậm 30-59 ngày |
| 4 | DebtRatio | float64 | Tỷ lệ nợ/thu nhập |
| 5 | MonthlyIncome | float64 | Thu nhập hàng tháng |
| 6 | NumberOfOpenCreditLinesAndLoans | int64 | Số khoản vay/thẻ đang mở |
| 7 | NumberOfTimes90DaysLate | int64 | Số lần chậm ≥90 ngày |
| 8 | NumberRealEstateLoansOrLines | int64 | Số khoản vay bất động sản |
| 9 | NumberOfTime60-89DaysPastDueNotWorse | int64 | Số lần chậm 60-89 ngày |
| 10 | NumberOfDependents | float64 | Số người phụ thuộc |

**Target**: SeriousDlqin2yrs (Binary: 0=Good, 1=Bad)

---

## 2️⃣ Missing Values Analysis

### Summary
| Feature | Missing Count | Missing % | Action Required |
|---------|--------------|-----------|-----------------|
| **MonthlyIncome** | 29,731 | **19.82%** | ⚠️ High - Need imputation |
| **NumberOfDependents** | 3,924 | **2.62%** | ✓ Moderate - Need imputation |

### Recommendations:
1. **MonthlyIncome** (19.82% missing):
   - Option 1: Median imputation (simple, robust)
   - Option 2: KNN imputation (more accurate)
   - Option 3: Predict using other features

2. **NumberOfDependents** (2.62% missing):
   - Option 1: Mode imputation (most common value)
   - Option 2: Median imputation
   - ✅ Recommended: Mode or Median

---

## 3️⃣ Target Variable Analysis

### Class Distribution

| Class | Label | Count | Percentage |
|-------|-------|-------|------------|
| 0 | Good Customer | 139,974 | **93.32%** |
| 1 | Bad Customer | 10,026 | **6.68%** |

### Key Insights:

**⚠️ HIGHLY IMBALANCED DATASET**
- Imbalance Ratio: **13.96:1**
- Class 0 (Good) is **13.96x** more than Class 1 (Bad)
- This is typical in credit scoring (most customers are good)

### Impact & Solutions:

**Problems:**
- Models may bias towards majority class
- Poor recall for minority class (bad customers)
- Accuracy is misleading metric

**Solutions:**
1. ✅ **SMOTE** (Synthetic Minority Over-sampling Technique)
2. ✅ **Class weights** in models
3. ✅ Use **stratified** train-test split
4. ✅ Focus on **ROC-AUC** and **Recall** metrics (not Accuracy)

---

## 4️⃣ Descriptive Statistics

### Summary Statistics

| Feature | Count | Missing | Mean | Std | Min | Q25 | Median | Q75 | Max |
|---------|-------|---------|------|-----|-----|-----|--------|-----|-----|
| RevolvingUtilization... | 150,000 | 0 | 6.05 | 249.76 | 0.0 | 0.03 | 0.15 | 0.56 | 50,708 |
| age | 150,000 | 0 | 52.30 | 14.77 | 0 | 41 | 52 | 63 | 109 |
| NumberOfTime30-59Days... | 150,000 | 0 | 0.42 | 4.19 | 0 | 0 | 0 | 0 | 98 |
| DebtRatio | 150,000 | 0 | 353.01 | 2,037.82 | 0.0 | 0.18 | 0.37 | 0.87 | 329,664 |
| MonthlyIncome | 120,269 | 29,731 | 6,670.22 | 14,384.67 | 0 | 3,400 | 5,400 | 8,249 | 3,008,750 |
| NumberOfOpenCredit... | 150,000 | 0 | 8.45 | 5.15 | 0 | 5 | 8 | 11 | 58 |
| NumberOfTimes90Days... | 150,000 | 0 | 0.27 | 4.17 | 0 | 0 | 0 | 0 | 98 |
| NumberRealEstate... | 150,000 | 0 | 1.02 | 1.13 | 0 | 0 | 1 | 2 | 54 |
| NumberOfTime60-89Days... | 150,000 | 0 | 0.24 | 4.16 | 0 | 0 | 0 | 0 | 98 |
| NumberOfDependents | 146,076 | 3,924 | 0.76 | 1.12 | 0 | 0 | 0 | 1 | 20 |

### Key Observations:

1. **RevolvingUtilizationOfUnsecuredLines**:
   - Mean: 6.05, Median: 0.15 → Highly skewed
   - Max: 50,708 → Extreme outliers (>1 doesn't make sense)

2. **age**:
   - Mean: 52.3 years, Median: 52 years
   - Min: 0 → Data error (age can't be 0)
   - Max: 109 → Possible but rare

3. **DebtRatio**:
   - Mean: 353.01, Median: 0.37 → Extremely skewed
   - Max: 329,664 → Extreme outliers

4. **MonthlyIncome**:
   - Mean: $6,670, Median: $5,400
   - Max: $3,008,750 → Extreme outliers
   - 19.82% missing values

5. **Late Payment Features**:
   - Most values are 0 (median = 0)
   - Max = 98 for all three → Possible data entry error or cap

---

## 5️⃣ Outlier Analysis (IQR Method)

### Features with Outliers (Sorted by %)

| Rank | Feature | Outliers Count | Percentage | Severity |
|------|---------|----------------|------------|----------|
| 1 | **DebtRatio** | 31,311 | **20.87%** | 🔴 Critical |
| 2 | **NumberOfTime30-59Days...** | 23,982 | **15.99%** | 🔴 Critical |
| 3 | **NumberOfDependents** | 13,336 | **9.13%** | 🟡 High |
| 4 | **NumberOfTimes90DaysLate** | 8,338 | **5.56%** | 🟡 High |
| 5 | **NumberOfTime60-89Days...** | 7,604 | **5.07%** | 🟡 High |
| 6 | MonthlyIncome | 4,879 | 4.06% | 🟢 Moderate |
| 7 | NumberOfOpenCredit... | 3,980 | 2.65% | 🟢 Moderate |
| 8 | NumberRealEstate... | 793 | 0.53% | 🟢 Low |
| 9 | RevolvingUtilization... | 763 | 0.51% | 🟢 Low |
| 10 | age | 46 | 0.03% | 🟢 Very Low |

### Outlier Treatment Recommendations:

**🔴 Critical (>15% outliers):**
- **DebtRatio**: Capping at 99th percentile (or remove if >1000%)
- **NumberOfTime30-59Days**: Cap at reasonable value (e.g., 10-15)

**🟡 High (5-15% outliers):**
- **NumberOfDependents**: Cap at 10 (20 is unrealistic)
- **NumberOfTimes90/60-89Days**: Cap at 10-15

**🟢 Moderate to Low (<5%):**
- Keep outliers or minimal capping

---

## 6️⃣ Correlation Analysis

### Correlation with Target Variable (SeriousDlqin2yrs)

#### Top 5 Positively Correlated (Higher = More Risk)

| Rank | Feature | Correlation | Interpretation |
|------|---------|-------------|----------------|
| 1 | **NumberOfTime30-59DaysPastDueNotWorse** | **+0.1256** | ⚠️ More late payments → Higher risk |
| 2 | **NumberOfTimes90DaysLate** | **+0.1172** | ⚠️ Severe late payments → Higher risk |
| 3 | **NumberOfTime60-89DaysPastDueNotWorse** | **+0.1023** | ⚠️ Late payments → Higher risk |
| 4 | NumberOfDependents | +0.0460 | More dependents → Slightly higher risk |
| 5 | RevolvingUtilizationOfUnsecuredLines | -0.0018 | Very weak correlation |

#### Top 5 Negatively Correlated (Higher = Less Risk)

| Rank | Feature | Correlation | Interpretation |
|------|---------|-------------|----------------|
| 1 | **age** | **-0.1154** | ✅ Older customers → Lower risk |
| 2 | NumberOfOpenCreditLinesAndLoans | -0.0297 | More credit lines → Slightly lower risk |
| 3 | MonthlyIncome | -0.0197 | Higher income → Slightly lower risk |
| 4 | DebtRatio | -0.0076 | Very weak correlation |
| 5 | NumberRealEstateLoansOrLines | -0.0070 | Very weak correlation |

### Key Insights:

1. **Late Payment History** is the STRONGEST predictor:
   - All 3 late payment features have highest correlation
   - This makes business sense: Past behavior predicts future behavior

2. **Age** is the second most important:
   - Negative correlation: Older customers are more stable

3. **Financial Features** (Income, DebtRatio) have WEAK correlation:
   - Surprising: Expected stronger correlation
   - May need feature engineering

4. **Overall correlations are LOW** (<0.15):
   - Non-linear relationships may exist
   - Tree-based models may perform better than linear models

---

## 7️⃣ Key Insights & Business Understanding

### ✅ Strengths of Dataset:

1. **Large Sample Size**: 150,000 samples → Good for ML
2. **All Numerical Features**: No categorical encoding needed
3. **Real-world Data**: From Kaggle competition, realistic
4. **Business Relevant**: Clear business impact (loan decisions)

### ⚠️ Challenges Identified:

1. **Imbalanced Classes** (13.96:1):
   - Most critical challenge
   - Need special handling (SMOTE, class weights)

2. **Missing Values** (19.82% in MonthlyIncome):
   - Significant missing data
   - Need robust imputation strategy

3. **Extreme Outliers** (5 features with >5%):
   - DebtRatio, Late payment features
   - Need capping or removal

4. **Weak Correlations** (<0.15):
   - Linear models may struggle
   - Need feature engineering
   - Tree-based models preferred

5. **Data Quality Issues**:
   - Age = 0 (impossible)
   - DebtRatio > 100 (doesn't make sense)
   - Need data cleaning

### 🎯 Feature Importance Insights:

**Tier 1 - Most Important** (Correlation >0.10):
- ⭐⭐⭐ NumberOfTime30-59DaysPastDueNotWorse
- ⭐⭐⭐ NumberOfTimes90DaysLate
- ⭐⭐⭐ age (negative)
- ⭐⭐⭐ NumberOfTime60-89DaysPastDueNotWorse

**Tier 2 - Moderate Importance** (0.02 < Correlation < 0.10):
- ⭐⭐ NumberOfDependents
- ⭐⭐ NumberOfOpenCreditLinesAndLoans (negative)
- ⭐⭐ MonthlyIncome (negative)

**Tier 3 - Low Importance** (Correlation < 0.02):
- ⭐ RevolvingUtilizationOfUnsecuredLines
- ⭐ DebtRatio
- ⭐ NumberRealEstateLoansOrLines

---

## 8️⃣ Recommendations for Next Steps

### Phase 2: Data Preprocessing (PRIORITY)

#### 1. Handle Missing Values ⚠️
```python
# MonthlyIncome (19.82% missing)
- Method: Median imputation or KNN imputation
- Rationale: Right-skewed distribution

# NumberOfDependents (2.62% missing)
- Method: Mode or Median imputation
- Rationale: Low % missing, discrete values
```

#### 2. Handle Outliers ⚠️
```python
# Critical outliers:
- DebtRatio: Cap at 99th percentile
- NumberOfTime30-59Days: Cap at 15
- NumberOfTimes90Days: Cap at 15
- NumberOfTime60-89Days: Cap at 15
- NumberOfDependents: Cap at 10

# Data cleaning:
- age: Remove age < 18 or age > 100
- RevolvingUtilization: Cap at 1.5 or 2.0
```

#### 3. Handle Imbalanced Data ⚠️
```python
# Primary method: SMOTE
from imblearn.over_sampling import SMOTE
smote = SMOTE(sampling_strategy=0.5)  # Increase minority to 50% of majority

# Alternative: Class weights
class_weight = {0: 1, 1: 13.96}  # Weight minority class higher
```

#### 4. Feature Scaling ✓
```python
# For Logistic Regression & Neural Networks
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Tree-based models (RF, XGBoost, LightGBM) don't need scaling
```

### Phase 3: Feature Engineering (RECOMMENDED)

#### Create New Features:
```python
# 1. Total late payments
TotalLateDays = (NumberOfTime30-59Days +
                 NumberOfTime60-89Days +
                 NumberOfTimes90Days)

# 2. Late payment severity score
SeverityScore = (NumberOfTime30-59Days * 1 +
                 NumberOfTime60-89Days * 2 +
                 NumberOfTimes90Days * 3)

# 3. Has bad history (binary)
HasBadHistory = (NumberOfTimes90Days > 0).astype(int)

# 4. Income per person
IncomePerPerson = MonthlyIncome / (NumberOfDependents + 1)

# 5. Credit utilization stress
FinancialStress = RevolvingUtilization * DebtRatio

# 6. Credit experience
CreditExperience = NumberOfOpenCreditLines / age

# 7. Age groups (binning)
AgeGroup = pd.cut(age, bins=[0, 30, 50, 70, 120],
                  labels=['Young', 'Middle', 'Senior', 'Elderly'])
```

### Phase 4: Model Strategy

#### Model Selection Priority:
1. **Logistic Regression** (Baseline - Start here)
   - Quick to train
   - Interpretable
   - Expected ROC-AUC: 0.75-0.80

2. **Random Forest** (Good performance)
   - Handles non-linearity
   - Robust to outliers
   - Expected ROC-AUC: 0.82-0.86

3. **XGBoost** (Best performance expected)
   - State-of-the-art
   - Handles missing values
   - Expected ROC-AUC: 0.86-0.90

4. **LightGBM** (Fast & efficient)
   - Similar to XGBoost but faster
   - Expected ROC-AUC: 0.86-0.90

5. **Neural Network** (Complex)
   - May capture complex patterns
   - Needs more tuning
   - Expected ROC-AUC: 0.83-0.88

#### Evaluation Strategy:
```python
# Primary metrics (in order of importance):
1. ROC-AUC Score ⭐⭐⭐⭐⭐ (Most important)
2. Recall (Sensitivity) ⭐⭐⭐⭐⭐ (Don't miss bad customers)
3. Precision ⭐⭐⭐⭐ (Don't reject good customers)
4. F1-Score ⭐⭐⭐ (Balance)
5. Accuracy ⭐⭐ (Misleading with imbalanced data)

# Use stratified K-Fold cross-validation (k=5)
```

---

## 9️⃣ Expected Timeline

| Phase | Estimated Time | Priority |
|-------|---------------|----------|
| ✅ Phase 1: EDA | ~2 hours | Completed |
| Phase 2: Preprocessing | 2-3 hours | High |
| Phase 3: Feature Engineering | 3-4 hours | Medium |
| Phase 4: Model Building | 4-6 hours | High |
| Phase 5: Evaluation | 2-3 hours | High |
| Phase 6: Final Report | 2-3 hours | Medium |

---

## 🔟 Conclusion

### Summary:

EDA đã cung cấp những insights quan trọng về dataset:

1. ✅ Dataset đủ lớn và chất lượng tốt
2. ⚠️ Cần xử lý imbalanced data (quan trọng nhất)
3. ⚠️ Cần impute missing values (MonthlyIncome)
4. ⚠️ Cần xử lý outliers (DebtRatio, Late payments)
5. 📈 Late payment history là predictor mạnh nhất
6. 🎯 Tree-based models sẽ perform tốt hơn linear models

### Next Action:
→ **Proceed to Phase 2: Data Preprocessing**

---

**Report Generated**: 2026-03-09
**Tools Used**: Python, pandas, numpy, matplotlib, seaborn
**Files Generated**:
- `notebooks/01_EDA.ipynb` - Detailed analysis notebook
- `quick_eda.py` - Quick EDA script
- `reports/EDA_REPORT.md` - This report

---
