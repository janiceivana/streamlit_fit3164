#######################
# Import libraries
import streamlit as st
import altair as alt
import pandas as pd  
import plotly.express as px
from plotly.subplots import make_subplots
from plotly import graph_objects as go
import numpy as np


#######################
# Page configuration
st.set_page_config(
    page_title="P5: Price Optimization",
    page_icon="💵",
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


#######################
with st.sidebar:
    st.title('💵 P5: Price Optimization')
    
    state_list = list(h1_opti.state_id.unique())[::-1]

    selected_department = st.selectbox('Select a deparment', dept_list)
    selected_data = department_data[selected_department]

    item_list = list(selected_data.item_id.unique())[::-1]

    selected_item = st.selectbox('Select a deparment', item_list)
    selected_data = selected_data[selected_data.item_id == selected_item]

    selected_state = st.selectbox('Select a state', state_list)
    selected_data = selected_data[selected_data.state_id == selected_state]

# #######################
# def vis_optimization_scatter(data):
#     # Create a scatter plot for the original and optimized data with trendline
#     fig = px.scatter(data, x='price', y='revenue', title='Original vs. Optimized Revenue',
#                      labels={'price': 'Price', 'revenue': 'Revenue'},
#                      color_discrete_map={'price': 'blue'},
#                      opacity=0.7)  # Add Ordinary Least Squares trendline
    
#     # Add optimized data as separate markers
#     fig.add_trace(go.Scatter(x=data['opti_price'], y=data['optimized_revenue'],
#                              mode='markers', marker_symbol='x', marker_color='orange',opacity=0.7,
#                              name='Optimized Data'))

#     # Display the plot using Streamlit
#     st.plotly_chart(fig, use_container_width=True)


# def vis_optimization_bar(data):
#     # Create a DataFrame for the bar chart
#     df = pd.DataFrame({
#         'Price Type': ['Original', 'Optimized'],
#         'Price': [data['price'].sum(), data['opti_price'].sum()],
#         'Revenue': [data['revenue'].sum(), data['optimized_revenue'].sum()]
#     })

#     # Create a bar chart for the original and optimized data
#     fig = px.bar(df, x='Price Type', y=['Revenue', 'Price'],
#                  title='Total Original vs. Optimized Revenue and Price',
#                  barmode='group',
#                  labels={'value': 'Total Value', 'variable': 'Metric'})

#     # Display the plot using Streamlit
#     st.plotly_chart(fig, use_container_width=True)


#######################
# Dashboard Main Panel
st.markdown('#### Price Optimization')
# col = st.columns((4, 4), gap='medium')

st.header("Optimal Price")
st.write(selected_data)


# with col[0]:
#     vis_optimization_scatter(selected_data)

# with col[1]:
#     vis_optimization_bar(selected_data)