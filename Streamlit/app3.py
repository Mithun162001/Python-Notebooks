# READING AND DISPLAYING CONTENTS OF A FILE
import streamlit as st
import pandas as pd

st.title("Reading and displaying the contents of the file")
st.text('''pd.read_csv("C:\\Users\\mithun\\Downloads\\death .csv") ''')
df = pd.read_csv("C:\\Users\\mithun\\Downloads\\death .csv")
st.write(df)    # this writes arguments into the app

st.text ('''df.describe()''')
st.write(df.describe())