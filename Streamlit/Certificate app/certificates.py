# importing libraries
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.title("My Certificates")
st.subheader("By Mithun G")
st.subheader("All certificates and badges received are displayed here")
st.markdown('<p>Have completed the courses and received certificates from various platforms</p>',unsafe_allow_html=True)
text_to_marked = """<p>Certifications and badges received are:</p>
                    <ul>
                    <li>Coursera            - Google Crash Course on Python
                    <li>Coursera            - Google Data Analytics 
                    <li>IBM                 - Machine Learning with Python
                    <li>LinkedIn Learning   - Data Science Essentials Part - 1
                    <li>LinkedIn Learning   - Statistics Foundations(4 parts)
                    <li>Kaggle              - Micro Courses
                    </ul>"""
st.markdown(text_to_marked,unsafe_allow_html=True)
st.text("---------------------------------------------------------------------------------------")
st.text("Certificate Image:")
st.sidebar.header("Select the Certificate platform to view")
selected = st.sidebar.selectbox('Platforms:', ['None','Coursera','IBM','LinkedIn Learning','Kaggle'])

if 'None' in selected:
    st.markdown("<h4>To view the certificates, select one from the slider</h4>",unsafe_allow_html=True)

if 'Coursera' in selected:
    new_select = st.sidebar.selectbox('Course:',['Google Crash Course on Python','Google Data Analytics'])
    if 'Google Crash Course on Python' in new_select:
        st.markdown("<a href='https://github.com/Mithun162001/My-Certificates/blob/main/Coursera/Google%20Crash%20Course%20Certificate.pdf'>GitHub Link</a>",unsafe_allow_html=True)
        st.markdown("<a href='coursera.org/verify/T7F6DP9J67B8'>Credentials</a>",unsafe_allow_html=True)
        google = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Coursera\\google-image.png")
        st.image(google,caption="Crash Course on Python")
    if 'Google Data Analytics' in new_select:
        st.markdown("<a href='https://github.com/Mithun162001/My-Certificates/tree/main/Google%20Data%20Analytics'>GitHub Link</a>",unsafe_allow_html=True)
        st.markdown("<a href='http://coursera.org/verify/87PUUMFWYUQU'>Credentials</a>",unsafe_allow_html=True)
        google_1 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Google Data Analytics\\data analytics image\\0001.jpg")
        google_2 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Google Data Analytics\\data analytics image\\0002.jpg")
        st.image(google_1,caption="Foundations: Data, Data, Everywhere")
        st.image(google_2,caption="Ask Questions to make Data Driven decisions")

if 'IBM' in selected:
    st.markdown("<a href='https://github.com/Mithun162001/My-Certificates/tree/main/IBM%20ML'>GitHub Link</a>",unsafe_allow_html=True)
    st.markdown("<a href='https://courses.cognitiveclass.ai/certificates/7639240d52d34dd98446654a7809f46b'>Credentials</a>",unsafe_allow_html=True)
    ibm = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\IBM ML\\Machine Learning with Python\\ML-image.png")
    st.image(ibm,caption="Machine Learning with Python - IBM")

if 'LinkedIn Learning' in selected:
    new_select_2 = st.sidebar.selectbox('Course:',['Data Science Essentials - Part 1','Statistics Foundations'])
    if 'Data Science Essentials - Part 1' in new_select_2:
        st.markdown("<a href='https://github.com/Mithun162001/My-Certificates/tree/main/Linkedin%20Learning/Data%20Science%20Essential%20Training%20Part%201'>GitHub Link</a>",unsafe_allow_html=True)
        st.markdown("<a href='https://www.linkedin.com/learning/certificates/033d39c77d09348ebb5cc3c489bf5395573f14361f39b9e3a7a374d94cc8871b?trk=share_certificate'>Credentials</a>",unsafe_allow_html=True)
        ll1 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Linkedin Learning\\Data Science Essential Training Part 1\\essential-image.png")
        st.image(ll1,caption="Data Science Essentials - Part 1")
    if 'Statistics Foundations' in new_select_2:
        st.markdown("<a href='https://github.com/Mithun162001/My-Certificates/tree/main/Linkedin%20Learning/Statistics%20Foundations'>GitHub Link</a>",unsafe_allow_html=True)
        st.markdown("<a href='https://www.linkedin.com/learning/certificates/7e4ba218edbcf2c807633e35f81272ccf801ea1883ef3191b13d6311fdf03e98?trk=share_certificate'>Credentials</a>",unsafe_allow_html=True)
        ll2 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Linkedin Learning\\Statistics Foundations\\1.jpg")
        ll3 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Linkedin Learning\\Statistics Foundations\\2.jpg")
        ll4 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Linkedin Learning\\Statistics Foundations\\3.jpg")
        st.image(ll2,caption="Statistics Foundations:1")
        st.image(ll3,caption="Statistics Foundations:2")
        st.image(ll4,caption="Statistics Foundations:3")

if 'Kaggle' in selected:
    st.markdown("<a href='https://github.com/Mithun162001/My-Certificates/tree/main/Kaggle'>GitHub Link</a>",unsafe_allow_html=True)
    st.markdown("<a href='https://www.kaggle.com/learn/certification/mithun162001/python'>Credentials</a>",unsafe_allow_html=True)
    kaggle_1 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Kaggle\\Kaggle Python Certficate.png")
    kaggle_2 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Kaggle\\Kaggle Pandas Certficate.png")
    kaggle_3 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Kaggle\\Mithun G - Data Visualization.png")
    kaggle_4 = Image.open("C:\\Users\\mithun\\OneDrive\\Desktop\\My-Certificates\\Kaggle\\Kaggle - Intro to Machine Learning.png")

    st.image(kaggle_1, caption="Python")
    st.image(kaggle_2, caption='Pandas')
    st.image(kaggle_3, caption='Data visualization')
    st.image(kaggle_4, caption='Intro to Machine Learning')

