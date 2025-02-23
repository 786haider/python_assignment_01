# Imports
import streamlit as st
import pandas as pd 
import os
from io import BytesIO

# Setup Our App
st.set_page_config(page_title="First App", layout='wide')
st.title('Hello World')
st.write('Tranform Your Files!')

uploaded_files = st.file_uploader("Upload your files here!")