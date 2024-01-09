import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor

 

def page_demo(model):
    st.title('Demo: Machine Learning')

    st.markdown(""" This model base on limited Data Source and information""")


    @st.cache_data
    def load_encoder():
        return pickle.load(open('model/encoder.pkl','rb'))
    
    encoder = load_encoder()

    st.subheader("Fill in your Customer Application and predict the credit score!")

    
    Age = st.number_input('How old are you?', 18, 70,value=18)

    Existing = st.radio('Are you an Existing Customer in this Finance Company?', ['Yes', 'No'])

    n_loan = st.slider("Do you Have another loan Exist? How much? (fill zero if you don't have any)", 0, 10)

    income = st.number_input("How much your income in a month?",9000,209000,step=1000)
    
    loan_tenure = st.number_input('How long you want to repay the debt? (month)', 0, 120,step=6)
    if loan_tenure <= 60:
        loan_tenure = 5
    else: 
        loan_tenure = 10
    
    loan_amount = st.number_input('How much your loan request? How much your prefer to loan? (Rupees)', 5000, 150000,step=1000)
    property_value = st.number_input('How much your money guarantee? (property value or the price of two wheeler you want to buy with this loan in rupees)', 15000, 350000,step=1000)
    
    Employment_profile = st.selectbox('What is your profile?',['Salaried','Self-Employed','Freelancer','Student','Unemployed'])
    
    

    if st.button('Calculate Credit Score!'):
        Age = Age ** 3/2

        LTV_ratio = (loan_amount/property_value)*100
        
        if Existing == 'Yes':
            Existing  = 15
        else:
            Existing = 30

        your_customer = pd.DataFrame({
            'Age':[Age],
            'Income':[income],
            'Number of Existing Loans' :[n_loan],
            'Loan Tenure':[loan_tenure],
            'Existing Customer':[Existing],
            'LTV Ratio':[LTV_ratio],
            'Employment Profile': [Employment_profile],
            'Property Value':[property_value],
        })

        your_customer['Employment Profile'] = encoder.transform(your_customer['Employment Profile'])
        
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
            st.success(f"\nFICO CREDIT SCORE : Very Bad Credit Score")
            
        elif (your_credit >= 580) & (your_credit <= 669):
            st.success(f"\nFICO CREDIT SCORE : Bad Credit Score")
            
        elif (your_credit >= 670) & (your_credit <= 739):
            st.success(f"\nFICO CREDIT SCORE : Average/Fair Credit Score")

        elif (your_credit >= 740) & (your_credit >= 799):
            st.success(f"\nFICO CREDIT SCORE : Good Credit Score")

        elif your_credit >= 800:
            st.success(f"\nFICO CREDIT SCORE : Excelent Credit Score")


