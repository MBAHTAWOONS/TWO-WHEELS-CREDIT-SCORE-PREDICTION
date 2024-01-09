import streamlit as st
import pandas as pd
import numpy as np

def page_bu():
    image1 = 'dataset/image1.jpg'
    image2 = 'dataset/image2.jpg'

    st.title('BUSSINESS UNDERSTANDING')

    st.image(image1, caption='TWO WHEELS LOAN ', use_column_width=True)
    st.write(
        
        """
        - People behaviour need money to get instant needs. The solution is loan.
        - Financial company need trusted customer
        - They build scores on customer ability called credit score

        """
    )

    if st.checkbox('WHAT PURPOSE TO PREDICT CREDIT SCORE?'):
        st.image(image2, caption='THE PURPOSE', use_column_width=True)

    st.subheader('CREDIT SCORE STANDARD')
    
    text1 = ("""
            Cibil Score (india) source IIFL finance.com

            - Excellent Credit Score -Around 750 and above\n
            These Individuals are likely to have a high likelihood of loan approval and can access loans and credit at favourable terms, including lower interest rates.

            - Good Credit Score - In the range of 700 to 749\n
            This scoring range also signifies a strong credit profile, and individuals within this range are generally considered reliable borrowers by lenders.

            - Fair Credit Score - Ranges from 650 to 699\n
            Individuals with fair credit scores can have access to credit, but they might face slightly higher interest rates or more stringent lending conditions than those with higher scores.

            - Poor Credit Score - Below 650\n
            They may face challenges in obtaining credit or loans as lenders may be more cautious due to the perceived higher credit risk.
            """)
    text2 = ("""
        Fico Credit score (US) mybanktracker.com 

        - Very Bad, 300-580:\n	
        Extremely difficult to obtain traditional loans and line of credit. Advised to use secured credit cards and loans to help rebuild credit.

        - Bad, 580-669:\n
        May be able to qualify for some loans and lines of credit, but the interest rates are likely to be high.

        - Average/Fair, 670-739:\n
        Eligible for many traditional loans, but the interest rates and terms may not be the best.

        - Good, 740-799:\n
        Valuable benefits come in the form of loans and lines of credit with comprehensive perks and low interest rates.

        - Excellent, 800-850:\n
        Qualify easily for most loans and lines of credit with low interest rates and favorable terms."""
            )

    ask = st.selectbox(options=['CIBIL CREDIT SCORE','FICO CREDIT SCORE'],label='Credit Score')
    container = st.container()

    if ask == 'CIBIL CREDIT SCORE':
        with container:
            st.write(text1)
    elif ask == 'FICO CREDIT SCORE':
        with container:
            st.write(text2)
    else:
        st.write ('Select Credit Score Standard')
            # text
                    
#     if st.button('FICO CREDIT SCORE'):
#         st.markdown(





