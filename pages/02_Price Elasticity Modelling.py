#######################
# Import libraries
import streamlit as st
import altair as alt
import pandas as pd  
import matplotlib.pylab as plt   
import streamlit as st
from st_files_connection import FilesConnection

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
conn = st.connection('s3', type=FilesConnection)
h1_opti = conn.read("fit3164-ds05/h1_opti.csv", input_format="csv")
h2_opti = conn.read("fit3164-ds05/h2_opti.csv", input_format="csv")
ho1_opti = conn.read("fit3164-ds05/ho1_opti.csv", input_format="csv")
ho2_opti = conn.read("fit3164-ds05/ho2_opti.csv", input_format="csv")
f1_opti = conn.read("fit3164-ds05/f1_opti.csv", input_format="csv")
f2_opti = conn.read("fit3164-ds05/f2_opti.csv", input_format="csv")
f3_opti = conn.read("fit3164-ds05/f3_opti.csv", input_format="csv")

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
    fig, ax = plt.subplots(figsize=(3,3))
    ax.scatter(data['price_change'], data['sale_change'])
    ax.set_title('Scatter Plot of Price Change% vs Sale Change%')
    ax.set_xlabel('Price Change%')
    ax.set_ylabel('Sale Change%')
    ax.grid(True)

    # Display the plot using Streamlit
    st.pyplot(fig)

    elasticity = data['elasticity'].mean()
    st.write(f'The elasticity: {elasticity}')

    if elasticity > 1:
        st.write("Price Elasticity: Elastic Demand Curve")
    elif elasticity < 1:
        st.write("Price Elasticity: Inelastic Demand Curve")
    elif elasticity == 1:
        st.write("Price Elasticity: Unitary elastic Demand Curve")
    elif elasticity == 0:
        st.write("Price Elasticity: Perfectly inelastic Demand Curve")
    else:
        st.write("Price Elasticity: Perfectly elastic Demand Curve")

    st.subheader("Main Findings")
    st.write("The higher discount show an almost straight line going down, where the correlation between price and sales changes becomes more significant, and specifically both price and sales are negative correlated. As price goes down, and demand goes up which will increase the sale, vice versa. Although the higher the discount, and more significant the straight line forms from each point which means the curve become more steep which leads to more inelastic. This does not conclude that the higher the discount the better the sales will be (higher elasticity).")

    st.write("The elasticity is judge by the steepness of the lines from each price and sales change point. In general, price elasticity that is greater than 1 means that the it is elastic demand, and lower than 1 means it is inelastic demand. The steeper the curve is means that it will started to approach inelastic demands, the flatter the curve is the demand will become more perfectly elastic.")

    st.write("As the discount increase from 0% to 10%, we can observe that the price elasticity goes up, where higher price elasticity means that consumers are more responsive to changes in price. Specifically, it indicates that a small change in price results in a relatively large change in quantity demanded, where customers buy more when prices are lower due to discounts.")

    st.write("However, when the discount started to rise up from 10% to 30%, the elasticity goes down by a little. At very high discount levels, the relationship can become more complex. There's a point where further increases in discount may not lead to proportionate increases in quantity demanded. This could be due to various factors such as perceived value, consumer expectations, or even signaling effects where excessively low prices might raise concerns about product quality. ")

    st.write("Finding the optimal discount level and optimal sell price involves balancing price elasticity with profitability. Offering very high discounts might attract more customers, but if the discounts erode profitability too much, it may not be sustainable in the long run.")

#######################

st.markdown('#### Price Elasticity Model')

vis_elasticity(selected_data)



    