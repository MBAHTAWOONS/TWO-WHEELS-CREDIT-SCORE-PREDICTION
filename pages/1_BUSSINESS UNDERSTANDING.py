import streamlit as st
import pandas as pd
import numpy as np

image1 = 'dataset/image1.jpg'
image2 = 'dataset/image2.jpg'

st.title('BUSSINESS UNDERSTANDING')

st.image(image1, caption='TWO WHEELS LOAN ', use_column_width=True)
st.markdown(
    """
    - People behaviour need money to get instant needs. The solution is loan.
    - Financial company need trusted customer
    - They build scores on customer ability called credit score

    """
)
st.subheader('CREDIT SCORE STANDARD')

if st.checkbox('CIBIL CREDIT SCORE'):
    st.markdown("""
    cibil score (india) source IIFL finance.com

    Excellent Credit Score - Around 750 and above
    These Individuals are likely to have a high likelihood of loan approval and can access loans and credit at favourable terms, including lower interest rates.

    Good Credit Score - In the range of 700 to 749
    This scoring range also signifies a strong credit profile, and individuals within this range are generally considered reliable borrowers by lenders.

    Fair Credit Score - Ranges from 650 to 699
    Individuals with fair credit scores can have access to credit, but they might face slightly higher interest rates or more stringent lending conditions than those with higher scores.

    Poor Credit Score - Below 650
    They may face challenges in obtaining credit or loans as lenders may be more cautious due to the perceived higher credit risk.
    """)
                
if st.checkbox('FICO CREDIT SCORE'):
    st.markdown("""
    Fico credit score (US) mybanktracker.com 

    300-580	Very Bad:	
    Extremely difficult to obtain traditional loans and line of credit. Advised to use secured credit cards and loans to help rebuild credit.

    580-669	Bad:
    May be able to qualify for some loans and lines of credit, but the interest rates are likely to be high.

    670-739	Average/Fair:
    Eligible for many traditional loans, but the interest rates and terms may not be the best.

    740-799	Good:
    Valuable benefits come in the form of loans and lines of credit with comprehensive perks and low interest rates.

    800-850	Excellent:
    Qualify easily for most loans and lines of credit with low interest rates and favorable terms.""")


if st.checkbox('WHAT PURPOSE TO PREDICT CREDIT SCORE?'):
    st.image(image2, caption='THE PURPOSE', use_column_width=True)
