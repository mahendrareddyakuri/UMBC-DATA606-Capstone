import streamlit as st
import pandas as pd
import pickle
import os
from dotenv import load_dotenv
from google import genai

# -----------------------------------
# LOAD ENVIRONMENT VARIABLES (.env)
# -----------------------------------
import streamlit as st
from google import genai

API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

# -----------------------------------
# CONFIGURE GEMINI CLIENT (NEW SDK)
# -----------------------------------
client = genai.Client(api_key=API_KEY)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="🫀",
    layout="centered"
)

st.title("🫀 Heart Disease Prediction App")
st.write("Answer a few simple questions to assess heart disease risk.")
st.warning("⚠️ This is NOT a medical diagnosis. Please consult a doctor for confirmation.")

# -----------------------------------
# LOAD MODEL, SCALER, FEATURE SCHEMA
# -----------------------------------
@st.cache_resource
def load_artifacts():
    with open("heart_model.pkl", "rb") as f:
        saved = pickle.load(f)
    return saved["model"], saved["scaler"], saved["features"]

model, Scaler, FEATURE_COLUMNS = load_artifacts()

# -----------------------------------
# GEMINI HELPER FUNCTION (PROBABILITY AWARE)
# -----------------------------------
def get_health_tips(user_profile, probability):
    percentage = round(probability * 100, 2)

    if probability >= 0.60:
        risk_type = "HIGH"
        focus_message = (
            "The risk is high. Give stronger lifestyle guidance "
            "and encourage strict healthy daily habits."
        )
    else:
        risk_type = "LOW"
        focus_message = (
            "The risk is low. Give advice to maintain good habits "
            "and prevent future health problems."
        )

    prompt = f"""
You are a friendly health assistant.

User details (self-reported, non-medical):
{user_profile}

Predicted heart disease risk:
- Category: {risk_type}
- Probability: {percentage}%

Additional guidance:
{focus_message}

VERY IMPORTANT INSTRUCTIONS:
- Give exactly 10 bullet points
- Use very simple English for normal people
- No medical terms
- No disease diagnosis
- No medicine suggestions
- Each bullet must be one short sentence
- Focus only on diet, physical activity, sleep, stress, and daily habits
- Be positive and easy to understand
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

# -----------------------------------
# USER INPUTS (COMMON-MAN FRIENDLY)
# -----------------------------------
st.subheader("Your Details")

age = st.number_input("Age", min_value=1, max_value=120, value=45)

sex = st.selectbox("Gender", ["male", "female"])

chest_pain_ui = st.selectbox(
    "Do you experience chest pain or discomfort?",
    [
        "No chest pain",
        "Mild chest discomfort",
        "Chest pain during physical activity",
        "Severe or frequent chest pain"
    ]
)

high_bp = st.selectbox(
    "Have you been told you have high blood pressure?",
    ["No", "Yes", "Don't know"]
)

cholesterol = st.selectbox(
    "Have you been told you have high cholesterol?",
    ["No", "Yes", "Not sure"]
)

diabetes = st.selectbox(
    "Do you have diabetes?",
    ["No", "Yes"]
)

breathless = st.selectbox(
    "Do you feel breathless or very tired during mild physical activity?",
    ["No", "Yes"]
)

# -----------------------------------
# CONVERSION LOGIC (UI → MODEL)
# -----------------------------------
cp_map = {
    "No chest pain": "asymptomatic",
    "Mild chest discomfort": "atypical angina",
    "Chest pain during physical activity": "typical angina",
    "Severe or frequent chest pain": "non-anginal pain"
}

bp_map = {
    "No": 120,
    "Yes": 145,
    "Don't know": 130
}

chol_map = {
    "No": 180,
    "Yes": 240,
    "Not sure": 210
}

user_input = {
    "age": age,
    "sex": sex,
    "cp": cp_map[chest_pain_ui],
    "trestbps": bp_map[high_bp],
    "chol": chol_map[cholesterol],
    "fbs": 1 if diabetes == "Yes" else 0,
    "thalch": 120 if breathless == "Yes" else 170
}

user_df = pd.DataFrame([user_input])

# -----------------------------------
# PREDICTION + AI GUIDANCE
# -----------------------------------
if st.button("🔍 Predict Risk"):
    try:
        # Encode categorical features
        user_encoded = pd.get_dummies(user_df, drop_first=True)

        # Align with training feature schema
        user_encoded = user_encoded.reindex(
            columns=FEATURE_COLUMNS,
            fill_value=0
        )

        # Scale input
        user_scaled = Scaler.transform(user_encoded)

        # Predict
        prediction = model.predict(user_scaled)[0]
        probability = model.predict_proba(user_scaled)[0][1]

        # -----------------------------------
        # RESULT
        # -----------------------------------
        st.subheader("Prediction Result")

        if prediction == 1:
            st.error(
                f"⚠️ High Risk of Heart Disease\n\n"
                f"Estimated Risk Probability: {probability * 100:.2f}%"
            )
        else:
            st.success(
                f"✅ Low Risk of Heart Disease\n\n"
                f"Estimated Risk Probability: {probability * 100:.2f}%"
            )

        # -----------------------------------
        # GEMINI AI HEALTH TIPS
        # -----------------------------------
        user_profile = f"""
Age: {age}
Gender: {sex}
Chest pain: {chest_pain_ui}
High blood pressure history: {high_bp}
High cholesterol history: {cholesterol}
Diabetes: {diabetes}
Breathlessness during activity: {breathless}
"""

        with st.spinner("🤖 Generating personalized health tips..."):
            tips = get_health_tips(user_profile, probability)

        st.subheader("🧠 AI Health Tips (Powered by Gemini)")
        st.write(tips)

        st.info(
            "ℹ️ These AI-generated tips are for general wellness guidance only "
            "and do not replace professional medical advice."
        )

    except Exception as e:
        st.error("❌ An error occurred during prediction.")
        st.code(str(e))

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")
st.caption("Educational use only • ML + LLM based early risk awareness tool")
