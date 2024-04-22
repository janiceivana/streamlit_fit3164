#######################
# Import libraries
import streamlit as st
import altair as alt
# import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="P5: Price Optimization",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################
with st.sidebar:
    st.title('📊 P5: Price Iptimization')
    
    # year_list = list(calendar.year.unique())[::-1]
    # state_list = list(h1_df.state_id.unique())[::-1]

    # selected_department = st.selectbox('Select a deparment', dept_list)
    # selected_data = department_data[selected_department]

    # # item_list = list(selected_data.item_id.unique())[::-1]

    # # selected_item= st.selectbox('Select an Item', item_list)
    # # selected_item_level = selected_data[selected_data.item_id == selected_item]

    # selected_state = st.selectbox('Select a state', state_list)
    # selected_data = selected_data[selected_data.state_id == selected_state]

    # selected_year = st.selectbox('Select a year', year_list)
    # selected_data = selected_data[selected_data.year == selected_year]
