from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
                
model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])
def get_response(soru):
    response=chat.send_message(soru,stream=True)
    return response

st.header('Gemini Chat Uygulaması')
input=st.text_input("Input",key='input')
submit=st.button('Sor')

if submit:
    response=get_response(input)
    st.header('Cevap')
    for chunk in response:
        st.write(chunk.text)
    st.write(chat.history)

    st.write(response)