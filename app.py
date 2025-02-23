# Imports
import streamlit as st
import pandas as pd 
import os
from io import BytesIO

# Setup Our App
st.set_page_config(page_title="First App", layout='wide')
st.title('Hello World 👋')
st.write('Tranform Your Files!')

uploaded_files = st.file_uploader("Upload your files here! 👇", type=["csv","xlsx"] , accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue
        
        # Display info about the file
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size /1024} ")
        
        # Show 5 rows of our df
        st.write("Preveiw the head of the Dataframe")
        st.dataframe(df.head())
        
        #Options for data cleaning
        st.subheader("Data cleaning options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 =st.coumn(2)
            
            with col1:
                if st.button(f"Remove Duplicate from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write(f"Duplicate removed from {file.name}")
                    
         with col2:
             if st.button(f"Fill missing values for {file.name}")
             