import streamlit as st
from pycaret.classification import setup, compare_models, pull, save_model, load_model
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
#import ydata_profiling 
import os

if os.path.exists('./train.csv'):
    df=pd.read_csv('./train.csv',index_col=None)

with st.sidebar:
    st.image('https://c8.alamy.com/comp/W4C7FW/machine-learning-thin-line-icon-creative-simple-design-from-artificial-intelligence-icons-collection-outline-machine-learning-icon-for-web-design-W4C7FW.jpg')
    st.title('AutoML Classification')
    choise=st.radio('Navigation',('Upload','EDA','Modelling','Download'))

if choise=='Upload':
    st.title('Upload your data')
    file=st.file_uploader('Upload your data')
    if file:
        df=pd.read_csv(file,index_col=None)
        df.to_csv('train.csv',index=None)
        st.dataframe(df.head())

if choise=='EDA':
    st.title('Exploratory Data Analysis')
    profile_df=df.profile_report()
    st_profile_report(profile_df)

if choise=='Modelling':
    target=st.selectbox('Choose the target column',df.columns)
    if st.button('train model'):
        setup(df,target=target)
        setup_df=pull()
        st.dataframe(setup_df)
        best_model=compare_models()
        compare_df=pull()
        st.dataframe(compare_df)
        save_model(best_model,'best_model')

if choise=='Download':
    with open('best_model.pkl','rb') as f:
        st.download('Download Best Model',f,'best_model.pkl')