import streamlit as st
from transformers import pipeline

st.title('허깅페이스 데모')
text = st.text_input("분석 위한 텍스트")
model = pipeline('sentiment-analysis')

if text :
  result = model(text)
  st.write('감정 : ', result[0]['label'])
  st.write('점수 : ', result[0]['score'])
