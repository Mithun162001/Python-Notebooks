# importing the streamlit library
import streamlit as st 

# to print hello world in streamlit
st.text("Hello World")

# trying to change the font size and font style using markdown
original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Hello World</p>'
st.markdown(original_title, unsafe_allow_html=True)

original_title = '<p style="font-family:sans-serif; color:Red; font-size: 40 px;">Hello World</p>'
st.markdown(original_title, unsafe_allow_html=True)

# trying other things in markdown
my_markdown = '''<h1>Hello World</h1>
                <ul>
                <li>Python
                <li>java
                </ul>'''
st.markdown(my_markdown, unsafe_allow_html=True)