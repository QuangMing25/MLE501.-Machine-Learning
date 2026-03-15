"""
Quick EDA Script - Credit Scoring
Run this for a quick overview of the data
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("QUICK EDA - CREDIT SCORING")
print("="*80)

# Load data
print("\n📂 Loading data...")
train_df = pd.read_csv('data/raw/cs-training.csv')
test_df = pd.read_csv('data/raw/cs-test.csv')

# Drop unnamed column if exists
if 'Unnamed: 0' in train_df.columns:
    train_df = train_df.drop('Unnamed: 0', axis=1)
    test_df = test_df.drop('Unnamed: 0', axis=1)

print(f"✅ Training data: {train_df.shape}")
print(f"✅ Test data: {test_df.shape}")

# 1. Basic Info
print("\n" + "="*80)
print("1️⃣ DATASET OVERVIEW")
print("="*80)
print(f"\nTraining samples: {train_df.shape[0]:,}")
print(f"Test samples: {test_df.shape[0]:,}")
print(f"Number of features: {train_df.shape[1] - 1}")

print("\nColumns:")
for i, col in enumerate(train_df.columns, 1):
    dtype = train_df[col].dtype
    print(f"  {i}. {col:45s} ({dtype})")

# 2. Missing Values
print("\n" + "="*80)
print("2️⃣ MISSING VALUES ANALYSIS")
print("="*80)

missing = pd.DataFrame({
    'Column': train_df.columns,
    'Missing_Count': train_df.isnull().sum().values,
    'Missing_Percentage': (train_df.isnull().sum().values / len(train_df) * 100).round(2)
})
missing = missing[missing['Missing_Count'] > 0].sort_values('Missing_Percentage', ascending=False)

if len(missing) == 0:
    print("\n✅ No missing values found!")
else:
    print(f"\n⚠️  Found {len(missing)} columns with missing values:\n")
    for _, row in missing.iterrows():
        print(f"   • {row['Column']:45s}: {row['Missing_Count']:6,} ({row['Missing_Percentage']:5.2f}%)")

# 3. Target Variable
print("\n" + "="*80)
print("3️⃣ TARGET VARIABLE ANALYSIS")
print("="*80)

target_col = 'SeriousDlqin2yrs'
target_counts = train_df[target_col].value_counts().sort_index()
target_pct = (target_counts / len(train_df) * 100).round(2)

print(f"\nClass Distribution:")
print(f"   • Class 0 (Good): {target_counts.iloc[0]:7,} ({target_pct.iloc[0]:5.2f}%)")
print(f"   • Class 1 (Bad):  {target_counts.iloc[1]:7,} ({target_pct.iloc[1]:5.2f}%)")

imbalance_ratio = target_counts.iloc[0] / target_counts.iloc[1]
print(f"\n⚠️  Imbalance Ratio: {imbalance_ratio:.2f}:1")
print(f"    → Class 0 is {imbalance_ratio:.2f}x more than Class 1")

# 4. Descriptive Statistics
print("\n" + "="*80)
print("4️⃣ DESCRIPTIVE STATISTICS")
print("="*80)

numerical_features = train_df.select_dtypes(include=[np.number]).columns.tolist()
if target_col in numerical_features:
    numerical_features.remove(target_col)

print(f"\nNumerical features: {len(numerical_features)}\n")

stats_summary = []
for feature in numerical_features:
    data = train_df[feature].dropna()
    stats_summary.append({
        'Feature': feature,
        'Count': len(data),
        'Missing': train_df[feature].isnull().sum(),
        'Mean': data.mean(),
        'Std': data.std(),
        'Min': data.min(),
        'Q25': data.quantile(0.25),
        'Median': data.median(),
        'Q75': data.quantile(0.75),
        'Max': data.max()
    })

stats_df = pd.DataFrame(stats_summary)
print(stats_df.to_string(index=False))

# 5. Outliers
print("\n" + "="*80)
print("5️⃣ OUTLIER DETECTION (IQR Method)")
print("="*80)

outlier_summary = []
for feature in numerical_features:
    data = train_df[feature].dropna()
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = ((data < lower_bound) | (data > upper_bound)).sum()
    outliers_pct = (outliers / len(data)) * 100

    outlier_summary.append({
        'Feature': feature,
        'Outliers': outliers,
        'Percentage': outliers_pct
    })

outlier_df = pd.DataFrame(outlier_summary).sort_values('Percentage', ascending=False)
print("\nFeatures with outliers (sorted by percentage):\n")
for _, row in outlier_df.iterrows():
    if row['Percentage'] > 0:
        print(f"   • {row['Feature']:45s}: {row['Outliers']:6,} ({row['Percentage']:5.2f}%)")

# 6. Correlation with Target
print("\n" + "="*80)
print("6️⃣ CORRELATION WITH TARGET")
print("="*80)

correlation = train_df[numerical_features + [target_col]].corr()[target_col].drop(target_col)
correlation = correlation.sort_values(ascending=False)

print("\nTop 5 Positively Correlated:")
for i, (feature, corr) in enumerate(correlation.head(5).items(), 1):
    print(f"   {i}. {feature:45s}: {corr:+.4f}")

print("\nTop 5 Negatively Correlated:")
for i, (feature, corr) in enumerate(correlation.tail(5).items(), 1):
    print(f"   {i}. {feature:45s}: {corr:+.4f}")

# 7. Recommendations
print("\n" + "="*80)
print("💡 KEY INSIGHTS & RECOMMENDATIONS")
print("="*80)

print("\n✅ STRENGTHS:")
print("   • Large dataset (150,000 samples)")
print("   • All numerical features (easy to process)")

print("\n⚠️  CHALLENGES:")
if len(missing) > 0:
    print(f"   • Missing values in {len(missing)} features need imputation")
print(f"   • Highly imbalanced dataset ({imbalance_ratio:.1f}:1)")
high_outliers = outlier_df[outlier_df['Percentage'] > 5]
if len(high_outliers) > 0:
    print(f"   • {len(high_outliers)} features have >5% outliers")

print("\n📋 NEXT STEPS:")
print("   1. Handle missing values (imputation)")
print("   2. Treat outliers (capping/removal)")
print("   3. Address class imbalance (SMOTE/class_weight)")
print("   4. Feature scaling (StandardScaler)")
print("   5. Feature engineering (create new features)")
print("   6. Model building & evaluation")

print("\n" + "="*80)
print("✅ Quick EDA completed!")
print("📊 For detailed analysis, open: notebooks/01_EDA.ipynb")
print("="*80)
