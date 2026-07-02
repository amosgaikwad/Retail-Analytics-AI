import streamlit as st
import os
from utils.theme import load_theme

load_theme()


st.set_page_config(
    page_title="Project Report",
    page_icon="",
    layout="wide"
)

st.title("Project Documentation")

st.markdown("""
## Retail Analytics & AI Powered Sales Forecasting System

This project is an end-to-end Data Analytics and Machine Learning solution
developed using Python, Streamlit, Plotly, Scikit-Learn, Prophet and Power BI.

The application analyzes retail sales, identifies trends,
segments stores using Machine Learning and forecasts future revenue.
""")

st.divider()

# -----------------------------------------------------
# PROJECT DETAILS
# -----------------------------------------------------

st.subheader("Project Information")

col1, col2 = st.columns(2)

with col1:
    st.info("""
### Domain

Retail Analytics

### Project Type

End-to-End Data Analytics Project

### Duration

3 Months

### Tools

Python

Pandas

NumPy

Plotly

Power BI

Streamlit

Scikit-Learn

Facebook Prophet
""")

with col2:
    st.success("""
### Features

✔ Interactive Dashboard

✔ Sales Analytics

✔ Exploratory Data Analysis

✔ Store Segmentation

✔ Revenue Forecasting

✔ Machine Learning

✔ Download Reports

✔ Interactive Visualizations
""")

st.divider()

# -----------------------------------------------------
# TECH STACK
# -----------------------------------------------------

st.subheader("Technology Stack")

tech = [
    "Python",
    "Pandas",
    "NumPy",
    "Plotly",
    "Matplotlib",
    "Scikit-Learn",
    "Facebook Prophet",
    "Power BI",
    "Streamlit",
    "Git",
    "GitHub"
]

st.write(tech)

st.divider()

# -----------------------------------------------------
# DOWNLOAD SECTION
# -----------------------------------------------------

st.subheader("⬇ Downloads")

report_path = "report/Retail_Analytics_Report.pdf"

dataset_path = "data/Retail_Sales_Cleaned.csv"

forecast_path = "data/Revenue_Forecast.csv"

cluster_path = "data/Store_Segments.csv"

col1,col2 = st.columns(2)

with col1:

    if os.path.exists(report_path):

        with open(report_path,"rb") as file:

            st.download_button(
                " Download Project Report",
                file,
                "Retail_Analytics_Report.pdf"
            )

    else:

        st.warning("Project report not found.")

    if os.path.exists(dataset_path):

        with open(dataset_path,"rb") as file:

            st.download_button(
                "Download Dataset",
                file,
                "Retail_Sales_Cleaned.csv"
            )

with col2:

    if os.path.exists(forecast_path):

        with open(forecast_path,"rb") as file:

            st.download_button(
                "Download Forecast",
                file,
                "Revenue_Forecast.csv"
            )

    if os.path.exists(cluster_path):

        with open(cluster_path,"rb") as file:

            st.download_button(
                "Download Store Segments",
                file,
                "Store_Segments.csv"
            )

st.divider()

# -----------------------------------------------------
# PROJECT WORKFLOW
# -----------------------------------------------------

st.subheader("Project Workflow")

st.markdown("""
1. Data Collection

2. Data Cleaning

3. Exploratory Data Analysis

4. Feature Engineering

5. Machine Learning

6. Time Series Forecasting

7. Dashboard Development

8. Deployment
""")

st.divider()

# -----------------------------------------------------
# PROJECT OBJECTIVES
# -----------------------------------------------------

st.subheader("Objectives")

st.markdown("""
- Analyze sales performance.

- Discover business insights.

- Segment stores using Machine Learning.

- Forecast future revenue.

- Build an interactive analytics platform.

- Assist business decision making.
""")

st.divider()

# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------

st.success("Thank you for exploring the Retail Analytics Project!")

st.caption(
"""
Retail Analytics & AI Powered Sales Forecasting

Developed using Streamlit, Plotly, Scikit-Learn and Facebook Prophet.
"""
)