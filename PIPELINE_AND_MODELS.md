# Pipeline & Models Comparison - Credit Scoring

## 🎯 Mục tiêu
So sánh **5 mô hình Machine Learning** khác nhau để tìm ra mô hình tốt nhất cho bài toán Credit Scoring.

---

## 📋 Pipeline tổng quan

```
┌─────────────────────────────────────────────────────────────────┐
│                    CREDIT SCORING PIPELINE                      │
└─────────────────────────────────────────────────────────────────┘

1️⃣ DATA LOADING & EDA
   ├─ Load training & test data
   ├─ Khám phá cấu trúc dữ liệu
   ├─ Phân tích phân phối features
   ├─ Kiểm tra missing values
   ├─ Phân tích tương quan
   └─ Kiểm tra imbalanced data
          ↓
2️⃣ DATA PREPROCESSING
   ├─ Xử lý missing values (imputation)
   ├─ Xử lý outliers (capping/removal)
   ├─ Feature scaling (StandardScaler/MinMaxScaler)
   ├─ Handle imbalanced data (SMOTE/class weights)
   └─ Train-test split
          ↓
3️⃣ FEATURE ENGINEERING
   ├─ Tạo features mới từ features hiện có
   ├─ Feature selection (correlation, importance)
   ├─ Feature encoding (nếu có categorical)
   └─ Polynomial features (nếu cần)
          ↓
4️⃣ MODEL BUILDING
   ├─ Model 1: Logistic Regression (Baseline)
   ├─ Model 2: Random Forest
   ├─ Model 3: XGBoost
   ├─ Model 4: LightGBM
   └─ Model 5: Neural Network (MLP)
          ↓
5️⃣ MODEL EVALUATION
   ├─ Cross-validation (K-Fold)
   ├─ Hyperparameter tuning (GridSearch/RandomSearch)
   ├─ Metrics: Accuracy, Precision, Recall, F1, ROC-AUC
   ├─ Confusion Matrix
   ├─ Feature Importance Analysis
   └─ Model comparison & selection
          ↓
6️⃣ FINAL PREDICTION
   ├─ Predict on test set
   ├─ Generate submission file
   └─ Final report & recommendations
```

---

## 🤖 5 Models được chọn để so sánh

### **Model 1: Logistic Regression** (Baseline)

**Lý do chọn:**
- ✅ Mô hình đơn giản, dễ hiểu, dễ giải thích
- ✅ Training nhanh
- ✅ Thường dùng làm baseline trong binary classification
- ✅ Phù hợp với dữ liệu có quan hệ tuyến tính

**Ưu điểm:**
- Interpretable (dễ giải thích coefficients)
- Không cần nhiều hyperparameters
- Hoạt động tốt với features có quan hệ tuyến tính

**Nhược điểm:**
- Không capture được non-linear relationships
- Giả định features độc lập
- Kém với dữ liệu phức tạp

**Hyperparameters cần tune:**
- `C`: Regularization strength
- `penalty`: L1 hoặc L2 regularization
- `class_weight`: Xử lý imbalanced data

**Expected Performance:** Moderate (baseline)

---

### **Model 2: Random Forest** (Ensemble - Bagging)

**Lý do chọn:**
- ✅ Mạnh mẽ với non-linear relationships
- ✅ Robust với outliers
- ✅ Không cần feature scaling
- ✅ Cung cấp feature importance

**Ưu điểm:**
- Xử lý tốt overfitting nhờ ensemble
- Hoạt động tốt với nhiều loại dữ liệu
- Feature importance giúp hiểu dữ liệu
- Ít cần preprocessing

**Nhược điểm:**
- Training chậm hơn Logistic Regression
- Chiếm nhiều memory
- Kém interpretable hơn

**Hyperparameters cần tune:**
- `n_estimators`: Số lượng trees (100-500)
- `max_depth`: Độ sâu của tree (10-50)
- `min_samples_split`: Số samples tối thiểu để split (2-10)
- `min_samples_leaf`: Số samples tối thiểu ở leaf (1-4)
- `max_features`: Số features cho mỗi split ('sqrt', 'log2')
- `class_weight`: Xử lý imbalanced data

**Expected Performance:** Good

---

### **Model 3: XGBoost** (Gradient Boosting)

**Lý do chọn:**
- ✅ State-of-the-art cho tabular data
- ✅ Thường đạt performance cao nhất trong competitions
- ✅ Xử lý tốt missing values
- ✅ Có built-in regularization

**Ưu điểm:**
- Performance rất cao
- Xử lý missing values tự động
- Regularization tránh overfitting
- Training nhanh hơn Random Forest
- Feature importance

**Nhược điểm:**
- Nhiều hyperparameters cần tune
- Dễ overfitting nếu không tune đúng
- Cần nhiều thời gian để optimize

**Hyperparameters cần tune:**
- `n_estimators`: Số boosting rounds (100-1000)
- `learning_rate`: Tốc độ học (0.01-0.3)
- `max_depth`: Độ sâu tree (3-10)
- `min_child_weight`: Trọng số tối thiểu (1-10)
- `subsample`: Tỷ lệ sampling (0.6-1.0)
- `colsample_bytree`: Tỷ lệ features (0.6-1.0)
- `gamma`: Regularization (0-5)
- `scale_pos_weight`: Xử lý imbalanced data

**Expected Performance:** Excellent

---

### **Model 4: LightGBM** (Gradient Boosting - Optimized)

**Lý do chọn:**
- ✅ Nhanh hơn XGBoost rất nhiều
- ✅ Hiệu quả với large dataset
- ✅ Xử lý categorical features tự động
- ✅ Dùng ít memory hơn

**Ưu điểm:**
- Training cực nhanh
- Tiết kiệm memory
- Performance tương đương XGBoost
- Xử lý tốt large dataset
- Categorical features support

**Nhược điểm:**
- Dễ overfitting với small dataset
- Cần tune cẩn thận với small data
- Ít interpretable

**Hyperparameters cần tune:**
- `n_estimators`: Số boosting rounds (100-1000)
- `learning_rate`: Tốc độ học (0.01-0.3)
- `num_leaves`: Số lá của tree (20-100)
- `max_depth`: Độ sâu tree (-1 hoặc 3-10)
- `min_child_samples`: Samples tối thiểu ở leaf (10-100)
- `subsample`: Tỷ lệ sampling (0.6-1.0)
- `colsample_bytree`: Tỷ lệ features (0.6-1.0)
- `reg_alpha`: L1 regularization (0-1)
- `reg_lambda`: L2 regularization (0-1)
- `scale_pos_weight`: Xử lý imbalanced data

**Expected Performance:** Excellent

---

### **Model 5: Neural Network - MLP** (Deep Learning)

**Lý do chọn:**
- ✅ Có thể học complex patterns
- ✅ Flexible architecture
- ✅ Tốt cho non-linear relationships
- ✅ Mở rộng được cho deep learning

**Ưu điểm:**
- Capture complex non-linear patterns
- Flexible architecture
- Có thể scale lên deep networks
- Universal function approximator

**Nhược điểm:**
- Cần nhiều data để train tốt
- Cần feature scaling bắt buộc
- Training chậm
- Black box (khó interpret)
- Dễ overfitting
- Nhiều hyperparameters

**Architecture đề xuất:**
```
Input (10 features)
    ↓
Dense(64, relu) + Dropout(0.3)
    ↓
Dense(32, relu) + Dropout(0.3)
    ↓
Dense(16, relu) + Dropout(0.2)
    ↓
Dense(1, sigmoid)
    ↓
Output (probability)
```

**Hyperparameters cần tune:**
- `hidden_layer_sizes`: Số neurons mỗi layer
- `activation`: relu, tanh
- `learning_rate`: Tốc độ học (0.001-0.01)
- `batch_size`: Kích thước batch (32-256)
- `epochs`: Số epochs (50-200)
- `dropout_rate`: Tỷ lệ dropout (0.2-0.5)
- `optimizer`: Adam, SGD, RMSprop
- `early_stopping`: Patience (10-20)

**Expected Performance:** Good to Excellent (tùy thuộc tuning)

---

## 📊 So sánh tổng quan các models

| Model | Speed | Performance | Interpretability | Tuning Effort | Overfitting Risk |
|-------|-------|-------------|------------------|---------------|------------------|
| Logistic Regression | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐ | ⭐ |
| Random Forest | ⚡⚡⚡ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| XGBoost | ⚡⚡⚡⚡ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| LightGBM | ⚡⚡⚡⚡⚡ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Neural Network | ⚡⚡ | ⭐⭐⭐⭐ | ⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 📈 Evaluation Metrics

### Primary Metrics:
1. **ROC-AUC Score** ⭐⭐⭐⭐⭐
   - Đánh giá tổng thể khả năng phân loại
   - Không bị ảnh hưởng bởi imbalanced data
   - Range: 0.5-1.0 (1.0 là perfect)

2. **Recall (Sensitivity)** ⭐⭐⭐⭐⭐
   - Tỷ lệ phát hiện đúng khách hàng xấu
   - Quan trọng: Không bỏ sót nợ xấu
   - Formula: TP / (TP + FN)

3. **Precision** ⭐⭐⭐⭐
   - Tỷ lệ dự đoán đúng trong số dự đoán là xấu
   - Tránh từ chối nhầm khách hàng tốt
   - Formula: TP / (TP + FP)

### Secondary Metrics:
4. **F1-Score**: Cân bằng Precision và Recall
5. **Accuracy**: Tỷ lệ dự đoán đúng tổng thể
6. **Confusion Matrix**: Ma trận nhầm lẫn
7. **PR-AUC**: Precision-Recall AUC (tốt cho imbalanced data)

### Business Metrics:
- **Cost of False Negatives**: Cho vay nhầm khách xấu → Tổn thất lớn
- **Cost of False Positives**: Từ chối nhầm khách tốt → Mất cơ hội kinh doanh

---

## 🔧 Chi tiết từng Phase

### **Phase 1: Data Loading & EDA**

**Mục tiêu:**
- Hiểu rõ dữ liệu
- Phát hiện vấn đề cần xử lý

**Tasks:**
1. Load cs-training.csv và cs-test.csv
2. Kiểm tra shape, dtypes, info
3. Thống kê mô tả (describe)
4. Phân tích missing values
5. Visualizations:
   - Distribution của mỗi feature
   - Boxplot để phát hiện outliers
   - Correlation heatmap
   - Target distribution (class imbalance)
   - Pairplot cho important features
6. Insights & Conclusions

**Output:**
- `01_EDA.ipynb`: Jupyter notebook với visualizations
- `eda_report.md`: Báo cáo phát hiện

---

### **Phase 2: Data Preprocessing**

**Mục tiêu:**
- Làm sạch dữ liệu
- Chuẩn bị cho modeling

**Tasks:**

1. **Missing Values:**
   - `MonthlyIncome`: Impute bằng median/mean hoặc KNN imputation
   - `NumberOfDependents`: Impute bằng median hoặc mode

2. **Outliers:**
   - `age`: Loại bỏ age < 18 hoặc age > 100
   - `DebtRatio`: Capping ở percentile 99%
   - `RevolvingUtilizationOfUnsecuredLines`: Capping ở > 1
   - Các NumberOfTimes features: Capping nếu quá lớn

3. **Feature Scaling:**
   - StandardScaler cho Logistic Regression, Neural Network
   - Không cần cho tree-based models

4. **Handle Imbalanced Data:**
   - Phân tích tỷ lệ class 0/1
   - Options:
     - SMOTE (Synthetic Minority Over-sampling)
     - Class weights trong models
     - Under-sampling majority class
     - Combination methods

5. **Train-Validation Split:**
   - Stratified split (80-20 hoặc 70-30)
   - Giữ nguyên tỷ lệ target classes

**Output:**
- `02_Preprocessing.ipynb`
- Cleaned datasets: `train_cleaned.csv`, `test_cleaned.csv`
- Preprocessing pipeline: `preprocessing_pipeline.pkl`

---

### **Phase 3: Feature Engineering**

**Mục tiêu:**
- Tạo features mới có ý nghĩa
- Cải thiện model performance

**Tasks:**

1. **Domain-based Features:**
   ```python
   # Tổng số lần chậm thanh toán
   TotalPastDue = NumberOfTime30-59 + NumberOfTime60-89 + NumberOfTimes90Days

   # Mức độ nghiêm trọng của nợ
   SeverityScore = (NumberOfTime30-59*1 + NumberOfTime60-89*2 +
                    NumberOfTimes90Days*3)

   # Tỷ lệ người phụ thuộc/tuổi
   DependentsPerAge = NumberOfDependents / age

   # Thu nhập trên đầu người
   IncomePerPerson = MonthlyIncome / (NumberOfDependents + 1)

   # Debt to Income Ratio (nếu DebtRatio không phải là %)
   # Đã có DebtRatio rồi

   # Tỷ lệ loans/age (kinh nghiệm tín dụng)
   CreditExperience = NumberOfOpenCreditLinesAndLoans / age

   # Có nợ xấu trong quá khứ hay không (binary)
   HasBadHistory = (NumberOfTimes90DaysLate > 0).astype(int)

   # Financial stress indicator
   FinancialStress = RevolvingUtilization * DebtRatio
   ```

2. **Interaction Features:**
   - age × MonthlyIncome
   - DebtRatio × NumberOfDependents
   - etc.

3. **Binning/Grouping:**
   - Age groups: Young (18-30), Middle (30-50), Senior (50+)
   - Income groups: Low, Medium, High

4. **Feature Selection:**
   - Correlation analysis (loại bỏ multicollinearity)
   - Feature importance từ Random Forest
   - Recursive Feature Elimination (RFE)
   - Select K Best features

**Output:**
- `03_Feature_Engineering.ipynb`
- Feature-engineered datasets
- Feature importance analysis

---

### **Phase 4: Model Building**

**Mục tiêu:**
- Train 5 models
- Hyperparameter tuning
- Cross-validation

**Tasks:**

1. **Baseline - Logistic Regression:**
   ```python
   from sklearn.linear_model import LogisticRegression
   from sklearn.model_selection import GridSearchCV

   param_grid = {
       'C': [0.001, 0.01, 0.1, 1, 10, 100],
       'penalty': ['l1', 'l2'],
       'class_weight': ['balanced', None]
   }
   ```

2. **Random Forest:**
   ```python
   from sklearn.ensemble import RandomForestClassifier

   param_grid = {
       'n_estimators': [100, 200, 300],
       'max_depth': [10, 20, 30, None],
       'min_samples_split': [2, 5, 10],
       'min_samples_leaf': [1, 2, 4],
       'class_weight': ['balanced', None]
   }
   ```

3. **XGBoost:**
   ```python
   import xgboost as xgb

   param_grid = {
       'n_estimators': [100, 200, 300],
       'learning_rate': [0.01, 0.05, 0.1],
       'max_depth': [3, 5, 7],
       'min_child_weight': [1, 3, 5],
       'subsample': [0.8, 0.9, 1.0],
       'colsample_bytree': [0.8, 0.9, 1.0],
       'gamma': [0, 0.1, 0.2]
   }
   ```

4. **LightGBM:**
   ```python
   import lightgbm as lgb

   param_grid = {
       'n_estimators': [100, 200, 300],
       'learning_rate': [0.01, 0.05, 0.1],
       'num_leaves': [31, 50, 70],
       'max_depth': [-1, 10, 20],
       'min_child_samples': [20, 30, 50],
       'subsample': [0.8, 0.9, 1.0],
       'colsample_bytree': [0.8, 0.9, 1.0]
   }
   ```

5. **Neural Network:**
   ```python
   from tensorflow.keras import Sequential
   from tensorflow.keras.layers import Dense, Dropout

   model = Sequential([
       Dense(64, activation='relu', input_shape=(n_features,)),
       Dropout(0.3),
       Dense(32, activation='relu'),
       Dropout(0.3),
       Dense(16, activation='relu'),
       Dropout(0.2),
       Dense(1, activation='sigmoid')
   ])
   ```

**Cross-Validation:**
- StratifiedKFold (5 hoặc 10 folds)
- Đảm bảo tỷ lệ target giống nhau ở mỗi fold

**Output:**
- `04_Model_Building.ipynb`
- Saved models: `models/*.pkl` hoặc `models/*.h5`
- Training logs

---

### **Phase 5: Model Evaluation**

**Mục tiêu:**
- So sánh performance các models
- Chọn model tốt nhất

**Tasks:**

1. **Calculate Metrics cho tất cả models:**
   - Accuracy
   - Precision
   - Recall
   - F1-Score
   - ROC-AUC
   - PR-AUC
   - Confusion Matrix

2. **Visualizations:**
   - ROC Curves comparison
   - Precision-Recall Curves
   - Feature Importance comparison
   - Confusion Matrix heatmaps
   - Learning Curves

3. **Model Comparison Table:**
   ```
   | Model               | Accuracy | Precision | Recall | F1   | ROC-AUC |
   |---------------------|----------|-----------|--------|------|---------|
   | Logistic Regression | 0.85     | 0.75      | 0.70   | 0.72 | 0.88    |
   | Random Forest       | 0.88     | 0.80      | 0.75   | 0.77 | 0.92    |
   | XGBoost             | 0.90     | 0.85      | 0.80   | 0.82 | 0.94    |
   | LightGBM            | 0.90     | 0.84      | 0.81   | 0.82 | 0.94    |
   | Neural Network      | 0.89     | 0.82      | 0.78   | 0.80 | 0.93    |
   ```

4. **Business Analysis:**
   - Cost-benefit analysis
   - Optimal threshold selection
   - False Positive vs False Negative trade-off

**Output:**
- `05_Model_Evaluation.ipynb`
- Comparison charts
- Best model selection

---

### **Phase 6: Final Prediction & Report**

**Mục tiêu:**
- Predict trên test set
- Tạo submission file
- Final report

**Tasks:**

1. **Prediction:**
   - Load best model
   - Predict on test set
   - Generate probabilities

2. **Create Submission:**
   ```python
   submission = pd.DataFrame({
       'Id': test_ids,
       'Probability': predictions
   })
   submission.to_csv('submission.csv', index=False)
   ```

3. **Final Report:**
   - Executive summary
   - Data insights
   - Model comparison
   - Best model & why
   - Recommendations
   - Future improvements

**Output:**
- `submission.csv`
- `FINAL_REPORT.md`
- Presentation slides (optional)

---

## 📁 Cấu trúc thư mục đề xuất

```
Give Me Some Credit/
├── data/
│   ├── raw/                          # Dữ liệu gốc
│   │   ├── cs-training.csv
│   │   ├── cs-test.csv
│   │   └── Data Dictionary.xls
│   ├── processed/                    # Dữ liệu đã xử lý
│   │   ├── train_cleaned.csv
│   │   ├── test_cleaned.csv
│   │   └── train_engineered.csv
│   └── submission/                   # Submission files
│       └── submission.csv
│
├── notebooks/                        # Jupyter notebooks
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   ├── 04_Model_Building.ipynb
│   ├── 05_Model_Evaluation.ipynb
│   └── 06_Final_Prediction.ipynb
│
├── src/                             # Source code
│   ├── __init__.py
│   ├── data_loader.py              # Load dữ liệu
│   ├── preprocessing.py            # Preprocessing functions
│   ├── feature_engineering.py      # Feature engineering
│   ├── models.py                   # Model definitions
│   ├── evaluation.py               # Evaluation metrics
│   └── utils.py                    # Utility functions
│
├── models/                          # Saved models
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   ├── lightgbm.pkl
│   └── neural_network.h5
│
├── reports/                         # Reports & visualizations
│   ├── figures/                    # Charts, plots
│   ├── eda_report.md
│   ├── model_comparison.md
│   └── FINAL_REPORT.md
│
├── config/                          # Configuration files
│   └── config.yaml
│
├── requirements.txt                 # Python dependencies
├── README.md                        # Project overview
├── DATA_DICTIONARY.md              # Feature descriptions
├── PROJECT_OBJECTIVE.md            # Project goals
├── PIPELINE_AND_MODELS.md          # This file
└── .gitignore
```

---

## 🔧 Required Libraries

```txt
# Data manipulation
pandas>=1.5.0
numpy>=1.23.0

# Visualization
matplotlib>=3.5.0
seaborn>=0.12.0
plotly>=5.10.0

# Machine Learning
scikit-learn>=1.2.0
xgboost>=1.7.0
lightgbm>=3.3.0

# Deep Learning
tensorflow>=2.10.0
# or pytorch>=1.13.0

# Imbalanced data
imbalanced-learn>=0.10.0

# Utilities
joblib>=1.2.0
pyyaml>=6.0

# Jupyter
jupyter>=1.0.0
ipykernel>=6.15.0
```

---

## 🎯 Success Criteria

**Minimum Goals:**
- ✅ ROC-AUC > 0.85
- ✅ Recall > 0.70 (detect 70% bad customers)
- ✅ All 5 models trained và evaluated

**Target Goals:**
- 🎯 ROC-AUC > 0.90
- 🎯 F1-Score > 0.75
- 🎯 Best model selected with clear justification

**Stretch Goals:**
- 🚀 ROC-AUC > 0.92
- 🚀 Ensemble methods (stacking/blending)
- 🚀 Feature importance analysis với SHAP values

---

## ⏱️ Timeline ước tính

| Phase | Estimated Time | Priority |
|-------|---------------|----------|
| Phase 1: EDA | 2-3 hours | High |
| Phase 2: Preprocessing | 2-3 hours | High |
| Phase 3: Feature Engineering | 3-4 hours | Medium |
| Phase 4: Model Building | 4-6 hours | High |
| Phase 5: Evaluation | 2-3 hours | High |
| Phase 6: Final Report | 2-3 hours | Medium |
| **Total** | **15-22 hours** | - |

---

## 📚 References

1. **Kaggle Competition**: Give Me Some Credit
2. **Documentation**:
   - Scikit-learn: https://scikit-learn.org/
   - XGBoost: https://xgboost.readthedocs.io/
   - LightGBM: https://lightgbm.readthedocs.io/
3. **Papers**:
   - SMOTE: https://arxiv.org/abs/1106.1813
   - Random Forest: Breiman (2001)
   - Gradient Boosting: Friedman (2001)

---

**Cập nhật lần cuối**: 2026-03-09
**Người thực hiện**: QuangMinh
