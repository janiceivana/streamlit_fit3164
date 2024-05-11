#######################
# Import libraries
import streamlit as st
import altair as alt
# import plotly.express as px

import pandas as pd  

#######################
# Page configuration
st.set_page_config(
    page_title="P5: Data Summary",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################

st.markdown('#### Upload your data here to get your summarisation!')

def main():
    uploaded_files = st.file_uploader("Choose CSV file(s)", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        if uploaded_file.name.endswith('.csv'):
            file_name = uploaded_file.name.replace(".csv", "").replace(" ", "_")
            bytes_data = pd.read_csv(uploaded_file)
            st.write(f"{file_name} is successfully uploaded")
            st.title(f"Data Summary: {file_name}")
            st.write(bytes_data)

            st.title(f"Statistic Summary: {file_name}")
            st.write(bytes_data.describe())
        else:
            st.write("Please upload only CSV files.")

if __name__ == "__main__":
    main()
