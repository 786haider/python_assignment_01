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
        st.write("🔎 Preveiw the head of the Dataframe")
        st.dataframe(df.head())
        
        #Options for data cleaning
        st.subheader("🧹 Data cleaning options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(f"Remove Duplicate from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write(f"Duplicate removed from {file.name}")
                    
            with col2:
             if st.button(f"Fill missing values for {file.name}"):
                 numeric_cols = df.select_dtypes(include=['number']).columns
                 df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                 st.write(f"Missing values have been filled!")
             
        # Chose specific column to keep or convert   
        st.subheader("📌 Select columns to convert")  
        columns =st.multiselect(f"Chose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]
        
        
        # Create some visualizations
        st.subheader("📉Data Visualizations")
        if st.checkbox(f"Show visualization for {file.name}") :
            st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])
            
            # Convert the file --> CSV to Excel
            st.subheader('⏳ Conversion Option')
            conversion_type = st.radio(f"Convert {file.name} to:", ['CSV', 'Excel'], key=file.name)
            if st.button(f"Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == 'CSV':
                    df.to_csv(buffer, index=False)
                    file.name = file.name.replace(file_ext,".csv")
                    mime_type = "text/csv"
                    
                elif conversion_type == 'Excel':
                    df.to_excel(buffer, index=False)
                    file.name = file.name.replace(file_ext,".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)     
                
                # Download button
            st.download_button(
                    label=f"⬇️ Downloaded {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file.name,
                    mime=mime_type
                )
                
            st.success("🎉 All files processed!")
                               