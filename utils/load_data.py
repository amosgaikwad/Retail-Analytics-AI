import pandas as pd
import streamlit as st


@st.cache_data
def load_sales_data():
    """
    Load the cleaned retail sales dataset.
    """
    df = pd.read_csv("data/Retail_Sales_Cleaned.csv")
    return df


@st.cache_data
def load_store_segments():
    """
    Load K-Means clustered store dataset.
    """
    df = pd.read_csv("data/Store_Segments.csv")
    return df


@st.cache_data
def load_forecast():
    """
    Load Prophet forecast dataset.
    """
    df = pd.read_csv("data/Revenue_Forecast.csv")
    return df