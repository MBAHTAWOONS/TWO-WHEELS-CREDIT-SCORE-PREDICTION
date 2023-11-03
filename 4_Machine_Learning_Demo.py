import streamlit as st
import pandas as pd
import numpy as np

import pickle
from xgboost import XGBRegressor

st.title('Demo: Machine Learning')

st.markdown(""" This model base on limited Data Source and information""")

# @st.cache_data
def load_model():
    return pickle.load(open('model/regression_xgb.pkl', 'rb'))
# @st.cache_data
def load_sc():
    return pickle.load(open('model/standarscaler.pkl','rb'))

model = load_model()
SC = load_sc()

st.subheader("Fill in your Customer Application and predict the credit score!")

Age = st.number_input('How old are you?', 18, 70,value=18)
# Age = st.radio('Number of Rooms: ', ['18-31 tahun', '32-44 tahun', '45-57 tahun', '>57 tahun'])
if Age <= 31:
    Age = 2 
elif (Age > 31) & (Age <= 44):
    Age = 0
elif (Age > 44) &(Age <= 57):
    Age = 1
elif Age >=  57 :
    Age = 3


Existing = st.radio('Are you an Existing Customer in this Finance Company?', ['Yes', 'No'])
if Existing == 'Yes':
    Existing  = 1
else:
    Existing = 0

n_loan = st.slider("Do you Have another loan Exist? How much? (fill zero if you don't have any)", 0, 10)
n_loan = n_loan ** 2

income = st.number_input("How much your income in a month?",9000,209000,step=1000)
loan_amount = st.number_input("How much loan amount requested?", 5000, 150000,step= 1000)
loan_tenure = st.number_input('How long you want to repay the debt? (month)', 0, 120,step=6)
property_value = st.number_input('How much your money guarantee? (property value or the price of two wheeler you want to buy with this loan)', 15000, 350000,step=1000)
Employment_profile = st.selectbox('What is your profile?',['Salaried','Self-Employed','Freelancer','Student','Unemployed'])
LTV_ratio = (loan_amount/property_value)*100

your_customer = pd.DataFrame({
    'Age':[Age],
    'Income':[income],
    'Number of Existing Loans' :[n_loan],
    'Loan Amount':[loan_amount],
    'Loan Tenure':[loan_tenure],
    'Existing Customer':[Existing],
    'LTV Ratio':[LTV_ratio],
    '25500:300000':[0],
    'Above300000':[0],
    'Below25500':[0],
    'Freelancer':[0],
    'Salaried':[0],
    'Self-Employed':[0],
    'Student':[0],
    'Unemployed':[0],
})

your_customer[Employment_profile] = 1
pv= 0
if property_value <= 25500:
    pv = 'Below25500'
elif (property_value > 25500) & (property_value <= 300000):
    pv = '25500:300000'
elif property_value > 300000:
    pv = 'Above300000'

your_customer[pv] = 1

col = your_customer.columns
notcontinous = ['Existing Customer'] + list(col[7::]) 
cc = [i for i in col if i not in notcontinous]

if st.button('Calculate Credit Score!'):
    scaled = SC.transform(your_customer[cc])
    scaled = pd.DataFrame(scaled)
    scaled.columns = cc
    your_customer = pd.concat([scaled,your_customer[notcontinous]],axis=1)
    your_credit = model.predict(your_customer)
    your_credit = your_credit[0]
    your_credit = np.round(your_credit,0)

    #CIBIL CREDIT SCORE:
    if your_credit < 650:
        st.success(f"### Your Credit Score is predicted at: {your_credit}\nCIBIL SCORE : Poor Credit Score")
        
    elif (your_credit >= 650) & (your_credit <= 699):
        st.success(f"### Your Credit Score is predicted at: {your_credit}\nCIBIL SCORE : Fair Credit Score")
        
    elif (your_credit >= 700) & (your_credit <= 749):
        st.success(f"### Your Credit Score is predicted at: {your_credit}\nCIBIL SCORE : Good Credit Score")

    elif your_credit >= 750:
        st.success(f"### Your Credit Score is predicted at: {your_credit}\nCIBIL SCORE : Excelent Credit Score")

    #FICO CREDIT SCORE
    if (your_credit >= 300) & (your_credit <= 579):
        st.success(f"\nFICO SCORE : Very Bad Credit Score")
        
    elif (your_credit >= 580) & (your_credit <= 669):
        st.success(f"\nFICO SCORE : Bad Credit Score")
        
    elif (your_credit >= 670) & (your_credit <= 739):
        st.success(f"\nFICO SCORE : Average/Fair Credit Score")

    elif (your_credit >= 740) & (your_credit >= 799):
        st.success(f"\nFICO SCORE : Good Credit Score")

    elif your_credit >= 800:
        st.success(f"\nFICO SCORE : Excelent Credit Score")


