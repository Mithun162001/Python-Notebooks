# ADDING A LOGO OR IMAGE TO YOUR APP
import streamlit as st
import pandas as pd
from PIL import Image

st.header("ADDING A LOGO OR IMAGE TO YOUR APP")

image1 = Image.open("C:\\Users\\mithun\\OneDrive\\Pictures\\1_kgmImYxdhX01Yfk5qzkX-A.jpeg")
image2 = Image.open("C:\\Users\\mithun\\OneDrive\\Pictures\\Saved Pictures\\Logo.png")
st.image(image1, width=500)
st.image(image2, width=500)

# creating a button for uploading the files
file_up = st.file_uploader("Upload a file", type='csv')    # Display a file uploader widget. By default, uploaded files are limited to 200MB
st.write(pd.DataFrame(file_up).head())