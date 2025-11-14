# app.py
import streamlit as st
import numpy as np
import joblib
import os

# Ensure correct working folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(page_title="Student Course Recommender", layout="centered")

st.title("🎓 Student Course Recommendation System")

@st.cache_resource
def load_artifacts():
    model = joblib.load("model.joblib")
    interest_le = joblib.load("interest_encoder.joblib")
    course_le = joblib.load("course_encoder.joblib")
    return model, interest_le, course_le

try:
    model, interest_le, course_le = load_artifacts()
except Exception as e:
    st.error("Failed to load model files. Make sure model.joblib and encoders exist and are valid.")
    st.write(e)
    st.stop()

# Input widgets
age = st.number_input("Age", min_value=15, max_value=60, value=20)
math_score = st.slider("Math Score (0-100)", 0, 100, 60)
coding_score = st.slider("Coding Score (0-100)", 0, 100, 70)
communication = st.slider("Communication (0-100)", 0, 100, 75)

# use encoder classes to populate interests
interests = list(interest_le.classes_)
interest = st.selectbox("Primary Interest", interests)

if st.button("Recommend Course"):
    try:
        # encode interest
        interest_enc = int(interest_le.transform([interest])[0])
        X = np.array([[age, math_score, coding_score, communication, interest_enc]])
        pred = model.predict(X)[0]
        course = course_le.inverse_transform([int(pred)])[0]
        st.success(f"Recommended Course: **{course}**")
    except Exception as e:
        st.error("Prediction failed. See error details below.")
        st.write(e)
