# 📁 Project Structure - Reports Organization
## Credit Scoring Project

**Updated**: 2026-03-10
**Author**: QuangMinh

---

## 🗂️ Cấu trúc Reports (Organized by Phase)

```
reports/
│
├── [1] Ket qua EDA/ ✅ COMPLETED
│   ├── EDA_REPORT.md
│   ├── summary_statistics.csv
│   ├── correlation_matrix.csv
│   ├── outlier_analysis.csv
│   ├── ttest_results.csv
│   └── figures/ (7 PNG files)
│       ├── 01_missing_values.png
│       ├── 02_target_distribution.png
│       ├── 03_feature_distributions.png
│       ├── 04_boxplots_outliers.png
│       ├── 05_correlation_heatmap.png
│       ├── 06_target_correlation.png
│       └── 07_distributions_by_target.png
│
├── [2] Ket qua Preprocessing/ ⏳ PENDING
│   ├── README.md ✅ (Template created)
│   ├── 02_Preprocessing.ipynb (future)
│   ├── preprocessing_report.md (future)
│   ├── Processed data files (future)
│   └── Visualizations (future)
│
├── [3] Ket qua Feature Engineering/ ⏳ PENDING
│   ├── README.md ✅ (Template created)
│   ├── 03_Feature_Engineering.ipynb (future)
│   ├── feature_engineering_report.md (future)
│   ├── Engineered data files (future)
│   └── Visualizations (future)
│
├── [4] Ket qua Model Building/ ⏳ PENDING
│   ├── README.md ✅ (Template created)
│   ├── Model notebooks (5 notebooks, future)
│   ├── Trained models (.pkl files, future)
│   ├── Tuning results (future)
│   └── Visualizations (future)
│
├── [5] Ket qua Model Evaluation/ ⏳ PENDING
│   ├── README.md ✅ (Template created)
│   ├── 05_Model_Evaluation.ipynb (future)
│   ├── evaluation_report.md (future)
│   ├── Metrics & comparison files (future)
│   └── Visualizations (9-10 charts, future)
│
└── [6] Final Report/ ⏳ PENDING
    ├── README.md ✅ (Template created)
    ├── 06_Final_Prediction.ipynb (future)
    ├── submission.csv (future)
    ├── FINAL_REPORT.md (future)
    ├── Presentation files (future)
    └── All deliverables (future)
```

---

## 📊 Phase-by-Phase Breakdown

### ✅ Phase 1: EDA (COMPLETED)
**Status**: ✅ Done
**Location**: `reports/[1] Ket qua EDA/`
**Size**: ~3.1MB

**Key Files**:
- Notebook: `notebooks/01_EDA.ipynb`
- Report: `EDA_REPORT.md`
- Charts: 7 PNG files (high-res)
- Data: 4 CSV files

**Key Findings**:
- Imbalanced data: 13.96:1
- Missing values: 2 features
- Outliers: 5 features >5%
- Top predictor: Late payment history

---

### ⏳ Phase 2: Preprocessing (PENDING)
**Status**: ⏳ Not started
**Location**: `reports/[2] Ket qua Preprocessing/`
**Expected Size**: ~33MB

**Will contain**:
- Notebook: `02_Preprocessing.ipynb`
- Cleaned data: Train & test CSVs
- Preprocessing objects: Scalers, imputers
- Report: `preprocessing_report.md`
- Visualizations: Before/after comparisons

**Tasks**:
1. Handle missing values (MonthlyIncome, NumberOfDependents)
2. Handle outliers (capping)
3. Feature scaling (StandardScaler)
4. SMOTE for imbalanced data
5. Train-validation split

---

### ⏳ Phase 3: Feature Engineering (PENDING)
**Status**: ⏳ Not started
**Location**: `reports/[3] Ket qua Feature Engineering/`
**Expected Size**: ~46MB

**Will contain**:
- Notebook: `03_Feature_Engineering.ipynb`
- Engineered data: Train & test with new features
- Feature lists: Created & selected features
- Report: `feature_engineering_report.md`
- Visualizations: Feature importance, correlations

**New Features to Create**:
- TotalPastDue
- SeverityScore
- HasBadHistory
- IncomePerPerson
- FinancialStress
- CreditExperience
- Plus 4-7 more features

**Expected**: 10 original → ~20 total → ~15-18 selected

---

### ⏳ Phase 4: Model Building (PENDING)
**Status**: ⏳ Not started
**Location**: `reports/[4] Ket qua Model Building/`
**Expected Size**: ~110-510MB

**Will contain**:
- 5 Notebooks (one per model)
- 5 Trained models (.pkl files)
- Tuning results (CSV files)
- Training logs
- Report: `model_building_report.md`
- Visualizations: Learning curves, CV scores

**5 Models**:
1. Logistic Regression (Baseline)
2. Support Vector Machine (SVM)
3. Random Forest
4. XGBoost
5. LightGBM

**Estimated Time**: 3-4 hours total

---

### ⏳ Phase 5: Model Evaluation (PENDING)
**Status**: ⏳ Not started
**Location**: `reports/[5] Ket qua Model Evaluation/`
**Expected Size**: ~58MB

**Will contain**:
- Notebook: `05_Model_Evaluation.ipynb`
- Metrics comparison: All models (CSV)
- Best model selection: Documentation
- Report: `model_evaluation_report.md`
- Visualizations: 9-10 charts (ROC, PR curves, confusion matrices)

**Key Deliverables**:
- Model comparison table
- ROC curves (all models)
- Confusion matrices
- Feature importance comparison
- Best model selection with reasoning

---

### ⏳ Phase 6: Final Report (PENDING)
**Status**: ⏳ Not started
**Location**: `reports/[6] Final Report/`
**Expected Size**: ~220-520MB

**Will contain**:
- Notebook: `06_Final_Prediction.ipynb`
- Predictions: `submission.csv`
- Final reports: Multiple formats (MD, PDF)
- Presentation: PowerPoint/PDF
- Deliverables: Zipped files

**Key Deliverables**:
- Test predictions
- Kaggle submission file
- Comprehensive final report (20-30 pages)
- Executive summary (2-3 pages)
- Presentation slides (15-20 slides)
- All code & models packaged

---

## 📋 Progress Tracking

### Completed ✅
- [x] Phase 1: EDA
- [x] Project structure organized
- [x] README templates for all phases

### In Progress ⏳
- [ ] Phase 2: Preprocessing

### Upcoming 📅
- [ ] Phase 3: Feature Engineering
- [ ] Phase 4: Model Building
- [ ] Phase 5: Model Evaluation
- [ ] Phase 6: Final Report

### Progress: 1/6 phases (16.7%) ✅

---

## 📊 Expected Total Project Size

| Phase | Status | Size |
|-------|--------|------|
| Phase 1: EDA | ✅ Done | 3.1 MB |
| Phase 2: Preprocessing | ⏳ Pending | ~33 MB |
| Phase 3: Feature Engineering | ⏳ Pending | ~46 MB |
| Phase 4: Model Building | ⏳ Pending | ~300 MB |
| Phase 5: Evaluation | ⏳ Pending | ~58 MB |
| Phase 6: Final Report | ⏳ Pending | ~350 MB |
| **Total** | | **~790 MB** |

---

## 🎯 Benefits of This Organization

### ✅ Advantages:

1. **Clear Separation**: Mỗi phase có folder riêng
2. **Easy Navigation**: Dễ tìm kết quả mỗi phase
3. **Version Control**: Dễ track changes
4. **Scalable**: Thêm sub-folders nếu cần
5. **Professional**: Organized như enterprise projects
6. **Documentation**: Mỗi folder có README template

### 📁 File Naming Convention:

- **Notebooks**: `0X_Phase_Name.ipynb` (01, 02, ..., 06)
- **Reports**: `phase_name_report.md`
- **Data**: `train_phase_name.csv`, `test_phase_name.csv`
- **Visualizations**: `number_description.png` (01, 02, ...)
- **Models**: `model_name_best.pkl`

---

## 💡 Usage Guidelines

### For Each Phase:

1. **Read README.md** in phase folder
2. **Create notebook** following naming convention
3. **Save results** in the phase folder
4. **Create visualizations** in appropriate subfolder
5. **Write report** documenting findings
6. **Update README** với actual results

### Best Practices:

- ✅ Keep files organized by phase
- ✅ Use descriptive file names
- ✅ Document everything
- ✅ Save intermediate results
- ✅ Create visualizations for key findings
- ✅ Write clear reports

---

## 🚀 Next Steps

### Immediate:
1. Review Phase 1 results in `[1] Ket qua EDA/`
2. Prepare for Phase 2: Preprocessing
3. Read `[2] Ket qua Preprocessing/README.md`

### Phase 2 Tasks:
- Create `02_Preprocessing.ipynb`
- Handle missing values
- Handle outliers
- Feature scaling
- SMOTE
- Save results in `[2] Ket qua Preprocessing/`

---

## 📞 Quick Reference

### Find EDA Results:
```bash
cd "reports/[1] Ket qua EDA/"
```

### Find Phase Templates:
```bash
# Each phase folder has README.md with:
# - Objectives
# - Expected files
# - Checklist
# - Tips
```

### View Project Structure:
```bash
ls -la reports/
```

---

## 📝 Notes

- **Folders created**: All 6 phase folders
- **Templates ready**: All README.md files
- **Naming convention**: [1], [2], ..., [6] for easy sorting
- **Language**: Vietnamese folder names, English content
- **Flexibility**: Can add subfolders if needed

---

**Document Created**: 2026-03-10
**Last Updated**: 2026-03-10
**Version**: 1.0
