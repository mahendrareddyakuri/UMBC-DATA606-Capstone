Heart Disease Prediction and AI-Based Health Guidance System

An AI-powered Heart Disease Risk Prediction web application built using Machine Learning, Streamlit, and Google Gemini AI.
This application predicts the probability of heart disease risk based on user-provided health information and generates personalized wellness tips using Generative AI.

📘 Project Information
Prepared For

Chaojie Wang

Author

Mahendra Reddy Akuri

Program

UMBC Data Science Master’s Degree Capstone

 Features
 Heart disease risk prediction using Machine Learning
 Interactive Streamlit web application
 AI-generated personalized health recommendations
 Probability-based risk analysis
 Beginner-friendly and clean UI
 Real-time prediction results
 Gemini AI integration for wellness guidance
Technologies Used
Python
Streamlit
Pandas
Scikit-learn
Pickle
Google Gemini AI
dotenv
📂 Project Structure
heart-disease-prediction/
│
├── app.py
├── heart_model.pkl
├── requirements.txt
├── README.md
├── .env
│
└── assets/
    ├── homepage.png
    └── prediction_result.png
⚙️ Installation & Setup
Clone the Repository
git clone https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone.git
cd UMBC-DATA606-Capstone
Create Virtual Environment (Recommended)
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Configure Gemini API Key

Create a .env file in the project root:

GEMINI_API_KEY="AIzaSyCuTqACqluca-jW4yAtzcAhMO5oqG7sIy8"

Or use Streamlit Secrets:

GEMINI_API_KEY="AIzaSyCuTqACqluca-jW4yAtzcAhMO5oqG7sIy8"
 Run the Application
streamlit run app.py
 How the Application Works
User enters health-related details.
Input data is transformed into ML-ready format.
The trained machine learning model predicts heart disease risk.
Prediction probability is calculated.
Gemini AI generates personalized health and wellness tips.
Final prediction results are displayed in the Streamlit dashboard.
<img width="802" height="766" alt="streamlit606_1" src="https://github.com/user-attachments/assets/dd0adc2b-b336-4886-abbc-77f4ffc1edbc" />
<img width="669" height="540" alt="Streamlit_02" src="https://github.com/user-attachments/assets/40a4f1f4-64df-459f-8cf2-9fdf098c20c7" />


Features Visible:
User-friendly health questionnaire
Age and gender selection
Chest pain and blood pressure inputs
Diabetes and cholesterol history
Simple and clean Streamlit interface
Prediction Result & AI Health Tips

Features Visible:
Risk probability prediction
High-risk / low-risk classification
AI-generated wellness suggestions
Gemini-powered health guidance
Personalized healthy lifestyle recommendations
AI Health Guidance

The application uses Google Gemini AI to generate:

Healthy eating suggestions
Exercise recommendations
Sleep improvement guidance
Stress management habits
General wellness tips

The AI recommendations are:

Simple to understand
Positive and encouraging
Non-medical lifestyle guidance only

The prediction results:

Are NOT medical diagnoses
Should NOT replace professional healthcare advice
Are intended for early awareness and learning purposes

Always consult certified healthcare professionals for medical concerns.

GitHub Repository:
https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone.git

LinkedIn Profile:
https://www.linkedin.com/in/mahendra-reddy-akuri-6b6976277/

PowerPoint Presentation:
https://docs.google.com/presentation/d/1lTPJgnKKfciBwd0vLyUJYqsFHJimzkKa-pkG7HUIrxc/edit?usp=sharing

YouTube Demonstration:
https://youtu.be/KQOULHU3mwg
 Future Improvements
Deploy on Streamlit Cloud or AWS
Add user authentication system
Improve ML model accuracy
Add historical prediction tracking
Multi-language support
Advanced visualization dashboards
Integration with healthcare APIs
 Acknowledgment

Special thanks to:

University of Maryland, Baltimore County
Chaojie Wang
Faculty members, mentors, and peers who supported the capstone project development.
 Author

Mahendra Reddy Akuri

GitHub Repository:
https://github.com/mahendrareddyakuri/UMBC-DATA606-Capstone.git

LinkedIn Profile:
https://www.linkedin.com/in/mahendra-reddy-akuri-6b6976277/

PowerPoint Presentation:
https://docs.google.com/presentation/d/1lTPJgnKKfciBwd0vLyUJYqsFHJimzkKa-pkG7HUIrxc/edit?usp=sharing

YouTube Demonstration:
https://youtu.be/KQOULHU3mwg

This project is open-source and available under the MIT License
