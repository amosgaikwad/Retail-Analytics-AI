import streamlit as st
import pandas as pd
import plotly.express as px
from utils.theme import load_theme

load_theme()


st.set_page_config(
    page_title="EDA",
    page_icon="",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/Retail_Sales_Cleaned.csv")

df = load_data()

st.title("Exploratory Data Analysis")

st.markdown("Analyze trends and distributions in the retail sales dataset.")

# -----------------------------
# FILTERS
# -----------------------------

col1, col2, col3 = st.columns(3)

with col1:
    selected_year = st.selectbox(
        "Select Year",
        sorted(df["Year"].unique())
    )

with col2:
    selected_region = st.selectbox(
        "Select Region",
        ["All"] + sorted(df["Region"].unique().tolist())
    )

with col3:
    selected_category = st.selectbox(
        "Select Category",
        ["All"] + sorted(df["Product_Category"].unique().tolist())
    )

filtered = df[df["Year"] == selected_year]

if selected_region != "All":
    filtered = filtered[
        filtered["Region"] == selected_region
    ]

if selected_category != "All":
    filtered = filtered[
        filtered["Product_Category"] == selected_category
    ]

# -----------------------------
# MONTHLY SALES
# -----------------------------

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

monthly = (
    filtered.groupby("Month_Name")["Revenue"]
    .sum()
    .reindex(month_order)
    .reset_index()
)

fig1 = px.line(
    monthly,
    x="Month_Name",
    y="Revenue",
    markers=True,
    title="Monthly Revenue"
)

# -----------------------------
# REGION SALES
# -----------------------------

region = (
    filtered.groupby("Region")["Revenue"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    region,
    x="Region",
    y="Revenue",
    color="Revenue",
    title="Revenue by Region"
)

left, right = st.columns(2)

with left:
    st.plotly_chart(fig1, use_container_width=True)

with right:
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# CATEGORY SALES
# -----------------------------

category = (
    filtered.groupby("Product_Category")["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Revenue", ascending=False)
)

fig3 = px.bar(
    category,
    x="Revenue",
    y="Product_Category",
    orientation="h",
    color="Revenue",
    title="Revenue by Product Category"
)

# -----------------------------
# BRAND SALES
# -----------------------------

brand = (
    filtered.groupby("Brand")["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

fig4 = px.bar(
    brand,
    x="Brand",
    y="Revenue",
    color="Revenue",
    title="Top 10 Brands"
)

left, right = st.columns(2)

with left:
    st.plotly_chart(fig3, use_container_width=True)

with right:
    st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# PAYMENT MODE
# -----------------------------

payment = (
    filtered.groupby("Payment_Mode")["Revenue"]
    .sum()
    .reset_index()
)

fig5 = px.pie(
    payment,
    names="Payment_Mode",
    values="Revenue",
    title="Payment Mode Distribution",
    hole=0.45
)

# -----------------------------
# CUSTOMER TYPE
# -----------------------------

customer = (
    filtered.groupby("Customer_Type")["Revenue"]
    .sum()
    .reset_index()
)

fig6 = px.pie(
    customer,
    names="Customer_Type",
    values="Revenue",
    title="Customer Type Distribution",
    hole=0.45
)

left, right = st.columns(2)

with left:
    st.plotly_chart(fig5, use_container_width=True)

with right:
    st.plotly_chart(fig6, use_container_width=True)

# -----------------------------
# DISCOUNT VS PROFIT
# -----------------------------

fig7 = px.scatter(
    filtered,
    x="Discount_Amount",
    y="Profit",
    color="Region",
    size="Units_Sold",
    hover_data=["Brand"],
    title="Discount vs Profit"
)

st.plotly_chart(fig7, use_container_width=True)

# -----------------------------
# HOLIDAY ANALYSIS
# -----------------------------

holiday = (
    filtered.groupby("Holiday_Flag")["Revenue"]
    .sum()
    .reset_index()
)

holiday["Holiday_Flag"] = holiday["Holiday_Flag"].replace(
    {
        0: "Non-Holiday",
        1: "Holiday"
    }
)

fig8 = px.bar(
    holiday,
    x="Holiday_Flag",
    y="Revenue",
    color="Holiday_Flag",
    title="Holiday vs Non-Holiday Revenue"
)

st.plotly_chart(fig8, use_container_width=True)

# -----------------------------
# SUMMARY
# -----------------------------

st.subheader("Dataset Summary")

st.write(filtered.describe())

st.subheader("Dataset Preview")

st.dataframe(
    filtered,
    use_container_width=True,
    height=500
)