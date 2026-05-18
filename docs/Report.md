# Heart Disease Prediction and AI-Based Health Guidance System

## UMBC Data Science Master’s Capstone Project (DATA 606)

**Prepared for:** Dr. Chaojie (Jay) Wang  
**Author:** Mahendra Reddy Akuri  
**Program:** UMBC Data Science Master’s Degree Capstone  

---

## Project Links

- GitHub Repository:  
  https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone.git

- LinkedIn Profile:  
  https://www.linkedin.com/in/mahendra-reddy-akuri-6b6976277/

- PowerPoint Presentation:  
  https://docs.google.com/presentation/d/1lTPJgnKKfciBwd0vLyUJYqsFHJimzkKa-pkG7HUIrxc/edit?usp=sharing

- YouTube Demonstration:  
  https://youtu.be/KQOULHU3mwg

---

# 1. Introduction

## 1.1 Project Overview

This project presents an intelligent web-based healthcare application designed to predict the likelihood of heart disease using machine learning techniques and AI-generated health guidance. The system combines the predictive capabilities of the XGBoost algorithm with the conversational intelligence of Google Gemini LLM to provide users with both risk assessment and personalized lifestyle recommendations.

The application is designed as an early screening and awareness tool rather than a clinical diagnostic system. Users can input basic health-related information, and the system generates a heart disease risk prediction along with safe, understandable wellness suggestions.

---

## 1.2 Motivation

Cardiovascular disease remains one of the leading causes of death globally. Many individuals are unaware of their cardiovascular risk until severe symptoms or life-threatening events occur.

Traditional medical diagnosis often requires expensive laboratory tests and clinical procedures such as:

- Electrocardiograms (ECG)
- Stress tests
- Blood analysis
- Imaging procedures

Machine learning offers a scalable and accessible alternative for early-stage prediction using limited and easily obtainable health features. This project aims to demonstrate how AI technologies can improve public health awareness and encourage preventive healthcare practices.

---

## 1.3 Research Questions

The project focuses on the following research questions:

1. Can heart disease be accurately predicted using simple health-related inputs?
2. Which machine learning algorithm performs best for this classification task?
3. How can Large Language Models (LLMs) provide safe and meaningful health guidance?
4. What preprocessing and feature engineering techniques improve model performance?

---

# 2. Dataset Description

## 2.1 Data Source

The project uses the UCI Heart Disease Dataset collected from multiple medical institutions and made publicly available through the UCI Machine Learning Repository.

---

## 2.2 Dataset Overview

| Attribute | Value |
|---|---|
| Dataset Type | Structured Tabular Data |
| File Format | CSV |
| Total Records | 920 |
| Total Features | 16 |
| Selected Features | 8 |
| Prediction Task | Binary Classification |

---

## 2.3 Selected Features

The following features were selected for model training:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Maximum Heart Rate
- Target Variable

These features were chosen based on clinical relevance and availability in real-world screening scenarios.

---

## 2.4 Target Variable

The target variable represents the presence of heart disease:

| Value | Meaning |
|---|---|
| 0 | No Heart Disease |
| 1 | Heart Disease Present |

---

# 3. Data Preprocessing and Exploratory Data Analysis (EDA)

## 3.1 Data Cleaning

Several preprocessing techniques were applied to improve dataset quality:

- Removed irrelevant or non-predictive columns
- Handled missing values using:
  - Median imputation for numerical features
  - Mode imputation for categorical features
- Verified datatype consistency

---

## 3.2 Outlier Handling

Outliers were identified using the Interquartile Range (IQR) method.

Instead of removing outliers completely, extreme values were capped to preserve valuable medical information while reducing model instability.

---

## 3.3 Feature Encoding and Scaling

### Encoding

Categorical variables were transformed using One-Hot Encoding.

### Feature Scaling

Numerical variables were normalized using StandardScaler to ensure consistent feature ranges across all models.

---

## 3.4 Dataset Readiness

After preprocessing:

- All features became numeric
- Missing values were resolved
- Data distributions were stabilized
- The dataset became suitable for machine learning training

---

# 4. Machine Learning Model Development

## 4.1 Models Evaluated

Multiple machine learning algorithms were trained and evaluated:

- Logistic Regression
- Naive Bayes
- Random Forest
- Support Vector Machine (SVM)
- XGBoost

---

## 4.2 Data Splitting Strategy

The dataset was divided using stratified sampling to preserve class distribution:

| Dataset Split | Percentage |
|---|---|
| Training Set | 70% |
| Validation Set | 15% |
| Test Set | 15% |

---

## 4.3 Feature Scaling

StandardScaler was applied during preprocessing to improve model convergence and stability, especially for SVM and Logistic Regression.

---

## 4.4 Hyperparameter Tuning

The XGBoost model was optimized using GridSearchCV.

The following parameters were tuned:

- `n_estimators`
- `max_depth`
- `learning_rate`
- `subsample`

This process improved prediction accuracy and reduced overfitting.

---

## 4.5 Model Performance Comparison

| Model | Accuracy | Recall |
|---|---|---|
| Logistic Regression | ~81% | ~81% |
| Random Forest | ~80% | ~81% |
| SVM | ~83% | ~88% |
| XGBoost | **85.51%** | ~85% |

### Best Performing Model

XGBoost achieved the highest overall performance and was selected as the final production model.

---

## 4.6 Evaluation Metrics

The following evaluation metrics were used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Importance of Recall

In healthcare applications, recall is especially important because false negatives can lead to missed disease detection.

---

# 5. System Design and Architecture

## 5.1 Web Application

The project was implemented as an interactive web application using Streamlit.

The application allows users to:

- Enter health information
- Receive heart disease risk predictions
- Obtain AI-generated wellness guidance

---

## 5.2 System Architecture

The application architecture consists of four layers:

### 1. Input Layer
Collects user responses through a simple questionnaire interface.

### 2. Processing Layer
Performs:
- Feature mapping
- Data transformation
- Scaling and encoding

### 3. Model Layer
Uses the trained XGBoost model for inference and probability prediction.

### 4. Output Layer
Displays:
- Heart disease risk score
- Prediction results
- AI-generated lifestyle recommendations

---
<img width="802" height="766" alt="Image" src="https://github.com/user-attachments/assets/7ae722ba-5932-4acc-937a-4d88e78843fa" />
<img width="669" height="540" alt="Image" src="https://github.com/user-attachments/assets/f1dbfcf4-51f8-481d-8a6c-84a80789f7aa" />

## 5.3 Model Persistence

The trained components were serialized using Pickle:

- Trained XGBoost model
- StandardScaler object
- Feature schema

This enables efficient deployment and reuse without retraining.

---

## 5.4 Input Mapping Strategy

Since users may not know exact medical measurements, the system maps questionnaire responses into estimated clinical values.

Examples include:

| User Response | Clinical Estimate |
|---|---|
| Blood pressure history | Estimated systolic BP |
| Cholesterol awareness | Estimated cholesterol |
| Breathlessness | Heart rate proxy |

This improves usability for non-medical users.

---

## 5.5 Gemini LLM Integration

Google Gemini API was integrated to generate personalized health guidance.

### Safety Constraints

The generated advice follows strict constraints:

- No medical diagnosis
- No medication recommendations
- Maximum of 10 bullet points
- Simple and understandable language
- Lifestyle-focused suggestions only

This ensures safer AI interaction in healthcare contexts.



---

## 5.6 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| Scikit-learn | ML Pipeline |
| XGBoost | Classification Model |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Streamlit | Web Application |
| Google Gemini API | AI Guidance |
| Pickle | Model Persistence |

---

# 6. Results and Discussion

## 6.1 Key Findings

The project demonstrates that heart disease prediction can be effectively performed using limited and easily accessible health inputs.

Key achievements include:

- XGBoost achieved **85.51% accuracy**
- SVM achieved the highest recall
- The AI guidance system improved user interpretability
- Streamlit enabled simple deployment and interaction

---

## 6.2 Real-World Applications

Potential applications include:

- Personal health screening tools
- Public health awareness programs
- Corporate wellness initiatives
- Educational healthcare systems
- Preventive health monitoring platforms

---

## 6.3 Limitations

Despite promising results, the project has several limitations:

- Small dataset size
- Use of proxy-based clinical estimates
- Binary classification simplification
- Lack of clinical validation
- Potential demographic bias in the dataset

The system should not replace professional medical evaluation.

---

## 6.4 Future Enhancements

Future improvements may include:

- Integration with larger healthcare datasets
- SHAP explainability for model transparency
- Real clinical parameter support
- Multi-language support
- Mobile application deployment
- Real-time health monitoring integration
- Clinical testing and validation studies

Potential datasets for future work:

- MIMIC Dataset
- UK Biobank

---

# 7. Conclusion

This project successfully combines machine learning and generative AI to create a healthcare-focused predictive system for heart disease risk assessment.

The XGBoost model demonstrated strong predictive performance, while Google Gemini enhanced user interaction through safe and understandable health guidance.

The project highlights the growing potential of AI-driven healthcare tools in preventive medicine, public awareness, and accessible digital health solutions.

Although the system is not intended for medical diagnosis, it demonstrates how AI can support early awareness and encourage healthier lifestyle decisions.

---

# 8. References

1. Detrano, R. et al. (1989).  
   International application of a new probability algorithm for the diagnosis of coronary artery disease.

2. UCI Machine Learning Repository  
   Heart Disease Dataset.

3. Chen, T., & Guestrin, C. (2016).  
   XGBoost: A Scalable Tree Boosting System.

4. Pedregosa, F. et al. (2011).  
   Scikit-learn: Machine Learning in Python.

5. World Health Organization (WHO)  
   Cardiovascular Disease Facts and Statistics.

6. Breiman, L. (2001).  
   Random Forests.

7. Cortes, C., & Vapnik, V. (1995).  
   Support Vector Networks.

8. McKinney, W. (2010).  
   Data Structures for Statistical Computing in Python.

9. Google Gemini API Documentation

10. Streamlit Documentation

---

# 9. Acknowledgements

Special thanks to:

- Dr. Chaojie (Jay) Wang
- UMBC Data Science Department
- UCI Machine Learning Repository
- Open-source Python and AI communities

for their support, resources, and guidance throughout this capstone project.

---
