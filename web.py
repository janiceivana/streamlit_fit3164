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
    page_title="P5: Pricing Optimization and Analysis Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

#######################
# Load data
calendar = pd.read_csv("calendar.csv")
# evaluation = pd.read_csv("sales_train_evaluation.csv")
# validation = pd.read_csv("sales_train_validation.csv")
# prices = pd.read_csv("sell_prices.csv")
# sample = pd.read_csv("sample_submission.csv")

# hobbies_1 = pd.read_csv('hobbies_1.csv')
# hobbies_2 = pd.read_csv('hobbies_2.csv')
# household_1 = pd.read_csv('household_1.csv')
# household_2 = pd.read_csv('household_2.csv')
# food_1 = pd.read_csv('food_1.csv')
# food_2 = pd.read_csv('food_2.csv')
# food_3 = pd.read_csv('food_3.csv')

h1_df = pd.read_csv('h1_df.csv')
h2_df= pd.read_csv('h2_df.csv')
ho1_df = pd.read_csv('ho1_df.csv')
ho2_df = pd.read_csv('ho2_df.csv')
f1_df = pd.read_csv('f1_df.csv')
f2_df = pd.read_csv('f2_df.csv')
f3_df = pd.read_csv('f3_df.csv')


# calendar = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\calendar.csv')
# f1_df = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\f1_df.csv')
# f2_df = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\f2_df.csv')
# f3_df = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\f3_df.csv')
# h1_df = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\h1_df.csv')
# h2_df = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\h2_df.csv')
# ho1_df = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\ho1_df.csv')
# ho2_df = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\ho2_df.csv')
evaluation = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\sales_train_evaluation.csv')
# validation = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\sales_train_validation.csv')
# sample = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\sample_submission.csv')
# prices = pd.read_csv('D:\\YEAR 3\\Semester 2\\backup\\sell_prices.csv')



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


#######################
# Sidebar
with st.sidebar:
    st.title('🤖 P5: Pricing Optimization and Analysis Dashboard')
    
    year_list = list(calendar.year.unique())[::-1]
    dept_list = list(evaluation.dept_id.unique())[::-1]
    state_list = list(evaluation.state_id.unique())[::-1]

    selected_department = st.selectbox('Select a deparment', dept_list)
    selected_data = department_data[selected_department]

    selected_state = st.selectbox('Select a state', state_list)
    selected_data = selected_data[selected_data.state_id == selected_state]

    selected_year = st.selectbox('Select a year', year_list)
    selected_data = selected_data[selected_data.year == selected_year]

    # df_selected_year_sorted = df_selected_year.sort_values(by="population", ascending=False)

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

    