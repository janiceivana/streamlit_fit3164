import streamlit as st
import pandas as pd

def main():
    st.title("Data Visualization App")

    session_state = st.session_state
    if 'dataframes' not in session_state:
        session_state.dataframes = {}

    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    if st.button("Load Data"):
        for uploaded_file in uploaded_files:
            file_name = uploaded_file.name.replace(".csv", "").replace(" ", "_")
            session_state.dataframes[file_name] = pd.read_csv(uploaded_file)
        st.success("Data loaded successfully!")

if __name__ == "__main__":
    main()
