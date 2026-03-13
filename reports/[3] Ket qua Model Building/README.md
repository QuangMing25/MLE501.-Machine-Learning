# [4] Kết quả Model Building
## Phase 4: Model Building & Training

**Status**: ⏳ Pending
**Expected completion**: TBD

---

## 🎯 Mục tiêu Phase 4

Train và tune 5 Machine Learning models:

1. ✅ Logistic Regression (Baseline)
2. ✅ Support Vector Machine (SVM)
3. ✅ Random Forest
4. ✅ XGBoost
5. ✅ LightGBM

---

## 📁 Files sẽ được lưu trong thư mục này

### 1. Notebooks (Per Model)
- `04a_Logistic_Regression.ipynb`
- `04b_SVM.ipynb`
- `04c_Random_Forest.ipynb`
- `04d_XGBoost.ipynb`
- `04e_LightGBM.ipynb`
- `04_Model_Building_Summary.ipynb` - Tổng hợp

### 2. Trained Models (Saved)
- `logistic_regression_best.pkl`
- `svm_best.pkl`
- `random_forest_best.pkl`
- `xgboost_best.pkl`
- `lightgbm_best.pkl`

### 3. Hyperparameter Tuning Results
- `logistic_tuning_results.csv`
- `svm_tuning_results.csv`
- `random_forest_tuning_results.csv`
- `xgboost_tuning_results.csv`
- `lightgbm_tuning_results.csv`

### 4. Training Logs
- `training_log.txt` - All training logs
- `best_params.json` - Best hyperparameters for each model
- `cv_scores.csv` - Cross-validation scores

### 5. Reports
- `model_building_report.md` - Báo cáo tổng hợp
- `training_summary.csv` - Training time, parameters
- `model_comparison_preliminary.csv` - So sánh sơ bộ

### 6. Visualizations
- `training_time_comparison.png`
- `cv_scores_comparison.png`
- `learning_curves/` (folder)
  - `learning_curve_lr.png`
  - `learning_curve_svm.png`
  - `learning_curve_rf.png`
  - `learning_curve_xgboost.png`
  - `learning_curve_lightgbm.png`

---

## 🤖 5 Models Details

### Model 1: Logistic Regression
**Type**: Linear baseline
**Training time**: ~1-2 minutes
**Tuning params**: C, penalty
**Expected ROC-AUC**: 0.75-0.80

### Model 2: Support Vector Machine (SVM)
**Type**: Kernel-based
**Training time**: ~10-20 minutes (can be slow)
**Tuning params**: C, kernel, gamma
**Expected ROC-AUC**: 0.82-0.87

### Model 3: Random Forest
**Type**: Ensemble (Bagging)
**Training time**: ~5-10 minutes
**Tuning params**: n_estimators, max_depth, min_samples_split
**Expected ROC-AUC**: 0.83-0.87

### Model 4: XGBoost
**Type**: Gradient Boosting
**Training time**: ~3-5 minutes
**Tuning params**: learning_rate, max_depth, n_estimators
**Expected ROC-AUC**: 0.86-0.91

### Model 5: LightGBM
**Type**: Gradient Boosting (Fast)
**Training time**: ~2-3 minutes
**Tuning params**: learning_rate, num_leaves, n_estimators
**Expected ROC-AUC**: 0.86-0.91

---

## 🔧 Training Strategy

### Cross-Validation:
- **Method**: Stratified K-Fold
- **K**: 5 folds
- **Scoring**: ROC-AUC

### Hyperparameter Tuning:
- **Method**: RandomizedSearchCV
- **Iterations**: 50
- **Scoring**: ROC-AUC
- **CV**: 5-fold

### Training Order:
1. Logistic Regression (fastest, baseline)
2. Random Forest (no scaling needed)
3. LightGBM (fast)
4. XGBoost (best expected)
5. SVM (slowest, consider subset)

---

## 📊 Expected Outputs

### Training Metrics (Per Model):
- Cross-validation ROC-AUC (mean ± std)
- Training time
- Best hyperparameters
- Feature importance (if available)

### Comparison Table:
| Model | CV ROC-AUC | Training Time | Tuning Time | Best Params |
|-------|------------|---------------|-------------|-------------|
| Logistic | 0.77 ± 0.02 | 1 min | 5 min | ... |
| SVM | 0.84 ± 0.02 | 15 min | 60 min | ... |
| Random Forest | 0.85 ± 0.02 | 8 min | 40 min | ... |
| XGBoost | 0.89 ± 0.01 | 4 min | 30 min | ... |
| LightGBM | 0.89 ± 0.01 | 2 min | 20 min | ... |

### Files Size Estimate:
- Saved models: ~100-500MB (total)
- Tuning results: ~5MB
- Training logs: ~1MB
- Visualizations: ~3MB

**Total**: ~110-510MB

---

## 📝 Checklist (Per Model)

### For Each Model:
- [ ] Load preprocessed data
- [ ] Apply scaling (if needed)
- [ ] Define hyperparameter grid
- [ ] Perform RandomizedSearchCV
- [ ] Train with best parameters
- [ ] Calculate CV scores
- [ ] Generate learning curves
- [ ] Extract feature importance
- [ ] Save trained model
- [ ] Save tuning results
- [ ] Document best parameters

### Overall:
- [ ] Train all 5 models
- [ ] Compare CV scores
- [ ] Create comparison visualizations
- [ ] Write summary report
- [ ] Identify top 2-3 models

---

## ⏱️ Estimated Time

| Phase | Time |
|-------|------|
| Model 1: Logistic | 10-15 min |
| Model 2: SVM | 60-90 min |
| Model 3: Random Forest | 45-60 min |
| Model 4: XGBoost | 30-45 min |
| Model 5: LightGBM | 20-30 min |
| **Total** | **~3-4 hours** |

---

## 💡 Tips

1. **Start with Logistic Regression** - Quick baseline
2. **Skip SVM if too slow** - Can train on subset
3. **Use early stopping** - For XGBoost/LightGBM
4. **Monitor overfitting** - Check train vs validation scores
5. **Save checkpoints** - Save after each model

---

**Created**: 2026-03-10
**Last updated**: TBD
