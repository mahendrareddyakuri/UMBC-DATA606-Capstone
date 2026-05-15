# akuri_606_final.ipynb

## Overview

`akuri_606_final.ipynb` is the primary Jupyter Notebook used for the complete machine learning workflow of the project.

The notebook contains:
- Data loading
- Data preprocessing
- Exploratory Data Analysis
- Model training
- Hyperparameter tuning
- Model evaluation
- Model saving

---

## Workflow Included

### 1. Data Loading
- Reads the UCI Heart Disease dataset
- Inspects structure and missing values

### 2. Data Cleaning
- Removes unnecessary columns
- Handles missing data
- Performs outlier treatment

### 3. Exploratory Data Analysis (EDA)
Visualizations include:
- Histograms
- Boxplots
- Correlation analysis
- Target distribution

### 4. Feature Engineering
- One-hot encoding
- Feature scaling
- Train-validation-test split

### 5. Model Training
Models trained:
- Logistic Regression
- Random Forest
- SVM
- XGBoost

### 6. Hyperparameter Tuning
Uses:
- GridSearchCV
- Cross-validation

### 7. Model Evaluation
Metrics used:
- Accuracy
- Recall
- Precision
- F1 Score
- Confusion Matrix

### 8. Model Serialization
Final artifacts saved using pickle:
- Trained model
- Scaler
- Feature schema

---

## Output Files Generated

| File | Purpose |
|---|---|
| `heart_model.pkl` | Saved trained model |
| Evaluation plots | Model analysis |
| Encoded datasets | Training pipeline |

---

## Libraries Used

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn
- Pickle

---

## Purpose of Notebook

This notebook demonstrates the complete end-to-end machine learning pipeline for the capstone project.
