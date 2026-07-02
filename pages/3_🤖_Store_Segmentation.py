import streamlit as st
import pandas as pd
import plotly.express as px
from utils.theme import load_theme

load_theme()


st.set_page_config(
    page_title="Store Segmentation",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------

@st.cache_data
def load_data():
    return pd.read_csv("data/Store_Segments.csv")

df = load_data()

st.title("🤖 Store Segmentation using K-Means")

st.markdown("""
This page segments stores based on their sales performance
using the K-Means Clustering algorithm.
""")

# -----------------------------
# SIDEBAR
# -----------------------------

clusters = sorted(df["Cluster"].unique())

selected_cluster = st.sidebar.multiselect(
    "Select Cluster",
    clusters,
    default=clusters
)

filtered = df[df["Cluster"].isin(selected_cluster)]

# -----------------------------
# KPI CARDS
# -----------------------------

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Stores",
    filtered["Store_ID"].nunique()
)

c2.metric(
    "Clusters",
    filtered["Cluster"].nunique()
)

c3.metric(
    "Average Revenue",
    f"₹{filtered['Revenue'].mean():,.0f}"
)

c4.metric(
    "Average Units Sold",
    f"{filtered['Units_Sold'].mean():,.0f}"
)

st.divider()

# -----------------------------
# CLUSTER SCATTER
# -----------------------------

fig1 = px.scatter(
    filtered,
    x="Revenue",
    y="Units_Sold",
    color="Cluster",
    hover_name="Store_ID",
    size="Revenue",
    title="Store Clusters"
)

fig1.update_layout(height=600)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# -----------------------------
# CLUSTER COUNT
# -----------------------------

cluster_count = (
    filtered.groupby("Cluster")
    .size()
    .reset_index(name="Stores")
)

fig2 = px.bar(
    cluster_count,
    x="Cluster",
    y="Stores",
    color="Cluster",
    title="Number of Stores in each Cluster"
)

# -----------------------------
# CLUSTER REVENUE
# -----------------------------

cluster_revenue = (
    filtered.groupby("Cluster")["Revenue"]
    .sum()
    .reset_index()
)

fig3 = px.bar(
    cluster_revenue,
    x="Cluster",
    y="Revenue",
    color="Cluster",
    title="Revenue by Cluster"
)

left,right = st.columns(2)

with left:
    st.plotly_chart(
        fig2,
        use_container_width=True
    )

with right:
    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# -----------------------------
# TOP STORES
# -----------------------------

top = (
    filtered
    .sort_values("Revenue",ascending=False)
    .head(10)
)

st.subheader("Top Performing Stores")

st.dataframe(
    top[
        [
            "Store_ID",
            "Revenue",
            "Units_Sold",
            "Cluster"
        ]
    ],
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# CLUSTER SUMMARY
# -----------------------------

summary = (
    filtered
    .groupby("Cluster")
    .agg(
        Average_Revenue=("Revenue","mean"),
        Average_Units=("Units_Sold","mean"),
        Stores=("Store_ID","count")
    )
    .reset_index()
)

st.subheader("Cluster Summary")

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# AI INSIGHTS
# -----------------------------

best_cluster = (
    summary.sort_values(
        "Average_Revenue",
        ascending=False
    )
    .iloc[0]["Cluster"]
)

best_store = (
    filtered.sort_values(
        "Revenue",
        ascending=False
    )
    .iloc[0]["Store_ID"]
)

st.subheader("AI Business Insights")

st.success(f"""
Cluster **{best_cluster}** has the highest average revenue.

Best performing store is **{best_store}**.

Total stores analyzed: **{filtered['Store_ID'].nunique()}**

K-Means successfully segmented stores based on performance.

These clusters can help management identify
high-performing and low-performing stores for
better decision-making.
""")

# -----------------------------
# DOWNLOAD
# -----------------------------

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Download Clustered Data",
    csv,
    "Store_Segments.csv",
    "text/csv"
)

st.divider()

st.caption(
    "Retail Analytics & AI Powered Sales Forecasting | Machine Learning Dashboard"
)