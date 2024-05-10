#######################
# Import libraries
import streamlit as st
import altair as alt
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

session_state = st.session_state
if 'dataframes' not in session_state:
    session_state.dataframes = {}

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
if st.button("Load Data"):
    for uploaded_file in uploaded_files:
        file_name = uploaded_file.name.replace(".csv", "").replace(" ", "_")
        session_state.dataframes[file_name] = pd.read_csv(uploaded_file)
    st.success("Data loaded successfully!")


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
# Sidebar
with st.sidebar:
    st.title('📊 P5: Price Elasticity Modelling')
    state_list = list(h1_opti.state_id.unique())[::-1]

    selected_department = st.selectbox('Select a deparment', dept_list)
    selected_data = department_data[selected_department]

    item_list = list(selected_data.item_id.unique())[::-1]

    selected_item = st.selectbox('Select an item',  ['Overall'] + item_list)

    selected_state = st.selectbox('Select a state', ['Overall'] + state_list)

    if selected_item != 'Overall':
        selected_data = selected_data[selected_data.item_id == selected_item]

    if selected_state != 'Overall':
        selected_data = selected_data[selected_data.state_id == selected_state]

    
    disc_list = list(h1_opti['discount%'].unique())[::-1]
    selected_disc = st.selectbox('Discount', disc_list)
    selected_data = selected_data[selected_data['discount%'] == selected_disc]




#######################

def vis_elasticity(data):
    
    # Find the maximum value in the list
    max_value = data['price_change'].max()

    # Remove the maximum value from the list
    data = data[data['price_change'] != max_value]

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



    