# importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

# Title and Markdown
st.title("AN EXAMPLE EDA APP")
st.markdown(''' <h3>This is an example of how to do EDA in streamlit app</h3>''',unsafe_allow_html=True)

# File upload
file_up = st.file_uploader("Upload a file", type='csv')

# Check if the file uploaded is successfull or not, if successfull then read the file
if file_up is not None:
    st.success("File uploaded successfully")
    df = pd.read_csv(file_up)
    obj = []
    int_float = []
    for i in df.columns:
        clas = df[i].dtypes
        if clas == 'object':
            obj.append(i)
        else:
            int_float.append(i)

# Remove null values and replace them with mean and median value
    with st.form(key='my_form'):
        with st.sidebar:
            st.sidebar.header("To remove NULL values press below button")
            submit_button = st.form_submit_button(label="Remove NULL")

    if submit_button:
        for i in df.columns:
            clas = df[i].dtypes
            if clas == 'object':
                df[i].fillna(df[i].mode()[0], inplace = True)
            else:
                df[i].fillna(df[i].mean(), inplace = True)

# finding the number of null values in each column
    ls = []
    for i in df.columns:
        dd = sum(pd.isnull(df[i]))
        ls.append(dd)

# if number of null values are zero it will display some text else it will plot bar plot by each column
    if max(ls) == 0:
        st.write("Total no. of NULL values: ", str(max(ls)))
    else:
        st.write("Bar plot to know the number of NULL values in each column")
        st.write("Total number of null values: ", str(max(ls)))
        fig = px.bar(x=df.columns, y=ls,labels={'x':"Column Names",'y':"No. of Null values"})
        st.plotly_chart(fig)

# Frequency Plot
    st.sidebar.header("Select variable")
    selected = st.sidebar.selectbox('Object variables',obj)
    st.write("Bar Plot to know the frequency of each category")
    frequency = df[selected].value_counts()

    fig2 = px.bar(frequency, x=frequency.index,y=selected,labels={'x':selected, 'y':'count'})
    st.plotly_chart(fig2)

# Correlation chart
    st.sidebar.header("Select variable")
    selected2 = st.sidebar.multiselect("Variables",int_float)
    st.write("Scatter plot for correlation")
    if len(selected2) == 2:
        fig3 = px.scatter(df,x=selected2[0], y=selected2[1])
        st.plotly_chart(fig3)
    else: 
        st.write("Select any 2 variables only")