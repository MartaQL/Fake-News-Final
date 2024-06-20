import streamlit as st

st.title('Fake News Detector')

st.subheader('Detecting fake news with machine learning')

text = st.text_area('Enter the news to check if it is fake or not')

button = st.button('Analyze')

if button:
    st.success('The news are real!')