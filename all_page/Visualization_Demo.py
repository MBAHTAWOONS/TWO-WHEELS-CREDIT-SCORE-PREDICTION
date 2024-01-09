import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots

def page_viz():
    select = option_menu(
        menu_title= False,
        options= ['High Influence Feature','Exploratory Data Analyst'],
        menu_icon='cast',
        orientation='horizontal'
    )
     #cleaned data
    df = pd.read_csv('dataset/cleaned_dataset.csv')
    df['Existing Customer'] = np.where(df['Existing Customer'] == 15, 'Yes', 'No')
    df2 = pd.read_csv('dataset/credit_data.csv')
    if select == 'High Influence Feature':
        #title
        st.title('FEATURE TO CREDIT SCORE')

        @st.cache_data
        def show_data():
            st.write(df)

        if st.checkbox('Show Data!'):
            show_data()

        #feature vs credit score 
        
        st.subheader('BOXPLOT EXISTING CUSTOMER TO CREDIT SCORE')
        st.markdown('###### Customer who was Existing Customer of Loan Product Have More Credit Score')

        def ex_customer():
            fig1 = px.box(df,x='Existing Customer', y= 'Credit Score', color= 'Existing Customer')
            st.plotly_chart(fig1,theme='streamlit')

        ex_customer()


        st.subheader('SCATTERPLOT NUMBER OF EXISTING LOAN TO CREDIT SCORE')
        st.markdown('###### More High Number of Existing Loan More High Credit Score')

        # unique_n_loan = ['All']
        # unique_n_loan.extend(int(i) for i in sorted(df['Number of Existing Loans'].unique()))

        # n_loan = st.selectbox('Select Number:', unique_n_loan)

        @st.cache_data
        def Visual_scatter():
            fig2 = px.scatter(df, x = 'Number of Existing Loans', y = 'Credit Score')
            st.plotly_chart(fig2, theme = 'streamlit')
        
        Visual_scatter()

        st.subheader('Recomendation')
        st.markdown(
            """- Financial Company Existing Customer has a big influence on Credit scoring so Financial company can do marketing plan for their Existing customer because it’s more trusted. 
- The number of existing loans has a big influence on Credit Score, Maybe it’s because Customer who has more loans can establish and manage their money for loan payment. 
- Model can predict two wheels loan CREDIT SCORE with RMSE 10.21, so for the predict about credit score mistakes is around 10.21 unit score for the scale 350 -850 credit score.
"""
        )
        
    if select == 'Exploratory Data Analyst':
        #existing customer
        st.subheader('Existing Customer')

        @st.cache_data
        def visual1():
            fig3 = px.box(x=df['Existing Customer'],y=df['LTV Ratio'])
            fig4 = px.box(x=df['Existing Customer'],y=df['Number of Existing Loans'])
            fig = make_subplots(rows=1,cols=2)
            fig.add_trace(fig3['data'][0],row=1,col=1,)
            fig.add_trace(fig4['data'][0],row=1,col=2)
            fig.update_xaxes(title_text='Existing Customer', row=1, col=1)
            fig.update_xaxes(title_text='Existing Customer', row=1, col=2)
            fig.update_yaxes(title_text='LTV Ratio', row=1, col=1)
            fig.update_yaxes(title_text='Number of Existing Loans', row=1, col=2)
            st.plotly_chart(fig,theme='streamlit')
        visual1()

        st.markdown('''Existing Customer have high influence to target feature, otherelse\n
        - Existing customers,mostly in LTV ratio with below 75 % priority below 65 %
    - Existing customers, mostly customers that have a number of existing loans more than 7 up to 9 count
    ''')

        st.subheader('Number of Existing Loans')

        unique_n_loan = ['All']
        unique_n_loan.extend(int(i) for i in sorted(df2['Number of Existing Loans'].unique()))
            
        n_loan = st.selectbox('Select Number:', unique_n_loan)

        @st.cache_data
        def visual2(n_loan):
            if n_loan == 'All':    
                fig5 = px.scatter(df2,x=df2['Number of Existing Loans'],y=df2['Loan Tenure'])
                st.plotly_chart(fig5)
            else:
                ds = df2[df2['Number of Existing Loans'] <= n_loan]
                fig5 = px.scatter(ds,x= ds['Number of Existing Loans'],y=ds['Loan Tenure'])
                st.plotly_chart(fig5)
        visual2(n_loan)

        st.markdown('''Customer that Have Number of Existing Loans more than 6 have loan tenure more than 60 months (5 years)
    ''')

        st.subheader('Recomendation')

        st.markdown(
            """- Financial Company Existing Customer has a big influence on Credit scoring so Financial company can do marketing plan for their Existing customer because it’s more trusted.
- For new customer we can focus on customer that have good credit score and LTV ratio below than 75 % priority 65 % 
- The number of existing loans has a big influence on Credit Score, Maybe it’s because Customer who has more loans can establish and manage their money for loan payment. So Finance company can do marketing loans for people who have another loan but with a limit of around 10 loan count.
- Financial Companies can do marketing with loan tenure more than 5 years, that have information are customers who have number of existing loans 7-9 count.
- Model can predict two wheels loan CREDIT SCORE with RMSE 10.21, so for the predict about credit score mistakes is around 10.21 unit score for the scale 350 -850 credit score.
"""
        )
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
