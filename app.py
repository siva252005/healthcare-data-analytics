import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(
    page_title="Healthcare Cost Predictor",
    page_icon="🩺",
    layout="wide"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg,#eef2ff,#f8fafc);
}

/* Title */
.main-title{
    font-size:50px;
    font-weight:700;
    color:#1e3a8a;
}

/* Subtitle */
.subtitle{
    font-size:20px;
    color:#334155;
}

/* Card style */
.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0 6px 15px rgba(0,0,0,0.1);
    font-size:18px;
}

/* Prediction result */
.result{
    background:linear-gradient(135deg,#2563eb,#06b6d4);
    padding:35px;
    border-radius:15px;
    text-align:center;
    color:white;
    font-size:35px;
    font-weight:700;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#1e3a8a,#2563eb);
}

[data-testid="stSidebar"] label{
    color:white;
    font-weight:bold;
}

[data-testid="stSidebar"] .stSelectbox,
[data-testid="stSidebar"] .stSlider{
    color:white;
}

/* Button */
div.stButton > button{
    background-color:#2563eb;
    color:white;
    font-size:18px;
    padding:10px 25px;
    border-radius:8px;
    border:none;
}

div.stButton > button:hover{
    background-color:#1e40af;
}

</style>
""", unsafe_allow_html=True)

# ---------- Load Model ----------
model = joblib.load("models/cost_prediction_model.pkl")
columns = joblib.load("models/model_columns.pkl")

# ---------- Header ----------
st.markdown('<p class="main-title">🩺 Healthcare Insurance Cost Predictor</p>', unsafe_allow_html=True)

st.markdown(
'<p class="subtitle">Predict insurance medical costs using Machine Learning based on patient health data.</p>',
unsafe_allow_html=True
)

st.write("")

# ---------- Sidebar Inputs ----------
st.sidebar.header("Patient Information")

age = st.sidebar.slider("Age",18,65,30)
bmi = st.sidebar.slider("BMI",15.0,50.0,25.0)
children = st.sidebar.slider("Children",0,5,0)

sex = st.sidebar.selectbox("Sex",["male","female"])
smoker = st.sidebar.selectbox("Smoker",["yes","no"])
region = st.sidebar.selectbox(
    "Region",
    ["northeast","northwest","southeast","southwest"]
)

# ---------- Layout ----------
col1,col2 = st.columns(2)

with col1:

    st.markdown("### 📋 Patient Details")

    st.markdown(f"""
    <div class="card">
    <b>Age:</b> {age}<br><br>
    <b>BMI:</b> {bmi}<br><br>
    <b>Children:</b> {children}<br><br>
    <b>Sex:</b> {sex}<br><br>
    <b>Smoker:</b> {smoker}<br><br>
    <b>Region:</b> {region}
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("### 💰 Prediction")

    if st.button("Predict Medical Cost"):

        input_data = pd.DataFrame({
            "age":[age],
            "bmi":[bmi],
            "children":[children],
            "sex":[sex],
            "smoker":[smoker],
            "region":[region]
        })

        input_encoded = pd.get_dummies(input_data)

        input_encoded = input_encoded.reindex(columns=columns,fill_value=0)

        prediction = model.predict(input_encoded)

        st.markdown(f"""
        <div class="result">
        Estimated Cost<br>
        ${prediction[0]:,.2f}
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.markdown("---")

st.markdown(
"<center>Developed by <b>Siva</b> | Healthcare Data Analytics Project</center>",
unsafe_allow_html=True
)