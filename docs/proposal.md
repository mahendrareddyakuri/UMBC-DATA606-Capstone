# Heart Disease Prediction and AI-Based Health Guidance System

**Author:** Mahendra Reddy Akuri  
**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang  

**GitHub Repository:** [https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone](https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone)  
**LinkedIn Profile:** [https://www.linkedin.com/in/mahendra-reddy-akuri-6b6976277/](https://www.linkedin.com/in/mahendra-reddy-akuri-6b6976277/)  
**PowerPoint Presentation:** *To be added after presentation is created*  
**YouTube Video:** *To be added after project demo video is recorded*  

---

## 1. Title and Author

**Project Title:** Heart Disease Prediction and AI-Based Health Guidance System  
**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang  
**Author:** Mahendra Reddy Akuri  

---

## 2. Background

### What is it about?
This project is a web-based application designed to analyze health-related data to predict heart disease risk at an early stage. It combines Machine Learning (ML) for statistical risk prediction and a Large Language Model (LLM)—specifically Google Gemini Flash—to provide personalized, non-medical lifestyle guidance. It is designed for "normal users" rather than medical professionals, using simple questions instead of complex medical jargon.  

### Why does it matter?
- **Early Detection:** Heart disease is a leading global cause of death; early awareness can lead to life-saving lifestyle changes.  
- **Accessibility:** Traditional diagnosis is often expensive, time-consuming, and requires physical visits to hospitals for tests like ECGs.  
- **Preventative Action:** It provides a basic early risk check for common people who want to understand if they should seek professional medical consultation.  

### Research Questions
1. Can a machine learning model accurately predict heart disease risk using non-invasive, simple health parameters provided by a user?  
2. How can an LLM be safely integrated into a health application to provide actionable wellness tips without offering medical diagnoses or medicinal suggestions?  
3. Which ML algorithm among Logistic Regression, Random Forest, SVM, and XGBoost provides the most reliable performance for this specific dataset?  

---

## 3. Data

### Dataset Description
- **Data Source:** UCI Heart Disease Dataset  
- **Data Size:** 79.3 KB  
- **Data Shape:** The dataset has 16 columns; the project focuses on 7 specific features.  
- **Row Representation:** Each row represents an individual’s medical and health profile.  

### Data Dictionary

| Column Name        | Data Type   | Definition                     | Potential Values                |
|-------------------|------------|--------------------------------|--------------------------------|
| Age               | Numeric    | Age of the user                | Integer                        |
| Sex               | Categorical| Biological sex                 | Male, Female                   |
| Chest pain type   | Categorical| Type/Level of chest discomfort | Simplified categories           |
| Resting BP        | Numeric    | Resting blood pressure history | Value in mmHg                   |
| Cholesterol       | Numeric    | Serum cholesterol history      | Value in mg/dl                  |
| Fasting blood sugar| Categorical| Blood sugar indicator          | True/False (> 120 mg/dl)       |
| Max heart rate    | Numeric    | Maximum heart rate achieved    | Beats per minute                |

### Target and Predictors
- **Target/Label:** Risk Label (0 or 1), where 0 = low risk, 1 = high risk.  
- **Features/Predictors:** Age, Sex, Chest Pain, Resting BP, Cholesterol, Fasting Blood Sugar, Max Heart Rate  

---


## Summary
The system successfully integrates predictive analytics and generative AI to create an early risk awareness tool. By prioritizing user accessibility and ethical safety (no medical diagnosis), it encourages healthy lifestyle choices and early intervention.
