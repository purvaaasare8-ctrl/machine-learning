import streamlit as st
import pandas as pd
import joblib

model = joblib.load("loan_model.pkl")

st.set_page_config(page_title="Loan Approval Prediction", layout="wide")

st.title("Loan Approval Prediction System")
st.write("Fill all the details below to predict loan approval.")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 70, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Marital Status", ["No", "Yes"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["No", "Yes"])
    income = st.number_input("Annual Income", 10000, 1000000, 50000)

with col2:
    co_income = st.number_input("Co-Applicant Income", 0, 500000, 0)
    loan = st.number_input("Loan Amount", 50000, 1000000, 200000)
    term = st.selectbox("Loan Amount Term (Months)", [60,120,180,240,300,360])
    credit = st.number_input("Credit Score", 300, 900, 650)
    property_area = st.selectbox("Property Area", ["Urban", "Semi Urban", "Rural"])

st.markdown("---")

st.subheader("Applicant Information")

st.write(f"**Age:** {age}")
st.write(f"**Gender:** {gender}")
st.write(f"**Marital Status:** {married}")
st.write(f"**Education:** {education}")
st.write(f"**Self Employed:** {self_employed}")
st.write(f"**Annual Income:** ₹{income:,}")
st.write(f"**Co-Applicant Income:** ₹{co_income:,}")
st.write(f"**Loan Amount:** ₹{loan:,}")
st.write(f"**Loan Term:** {term} Months")
st.write(f"**Credit Score:** {credit}")
st.write(f"**Property Area:** {property_area}")

if st.button("Predict Loan Approval"):

    data = pd.DataFrame([[income, credit, loan]],
                        columns=["Income", "CreditScore", "LoanAmount"])

    result = model.predict(data)

    st.markdown("---")

    if result[0] == 1:
        st.success("✅ Congratulations! Loan is likely to be Approved.")
        st.balloons()
    else:
        st.error("❌ Loan is likely to be Rejected.")

st.markdown("---")
st.info("This prediction is generated using a Machine Learning model and is for educational purposes only.")