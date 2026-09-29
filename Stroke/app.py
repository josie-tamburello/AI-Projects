import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Stroke Risk Predictor", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #f0f5ff; }
    .stButton>button { background-color: #1f77b4; color: white; }
    h1 { color: #0047ab; }
    </style>
    """, unsafe_allow_html=True)

try:
    model = joblib.load('tuned_logistic_pipeline.pkl')
    MODEL_LOADED = True
except Exception as e:
    st.error(f"Error loading model: {e}")
    MODEL_LOADED = False

st.title("Stroke Risk Prediction")

if MODEL_LOADED:
    st.sidebar.header("Patient Information")

    # Input collection
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    age = st.sidebar.slider("Age", 0, 100, 40)
    hypertension = st.sidebar.selectbox("Hypertension", ["No", "Yes"])
    heart_disease = st.sidebar.selectbox("Heart Disease", ["No", "Yes"])
    ever_married = st.sidebar.selectbox("Ever Married", ["Yes", "No"])
    work_type = st.sidebar.selectbox(
        "Work Type", 
        ["Private", "Self-employed", "not_working", "Govt_job"]
    )
    residence_type = st.sidebar.selectbox("Residence Type", ["Urban", "Rural"])
    avg_glucose_level = st.sidebar.slider(
        "Average Glucose Level (mg/dL)", 
        50.0, 300.0, 100.0
    )
    bmi = st.sidebar.slider("BMI", 10.0, 60.0, 25.0)
    smoking_status = st.sidebar.selectbox(
        "Smoking Status", 
        ["never_smoked", "formerly_smoked", "smokes", "Unknown"]
    )

    if st.button("Predict"):
        # Create input DataFrame
        input_df = pd.DataFrame([{
            'gender': gender,
            'age': age,
            'hypertension': 1 if hypertension == "Yes" else 0,
            'heart_disease': 1 if heart_disease == "Yes" else 0,
            'ever_married': ever_married,
            'work_type': work_type,
            'Residence_type': residence_type,
            'avg_glucose_level': avg_glucose_level,
            'bmi': bmi,
            'smoking_status': smoking_status
        }])
        try:
            with st.spinner("Calculating risk..."):
                prob = model.predict_proba(input_df)[0][1]
                pred = model.predict(input_df)[0]

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Prediction Result")
                if pred == 1:
                    st.error(f"High Risk of Stroke\nProbability: {prob:.2%}")
                else:
                    st.success(f"Low Risk of Stroke\nProbability: {prob:.2%}")

            with col2:
                st.subheader("Risk Factors")
                risk_factors = []
                if age > 65:
                    risk_factors.append("Age above 65")
                if hypertension == "Yes":
                    risk_factors.append("Has hypertension")
                if heart_disease == "Yes":
                    risk_factors.append("Has heart disease")
                if avg_glucose_level > 200:
                    risk_factors.append("High glucose level")
                if bmi > 30:
                    risk_factors.append("BMI indicates obesity")
                
                if risk_factors:
                    for factor in risk_factors:
                        st.warning(f"• {factor}")
                else:
                    st.info("No major risk factors identified")

            st.markdown("---")
            st.subheader("Feature Importance Analysis")
            
            try:
                categorical_features = ['gender', 'ever_married', 'work_type', 
                                     'Residence_type', 'smoking_status']
                numerical_features = ['age', 'hypertension', 'heart_disease', 
                                    'avg_glucose_level', 'bmi']
                
        
                cat_features = model.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(categorical_features)
                feature_names = np.concatenate([numerical_features, cat_features])
                
                coefficients = model.named_steps['classifier'].coef_[0]
                
                importance_df = pd.DataFrame({
                    'Feature': feature_names,
                    'Importance': np.abs(coefficients)
                })
                importance_df = importance_df.sort_values('Importance', ascending=True)
                

                fig, ax = plt.subplots(figsize=(10, 6))
                plt.barh(importance_df['Feature'], importance_df['Importance'])
                plt.title('Feature Importance')
                plt.xlabel('Absolute Coefficient Value')
                
                # Customize plot appearance
                plt.grid(alpha=0.3)
                plt.tight_layout()
                
                # Display plot in Streamlit
                st.pyplot(fig)
                
            except Exception as e:
                st.error(f"Error generating feature importance plot: {e}")

        except Exception as e:
            st.error(f"Error making prediction: {e}")
else:
    st.warning("Please ensure the model file 'tuned_logistic_pipeline.pkl' is available.")