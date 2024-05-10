import streamlit as st
import pandas as pd

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
count = 0
for uploaded_file in uploaded_files:
    file_name = uploaded_file.name.replace(".csv", "").replace(" ", "_")
    exec(f"{file_name} = pd.read_csv(uploaded_file)")
    st.write("filename:", file_name)
    count = count + 1

if len(uploaded_files) == count:
    st.write("Hey, All the files are successfully uploaded")