# [5] Kết quả Model Evaluation
## Phase 5: Model Evaluation & Comparison

**Status**: ⏳ Pending
**Expected completion**: TBD

---

## 🎯 Mục tiêu Phase 5

Đánh giá và so sánh 5 models để chọn model tốt nhất:

1. ✅ Calculate all metrics (ROC-AUC, Recall, Precision, F1)
2. ✅ Create ROC curves comparison
3. ✅ Confusion matrices
4. ✅ Feature importance comparison
5. ✅ Select best model

---

## 📁 Files sẽ được lưu trong thư mục này

### 1. Notebook
- `05_Model_Evaluation.ipynb` - Evaluation chi tiết

### 2. Evaluation Results
- `all_models_metrics.csv` - Tất cả metrics cho 5 models
- `confusion_matrices.csv` - All confusion matrices
- `roc_curves_data.csv` - ROC curve coordinates
- `feature_importance_comparison.csv` - Feature importance từ các models

### 3. Model Selection
- `best_model_selection.txt` - Model được chọn và lý do
- `model_ranking.csv` - Ranking models theo metrics
- `best_model_final.pkl` - Best model saved

### 4. Reports
- `model_evaluation_report.md` - Báo cáo đầy đủ
- `model_comparison_summary.txt` - Tóm tắt so sánh
- `business_impact_analysis.md` - Phân tích business impact

### 5. Visualizations (Nhiều nhất!)
- `metrics_comparison_bar.png` - Bar charts so sánh metrics
- `roc_curves_all_models.png` - ROC curves overlay
- `pr_curves_all_models.png` - Precision-Recall curves
- `confusion_matrices_heatmap.png` - All confusion matrices
- `feature_importance_comparison.png` - Compare feature importance
- `calibration_curves.png` - Probability calibration
- `threshold_analysis.png` - Optimal threshold selection
- `metrics_radar_chart.png` - Radar chart comparison
- `model_performance_table.png` - Summary table as image

---

## 📊 Evaluation Metrics

### Primary Metrics (Most Important):

1. **ROC-AUC Score** ⭐⭐⭐⭐⭐
   - Range: 0.5 - 1.0
   - Target: > 0.90
   - Use: Overall model performance

2. **Recall (Sensitivity)** ⭐⭐⭐⭐⭐
   - Formula: TP / (TP + FN)
   - Target: > 0.75
   - Use: Catch bad customers (minimize False Negatives)

3. **Precision** ⭐⭐⭐⭐
   - Formula: TP / (TP + FP)
   - Target: > 0.70
   - Use: Avoid rejecting good customers

### Secondary Metrics:

4. **F1-Score** ⭐⭐⭐
   - Harmonic mean of Precision & Recall
   - Target: > 0.75

5. **Accuracy** ⭐⭐
   - Overall correctness
   - Note: Misleading with imbalanced data

6. **PR-AUC** ⭐⭐⭐
   - Area under Precision-Recall curve
   - Better for imbalanced data

### Business Metrics:

- **Cost of False Negatives**: Loan to bad customer → Loss
- **Cost of False Positives**: Reject good customer → Lost opportunity
- **Expected Profit**: Based on confusion matrix

---

## 📋 Expected Comparison Table

| Model | ROC-AUC | Recall | Precision | F1 | Accuracy | Training Time | Rank |
|-------|---------|--------|-----------|----|----|---------------|------|
| **Logistic Regression** | 0.78 | 0.68 | 0.72 | 0.70 | 0.92 | 1 min | 5 |
| **SVM** | 0.85 | 0.75 | 0.78 | 0.76 | 0.93 | 15 min | 3 |
| **Random Forest** | 0.86 | 0.77 | 0.80 | 0.78 | 0.93 | 8 min | 2 |
| **XGBoost** | 0.89 | 0.81 | 0.83 | 0.82 | 0.94 | 4 min | 1 |
| **LightGBM** | 0.89 | 0.80 | 0.82 | 0.81 | 0.94 | 2 min | 1 |

**Expected Winner**: XGBoost or LightGBM

---

## 🎯 Model Selection Criteria

### Ranking Factors (Weighted):

1. **ROC-AUC** (40%)
2. **Recall** (30%) - Important for risk detection
3. **F1-Score** (20%)
4. **Training Speed** (10%)

### Decision Rules:

- If ROC-AUC difference < 0.01: Choose faster model
- If Recall < 0.70: Reject model (too many missed bad customers)
- Consider interpretability for business

---

## 📊 Confusion Matrix Analysis

### For Each Model:

```
                Predicted
                 0      1
Actual  0     TN      FP    (Good customers)
        1     FN      TP    (Bad customers)
```

### Key Questions:

1. How many bad customers do we miss? (FN)
2. How many good customers do we reject? (FP)
3. What's the optimal threshold?

---

## 🔍 Feature Importance Analysis

### Compare across models:

- Which features are consistently important?
- Are engineered features useful?
- Can we remove any features?

### Expected Top Features:

1. NumberOfTimes90DaysLate
2. SeverityScore (engineered)
3. age
4. NumberOfTime30-59DaysPastDueNotWorse
5. RevolvingUtilizationOfUnsecuredLines

---

## 📊 Expected Outputs

### Metrics Summary:
- 5 models × 6 metrics = 30 values
- Best model identified
- Reasoning documented

### Visualizations:
- 9-10 high-quality charts
- Ready for presentation

### Files Size Estimate:
- Evaluation results: ~2MB
- Visualizations: ~5MB
- Reports: ~1MB
- Best model: ~50MB

**Total**: ~58MB

---

## 📝 Checklist

### Evaluation Steps:
- [ ] Load all 5 trained models
- [ ] Load validation/test data
- [ ] Calculate all metrics for each model
- [ ] Create confusion matrices
- [ ] Generate ROC curves
- [ ] Generate PR curves
- [ ] Compare feature importance
- [ ] Analyze threshold impact
- [ ] Rank models
- [ ] Select best model

### Visualization Steps:
- [ ] Metrics comparison bar chart
- [ ] ROC curves overlay
- [ ] PR curves overlay
- [ ] Confusion matrices heatmaps
- [ ] Feature importance comparison
- [ ] Calibration curves
- [ ] Threshold analysis
- [ ] Radar chart
- [ ] Summary table

### Documentation:
- [ ] Write evaluation report
- [ ] Document model selection reasoning
- [ ] Business impact analysis
- [ ] Recommendations for deployment

---

## 💡 Key Questions to Answer

1. **Which model performs best overall?**
2. **What's the trade-off between Precision and Recall?**
3. **Are engineered features helping?**
4. **What's the optimal probability threshold?**
5. **Is the best model worth the complexity?**
6. **Can we ensemble models for better performance?**

---

## 🎯 Success Criteria

### Minimum Goals:
- ✅ Best model ROC-AUC > 0.85
- ✅ Best model Recall > 0.70
- ✅ All 5 models evaluated

### Target Goals:
- 🎯 Best model ROC-AUC > 0.90
- 🎯 Best model F1-Score > 0.75
- 🎯 Clear winner identified

### Stretch Goals:
- 🚀 Best model ROC-AUC > 0.92
- 🚀 Ensemble model created
- 🚀 SHAP values analysis

---

**Created**: 2026-03-10
**Last updated**: TBD
