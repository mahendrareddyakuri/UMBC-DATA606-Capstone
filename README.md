# ❤️ Heart Disease Prediction and AI-Based Health Guidance System

## UMBC DATA 606 Capstone Project

This project is an end-to-end machine learning and AI-powered web application that predicts the likelihood of heart disease using simple health indicators provided by the user.

The system combines:
- XGBoost Machine Learning Model
- Google Gemini Large Language Model (LLM)
- Streamlit Web Application

The goal is to make preventive heart health awareness more accessible to the general public using artificial intelligence.

---

# 👨‍🎓 Author

Mahendra Reddy Akuri

UMBC — Master’s in Data Science

Course:
DATA 606 – Capstone in Data Science

Instructor:
Dr. Chaojie (Jay) Wang

---

# 🔗 Project Links

- [GitHub Repository](https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone.git?utm_source=chatgpt.com)
- [LinkedIn Profile](https://www.linkedin.com/in/mahendra-reddy-akuri-6b6976277/?utm_source=chatgpt.com)
- [PowerPoint Presentation](https://docs.google.com/presentation/d/1lTPJgnKKfciBwd0vLyUJYqsFHJimzkKa-pkG7HUIrxc/edit?usp=sharing&utm_source=chatgpt.com)
- [YouTube Demo](https://youtu.be/KQOULHU3mwg?utm_source=chatgpt.com)

---

# 📌 Project Objective

The project predicts heart disease risk using:
- Age
- Gender
- Chest pain symptoms
- Blood pressure history
- Cholesterol history
- Diabetes status
- Maximum heart rate approximation

The application then generates AI-based wellness guidance using Google Gemini.

---

# 🚀 Features

## Machine Learning Prediction
- XGBoost classification model
- Probability-based risk prediction
- Binary classification output

## AI Health Guidance
- Personalized wellness recommendations
- Google Gemini integration
- Simple English responses

## User-Friendly Design
- Streamlit interface
- No medical expertise required
- Easy-to-use questionnaire

## Safety Constraints
The AI system strictly avoids:
- Medical diagnosis
- Medication recommendations
- Complex medical terminology

---

# 🧠 Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| ML Libraries | Scikit-learn, XGBoost |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Web Framework | Streamlit |
| AI Integration | Google Gemini API |
| Serialization | Pickle |

---

# 📂 Project Structure

```bash
Heart-Disease-App/
│
├── app.py
├── heart_model.pkl
├── requirements.txt
├── report.md
├── akuri_606_final.ipynb
│
├── data/
│   └── heart_disease_uci.csv
│
├── .streamlit/
│   └── secrets.toml
│
└── README.md
```

---

# 📊 Dataset Information

## Dataset Source
UCI Heart Disease Dataset

## Dataset Details

| Attribute | Value |
|---|---|
| File Format | CSV |
| Dataset Size | 79.3 KB |
| Rows | 920 |
| Columns | 16 |

## Selected Features

| Feature | Description |
|---|---|
| Age | Patient age |
| Sex | Biological gender |
| Chest Pain Type | Chest discomfort category |
| Resting BP | Blood pressure |
| Cholesterol | Serum cholesterol |
| Fasting Blood Sugar | Diabetes indicator |
| Max Heart Rate | Maximum heart rate achieved |

## Target Variable

| Value | Meaning |
|---|---|
| 0 | No Heart Disease |
| 1 | Heart Disease Present |

---

# ⚙️ Machine Learning Workflow

## Data Preprocessing
- Missing value handling
- Median and mode imputation
- Outlier capping using IQR
- One-hot encoding
- Feature scaling

## Models Evaluated
- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- XGBoost

## Final Model
XGBoost achieved the best performance.

| Metric | Score |
|---|---|
| Accuracy | 85.51% |
| Recall | ~85% |

---

# 🤖 Gemini AI Integration

The project integrates Google Gemini 2.5 Flash to generate personalized health guidance.

The AI system:
- Uses prediction probability
- Adjusts recommendations based on risk level
- Produces simple and safe wellness advice

### AI Safety Rules
- No diagnosis
- No medications
- Simple English only
- Maximum 10 bullet points

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone.git
cd UMBC-DATA606-Capstone
```

---

# 🐍 Create Virtual Environment

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

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure Gemini API Key

Create this file:

```bash
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📷 Application Workflow

1. User enters health information
2. Inputs are processed and encoded
3. Model predicts heart disease risk
4. Risk probability is calculated
5. Gemini generates personalized tips
6. Results are displayed in Streamlit

---

# 📚 Files Description

| File | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `heart_model.pkl` | Saved ML model and scaler |
| `akuri_606_final.ipynb` | Complete ML training notebook |
| `report.md` | Full research report |
| `heart_disease_uci.csv` | Dataset |
| `requirements.txt` | Python dependencies |

---

# ⚠️ Disclaimer

This project is:
- Educational
- Research-focused
- Demonstration-based

It is NOT intended for:
- Clinical diagnosis
- Professional medical use
- Emergency healthcare decisions

Always consult healthcare professionals for medical advice.

---

# 📖 References

- UCI Machine Learning Repository
- XGBoost Documentation
- Scikit-learn Documentation
- Streamlit Documentation
- Google Gemini Documentation

---

# ⭐ Acknowledgements

Special thanks to:
- UMBC Data Science Department
- Dr. Chaojie (Jay) Wang
- UCI Machine Learning Repository
- Open-source AI and ML communities
