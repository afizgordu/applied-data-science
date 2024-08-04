import streamlit as st
import pandas as pd
import pickle

st.title('Yazılı ve Sözlü Sınava Göre Maaş Tahmin Eden Model :moneybag:')
model=pickle.load(open('maas.pkl','rb'))
tecrube=st.number_input('Tecrube',1,10)
yazili=st.number_input('Yazili',1,10)
mulakat=st.number_input('Mulakat',1,10)
if st.button('Tahmin Et'):
    tahmin=model.predict([[tecrube,yazili,mulakat]])
    tahmin=round(tahmin[0][0],2)
    st.success(f'Maaş Tahmini:{tahmin}')