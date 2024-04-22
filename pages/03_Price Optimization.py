#######################
# Import libraries
import streamlit as st
import altair as alt
import pandas as pd  
import plotly.express as px
from plotly.subplots import make_subplots
from plotly import graph_objects as go


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
    # Create a scatter plot for the original and optimized data
    fig = px.scatter(data, x=data['price'], y=data['revenue'], title='Original vs. Optimized Revenue',
                     labels={'x': 'Price', 'y': 'Revenue'},
                     color_discrete_map={'price': 'blue'},
                     opacity=0.7,
                     symbol_map={'price': 'circle'})

    # Add optimized data as separate markers
    fig.add_trace(go.Scatter(x=data['opti_price'], y=data['optimized_revenue'],
                             mode='markers', marker_symbol='x', marker_color='red',
                             name='Optimized Data'))

    # Display the plot using Streamlit
    st.plotly_chart(fig, use_container_width=True)


def vis_optimization_bar(data):
    # Create a DataFrame for the bar chart
    df = pd.DataFrame({
        'Price Type': ['Original', 'Optimized'],
        'Price': [data['price'].mean(), data['opti_price'].mean()],
        'Revenue': [data['revenue'].mean(), data['optimized_revenue'].mean()]
    })

    # Create a bar chart for the original and optimized data
    fig = px.bar(df, x='Price Type', y=['Revenue', 'Price'],
                 title='Average Original vs. Optimized Revenue and Price',
                 barmode='group',
                 labels={'value': 'Average Value', 'variable': 'Metric'})

    # Display the plot using Streamlit
    st.plotly_chart(fig, use_container_width=True)


#######################
# Dashboard Main Panel
col = st.columns((4, 4), gap='medium')

with col[0]:
    st.markdown('#### Price Optimization')
    
    vis_optimization_scatter(selected_data)
    vis_optimization_bar(selected_data)