import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from utils.theme import load_theme

load_theme()


# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="",
    layout="wide"
)

# ---------------- LOAD DATA ---------------- #

@st.cache_data
def load_data():
    return pd.read_csv("data/Retail_Sales_Cleaned.csv")

df = load_data()

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("Dashboard Filters")

years = sorted(df["Year"].unique())
regions = sorted(df["Region"].unique())
categories = sorted(df["Product_Category"].unique())
brands = sorted(df["Brand"].unique())
customers = sorted(df["Customer_Type"].unique())
payments = sorted(df["Payment_Mode"].unique())

selected_year = st.sidebar.multiselect(
    "Year",
    years,
    default=years
)

selected_region = st.sidebar.multiselect(
    "Region",
    regions,
    default=regions
)

selected_category = st.sidebar.multiselect(
    "Product Category",
    categories,
    default=categories
)

selected_brand = st.sidebar.multiselect(
    "Brand",
    brands,
    default=brands
)

selected_customer = st.sidebar.multiselect(
    "Customer Type",
    customers,
    default=customers
)

selected_payment = st.sidebar.multiselect(
    "Payment Mode",
    payments,
    default=payments
)

filtered_df = df[
    (df["Year"].isin(selected_year))
    &
    (df["Region"].isin(selected_region))
    &
    (df["Product_Category"].isin(selected_category))
    &
    (df["Brand"].isin(selected_brand))
    &
    (df["Customer_Type"].isin(selected_customer))
    &
    (df["Payment_Mode"].isin(selected_payment))
]

# ---------------- HEADER ---------------- #

st.title("Retail Sales Dashboard")

st.caption(
    f"Last Updated : {datetime.now().strftime('%d %B %Y %I:%M %p')}"
)

st.divider()

# ---------------- KPI CALCULATIONS ---------------- #

total_revenue = filtered_df["Revenue"].sum()
total_sales = filtered_df["Total_Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_units = filtered_df["Units_Sold"].sum()

total_products = filtered_df["Product_ID"].nunique()
total_stores = filtered_df["Store_ID"].nunique()

avg_order = total_revenue / len(filtered_df)

# ---------------- KPI ROW ---------------- #

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    st.metric(
        "Revenue",
        f"₹{total_revenue/1e9:.2f} B"
    )

with c2:
    st.metric(
        "Sales",
        f"₹{total_sales/1e9:.2f} B"
    )

with c3:
    st.metric(
        "Profit",
        f"₹{total_profit/1e9:.2f} B"
    )

with c4:
    st.metric(
        "Units Sold",
        f"{total_units:,.0f}"
    )

with c5:
    st.metric(
        "Stores",
        total_stores
    )

with c6:
    st.metric(
        "Products",
        total_products
    )

st.divider()

# ---------------- MONTH ORDER ---------------- #

month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

filtered_df["Month_Name"] = pd.Categorical(
    filtered_df["Month_Name"],
    categories=month_order,
    ordered=True
)

# ---------------- MONTHLY REVENUE ---------------- #

monthly = (
    filtered_df
    .groupby("Month_Name")["Revenue"]
    .sum()
    .reset_index()
)

monthly = monthly.sort_values("Month_Name")

fig_month = px.line(
    monthly,
    x="Month_Name",
    y="Revenue",
    markers=True,
    title="Monthly Revenue Trend"
)

fig_month.update_layout(
    template="plotly_dark",
    height=450
)

# ---------------- REGION REVENUE ---------------- #

region = (
    filtered_df
    .groupby("Region")["Revenue"]
    .sum()
    .reset_index()
)

fig_region = px.bar(
    region,
    x="Region",
    y="Revenue",
    color="Revenue",
    title="Revenue by Region"
)

fig_region.update_layout(
    template="plotly_dark",
    height=450
)

left, right = st.columns(2)

with left:
    st.plotly_chart(
        fig_month,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig_region,
        use_container_width=True
    )

# ---------------- CATEGORY REVENUE ---------------- #

category = (
    filtered_df
    .groupby("Product_Category")["Revenue"]
    .sum()
    .reset_index()
)

category = category.sort_values(
    "Revenue",
    ascending=False
)

fig_category = px.bar(
    category,
    x="Revenue",
    y="Product_Category",
    orientation="h",
    color="Revenue",
    title="Revenue by Product Category"
)

fig_category.update_layout(
    template="plotly_dark",
    height=500
)

# ---------------- CATEGORY CHART ---------------- #

# (Display the category chart prepared in Part 1)
st.plotly_chart(
    fig_category,
    use_container_width=True
)

# ---------------- BRAND REVENUE ---------------- #

brand = (
    filtered_df
    .groupby("Brand")["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

fig_brand = px.bar(
    brand,
    x="Brand",
    y="Revenue",
    color="Revenue",
    title="Top 10 Brands by Revenue"
)

fig_brand.update_layout(
    template="plotly_dark",
    height=450
)

# ---------------- CUSTOMER TYPE ---------------- #

customer = (
    filtered_df
    .groupby("Customer_Type")["Revenue"]
    .sum()
    .reset_index()
)

fig_customer = px.pie(
    customer,
    names="Customer_Type",
    values="Revenue",
    hole=0.5,
    title="Revenue by Customer Type"
)

fig_customer.update_layout(
    template="plotly_dark",
    height=450
)

left, right = st.columns(2)

with left:
    st.plotly_chart(
        fig_brand,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig_customer,
        use_container_width=True
    )

# ---------------- PAYMENT MODE ---------------- #

payment = (
    filtered_df
    .groupby("Payment_Mode")["Revenue"]
    .sum()
    .reset_index()
)

fig_payment = px.bar(
    payment,
    x="Payment_Mode",
    y="Revenue",
    color="Revenue",
    title="Revenue by Payment Mode"
)

fig_payment.update_layout(
    template="plotly_dark",
    height=450
)

# ---------------- TOP STORES ---------------- #

stores = (
    filtered_df
    .groupby("Store_ID")["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

fig_store = px.bar(
    stores,
    x="Store_ID",
    y="Revenue",
    color="Revenue",
    title="Top 10 Stores"
)

fig_store.update_layout(
    template="plotly_dark",
    height=450
)

left, right = st.columns(2)

with left:
    st.plotly_chart(
        fig_payment,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig_store,
        use_container_width=True
    )

# ---------------- TOP PRODUCTS ---------------- #

products = (
    filtered_df
    .groupby(["Product_ID", "Brand"])["Revenue"]
    .sum()
    .reset_index()
    .sort_values("Revenue", ascending=False)
    .head(10)
)

st.subheader("Top 10 Products")

st.dataframe(
    products,
    use_container_width=True,
    hide_index=True
)

# ---------------- BUSINESS INSIGHTS ---------------- #

top_region = (
    region.sort_values("Revenue", ascending=False)
    .iloc[0]["Region"]
)

top_category = (
    category.sort_values("Revenue", ascending=False)
    .iloc[0]["Product_Category"]
)

top_brand = (
    brand.sort_values("Revenue", ascending=False)
    .iloc[0]["Brand"]
)

st.subheader("Business Insights")

st.success(f"""
• **{top_region}** region generated the highest revenue.

• **{top_category}** is the best performing product category.

• **{top_brand}** is the highest revenue generating brand.

• Total Revenue: **₹{total_revenue:,.2f}**

• Total Profit: **₹{total_profit:,.2f}**

• Average Order Value: **₹{avg_order:,.2f}**
""")

# ---------------- DOWNLOAD FILTERED DATA ---------------- #

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="Filtered_Retail_Data.csv",
    mime="text/csv"
)

# ---------------- DATA TABLE ---------------- #

st.subheader("Filtered Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=500
)

st.markdown("---")

st.caption("Retail Analytics & AI Powered Sales Forecasting System | Built with Streamlit + Plotly")