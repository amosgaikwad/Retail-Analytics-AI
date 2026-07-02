import streamlit as st

from utils.theme import load_theme

st.set_page_config(
    page_title="Retail Analytics AI",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.main-title{

    font-size:64px;
    font-weight:800;
    margin-bottom:0;

}

.gradient-title{
    font-weight:900;

    background:linear-gradient(
        90deg,
        #38BDF8,
        #3B82F6,
        #8B5CF6,
        #38BDF8
    );

    background-size:300%;

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    animation:titleGradient 10s linear infinite;

}

@keyframes titleGradient{

    0%{
        background-position:0%;
    }

    50%{
        background-position:100%;
    }

    100%{
        background-position:0%;
    }

}

.subtitle{

    font-size:58px;
    color:#B8BCC8;
    margin-top:8px;
    margin-bottom:35px;

}

</style>
""", unsafe_allow_html=True)

load_theme()



st.markdown("""
<div class="main-title">

<span class="gradient-title">Retail Analytics Platform</span>

</div>

<div class="subtitle">

AI Powered Sales Analytics & Revenue Forecasting

</div>
""", unsafe_allow_html=True)

col1,col2,col3,col4=st.columns(4)

with col1:

    st.markdown("""

<div class="metric-card">

<div class="metric-title">

Stores

</div>

<div class="metric-value">

8

</div>

</div>

""",unsafe_allow_html=True)

with col2:

    st.markdown("""

<div class="metric-card">

<div class="metric-title">

Products

</div>

<div class="metric-value">

998

</div>

</div>

""",unsafe_allow_html=True)

with col3:

    st.markdown("""

<div class="metric-card">

<div class="metric-title">

Revenue

</div>

<div class="metric-value">

₹41.13B

</div>

</div>

""",unsafe_allow_html=True)

with col4:

    st.markdown("""

<div class="metric-card">

<div class="metric-title">

Units Sold

</div>

<div class="metric-value">

2M

</div>

</div>

""",unsafe_allow_html=True)

st.markdown("---")

st.header("Project Overview")

st.write("""

This application is an end-to-end Retail Analytics platform developed using:

- Python
- Streamlit
- Plotly
- Pandas
- Scikit-Learn
- Prophet
- Power BI

Navigate through the pages using the sidebar to explore dashboards,
EDA, machine learning, forecasting, and business insights.

""")