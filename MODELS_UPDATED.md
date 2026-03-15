# 🤖 5 Machine Learning Models - Updated
## Credit Scoring Project

**Updated**: 2026-03-09
**Change**: Removed Neural Network (Deep Learning) → Replaced with Support Vector Machine (SVM)

---

## 🎯 5 Machine Learning Models (All Classical ML)

| # | Model | Type | Category | Performance | Speed |
|---|-------|------|----------|-------------|-------|
| 1 | **Logistic Regression** | Linear | Baseline | ⭐⭐⭐ | ⚡⚡⚡⚡⚡ |
| 2 | **Support Vector Machine (SVM)** | Kernel-based | Advanced Linear | ⭐⭐⭐⭐ | ⚡⚡⚡ |
| 3 | **Random Forest** | Ensemble (Bagging) | Tree-based | ⭐⭐⭐⭐ | ⚡⚡⚡ |
| 4 | **XGBoost** | Ensemble (Boosting) | Tree-based | ⭐⭐⭐⭐⭐ | ⚡⚡⚡⚡ |
| 5 | **LightGBM** | Ensemble (Boosting) | Tree-based | ⭐⭐⭐⭐⭐ | ⚡⚡⚡⚡⚡ |

---

## Chi tiết từng Model

### **Model 1: Logistic Regression** (Baseline)

**Loại**: Linear Classifier

**Lý do chọn:**
- ✅ Model đơn giản nhất, dễ hiểu
- ✅ Baseline performance tốt cho binary classification
- ✅ Training cực nhanh
- ✅ Interpretable (có thể giải thích coefficients)
- ✅ Phù hợp khi features có quan hệ tuyến tính với target

**Ưu điểm:**
- Rất nhanh (training & prediction)
- Dễ giải thích cho business
- Ít hyperparameters cần tune
- Hoạt động tốt với large dataset
- Output là probability (useful cho threshold tuning)

**Nhược điểm:**
- Giả định linear relationship
- Không capture non-linear patterns
- Kém với complex feature interactions

**Hyperparameters cần tune:**
```python
from sklearn.linear_model import LogisticRegression

params = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],  # Regularization strength
    'penalty': ['l1', 'l2'],               # L1 (Lasso) or L2 (Ridge)
    'solver': ['liblinear', 'saga'],       # For L1
    'class_weight': ['balanced', None],    # Handle imbalance
    'max_iter': 1000
}
```

**Expected Performance**: ROC-AUC ~ 0.75-0.80

---

### **Model 2: Support Vector Machine (SVM)** ⭐ NEW!

**Loại**: Kernel-based Classifier

**Lý do chọn (thay Neural Network):**
- ✅ Classical ML (không phải Deep Learning)
- ✅ Mạnh mẽ với classification problems
- ✅ Kernel trick cho phép học non-linear patterns
- ✅ Hiệu quả với medium-sized datasets
- ✅ Robust với outliers (khi dùng RBF kernel)
- ✅ Ít overfitting hơn Neural Networks

**Ưu điểm:**
- Hiệu quả trong high-dimensional spaces
- Memory efficient (chỉ dùng support vectors)
- Versatile (nhiều kernel functions: linear, RBF, poly)
- Robust với outliers
- Hoạt động tốt với clear margin of separation

**Nhược điểm:**
- Training chậm với large datasets (>100k samples)
- Cần feature scaling bắt buộc
- Khó interpret hơn Logistic Regression
- Hyperparameter tuning phức tạp

**Hyperparameters cần tune:**
```python
from sklearn.svm import SVC

params = {
    'C': [0.1, 1, 10, 100],                    # Regularization
    'kernel': ['linear', 'rbf', 'poly'],       # Kernel type
    'gamma': ['scale', 'auto', 0.001, 0.01],   # For RBF/poly
    'degree': [2, 3, 4],                       # For poly kernel
    'class_weight': ['balanced', None],        # Handle imbalance
    'probability': True                        # Enable probability estimates
}
```

**Note**:
- Với 150k samples, có thể training chậm
- Recommend: Train trên subset hoặc dùng LinearSVC (nhanh hơn)

**Expected Performance**: ROC-AUC ~ 0.82-0.87

**Comparison với Neural Network:**
| Aspect | SVM | Neural Network |
|--------|-----|----------------|
| Type | Classical ML ✅ | Deep Learning ❌ |
| Training Speed | Moderate | Slow |
| Tuning Complexity | Medium | High |
| Interpretability | Low | Very Low |
| Performance | Good | Good-Excellent |
| Overfitting Risk | Medium | High |

---

### **Model 3: Random Forest**

**Loại**: Ensemble Learning (Bagging)

**Lý do chọn:**
- ✅ Mạnh với non-linear relationships
- ✅ Robust với outliers
- ✅ Không cần feature scaling
- ✅ Feature importance built-in
- ✅ Handle missing values tốt

**Ưu điểm:**
- Reduce overfitting (ensemble of trees)
- Hoạt động tốt out-of-the-box
- Parallel training (nhanh)
- Feature importance
- Robust với outliers & missing values

**Nhược điểm:**
- Memory intensive
- Chậm prediction với nhiều trees
- Kém interpretable

**Hyperparameters cần tune:**
```python
from sklearn.ensemble import RandomForestClassifier

params = {
    'n_estimators': [100, 200, 300, 500],
    'max_depth': [10, 20, 30, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2', None],
    'class_weight': ['balanced', 'balanced_subsample', None],
    'bootstrap': [True],
    'n_jobs': -1
}
```

**Expected Performance**: ROC-AUC ~ 0.83-0.87

---

### **Model 4: XGBoost**

**Loại**: Gradient Boosting

**Lý do chọn:**
- ✅ State-of-the-art cho tabular data
- ✅ Thường thắng Kaggle competitions
- ✅ Xử lý missing values tự động
- ✅ Regularization tránh overfitting
- ✅ Feature importance

**Ưu điểm:**
- Performance tốt nhất cho tabular data
- Xử lý missing values
- Built-in regularization
- Training nhanh (parallel)
- Early stopping
- Feature importance

**Nhược điểm:**
- Nhiều hyperparameters
- Dễ overfitting nếu không tune
- Cần thời gian tune

**Hyperparameters cần tune:**
```python
import xgboost as xgb

params = {
    'n_estimators': [100, 200, 300, 500],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'max_depth': [3, 5, 7, 9],
    'min_child_weight': [1, 3, 5],
    'subsample': [0.7, 0.8, 0.9, 1.0],
    'colsample_bytree': [0.7, 0.8, 0.9, 1.0],
    'gamma': [0, 0.1, 0.2, 0.5],
    'reg_alpha': [0, 0.1, 0.5, 1],
    'reg_lambda': [0, 0.1, 0.5, 1],
    'scale_pos_weight': [1, 5, 10, 13.96],  # For imbalance
    'eval_metric': 'auc',
    'tree_method': 'hist'
}
```

**Expected Performance**: ROC-AUC ~ 0.86-0.91

---

### **Model 5: LightGBM**

**Loại**: Gradient Boosting (Optimized)

**Lý do chọn:**
- ✅ Nhanh hơn XGBoost rất nhiều
- ✅ Hiệu quả với large datasets
- ✅ Performance tương đương XGBoost
- ✅ Dùng ít memory
- ✅ Handle categorical features

**Ưu điểm:**
- Cực nhanh (fastest boosting)
- Memory efficient
- Performance cao
- Xử lý categorical features
- Large dataset friendly

**Nhược điểm:**
- Dễ overfitting với small data
- Cần tune cẩn thận

**Hyperparameters cần tune:**
```python
import lightgbm as lgb

params = {
    'n_estimators': [100, 200, 300, 500],
    'learning_rate': [0.01, 0.05, 0.1, 0.2],
    'num_leaves': [31, 50, 70, 100],
    'max_depth': [-1, 10, 20, 30],
    'min_child_samples': [10, 20, 30, 50],
    'subsample': [0.7, 0.8, 0.9, 1.0],
    'colsample_bytree': [0.7, 0.8, 0.9, 1.0],
    'reg_alpha': [0, 0.1, 0.5, 1],
    'reg_lambda': [0, 0.1, 0.5, 1],
    'scale_pos_weight': [1, 5, 10, 13.96],
    'metric': 'auc',
    'boosting_type': 'gbdt'
}
```

**Expected Performance**: ROC-AUC ~ 0.86-0.91

---

## 📊 Model Comparison Summary

### Performance Comparison

| Model | Expected ROC-AUC | Training Speed | Tuning Effort | Interpretability |
|-------|------------------|----------------|---------------|------------------|
| **Logistic Regression** | 0.75-0.80 | ⚡⚡⚡⚡⚡ Very Fast | ⭐ Easy | ⭐⭐⭐⭐⭐ High |
| **SVM** | 0.82-0.87 | ⚡⚡⚡ Moderate | ⭐⭐⭐ Medium | ⭐⭐ Low |
| **Random Forest** | 0.83-0.87 | ⚡⚡⚡ Moderate | ⭐⭐ Easy | ⭐⭐⭐ Medium |
| **XGBoost** | 0.86-0.91 | ⚡⚡⚡⚡ Fast | ⭐⭐⭐⭐ Hard | ⭐⭐ Low |
| **LightGBM** | 0.86-0.91 | ⚡⚡⚡⚡⚡ Very Fast | ⭐⭐⭐⭐ Hard | ⭐⭐ Low |

### Model Categories

**Linear Models:**
- Logistic Regression
- SVM (with linear kernel)

**Kernel-based:**
- SVM (with RBF/poly kernel)

**Tree-based Ensemble:**
- Random Forest (Bagging)
- XGBoost (Boosting)
- LightGBM (Boosting)

### Strengths by Category

**Best for Interpretability:**
1. Logistic Regression ⭐⭐⭐⭐⭐
2. Random Forest ⭐⭐⭐
3. SVM/XGBoost/LightGBM ⭐⭐

**Best Performance Expected:**
1. XGBoost ⭐⭐⭐⭐⭐
2. LightGBM ⭐⭐⭐⭐⭐
3. Random Forest ⭐⭐⭐⭐
4. SVM ⭐⭐⭐⭐
5. Logistic Regression ⭐⭐⭐

**Best Training Speed:**
1. Logistic Regression ⚡⚡⚡⚡⚡
2. LightGBM ⚡⚡⚡⚡⚡
3. XGBoost ⚡⚡⚡⚡
4. Random Forest ⚡⚡⚡
5. SVM ⚡⚡⚡

**Best for Large Datasets:**
1. LightGBM ⭐⭐⭐⭐⭐
2. XGBoost ⭐⭐⭐⭐
3. Logistic Regression ⭐⭐⭐⭐
4. Random Forest ⭐⭐⭐
5. SVM ⭐⭐

---

## 🎯 Modeling Strategy

### Training Order (Recommended):

```
Step 1: Logistic Regression (Baseline)
  ↓
Step 2: Random Forest (Improve performance)
  ↓
Step 3: XGBoost (Best performance expected)
  ↓
Step 4: LightGBM (Fast alternative to XGBoost)
  ↓
Step 5: SVM (Advanced linear model)
```

### Why this order?

1. **Start simple** (Logistic Regression)
   - Establish baseline
   - Fast to train
   - Understand linear patterns

2. **Add complexity** (Random Forest)
   - Capture non-linear patterns
   - See improvement over baseline

3. **Optimize** (XGBoost)
   - State-of-the-art performance
   - Fine-tune hyperparameters

4. **Fast alternative** (LightGBM)
   - Compare with XGBoost
   - Faster training

5. **Kernel magic** (SVM)
   - Different approach
   - May capture unique patterns

---

## 📋 Implementation Checklist

### For Each Model:

- [ ] Data preprocessing (scaling if needed)
- [ ] Train-test split (stratified)
- [ ] Cross-validation (5-fold stratified)
- [ ] Hyperparameter tuning (GridSearch/RandomSearch)
- [ ] Train best model
- [ ] Evaluate metrics:
  - [ ] ROC-AUC
  - [ ] Recall
  - [ ] Precision
  - [ ] F1-Score
  - [ ] Confusion Matrix
- [ ] Feature importance (if available)
- [ ] Save model
- [ ] Compare with previous models

---

## 🔄 Changes Summary

### ❌ Removed:
- **Neural Network (MLP)** - Deep Learning model

### ✅ Added:
- **Support Vector Machine (SVM)** - Classical ML model

### Why Replace?

| Aspect | Neural Network | SVM |
|--------|---------------|-----|
| **Type** | Deep Learning ❌ | Classical ML ✅ |
| **Complexity** | High | Medium |
| **Training Time** | Slow | Moderate |
| **Hyperparameter Tuning** | Very Complex | Medium |
| **Overfitting Risk** | High | Medium |
| **Feature Scaling** | Required | Required |
| **Interpretability** | Very Low | Low |
| **Performance** | Good-Excellent | Good-Excellent |

**Conclusion**: SVM is a better fit for:
- ✅ All-ML pipeline (no Deep Learning)
- ✅ Easier to tune than Neural Networks
- ✅ Less prone to overfitting
- ✅ Comparable performance

---

## 📦 Updated Requirements

```python
# Core
pandas>=1.5.0
numpy>=1.23.0

# Visualization
matplotlib>=3.5.0
seaborn>=0.12.0
plotly>=5.10.0

# Machine Learning
scikit-learn>=1.2.0      # Logistic, SVM, Random Forest
xgboost>=1.7.0           # XGBoost
lightgbm>=3.3.0          # LightGBM

# Imbalanced data
imbalanced-learn>=0.10.0  # SMOTE

# Utilities
joblib>=1.2.0
```

**Note**: No need for TensorFlow/PyTorch anymore! 🎉

---

## 🎓 Learning Objectives

By implementing these 5 ML models, you will learn:

1. **Linear Classification** (Logistic Regression)
2. **Kernel Methods** (SVM)
3. **Ensemble Bagging** (Random Forest)
4. **Gradient Boosting** (XGBoost, LightGBM)
5. **Hyperparameter Tuning**
6. **Model Comparison & Selection**
7. **Handling Imbalanced Data**
8. **Feature Importance Analysis**

---

**Updated**: 2026-03-09
**All models are now Classical Machine Learning** ✅
**No Deep Learning** ✅

---
