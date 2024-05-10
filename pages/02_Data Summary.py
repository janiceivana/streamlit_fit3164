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

# Load data
calendar = pd.read_csv("calendar.csv")
h1_opti = pd.read_csv('h1_opti.csv')
h2_opti= pd.read_csv('h2_opti.csv')
ho1_opti = pd.read_csv('ho1_opti.csv')
ho2_opti = pd.read_csv('ho2_opti.csv')
f1_opti = pd.read_csv('f1_opti.csv')
f2_opti = pd.read_csv('f2_opti.csv')
f3_opti = pd.read_csv('f3_opti.csv')

#######################
dept_list = [ 'FOODS_3', 'FOODS_2', 'FOODS_1' , 'HOUSEHOLD_2', 'HOUSEHOLD_1', 'HOBBIES_2', 'HOBBIES_1']
department_data = {
'FOODS_3': f3_opti,
'FOODS_2': f2_opti,
'FOODS_1' : f1_opti,
'HOUSEHOLD_2' : ho2_opti,
'HOUSEHOLD_1': ho1_opti, 
'HOBBIES_2': h2_opti,
'HOBBIES_1': h1_opti

}

# Sidebar
with st.sidebar:
    st.title('📋 P5: Data Summary')

    selected_department = st.selectbox('Select a deparment', dept_list)
    selected_data = department_data[selected_department]


#######################
st.header("Dataframe")
st.write(selected_data)

st.header("Statistic Summary")
st.write(selected_data.describe())



def main():
    st.title("Data Summary")

    # Access uploaded files from session state
    session_state = st.session_state
    if 'csv_files' in session_state:
        for name, data in session_state.csv_files.items():
            st.write(f"DataFrame Name: {name}")
            name = pd.read_csv(data)
            st.write(name)

if __name__ == "__main__":
    main()
