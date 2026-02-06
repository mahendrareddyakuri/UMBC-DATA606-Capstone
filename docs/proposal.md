# Project Report: Heart Disease Prediction and AI-Based Health Guidance System

**Author:** Mahendra Reddy Akuri  
**Project Title:** Heart Disease Prediction and AI-Based Health Guidance System  
[cite_start]**Prepared for:** UMBC Data Science Master Degree Capstone by Dr. Chaojie (Jay) Wang [cite: 1, 192-195]

---

## 1. Links and Resources
* [cite_start]**GitHub Repository:** [https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone](https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone) [cite: 201]
* [cite_start]**LinkedIn Profile:** [https://www.linkedin.com/in/mahendra-reddy-akuri-6b6976277/](https://www.linkedin.com/in/mahendra-reddy-akuri-6b6976277/) [cite: 202]
* [cite_start]**PowerPoint Presentation:** [To be added after presentation is created] [cite: 203]
* [cite_start]**YouTube Video:** [To be added after project demo video is recorded] [cite: 204]

---

## 2. Background

### What is it about?
[cite_start]This project is a web-based application designed to analyze health-related data to predict heart disease risk at an early stage[cite: 34, 207]. [cite_start]It combines **Machine Learning (ML)** for statistical risk prediction and a **Large Language Model (LLM)**—specifically Google Gemini Flash—to provide personalized, non-medical lifestyle guidance [cite: 36-38, 208]. [cite_start]It is specifically built for "normal users" rather than medical professionals, using simple questions instead of complex jargon [cite: 8-9, 209].

### Why does it matter?
* [cite_start]**Early Detection:** Heart disease is a leading global cause of death; early awareness can lead to life-saving lifestyle changes [cite: 3-5, 211].
* [cite_start]**Accessibility:** Traditional diagnosis is often expensive, time-consuming, and requires physical visits to hospitals for tests like ECGs or blood work [cite: 11-16, 212].
* [cite_start]**Preventative Action:** It provides a basic early risk check for common people who want to understand if they should seek professional medical consultation[cite: 17, 213].

### What are your research questions?
1. [cite_start]Can a machine learning model accurately predict heart disease risk using non-invasive, simple health parameters provided by a user? [cite: 215]
2. [cite_start]How can an LLM be safely integrated into a health application to provide actionable wellness tips without offering medical diagnoses or medicinal suggestions? [cite: 216]
3. [cite_start]Which ML algorithm among Logistic Regression, Random Forest, SVM, and XGBoost provides the most reliable performance for this specific dataset? [cite: 119-124, 217]

---

## 3. Data

### Dataset Description
* [cite_start]**Data Source:** UCI Heart Disease Dataset[cite: 110, 221].
* [cite_start]**Data Size:** Standard tabular dataset, approximately 79.3KB[cite: 222].
* [cite_start]**Data Shape:** While standard versions have 16 columns, this project focuses on 7 specific features for its prediction module [cite: 223-224].
* [cite_start]**Row Representation:** Each row represents a patient or individual's medical and health profile[cite: 225].

### Data Dictionary
[cite_start]The system uses the following features to ensure a user-friendly experience[cite: 227]:

| Column Name | Data Type | Definition | Potential Values |
| :--- | :--- | :--- | :--- |
| **Age** | Numeric | Age of the user | [cite_start]Integer [cite: 228] |
| **Sex** | Categorical | Biological sex | [cite_start]Male, Female [cite: 228] |
| **Chest pain type** | Categorical | Level of chest discomfort | [cite_start]Simplified categories [cite: 228] |
| **Resting BP** | Numeric | Resting blood pressure history | [cite_start]Value in mmHg [cite: 228] |
| **Cholesterol** | Numeric | Serum cholesterol history | [cite_start]Value in mg/dl [cite: 228] |
| **Fasting blood sugar** | Categorical | Blood sugar indicator | [cite_start]True/False (> 120 mg/dl) [cite: 229] |
| **Max heart rate** | Numeric | Maximum heart rate achieved | [cite_start]Beats per minute [cite: 229] |

### Target and Predictors
* [cite_start]**Target/Label:** The Risk Label (0 or 1), where 0 represents low risk and 1 represents high risk[cite: 126, 232].
* [cite_start]**Features/Predictors:** The seven variables listed in the table above: Age, Sex, Chest Pain, BP, Cholesterol, Blood Sugar, and Max Heart Rate [cite: 111-118, 233].

---

## 4. Technology Stack & Modules

### Software Requirements
* [cite_start]**Language:** Python 3.10+[cite: 143, 236].
* [cite_start]**Frameworks:** Streamlit (UI), Scikit-learn (ML), Pandas/NumPy (Data), Google GenAI SDK (LLM) [cite: 144-148, 237].
* [cite_start]**Security:** `python-dotenv` for secure API key handling[cite: 149, 238].

### System Modules
1. [cite_start]**User Interface Module:** A Streamlit-based web interface for simple data collection[cite: 90, 240].
2. [cite_start]**Data Preprocessing Module:** Handles encoding, outlier capping, and feature scaling using `StandardScaler` [cite: 103-107, 241].
3. [cite_start]**Machine Learning Module:** Runs input through the best-performing model (e.g., XGBoost or Random Forest) to produce a probability score[cite: 124, 242].
4. [cite_start]**AI Guidance Module:** Sends the risk score and profile to Gemini AI to generate 10 bullet points of wellness guidance [cite: 128-134, 243].



---

## 5. Conclusion
[cite_start]The system successfully integrates predictive analytics and generative AI to create an early risk awareness tool[cite: 184, 245]. [cite_start]By prioritizing user accessibility and ethical safety—ensuring no medical diagnosis is provided—it encourages healthy lifestyle choices and early intervention [cite: 185-186, 246-247].
