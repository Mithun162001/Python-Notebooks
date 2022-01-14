# CREATING AND DISPLAYING GRAPHS
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

df = pd.read_csv("C:\\Users\\mithun\\Downloads\\breast-cancer_csv.csv")

plt.figure(figsize=(1,1))
graph1 = sns.displot(df['Class'])
st.pyplot(graph1)

graph2 = px.line(df,x='tumor-size',y='age')
st.plotly_chart(graph2)