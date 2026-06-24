import streamlit as st
import pickle
import numpy as np
import os

# ── Load model and scaler ──
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'diabetes_model.pkl'), 'rb') as f:
    model = pickle.load(f)

with open(os.path.join(BASE_DIR, 'scaler.pkl'), 'rb') as f:
    scaler = pickle.load(f)

# ── Page config ──
st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🩺",
    layout="centered"
)

# ── Header ──
st.title("🩺 Diabetes Risk Prediction App")
st.markdown("### Cavendish University Uganda — Data Science Graduation Project")
st.markdown("---")
st.write("Enter the patient's medical details below to predict diabetes risk.")

# ── Input form ──
st.markdown("### 📋 Patient Information")

col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input(
        "Number of Pregnancies", min_value=0, max_value=20, value=1)
    glucose = st.number_input(
        "Glucose Level (mg/dL)", min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input(
        "Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input(
        "Skin Thickness (mm)", min_value=0, max_value=100, value=20)

with col2:
    insulin = st.number_input(
        "Insulin Level (mu U/ml)", min_value=0, max_value=900, value=80)
    bmi = st.number_input(
        "BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
    dpf = st.number_input(
        "Diabetes Pedigree Function", min_value=0.0, max_value=3.0,
        value=0.5, step=0.01)
    age = st.number_input(
        "Age (years)", min_value=1, max_value=120, value=30)

st.markdown("---")

# ── Predict button ──
if st.button("🔍 Predict Diabetes Risk", use_container_width=True):

    # Prepare input
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])
    input_scaled = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0]

    st.markdown("---")
    st.markdown("### 📊 Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk — This patient is likely DIABETIC")
        st.metric(label="Probability of Diabetes",
                  value=f"{probability[1] * 100:.1f}%")
        st.markdown("""
        **Recommended Actions:**
        - Refer patient for full clinical diabetes diagnosis
        - Advise lifestyle changes: diet and exercise
        - Monitor blood glucose levels regularly
        - Consult an endocrinologist
        """)
    else:
        st.success("✅ Low Risk — This patient is likely NON-DIABETIC")
        st.metric(label="Probability of No Diabetes",
                  value=f"{probability[0] * 100:.1f}%")
        st.markdown("""
        **Recommended Actions:**
        - Maintain a healthy lifestyle
        - Continue regular health checkups
        - Monitor weight and blood pressure
        """)

    st.markdown("---")
    st.caption("⚠️ Disclaimer: This app is a decision-support tool only and does not replace clinical diagnosis.")

# ── Sidebar ──
st.sidebar.title("ℹ️ About This App")
st.sidebar.info("""
This application uses a **Random Forest Classifier** trained on the
Pima Indians Diabetes Dataset to predict whether a patient is at risk
of diabetes based on 8 medical measurements.

**Model Accuracy:** ~78%
**Dataset:** 768 patient records
**Algorithm:** Random Forest (100 trees)
""")
st.sidebar.markdown("---")
st.sidebar.markdown("**Developed by:** NASSOLO ALLEN JUSTINE")
st.sidebar.markdown("**STUDENT ID:** 233409")
st.sidebar.markdown("**Institution:** Cavendish University Uganda")
st.sidebar.markdown("**Programme:** Diploma in Data Science and Analytics")
st.sidebar.markdown("**Year:** 2026")