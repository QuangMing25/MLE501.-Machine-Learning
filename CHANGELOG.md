# 📝 Changelog - Credit Scoring Project

## [1.1.0] - 2026-03-09 - Model Update

### 🔄 Changed

#### Models Selection
**Replaced Neural Network with Support Vector Machine (SVM)**

**Reason**: User requested all models to be Classical Machine Learning (no Deep Learning)

### ❌ Removed:
- **Model 5: Neural Network (MLP)**
  - Type: Deep Learning
  - Framework: TensorFlow/Keras
  - Reason: User wants only ML models

### ✅ Added:
- **Model 2: Support Vector Machine (SVM)**
  - Type: Classical Machine Learning (Kernel-based)
  - Library: scikit-learn
  - Expected ROC-AUC: 0.82-0.87

### 📋 Updated 5 Models List:

| # | Model | Type | Category |
|---|-------|------|----------|
| 1 | Logistic Regression | Linear | Baseline |
| 2 | **Support Vector Machine (SVM)** ⭐ NEW | Kernel-based | Advanced |
| 3 | Random Forest | Ensemble (Bagging) | Tree-based |
| 4 | XGBoost | Ensemble (Boosting) | Tree-based |
| 5 | LightGBM | Ensemble (Boosting) | Tree-based |

### 📁 Files Updated:

1. **MODELS_UPDATED.md** ✅ NEW
   - Detailed documentation of new model lineup
   - SVM specifications and hyperparameters
   - Comparison with removed Neural Network

2. **config/config.yaml** ✅ UPDATED
   - Removed: `neural_network` configuration
   - Added: `svm` configuration with hyperparameters

3. **requirements.txt** ✅ UPDATED
   - Removed: `tensorflow>=2.10.0`
   - Note: "No Deep Learning needed - All Classical ML!"

4. **CHANGELOG.md** ✅ NEW (this file)

### 💡 Benefits of This Change:

✅ **Simpler Setup**:
- No need to install TensorFlow (large dependency)
- Faster environment setup
- Less memory usage

✅ **Faster Training**:
- SVM trains faster than Neural Networks on this dataset
- Less hyperparameter tuning complexity

✅ **More Interpretable**:
- SVM decision boundary can be understood
- No black-box deep learning

✅ **Less Overfitting**:
- SVM is less prone to overfitting than Neural Networks
- More stable across different random seeds

✅ **All Classical ML**:
- Consistent methodology across all 5 models
- Easier to compare and understand

### 📊 Expected Performance Impact:

| Model | Previous Estimate | Current Estimate | Change |
|-------|------------------|------------------|---------|
| Neural Network | 0.83-0.88 | N/A | Removed |
| SVM | N/A | 0.82-0.87 | Added |

**Note**: SVM may perform similarly or slightly better than Neural Network on this dataset while being faster and more stable.

---

## [1.0.0] - 2026-03-09 - Initial Setup

### ✅ Completed

#### Project Structure
- Created complete directory structure
- Set up notebooks/, src/, models/, reports/ folders

#### Documentation (5 files)
1. README.md - Project overview
2. DATA_DICTIONARY.md - Feature descriptions
3. PROJECT_OBJECTIVE.md - Goals and objectives
4. PIPELINE_AND_MODELS.md - Original pipeline (with Neural Network)
5. PROJECT_SUMMARY.md - Progress tracking

#### Configuration
1. config/config.yaml - Complete configuration
2. requirements.txt - Python dependencies
3. .gitignore - Git ignore patterns

#### Data Analysis
1. notebooks/01_EDA.ipynb - Comprehensive EDA notebook
2. quick_eda.py - Quick EDA script
3. reports/EDA_REPORT.md - Detailed EDA findings

#### Key Findings from EDA:
- Dataset: 150,000 training samples
- Imbalanced: 13.96:1 ratio
- Missing values: MonthlyIncome (19.82%), NumberOfDependents (2.62%)
- Outliers: 5 features with >5% outliers
- Top predictors: Late payment features, age

---

## 📅 Timeline

| Date | Version | Description |
|------|---------|-------------|
| 2026-03-09 | 1.0.0 | Initial project setup & EDA |
| 2026-03-09 | 1.1.0 | Model update: Neural Network → SVM |

---

## 🔮 Upcoming Changes

### Phase 2: Data Preprocessing (Planned)
- [ ] Handle missing values
- [ ] Handle outliers
- [ ] Feature scaling
- [ ] Handle imbalanced data

### Phase 3: Feature Engineering (Planned)
- [ ] Create new features
- [ ] Feature selection

### Phase 4: Model Building (Planned)
- [ ] Train all 5 ML models
- [ ] Hyperparameter tuning

### Phase 5: Evaluation (Planned)
- [ ] Compare models
- [ ] Select best model

### Phase 6: Final Report (Planned)
- [ ] Generate predictions
- [ ] Create submission
- [ ] Final report

---

## 📞 Contact

**Author**: QuangMinh
**Course**: MLE501 - AI & Machine Learning
**Date**: 2026-03-09

---
