import streamlit as st
import pandas as pd
import time
from zipfile import ZipFile




def page_df():
    DATA_PATH1= ('dataset/credit_data.zip')

    DATA_PATH2 = ('dataset/cleaned_dataset.csv')
    imgmul1 = 'dataset/imagemul1.jpg'
    imgmul2 = 'dataset/imagemul2.jpg'
    imgheat = 'dataset/imageheatmap.jpg'


    @st.cache_data
    def load_data(nrow,path):
        ### Simulating Loading a Large Dataset
        if 'zip' in path:
            with ZipFile(path,'r') as zip_file:
                with zip_file.open('credit_data.csv') as csv_file:
                    data = pd.read_csv(csv_file)
        else:
            data = pd.read_csv(path)
        
        chunk_1 = data[0:50000]
        chunk_2 = data[50000:100000]
        chunk_3 = data[100000:150000]
        chunk_4 = data[150000:200000]
        chunk_5 = data[200000:]

        all_chunk = [chunk_1, chunk_2, chunk_3, chunk_4, chunk_5]

        new_data = pd.DataFrame()
        for i, chunk in enumerate(all_chunk):
            # counter_text.text(f"Processing Part {i+1}/{len(all_chunk)}")
            time.sleep(0.6)
            new_data = pd.concat([new_data,chunk],ignore_index=True)#.reset_index(drop = True)
        return data#.drop(columns='Unnamed: 0')

    data_load_state = st.text('Loading data...')
    data = load_data(1000,DATA_PATH1)
    data2 = load_data(1000,DATA_PATH2)
    data_load_state.text('Done!')
    data_load_state.text('')
    del data_load_state
    st.title('INDIA TWO WHEELS LOAN (CREDIT SCORE) DATASET')

    st.subheader('METRICS USED')
    st.write("""
    - MSE, RMSE for same unit scale according to feature
    - the model predict customer credit score, for  we to make decision which classification are customer base on CIBIL SCORE or FICO CREDIT SCORE
    """
    )

    st.subheader('Handling Process')
    if st.checkbox('Duplicate Handling'):
        st.write("""
          - 279.856 entries data 
          - Problem : Duplicated records (All columns subset) = 100.814 rows
          - Handle : Drop into 179.042 rows 
        """
        )
    if st.checkbox('Missing Value'):
        st.write("""
          - Feature : Occupation (11.690 rows/ 6%)
          - Problem : Missing value are based on Unemployed customer (Employments profile)
          - Handle : Change the value to “ None”
        """
        )

        if st.checkbox('Show Missing Value'):
            st.image('dataset/image3.jpg',caption= 'Duplicated Rows Shows',use_column_width=False)

    if st.checkbox('Dropped Feature'):
        st.write("""
          - less contribution to model : Gender, Occupation, State
          - less information : Profile Score (Missing information how to get data Value)
        """
        )
        st.image(imgheat,caption= 'Pearson Correlation Heatmap')

    if st.checkbox('Feature Encoding'):
        if st.button('Multicolinearity'):
            st.image([imgmul1,imgmul2],caption= ['Before','After Handling'],width= 250)
           
            st.write(""" 
            Multicolinearity Handling :
             - Power Transformation 3/2 on Age Feature
             - Drop Credit History Length (because less contribution to model too)
             - Drop Loan ammount (more less contribution to model)
            """
            )


    st.subheader('DATASET')
    if st.button('Show Raw DATASET'):
        st.subheader('RAW DATASET')
        st.write(data)

    if st.button('Show Clean DATASET'):
        st.subheader('Clean DATASET')
        st.write(data2)

    if st.checkbox('DICTIONARY FOR FEATURE USED'):
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

        