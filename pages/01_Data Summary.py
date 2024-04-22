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
h1_df = pd.read_csv('h1_df.csv')
h2_df= pd.read_csv('h2_df.csv')
ho1_df = pd.read_csv('ho1_df.csv')
ho2_df = pd.read_csv('ho2_df.csv')
f1_df = pd.read_csv('f1_df.csv')
f2_df = pd.read_csv('f2_df.csv')
f3_df = pd.read_csv('f3_df.csv')

#######################
dept_list = [ 'FOODS_3', 'FOODS_2', 'FOODS_1' , 'HOUSEHOLD_2', 'HOUSEHOLD_1', 'HOBBIES_2', 'HOBBIES_1']
department_data = {
'FOODS_3': f3_df,
'FOODS_2': f2_df,
'FOODS_1' : f1_df,
'HOUSEHOLD_2' : ho2_df,
'HOUSEHOLD_1': ho1_df, 
'HOBBIES_2': h2_df,
'HOBBIES_1': h1_df

}

# Sidebar
with st.sidebar:
    st.title('📊 P5: Price Elasticity Modelling')

    selected_department = st.selectbox('Select a deparment', dept_list)
    selected_data = department_data[selected_department]


#######################
st.header("Dataframe")
st.write(selected_data)

st.header("Statistic Summary")
st.write(selected_data.describe())