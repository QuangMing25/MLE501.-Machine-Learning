"""
Predict on cs-test.csv and generate Kaggle submission file.
Uses LightGBM (best model from Phase 4) + same preprocessing pipeline as Phase 2.
"""

import pandas as pd
import numpy as np
import joblib
import os

print("="*80)
print("KAGGLE SUBMISSION — Give Me Some Credit")
print("="*80)

# ============================================================
# 1. Load raw test data
# ============================================================
print("\n[1/5] Loading raw test data...")
test_raw = pd.read_csv('../data/raw/cs-test.csv')
test_id = test_raw['Unnamed: 0']  # Id column
X_test_raw = test_raw.drop(columns=['Unnamed: 0', 'SeriousDlqin2yrs'])

print(f"  Shape: {X_test_raw.shape}")
print(f"  Missing values:\n{X_test_raw.isnull().sum()[X_test_raw.isnull().sum() > 0]}")

# ============================================================
# 2. Apply same preprocessing as Phase 2
# ============================================================
print("\n[2/5] Applying preprocessing pipeline...")

processed_dir = '../data/processed/'

# --- Step 1: Impute Missing Values ---
income_imputer = joblib.load(processed_dir + 'income_imputer.pkl')
dependents_imputer = joblib.load(processed_dir + 'dependents_imputer.pkl')

missing_income = X_test_raw['MonthlyIncome'].isnull().sum()
missing_dep = X_test_raw['NumberOfDependents'].isnull().sum()

# SimpleImputer → dùng .transform()
X_test_raw['MonthlyIncome'] = income_imputer.transform(X_test_raw[['MonthlyIncome']]).ravel()
X_test_raw['NumberOfDependents'] = dependents_imputer.transform(X_test_raw[['NumberOfDependents']]).ravel()

print(f"  Imputed MonthlyIncome: {missing_income:,} values")
print(f"  Imputed NumberOfDependents: {missing_dep:,} values")

# --- Step 2: Cap Outliers ---
capping_rules = joblib.load(processed_dir + 'capping_rules.pkl')

for feature, rules in capping_rules.items():
    min_val = rules.get('min', None)
    max_val = rules.get('max', None)
    if min_val is not None:
        X_test_raw[feature] = X_test_raw[feature].clip(lower=min_val)
    if max_val is not None:
        X_test_raw[feature] = X_test_raw[feature].clip(upper=max_val)

print(f"  Outliers capped: {len(capping_rules)} features")

# --- Step 3: Feature Engineering (same as Phase 2) ---
X_test_raw['TotalLatePayments'] = (
    X_test_raw['NumberOfTime30-59DaysPastDueNotWorse'] +
    X_test_raw['NumberOfTime60-89DaysPastDueNotWorse'] +
    X_test_raw['NumberOfTimes90DaysLate']
)
X_test_raw['HasLatePayment'] = (X_test_raw['TotalLatePayments'] > 0).astype(int)

X_test_raw['IncomePerDependent'] = X_test_raw['MonthlyIncome'] / (X_test_raw['NumberOfDependents'] + 1)
X_test_raw['EstMonthlyDebt'] = X_test_raw['DebtRatio'] * X_test_raw['MonthlyIncome']

# Cap FE features (using saved values from Phase 2)
fe_capping = joblib.load(processed_dir + 'fe_capping.pkl')
X_test_raw['IncomePerDependent'] = X_test_raw['IncomePerDependent'].clip(upper=fe_capping['IncomePerDependent_cap'])
X_test_raw['EstMonthlyDebt'] = X_test_raw['EstMonthlyDebt'].clip(upper=fe_capping['EstMonthlyDebt_cap'])

X_test_raw['HighDebt'] = (X_test_raw['DebtRatio'] > 1).astype(int)

age_bins = [0, 30, 40, 50, 60, 70, 120]
age_labels = [0, 1, 2, 3, 4, 5]
X_test_raw['AgeBin'] = pd.cut(X_test_raw['age'], bins=age_bins, labels=age_labels).astype(int)

X_test_raw['HighCreditUtil'] = (X_test_raw['RevolvingUtilizationOfUnsecuredLines'] > 1).astype(int)

print(f"  Feature Engineering: 7 new features added")
print(f"  Final shape: {X_test_raw.shape}")

# ============================================================
# 3. Verify features match training data
# ============================================================
print("\n[3/5] Verifying features...")
X_train_ref = pd.read_csv(processed_dir + 'X_train.csv')
train_features = X_train_ref.columns.tolist()
test_features = X_test_raw.columns.tolist()

if train_features == test_features:
    print(f"  ✅ Features match! ({len(train_features)} features)")
else:
    missing = set(train_features) - set(test_features)
    extra = set(test_features) - set(train_features)
    if missing:
        print(f"  ⚠️ Missing features: {missing}")
    if extra:
        print(f"  ⚠️ Extra features: {extra}")
    # Reorder to match training
    X_test_raw = X_test_raw[train_features]
    print(f"  Reordered to match training features")

# ============================================================
# 4. Predict with LightGBM (best model)
# ============================================================
print("\n[4/5] Predicting with LightGBM (best model)...")
lgbm_model = joblib.load('../models/lightgbm.pkl')

# LightGBM uses unscaled data
y_prob = lgbm_model.predict_proba(X_test_raw)[:, 1]

print(f"  Predictions: {len(y_prob):,} samples")
print(f"  Probability range: [{y_prob.min():.4f}, {y_prob.max():.4f}]")
print(f"  Mean probability: {y_prob.mean():.4f}")

# ============================================================
# 5. Create submission file
# ============================================================
print("\n[5/5] Creating submission file...")

submission = pd.DataFrame({
    'Id': test_id,
    'Probability': y_prob
})

output_dir = '../data/submission/'
os.makedirs(output_dir, exist_ok=True)
output_path = output_dir + 'submission_lightgbm.csv'
submission.to_csv(output_path, index=False)

print(f"\n{'='*80}")
print(f"✅ SUBMISSION FILE CREATED")
print(f"{'='*80}")
print(f"  File: {output_path}")
print(f"  Shape: {submission.shape}")
print(f"  Preview:")
print(submission.head(10).to_string(index=False))
