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
h1_df = pd.read_csv('h1_df.csv')
h2_df= pd.read_csv('h2_df.csv')
ho1_df = pd.read_csv('ho1_df.csv')
ho2_df = pd.read_csv('ho2_df.csv')
f1_df = pd.read_csv('f1_df.csv')
f2_df = pd.read_csv('f2_df.csv')
f3_df = pd.read_csv('f3_df.csv')


department_data = {
    'FOODS_3': f3_df,
    'FOODS_2': f2_df,
    'FOODS_1' : f1_df,
    'HOUSEHOLD_2' : ho2_df,
    'HOUSEHOLD_1': ho1_df, 
    'HOBBIES_2': h2_df,
    'HOBBIES_1': h1_df

}

dept_list = [ 'FOODS_3', 'FOODS_2', 'FOODS_1' , 'HOUSEHOLD_2', 'HOUSEHOLD_1', 'HOBBIES_2', 'HOBBIES_1']


#######################
with st.sidebar:
    st.title('💵 P5: Price Optimization')
    
    year_list = list(calendar.year.unique())[::-1]
    state_list = list(h1_df.state_id.unique())[::-1]

    selected_department = st.selectbox('Select a deparment', dept_list)
    selected_data = department_data[selected_department]

    selected_state = st.selectbox('Select a state', state_list)
    selected_data = selected_data[selected_data.state_id == selected_state]

    selected_year = st.selectbox('Select a year', year_list)
    selected_data = selected_data[selected_data.year == selected_year]

#######################
def vis_optimization_scatter(data):
    # Create a scatter plot for the original and optimized data with trendline
    fig = px.scatter(data, x='price', y='revenue', title='Original vs. Optimized Revenue',
                     labels={'price': 'Price', 'revenue': 'Revenue'},
                     color_discrete_map={'price': 'blue'},
                     opacity=0.7,
                     trendline='ols')  # Add Ordinary Least Squares trendline
    
    # Add optimized data as separate markers
    fig.add_trace(go.Scatter(x=data['opti_price'], y=data['optimized_revenue'],
                             mode='markers', marker_symbol='x', marker_color='red',
                             name='Optimized Data'))

    # Display the plot using Streamlit
    st.plotly_chart(fig, use_container_width=True)


def vis_optimization_scatter_OLS(data):
    # Calculate OLS trendlines
    z_orig = np.polyfit(data['price'], data['revenue'], 1)
    p_orig = np.poly1d(z_orig)
    trend_orig = p_orig(data['price'])

    z_opti = np.polyfit(data['opti_price'], data['optimized_revenue'], 1)
    p_opti = np.poly1d(z_opti)
    trend_opti = p_opti(data['opti_price'])

    # Create a scatter plot for the original and optimized data with trendlines
    fig = px.scatter(data, x='price', y='revenue', title='Original vs. Optimized Revenue',
                     labels={'price': 'Price', 'revenue': 'Revenue'},
                     color_discrete_map={'price': 'blue'},
                     opacity=0.7,
                     trendline='ols')  # Add Ordinary Least Squares trendline
    
    # Add optimized data as separate markers with trendline
    fig.add_trace(go.Scatter(x=data['opti_price'], y=data['optimized_revenue'],
                             mode='markers', marker_symbol='x', marker_color='red',
                             name='Optimized Data'))
    fig.add_trace(go.Scatter(x=data['price'], y=trend_orig, mode='lines', 
                             line=dict(color='blue', width=2, dash='dash'), name='Original Trend'))
    fig.add_trace(go.Scatter(x=data['opti_price'], y=trend_opti, mode='lines', 
                             line=dict(color='red', width=2, dash='dash'), name='Optimized Trend'))

    # Display the plot using Streamlit
    st.plotly_chart(fig, use_container_width=True)



def vis_optimization_bar(data):
    # Create a DataFrame for the bar chart
    df = pd.DataFrame({
        'Price Type': ['Original', 'Optimized'],
        'Price': [data['price'].sum(), data['opti_price'].sum()],
        'Revenue': [data['revenue'].sum(), data['optimized_revenue'].sum()]
    })

    # Create a bar chart for the original and optimized data
    fig = px.bar(df, x='Price Type', y=['Revenue', 'Price'],
                 title='Total Original vs. Optimized Revenue and Price',
                 barmode='group',
                 labels={'value': 'Total Value', 'variable': 'Metric'})

    # Display the plot using Streamlit
    st.plotly_chart(fig, use_container_width=True)


#######################
# Dashboard Main Panel
col = st.columns((4, 4), gap='medium')

with col[0]:
    st.markdown('#### Price Optimization')
    
    vis_optimization_scatter(selected_data)
    vis_optimization_bar(selected_data)
    vis_optimization_scatter_OLS(selected_data)