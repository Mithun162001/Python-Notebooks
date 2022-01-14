# SUBMIT BUTTON, SELECTION BUTTON AND SLIDERS
from cProfile import label
import pandas as pd
import streamlit as st

# select box/ drop down menu
specalization = st.selectbox("Select the Specalization", ["Data Science","Artifical Intelligence","Software Engineering"])
st.write("You have choosen the specalization: ", specalization)

with st.form(key='my_form'):
    text_input = st.text_input(label="Enter your name")
    submit_button = st.form_submit_button(label='Submit')

with st.form(key='new_form'):
    st.selectbox("Select the algorithm",['Logistic','Linear','SVM'], key=1)
    st.multiselect("Select the algorithm",['Logistic','Linear','SVM'], key=1)
    st.slider(label="Select the knowledge level", min_value=0,max_value=10, key=2)
    submit_button = st.form_submit_button(label='Submit')
    st.success("Submitted succesfully")
