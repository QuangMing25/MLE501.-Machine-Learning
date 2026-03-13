# Credit Scoring - Give Me Some Credit

> Du an phan tich va du doan rui ro tin dung khach hang su dung Machine Learning

## Tong quan

Du an nay nham muc dich xay dung mo hinh Machine Learning de du doan xac suat mot khach hang se gap kho khan tai chinh nghiem trong (no xau) trong vong 2 nam toi.

**Dataset**: Give Me Some Credit (Kaggle Competition)
- **Training set**: 150,000 mau
- **Test set**: 101,503 mau
- **Features**: 10 features goc + 7 features moi (Feature Engineering) = 17 features
- **Target**: SeriousDlqin2yrs - Binary classification (0 = khach tot, 1 = khach xau)
- **Mat can bang lop**: 93.32% Good vs 6.68% Bad (ty le 13.96:1)

## Muc tieu

### Input (10 features goc):
| # | Feature | Mo ta |
|---|---------|-------|
| 1 | RevolvingUtilizationOfUnsecuredLines | Ty le su dung han muc tin dung |
| 2 | age | Tuoi |
| 3 | NumberOfTime30-59DaysPastDueNotWorse | So lan cham 30-59 ngay |
| 4 | DebtRatio | Ty le no/thu nhap |
| 5 | MonthlyIncome | Thu nhap hang thang |
| 6 | NumberOfOpenCreditLinesAndLoans | So khoan vay/the dang mo |
| 7 | NumberOfTimes90DaysLate | So lan cham >=90 ngay |
| 8 | NumberRealEstateLoansOrLines | So khoan vay bat dong san |
| 9 | NumberOfTime60-89DaysPastDueNotWorse | So lan cham 60-89 ngay |
| 10 | NumberOfDependents | So nguoi phu thuoc |

### Features moi (Feature Engineering trong Phase 2):
| # | Feature | Cong thuc | Y nghia |
|---|---------|-----------|---------|
| 11 | TotalLatePayments | Late30 + Late60 + Late90 | Tong hop tin hieu tre no |
| 12 | HasLatePayment | 1 neu TotalLate > 0 | Flag co tre no |
| 13 | IncomePerDependent | Income / (Dependents + 1) | Thu nhap/nguoi phu thuoc |
| 14 | EstMonthlyDebt | DebtRatio x MonthlyIncome | No uoc tinh/thang |
| 15 | HighDebt | 1 neu DebtRatio > 1 | Flag no vuot thu nhap |
| 16 | AgeBin | 6 nhom tuoi | Hieu ung phi tuyen cua tuoi |
| 17 | HighCreditUtil | 1 neu Utilization > 1 | Flag dung het han muc |

### Output:
- **SeriousDlqin2yrs**: 0 (khach tot) hoac 1 (khach xau)

## Cau truc du an

```
Give Me Some Credit/
├── data/
│   ├── raw/                    # Du lieu goc (cs-training.csv, cs-test.csv)
│   ├── processed/              # Du lieu da xu ly (11 CSV + 5 PKL)
│   └── submission/             # Submission files
├── notebooks/
│   ├── 01_EDA.ipynb                        # Phase 1: EDA
│   ├── 02_Preprocessing.ipynb              # Phase 2: Preprocessing & FE
│   ├── 03_Model_Building.ipynb             # Phase 3: Model Building
│   ├── 04_Model_Evaluation.ipynb           # Phase 4: Model Evaluation
│   └── 05_Final_Report.ipynb               # Phase 5: Final Report
├── models/                     # Saved models (.pkl)
├── reports/
│   ├── [1] Ket qua EDA/
│   ├── [2] Ket qua Preprocessing & Feature Engineering/
│   ├── [3] Ket qua Model Building/
│   ├── [4] Ket qua Model Evaluation/
│   └── [5] Final Report/
├── config/
│   └── config.yaml
├── src/                        # Source code (neu can)
├── requirements.txt
├── README.md
├── DATA_DICTIONARY.md
├── PROJECT_OBJECTIVE.md
└── PIPELINE_AND_MODELS.md
```

## 5 Phases

```
Phase 1: EDA                                    [DA XONG]
  - Kham pha du lieu, phan phoi, missing values, outliers, tuong quan
  ↓
Phase 2: Preprocessing & Feature Engineering     [DA XONG]
  - Missing Values (Median Imputation)
  - Outliers (Capping: DebtRatio max=5)
  - Feature Engineering (+7 features moi)
  - Train-Val Split (80/20, Stratified)
  - Feature Scaling (StandardScaler)
  - Imbalance: class_weight='balanced' (Phase 3, khong dung SMOTE)
  ↓
Phase 3: Model Building                          [DA XONG]
  - Train 5 models ML (LR, LinearSVC, RF, XGBoost, LightGBM)
  - Hyperparameter tuning
  ↓
Phase 4: Model Evaluation                        [DA XONG]
  - So sanh 5 models
  - Chon best model: LightGBM (AUC=0.867)
  ↓
Phase 5: Final Report                            [DA XONG]
  - Tong hop ket qua
  - Ket luan & de xuat
  - Tao submission file
```

## 5 Models (chi Machine Learning)

| # | Model | Loai | Vai tro |
|---|-------|------|---------|
| 1 | **Logistic Regression** | Linear | Baseline |
| 2 | **SVM** | Kernel-based | So sanh |
| 3 | **Random Forest** | Ensemble (Bagging) | So sanh |
| 4 | **XGBoost** | Gradient Boosting | So sanh |
| 5 | **LightGBM** | Gradient Boosting | So sanh |

## Evaluation Metrics

**Primary Metrics (khong dung Accuracy vi du lieu mat can bang):**
- **ROC-AUC**: Danh gia tong the kha nang phan biet Good/Bad
- **Recall**: Phat hien khach hang xau (quan trong nhat trong credit scoring)
- **F1-Score**: Can bang Precision & Recall

**Secondary Metrics:**
- Precision
- Confusion Matrix
- PR-AUC
- Classification Report

## Ket qua

| Rank | Model | ROC-AUC | Recall | F1-Score | Precision |
|------|-------|---------|--------|----------|-----------|
| 1 | **LightGBM** | **0.8672** | **0.7711** | 0.3428 | 0.2204 |
| 2 | Logistic Regression | 0.8610 | 0.7616 | 0.3356 | 0.2152 |
| 3 | LinearSVC | 0.8574 | 0.0658 | 0.1182 | 0.5789 |
| 4 | XGBoost | 0.8506 | 0.7042 | 0.3534 | 0.2359 |
| 5 | Random Forest | 0.8335 | 0.1671 | 0.2566 | 0.5528 |

**Best Model**: LightGBM (AUC-ROC = 0.8672, Recall = 77.11%)

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Verify
python -c "import pandas, sklearn, xgboost, lightgbm; print('OK')"
```

## Usage

```bash
# Phase 1: EDA
jupyter notebook notebooks/01_EDA.ipynb

# Phase 2: Preprocessing & Feature Engineering
jupyter notebook notebooks/02_Preprocessing.ipynb

# Phase 3: Model Building
jupyter notebook notebooks/03_Model_Building.ipynb

# Phase 4: Model Evaluation
jupyter notebook notebooks/04_Model_Evaluation.ipynb

# Phase 5: Final Report
jupyter notebook notebooks/05_Final_Report.ipynb
```

## Author

**QuangMinh**
- Course: MLE501 - Tri tue nhan tao 01 - Hoc may
- Semester: Ky II - MSE35HN
- Project: Final Project - Credit Scoring

## Changelog

### Version 3.0.0 (2026-03-13)
- Hoan thanh Phase 3: Model Building - Train 5 models (LR, LinearSVC, RF, XGBoost, LightGBM)
- Hoan thanh Phase 4: Model Evaluation - Best model: LightGBM (AUC=0.867)
- Hoan thanh Phase 5: Final Report - Tong hop ket qua & tao submission
- Cap nhat README voi ket qua thuc te

### Version 2.0.0 (2026-03-11)
- Cap nhat tu 6 phases → 5 phases (gop FE vao Phase 2)
- Cap nhat 5 models: thay Neural Network bang SVM
- Cap nhat cau truc thu muc reports/

### Version 1.0.0 (2026-03-09)
- Khoi tao du an
- Hoan thanh Phase 1: EDA
- Hoan thanh Phase 2: Preprocessing & Feature Engineering

---

**Last Updated**: 2026-03-13
