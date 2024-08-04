import streamlit as st
import pandas as pd

st.title('Formdan veri alma ve CSV dosyasına yazma')
isim=st.text_input('İsminizi Giriniz')
sifre=st.text_input('Şifrenizi Giriniz',type='password')
dob=st.date_input('Doğum Tarihinizi Giriniz')
yas=st.slider('Yaşınızı Seçiniz',1,120)
mesaj=st.text_area('Mesajınızı Giriniz',height=100)
if st.button('Gönder'):
    ndf=pd.DataFrame({'isim':[isim],
                      'sifre':[sifre],
                      'dob':[dob],
                      'mesaj':[mesaj],
                      })
    st.write(ndf)
    ndf.to_csv('katilimformu.csv',index=False)
st.divider()
