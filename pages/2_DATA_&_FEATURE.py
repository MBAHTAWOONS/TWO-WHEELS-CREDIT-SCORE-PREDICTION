import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('INDIA TWO WHEELS LOAN (CREDIT SCORE) DATASET')

DATA_URL = ('dataset/cleaned_dataset.csv')

@st.cache_data
def load_data(nrow):
    ### Simulating Loading a Large Dataset
    data = pd.read_csv(DATA_URL, nrows=nrow)

    chunk_1 = data[0:200]
    chunk_2 = data[200:400]
    chunk_3 = data[400:600]
    chunk_4 = data[600:800]
    chunk_5 = data[800:]

    all_chunk = [chunk_1, chunk_2, chunk_3, chunk_4, chunk_5]

    new_data = pd.DataFrame()
    counter_text = st.text('Processing...')
    for i, chunk in enumerate(all_chunk):
        counter_text.text(f"Processing Part {i+1}/{len(all_chunk)}")
        time.sleep(0.6)
        new_data = pd.concat([new_data,chunk],ignore_index=True)#.reset_index(drop = True)
    del counter_text
    return data.drop(columns='Unnamed: 0')

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Done!')

if st.checkbox('Show DATASET'):
    st.subheader('DATASET')
    st.write(data)

if st.checkbox('DICTIONARY'):
    st.subheader('Dictionary')
    st.markdown(
    """
    - Age:\n
    Type: Category\n
    Description: Represents the age of the applicant. Indicates the applicant's maturity level.\n
    Categories: (<=31,32-44,45-57,58-70)\n
    \n
    - Income:\n
    Type: Integer\n
    Description: The applicant's income, which is critical in assessing their ability to repay the loan.\n
    Range: Multiples of 1000's\n
    \n
    - Credit Score:\n
    Type: Integer\n
    Description: A score quantifying the applicant's creditworthiness based on their credit history.\n
    Range: 300 to 850\n
    \n
    - Number of Existing Loans:\n
    Type: Integer\n
    Description: The number of loans the applicant currently has.\n
    Range: 0 to 10\n
    \n
   - Loan Amount:\n
    Type: Integer\n
    Description: The amount of money the applicant is requesting.\n
    Range: 0 to 150,000\n

    - Loan Tenure:\n
    Type: Integer\n
    Description: The number of months the applicant wants to repay the loan over.\n
    Units: Months (0-120)\n
    \n
    - Existing Customer:\n
    Type: Categorical\n
    Description: Whether the applicant is an existing customer of the finance company.\n
    Categories: Yes, No\n
    \n
    - LTV Ratio:\n
    Type: Float\n
    Description: The loan-to-value ratio, represents the ratio of the loan amount to the appraised value of the asset (typically a house). Higher LTVs can indicate higher risk.\n
    Range: 40% to 95%\n
    \n
    - Property Value:\n
    Type: Categorical\n
    Description: Customer money guarantee or two wheeler value the reason customer loan.\n
    Categories: <=25500, >25500 - 300000, >300000\n
    \n
    - Employment Profile:\n
    Type: Categorical\n
    Description: General employment category of the applicant.\n
    Categories: Salaried, Self-Employed, Freelancer, Unemployed, Student\n
    \n
    """
    )

st.subheader('METRICS')
st.write("""
- MSE, RMSE for same unit scale according to feature
- the model predict customer credit score, for  we to make decision which classification are customer base on CIBIL SCORE or FICO CREDIT SCORE
"""
)
