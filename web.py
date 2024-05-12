#######################
# Import libraries
import streamlit as st


st.header("Welcome to FIT3164_DS05 Webpage!")

st.subheader("Introduction")
st.write("Our Retail Product Pricing Optimization and Analytics project involved leveraging the M5 Kaggle dataset to develop optimal pricing strategies. The optimization was studied by analyzing historical sales data, product attributes, and pricing information. By employing data analytics, price elasticity modeling, and visualization techniques, we seek to determine the optimal pricing point for various products and explore the impact of pricing on sales performance.  ")

st.subheader("Getting Started")
st.write("Start of by uploading your data to get your pricing analysis and strategies!")

st.subheader("Meet our team members!")
col1, col2, col3 = st.columns([1,1,1])
# Using 'with' notation:
with col1:
    st.write("Janice Ivana - 32959796")
    st.image("IMG-20240108-WA0049.jpg")

with col2:
    st.write("Jiayi Wang (Wendy) - 31513638")
    st.image("Image (1).jpeg")
    
with col3:
    st.write("Nguyen Pham (Chris) - 30750814")
    st.image("pfp.jpeg")



