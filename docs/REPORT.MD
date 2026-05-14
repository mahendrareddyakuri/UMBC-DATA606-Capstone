# Heart Disease Prediction and AI-Based Health Guidance System

## UMBC Data Science Master’s Capstone Project (DATA 606)

**Prepared for:** Dr. Chaojie Wang  
**Author:** Mahendra Reddy Akuri  
**Program:** UMBC Data Science Master’s Degree Capstone  

---

## 1. Background

### 1.1 Project Overview
This project develops an end-to-end machine learning web application that predicts the likelihood of heart disease based on user health inputs. It combines an XGBoost model with Google Gemini to generate personalized health guidance through a Streamlit interface.

The system is designed for general users and is not a medical diagnostic tool.

### 1.2 Motivation
Cardiovascular disease is a leading global cause of death. Early detection is often limited by cost and accessibility. Machine learning provides a way to estimate risk using limited features, and LLMs can translate predictions into simple advice.

### 1.3 Research Questions
- Can heart disease be predicted using simple health inputs?
- Which ML model performs best for binary classification?
- How can LLMs improve interpretability of ML predictions?
- What preprocessing is best for the UCI dataset?

---

## 2. Data

### 2.1 Data Source
UCI Heart Disease dataset combining records from multiple institutions.

### 2.2 Dataset Overview
- Format: CSV  
- Records: 920  
- Features: 16 (8 selected)  
- Target: Binary classification  

### 2.3 Selected Features
- Age  
- Sex  
- Chest pain type  
- Resting blood pressure  
- Serum cholesterol  
- Fasting blood sugar  
- Max heart rate  
- Target variable  

### 2.4 Target Variable
- 0 = No heart disease  
- 1 = Heart disease  

---

## 3. Data Preprocessing

### 3.1 Cleaning
- Removed irrelevant columns
- Handled missing values using median/mode imputation

### 3.2 Outliers
Handled using IQR method with value capping instead of deletion.

### 3.3 Encoding
- One-hot encoding for categorical variables
- StandardScaler for normalization

### 3.4 Final Dataset
Clean, numeric, and model-ready dataset with no missing values.

---

## 4. Model Development

### 4.1 Models Tested
- Logistic Regression  
- Random Forest  
- SVM  
- XGBoost  

### 4.2 Data Split
- Train: 70%  
- Validation: 15%  
- Test: 15%  
- Stratified splitting used  

### 4.3 Scaling
StandardScaler applied to all features.

### 4.4 Hyperparameter Tuning
GridSearchCV used for XGBoost:
- n_estimators  
- max_depth  
- learning_rate  
- subsample  

### 4.5 Results

| Model | Accuracy | Recall |
|------|----------|--------|
| Logistic Regression | 81% | 81% |
| Random Forest | 80% | 81% |
| SVM | 83% | 88% |
| XGBoost | **85.51%** | 85% |

XGBoost performed best and was selected.

### 4.6 Metrics
- Accuracy  
- Recall (important for medical use)  
- Confusion Matrix  

---

## 5. System Design

### 5.1 Web App
Built using Streamlit for interactive user input and prediction.

### 5.2 Architecture
- Input layer: User questionnaire  
- Processing: Feature mapping + scaling  
- Model: XGBoost inference  
- Output: Risk score + AI advice  

### 5.3 Model Saving
Model, scaler, and features saved using pickle.

### 5.4 Input Mapping
User answers mapped to clinical values:
- BP history → estimated systolic BP  
- Cholesterol awareness → estimated cholesterol  
- Breathing difficulty → heart rate proxy  

### 5.5 Gemini Integration
Gemini generates lifestyle advice with rules:
- No diagnosis  
- No medication advice  
- Max 10 bullet points  
- Simple language  

### 5.6 Tech Stack
- Python  
- Scikit-learn  
- XGBoost  
- Pandas  
- Streamlit  
- Google Gemini API  

---

## 6. Conclusion

### 6.1 Summary
Achieved 85.51% accuracy using XGBoost. Integrated ML + LLM for user-friendly health insights.

### 6.2 Applications
- Personal health screening  
- Public health awareness  
- Corporate wellness tools  
- Education  

### 6.3 Limitations
- Proxy-based inputs reduce accuracy  
- Limited dataset size  
- No real clinical validation  
- Simplified binary classification  

### 6.4 Future Work
- Add more clinical features  
- Use larger datasets (MIMIC, UK Biobank)  
- Add SHAP explainability  
- Multilingual support  
- Clinical validation  

---

## 7. References
- UCI Machine Learning Repository  
- XGBoost Paper (Chen & Guestrin)  
- Scikit-learn documentation  
- WHO Cardiovascular Facts  
- Streamlit documentation  
