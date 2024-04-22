#######################
# Import libraries
import streamlit as st
import altair as alt
import pandas as pd  
import matplotlib.pylab as plt
from scipy.stats import linregress
# import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="P5: Forecasting",
    page_icon="📈",
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
    st.title('📈 P5: Forecasting')

    state_list = list(h1_df.state_id.unique())[::-1]

    selected_department = st.selectbox('Select a deparment', dept_list)
    selected_data = department_data[selected_department]



yearly_predicted_revenue = selected_data.groupby('year')['optimized_revenue'].sum()
yearly_optimal_price = selected_data.groupby('year')['opti_price'].mean()

# Linear regression for predicted revenue
slope_revenue, intercept_revenue, _, _, _ = linregress(yearly_predicted_revenue.index, yearly_predicted_revenue)
line_revenue = slope_revenue * yearly_predicted_revenue.index + intercept_revenue

# Linear regression for optimal price
slope_price, intercept_price, _, _, _ = linregress(yearly_optimal_price.index, yearly_optimal_price)
line_price = slope_price * yearly_optimal_price.index + intercept_price

# Make predictions for the next year
next_year = max(yearly_predicted_revenue.index) + 1
future_revenue_prediction = slope_revenue * next_year + intercept_revenue
future_price_prediction = slope_price * next_year + intercept_price

# Print the predictions
st.write(f"Department {selected_department} - Future Revenue Prediction for Year {next_year}: {future_revenue_prediction}")
st.write(f"Department {selected_department} - Future Price Prediction for Year {next_year}: {future_price_prediction}")

# Plot the linear regression and predictions
plt.figure(figsize=(16, 6))

# Plot linear regression for predicted revenue
plt.subplot(1, 2, 1)
plt.plot(yearly_predicted_revenue.index, line_revenue, label='Linear Regression')
plt.scatter(yearly_predicted_revenue.index, yearly_predicted_revenue, marker='x', label='Predicted Revenue')
plt.plot([next_year], [future_revenue_prediction], marker='o', markersize=8, label='Next Year Prediction')
plt.xlabel('Year')
plt.ylabel('Revenue')
plt.title(f'Linear Regression for Predicted Revenue Over Time - Department {selected_department}')
plt.legend()
plt.grid(True)

# Plot linear regression for optimal price
plt.subplot(1, 2, 2)
plt.plot(yearly_optimal_price.index, line_price, label='Linear Regression')
plt.scatter(yearly_optimal_price.index, yearly_optimal_price, marker='x', label='Optimal Price')
plt.plot([next_year], [future_price_prediction], marker='o', markersize=8, label='Next Year Prediction')
plt.xlabel('Year')
plt.ylabel('Price')
plt.title(f'Linear Regression for Optimal Price Over Time - Department {selected_department}')
plt.legend()
plt.grid(True)

plt.tight_layout()
st.pyplot(plt)

