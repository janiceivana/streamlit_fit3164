import streamlit as st
import pandas as pd
from streamlit.state.session_state import get

def save_dataframes(dataframes):
    session_state = get(email=None, dataframes={})
    session_state.dataframes.update(dataframes)

def main():
    st.title("Data Visualization App")

    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    if st.button("Load Data"):
        dataframes = {}
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name.replace(".csv", "").replace(" ", "_")
            dataframes[file_name] = pd.read_csv(uploaded_file)
        save_dataframes(dataframes)
        st.success("Data loaded successfully!")

if __name__ == "__main__":
    main()
