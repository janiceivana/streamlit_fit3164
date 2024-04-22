#######################
# Import libraries
import streamlit as st
import altair as alt
# import plotly.express as px

import pandas as pd  
import matplotlib.pylab as plt   

#######################
# Page configuration
st.set_page_config(
    page_title="P5: Price Elasticity Modelling",
    page_icon="📊",
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

# st.write('Hello World')
# name = st.text_input('Whats your name?')
# st.write(sample)

# if st.button("Click Me"):
#     st.write(f"Hello `{name}`")

dept_list = [ 'FOODS_3', 'FOODS_2', 'FOODS_1' , 'HOUSEHOLD_2', 'HOUSEHOLD_1', 'HOBBIES_2', 'HOBBIES_1']
#######################
# Sidebar
with st.sidebar:
    st.title('📊 P5: Price Elasticity Modelling')
    
    year_list = list(calendar.year.unique())[::-1]
    year_list.append("Overall")
    st.write(year_list)
    state_list = list(h1_df.state_id.unique())[::-1]

    selected_department = st.selectbox('Select a deparment', dept_list)
    selected_data = department_data[selected_department]

    # item_list = list(selected_data.item_id.unique())[::-1]

    # selected_item= st.selectbox('Select an Item', item_list)
    # selected_item_level = selected_data[selected_data.item_id == selected_item]

    selected_state = st.selectbox('Select a state', state_list)
    selected_data = selected_data[selected_data.state_id == selected_state]

    selected_year = st.selectbox('Select a year', year_list)
    if isinstance(selected_year, pd.Timestamp):
        selected_data = selected_data[selected_data.year == selected_year]


    # color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
    # selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

#######################

def vis_elasticity(data):
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data['price_change'], data['sale_change'])
    ax.set_title('Scatter Plot of Price Change% vs Sale Change%')
    ax.set_xlabel('Price Change%')
    ax.set_ylabel('Sale Change%')
    ax.grid(True)

    # Display the plot using Streamlit
    st.pyplot(fig)


#######################
# Dashboard Main Panel
col = st.columns((4, 4), gap='medium')

with col[0]:
    st.markdown('#### Price Elasticity Model')
    
    vis_elasticity(selected_data)



    