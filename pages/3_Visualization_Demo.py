import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

st.title('VISUALIZATION')

st.markdown(
    """
    ##### FEATURE TO CREDIT SCORE
    """
)

df = pd.read_csv('dataset/cleaned_dataset.csv')
df['Existing Customer'] = np.where(df['Existing Customer'] == 1, 'Yes', 'No')

@st.cache_data
def show_data():
    st.write(df)

if st.checkbox('Show Data!'):
    show_data()


st.subheader('BOXPLOT EXISTING CUSTOMER TO CREDIT SCORE')
st.markdown('###### Customer who was Existing Customer of Loan Product Have More Credit Score')

@st.cache_data
def ex_customer():
    fig2 = px.box(df,x='Existing Customer', y= 'Credit Score', color= 'Existing Customer')
    st.plotly_chart(fig2,theme='streamlit')

ex_customer()

st.subheader('SCATTERPLOT NUMBER OF EXISTING LOAN TO CREDIT SCORE')
st.markdown('###### More High Number of Existing Loan More High Credit Score')

unique_n_loan = ['All']
unique_n_loan.extend(int(i) for i in sorted(df['Number of Existing Loans'].unique()))

n_loan = st.selectbox('Select Number:', unique_n_loan)

@st.cache_data
def Visual_scatter(n_loan):
    if n_loan == 'All':
        fig = px.scatter(df, x = 'Number of Existing Loans', y = 'Credit Score')
        st.plotly_chart(fig, theme = 'streamlit')
    else:
        df_select = df[df['Number of Existing Loans'] <= n_loan]
        fig = px.scatter(df_select, x = 'Number of Existing Loans', y = 'Credit Score')
        st.plotly_chart(fig, theme = 'streamlit')        

Visual_scatter(n_loan)


# st.subheader('Price Boxplot for Apartments in Jakarta')

# @st.cache_data
# def visualize_boxplot():
#     tab1, tab2 = st.tabs(['By Number of Bedrooms', 'By Region'])
#     with tab1:
#         fig = px.box(df, x = 'No_Rooms', y='AnnualPrice')
#         st.plotly_chart(fig, theme = 'streamlit', use_container_width = True)
#     with tab2:
#         fig = px.box(df, x = 'Region', y = 'AnnualPrice')
#         st.plotly_chart(fig, theme = 'streamlit', use_container_width = True)

# visualize_boxplot()
