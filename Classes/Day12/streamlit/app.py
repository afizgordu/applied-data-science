import streamlit as st
import pandas as pd
import plotly.express as px


st.title(' MLOps Streamlit Apps :coffee:')
st.slider('Bir Puan Veriniz',1,10)
st.audio('song.mp3')
menu=['Anasayfa','Makine Ogrenmesi','AI','İletisim']
st.sidebar.selectbox('Menu',menu)
df=pd.read_csv('prog_languages_data.csv')

fig=px.pie(df,values='Sum')
st.plotly_chart(fig)

fig2=px.bar(df,'lang',y='Sum')
st.plotly_chart(fig2)

file=st.file_uploader('Dosya Yukleyiniz')

st.success('Basarili')
st.error('Bir Hata Olustu')
st.warning('Kabul edilmedi')
st.info('Biraz daha lutfen')
st.code("""
    import streamlit as st
    import pandas as pd
    df=pd.read_csv('iris.csv')
    """)

isim=st.text_input('isminizi giriniz', max_chars=50)
#st.video('secret_of_success.mp4')
#st.camera_input('camera')
st.date_input('tarih seciniz')
st.time_input('saat seciniz')
st.text_input('sifrenizi giriniz', type='password')
st.text_area('mesajinizi yaziniz',height=100)
st.number_input('yasinizi giriniz',1,100)
st.radio('Medeni Durumunuz',('Evli','Bekar','Dul'))
#st.selectbox('Bilgidiniz Programlama Dilleri',['C++','Python','Java','Julia','Q#'])
st.multiselect('Bilgidiniz Programlama Dilleri',['C++','Python','Java','Julia','Q#'])
#st.video('http://192.168.182.227/video') iphone da nasıl olduğunu henüz çözemedim
st.image('image_01.jpg')
st.divider()
df=pd.read_csv('iris.csv')
st.table(df)
st.dataframe(df)
st.write(df)
dt.area_chart(df)
