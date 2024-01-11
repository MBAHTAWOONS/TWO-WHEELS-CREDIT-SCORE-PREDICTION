import streamlit as st
from streamlit_option_menu import option_menu
from all_page.BUSSINESS_UNDERSTANDING import page_bu
from all_page.DATA_FEATURE import page_df
from all_page.Home_page import page_home
from all_page.Visualization_Demo import page_viz
from all_page.Machine_Learning_Demo import page_demo
import gdown
from zipfile import ZipFile
import pickle
import time
import os



# @st.cache_data
# def load_model(modelzip):
#     # output_file = 'model.zip'
#     # print('sedang mengunduh model')
#     # time.sleep(3)
    
#     # gdown.download(f'https://drive.google.com/uc?id={file_id}',output_file,quiet=False)
#     # done = 'done'
#     # print(done)
#     # time.sleep(3)
#     with ZipFile(modelzip, 'r') as file:
#         with file.open('modelRFRegressor.pkl') as model:
#             return pickle.load(model)


def main(model):

    # Menambahkan opsi menu di sidebar
    menu_option = option_menu(
        menu_title= False,
        options= ['HOME','BUSSINESS UNDERSTANDING','DATA & FEATURE', 'VISUALIZATION','MACHINE LEARNING DEMO'],
        icons= ['book','clipboard-data-fill','bar-chart-line-fill','display'],
        menu_icon= 'cast',
        default_index= 0,
        orientation= 'horizontal'
    )
    # Menampilkan halaman berdasarkan opsi menu
    if menu_option == 'HOME':
        page_home()
    elif menu_option == "BUSSINESS UNDERSTANDING":
        page_bu()
    elif menu_option == "DATA & FEATURE":
        page_df()
    elif menu_option == 'VISUALIZATION':
        page_viz()
    elif menu_option == 'MACHINE LEARNING DEMO':
        page_demo(model)

@st.cache_data
def load_model(modelzip):
    with ZipFile(modelzip, 'r') as file:
        with file.open('modelRFRegressor.pkl') as model:
            model = pickle.load(model)
            return model

if __name__ == '__main__':
    
    modelzip = 'model.zip'
    url1 = 'https://drive.google.com/uc?id=15qvS2MpqZL5Vxf3oCd-oJL2K3eH9oWZa'
    url = 'https://drive.google.com/file/d/15qvS2MpqZL5Vxf3oCd-oJL2K3eH9oWZa/view?usp=sharing'
    
    if not os.path.exists(modelzip):
        call = st.text('Loading For Model')
        gdown.download(url,modelzip,quiet=False)  
        call.text("")

    model =  load_model(modelzip)
    st.subheader("TWO WHEELER LOAN CREDIT SCORE PREDICTION",)
    
    st.text(
    """
    Welcome to this try Credit Score for two wheeler loan model !

    **👇 Select any pages from the sidebar** to see some of description and try model!
    """
    )
    main(model)
   




