#######################
# Import libraries
import streamlit as st
import altair as alt
# import plotly.express as px

#######################
# Page configuration
st.set_page_config(
    page_title="P5: Price Optimization",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")
