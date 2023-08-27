import streamlit as st
import numpy as np
import pandas as pd
import joblib


model = joblib.load('C:/Users/ASUS/OneDrive/Dokumen/PROJECT DATA/VIX/Rakamin - Home Credit/Deploy/logistic_regression_model.joblib')


## MAPPING UNTUK FITUR KATEGORIK
gender_mapping = {
    'Female': 0, 
    'Male': 1
    }

education_mapping = {
    'Lower secondary' : 0,
    'Secondary / secondary special' : 1,
    'Incomplete higher' : 2,
    'Higher education' : 3
    }

contract_mapping = {
    'Cash loans' : 0,
    'Revolving loans' : 1
    }



## CREATING UI DESIGN
st.title("Loan Approval Predictor 💰")
st.subheader("Demographic Information")

NAME = st.text_input('Input name','Anonim')
AGE = st.number_input('Input age',15,100)
CODE_GENDER_CAT = st.radio('Select gender',['Female', 'Male'])
CODE_GENDER = gender_mapping[CODE_GENDER_CAT]
NAME_EDUCATION_TYPE_CAT = st.selectbox('Select last education',['Lower secondary','Secondary / secondary special','Incomplete higher','Higher education','Academic degree'])
NAME_EDUCATION_TYPE = education_mapping[NAME_EDUCATION_TYPE_CAT]
YEAR_EMPLOYED = st.number_input('Length of employment in year, if under 1 year input 0',0,100)
AMT_INCOME_TOTAL = st.number_input('Amount income',0)

st.write("\n")
st.subheader("Type Application and Profil Credit Information")
NAME_CONTRACT_TYPE_CAT = st.radio('Select contract type',['Cash loans', 'Revolving loans'])
NAME_CONTRACT_TYPE = contract_mapping[NAME_CONTRACT_TYPE_CAT]
YEAR_ID_PUBLISH = st.number_input('Year of last card issuance, if under 1 year input 0',0)
AMT_CREDIT = st.slider('Input amount credit',0,5000000)
EXT_SOURCE_1 = st.slider('Input External Source 1',0.0,1.0)
EXT_SOURCE_2 = st.slider('Input External Source 2',0.0,1.0)
EXT_SOURCE_3 = st.slider('Input External Source 3',0.0,1.0)



## MEMBUAT FUNGSI
def predict():
    X = pd.DataFrame(
        {
            'NAME_EDUCATION_TYPE': NAME_EDUCATION_TYPE, 
            'CODE_GENDER': CODE_GENDER,
            'NAME_CONTRACT_TYPE': NAME_CONTRACT_TYPE,
            'EXT_SOURCE_3': EXT_SOURCE_3,
            'EXT_SOURCE_2': EXT_SOURCE_2,
            'YEAR_EMPLOYED': YEAR_EMPLOYED,
            'AGE': AGE,
            'YEAR_ID_PUBLISH': YEAR_ID_PUBLISH,
            'AMT_CREDIT': AMT_CREDIT,
            'AMT_INCOME_TOTAL': AMT_INCOME_TOTAL
        }, index=[0]
    )

    from sklearn.preprocessing import RobustScaler
    scaler = RobustScaler()
    X = scaler.fit_transform(X)
    prediction = model.predict(X)[0]
    return prediction



if st.button("Predict", on_click=predict):
    st.session_state.prediction = None  # Menghapus hasil prediksi sebelumnya
    if all([AGE, CODE_GENDER_CAT, NAME_EDUCATION_TYPE_CAT, AMT_INCOME_TOTAL,
            NAME_CONTRACT_TYPE_CAT, AMT_CREDIT]):
        prediction_result = predict()
        st.session_state.prediction = prediction_result
    else:
        st.warning('Please fill in all the input fields to make a prediction')


if 'prediction' in st.session_state:
    st.write("\n\n")
    st.markdown("Input Values:")
    st.write(f"Age: {AGE}")
    st.write(f"Gender: {CODE_GENDER_CAT}")
    st.write(f"Education: {NAME_EDUCATION_TYPE_CAT}")
    st.write(f"Years Employed: {YEAR_EMPLOYED}")
    st.write(f"Income Total: {AMT_INCOME_TOTAL}")
    st.write(f"Contract Type: {NAME_CONTRACT_TYPE_CAT}")
    st.write(f"Year of Last Card Issuance: {YEAR_ID_PUBLISH}")
    st.write(f"Amount Credit: {AMT_CREDIT}")
    st.write(f"External Source 1: {EXT_SOURCE_1}")
    st.write(f"External Source 2: {EXT_SOURCE_2}")
    st.write(f"External Source 3: {EXT_SOURCE_3}")
    st.write("\n")
    st.markdown("Prediction Result:")
    if st.session_state.prediction == 0:
        st.success('Loan Approval Prediction: Approved')
    else:
        st.error('Loan Approval Prediction: Declined')