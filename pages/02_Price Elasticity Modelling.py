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
    state_list = list(h1_opti.state_id.unique())[::-1]

    selected_department = st.selectbox('Select a deparment', dept_list)
    selected_data = department_data[selected_department]

    # item_list = list(selected_data.item_id.unique())[::-1]

    # selected_item= st.selectbox('Select an Item', item_list)
    # selected_item_level = selected_data[selected_data.item_id == selected_item]

    selected_state = st.selectbox('Select a state', ['Overall'] + state_list)

    if selected_state != 'Overall':
        selected_data = selected_data[selected_data.state_id == selected_state]



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



    