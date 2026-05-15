# Dataset: heart_disease_uci.csv

## Dataset Overview

This dataset is based on the UCI Heart Disease Dataset and is used to train the machine learning model for predicting heart disease risk.

Each row represents one patient's medical profile.

---

## Dataset Information

| Attribute | Value |
|---|---|
| Dataset Name | UCI Heart Disease Dataset |
| File Name | `heart_disease_uci.csv` |
| File Format | CSV |
| File Size | 79.3 KB |
| Number of Rows | 920 |
| Number of Columns | 16 |

---

## Purpose of Dataset

The dataset is used for:
- Machine learning classification
- Heart disease risk prediction
- Medical data preprocessing experiments
- AI healthcare research

---

## Selected Features Used in the Project

The project uses 7 major features:

| Feature | Description |
|---|---|
| Age | Age of the patient |
| Sex | Biological gender |
| Chest Pain Type | Type of chest discomfort |
| Resting BP | Resting blood pressure |
| Cholesterol | Serum cholesterol level |
| Fasting Blood Sugar | Diabetes indicator |
| Max Heart Rate | Maximum heart rate achieved |

---

## Target Variable

| Label | Meaning |
|---|---|
| 0 | Low Risk / No Heart Disease |
| 1 | High Risk / Heart Disease |

---

## Data Preprocessing Performed

The dataset underwent several preprocessing steps:

- Missing value handling
- Median imputation
- Mode imputation
- Outlier capping using IQR
- One-hot encoding
- Feature scaling using StandardScaler

---

## Source

UCI Machine Learning Repository:
https://archive.ics.uci.edu/ml/datasets/Heart+Disease

---

## Notes

This dataset is used strictly for:
- Educational purposes
- Research work
- Machine learning demonstrations

It is not intended for real clinical diagnosis.
