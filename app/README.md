# Heart Disease Prediction & AI Health Guidance System

A machine learning-powered web application that predicts the likelihood of heart disease using simple health-related inputs and provides personalized wellness recommendations using Google Gemini AI.

Built with Python, Streamlit, XGBoost, and Gemini AI for guidance tips.

---

# Project Overview

This project combines a trained XGBoost classification model with Google Gemini AI to create an intelligent and user-friendly heart disease risk assessment system.

Users answer a few simple health questions through a Streamlit web interface. The application then:

- Predicts heart disease risk probability
- Classifies the user as Low Risk or High Risk
- Generates personalized AI-powered lifestyle recommendations
- Displays results in plain and easy-to-understand language

The system is designed for educational and awareness purposes only and is NOT intended for medical diagnosis.

---

# Features

- Heart disease risk prediction using Machine Learning
- AI-generated personalized health tips using Gemini
- User-friendly Streamlit interface
- Real-time prediction results
- Probability-based risk scoring
- Simple non-clinical questionnaire
- Secure API integration using Streamlit Secrets
- Cached model loading for improved performance

---

# Technologies Used

## Machine Learning
- XGBoost Classifier
- Scikit-learn
- Pandas
- NumPy

## Frontend / Deployment
- Streamlit

## AI Integration
- Google Gemini 2.5 Flash
- Google GenAI SDK

## Model Storage
- Pickle

---

# Dataset

This project uses the UCI Heart Disease Dataset.

Dataset Source:  
https://archive.ics.uci.edu/ml/datasets/Heart+Disease

## Features Used

- Age
- Gender
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Diabetes / Fasting Blood Sugar
- Maximum Heart Rate

## Target Variable

- 0 → No Heart Disease
- 1 → Heart Disease Present

---

# How the Application Works

## Step 1 — User Input

The user answers simple health-related questions such as:

- Age
- Gender
- Chest discomfort
- Blood pressure history
- Cholesterol history
- Diabetes status
- Breathlessness during activity

---

## Step 2 — Data Processing

The application:

- Converts user-friendly answers into model-compatible values
- Encodes categorical features
- Aligns feature columns with the training schema
- Applies feature scaling using StandardScaler

---

## Step 3 — Risk Prediction

The trained XGBoost model predicts:

- Heart disease class
- Risk probability percentage

---

## Step 4 — AI Health Guidance

Google Gemini AI generates:

- Personalized lifestyle guidance
- Exercise recommendations
- Diet suggestions
- Sleep and stress management tips

The AI output is controlled using strict prompt engineering:

- No diagnosis
- No medication suggestions
- Simple English only
- Maximum 10 bullet points

---

# Project Structure

```bash
Heart-Disease-App/
│
├── app.py
├── heart_model.pkl
├── requirements.txt
├── .streamlit/
│   └── secrets.toml
├── README.md
└── dataset/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone.git
```

```bash
cd UMBC-DATA606-Capstone
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Gemini API Key

Create the following file:

```bash
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "AIzaSyCuTqACqluca-jW4yAtzcAhMO5oqG7sIy8"
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Model Performance

| Model | Accuracy | Recall |
|------|------|------|
| Logistic Regression | 81% | 81% |
| Random Forest | 80% | 81% |
| SVM | 83% | 88% |
| XGBoost | 85.51% | 85% |

XGBoost achieved the best overall performance and was selected for deployment.

---

# Example Application Flow

## User Inputs

- Age: 52
- Gender: Male
- High Blood Pressure: Yes
- Diabetes: No

## Prediction Output

- High Risk of Heart Disease
- Estimated Probability: 78.45%
<img width="802" height="766" alt="streamlit606_1" src="https://github.com/user-attachments/assets/08a95ac9-83bb-4d75-866a-ea3f518cb8be" />

## AI Guidance

<img width="669" height="540" alt="Streamlit_02" src="https://github.com/user-attachments/assets/bc661dc5-ae7c-404b-9ea0-a8f24b5b81e7" />


---

# Safety Notice

This application is designed for:

- Educational use
- Research demonstrations
- Preventive health awareness

This application:

- Does NOT provide medical diagnosis
- Does NOT replace professional healthcare advice
- Should NOT be used for emergency medical decisions

Always consult a licensed healthcare professional for medical concerns.

---

# Future Improvements

- SHAP explainability integration
- Additional clinical features
- Real-world validation studies
- Multi-language support
- Federated learning support
- Improved UI/UX
- Cloud deployment

---

# Author

## Mahendra Reddy Akuri

- UMBC Data Science Graduate Student
- DATA 606 Capstone Project

### Links

- GitHub: https://github.com/mahendrareddyakuri
- LinkedIn: https://www.linkedin.com/in/mahendra-reddy-akuri-6b6976277/
- YouTube Demo: https://youtu.be/KQOULHU3mwg

---

# References

- UCI Machine Learning Repository
- Scikit-learn Documentation
- XGBoost Documentation
- Streamlit Documentation
- Google Gemini API Documentation
- World Health Organization Cardiovascular Reports

---

# License

This project is intended for educational and academic purposes only.
