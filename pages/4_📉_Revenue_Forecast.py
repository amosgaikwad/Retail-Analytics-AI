import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.theme import load_theme

load_theme()


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Revenue Forecast",
    page_icon="",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/Revenue_Forecast.csv")
    df["ds"] = pd.to_datetime(df["ds"])
    return df

df = load_data()

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("AI Revenue Forecast Dashboard")

st.markdown("""
Forecast generated using **Facebook Prophet**.

This dashboard predicts future revenue trends and helps
businesses make data-driven decisions.
""")

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("Forecast Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    df["ds"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["ds"].max()
)

filtered = df[
    (df["ds"] >= pd.to_datetime(start_date))
    &
    (df["ds"] <= pd.to_datetime(end_date))
]

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

forecast_sum = filtered["yhat"].sum()

forecast_avg = filtered["yhat"].mean()

forecast_max = filtered["yhat"].max()

forecast_min = filtered["yhat"].min()

growth = (
    (
        filtered["yhat"].iloc[-1]
        -
        filtered["yhat"].iloc[0]
    )
    /
    filtered["yhat"].iloc[0]
) * 100

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric(
    "Forecast Days",
    len(filtered)
)

c2.metric(
    "Total Forecast",
    f"₹{forecast_sum/1e9:.2f} B"
)

c3.metric(
    "Average Revenue",
    f"₹{forecast_avg:,.0f}"
)

c4.metric(
    "Highest Forecast",
    f"₹{forecast_max:,.0f}"
)

c5.metric(
    "Growth",
    f"{growth:.2f}%"
)

st.divider()

# ---------------------------------------------------
# FORECAST CHART
# ---------------------------------------------------

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=filtered["ds"],
        y=filtered["yhat"],
        mode="lines",
        name="Forecast",
        line=dict(
            color="#00BFFF",
            width=3
        )
    )
)

fig.add_trace(
    go.Scatter(
        x=filtered["ds"],
        y=filtered["yhat_upper"],
        line=dict(width=0),
        showlegend=False
    )
)

fig.add_trace(
    go.Scatter(
        x=filtered["ds"],
        y=filtered["yhat_lower"],
        fill="tonexty",
        fillcolor="rgba(0,191,255,0.2)",
        line=dict(width=0),
        name="Confidence Interval"
    )
)

fig.update_layout(
    title="Revenue Forecast",
    template="plotly_dark",
    height=600,
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ---------------------------------------------------
# MONTHLY FORECAST
# ---------------------------------------------------

filtered["Month"] = filtered["ds"].dt.month_name()

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

monthly = (
    filtered
    .groupby("Month")["yhat"]
    .sum()
    .reindex(month_order)
    .reset_index()
)

fig2 = px.bar(
    monthly,
    x="Month",
    y="yhat",
    color="yhat",
    title="Monthly Forecast Revenue",
    color_continuous_scale="Blues"
)

fig2.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# ---------------------------------------------------
# WEEKLY TREND
# ---------------------------------------------------

filtered["Weekday"] = filtered["ds"].dt.day_name()

week_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

weekly = (
    filtered
    .groupby("Weekday")["yhat"]
    .mean()
    .reindex(week_order)
    .reset_index()
)

fig3 = px.line(
    weekly,
    x="Weekday",
    y="yhat",
    markers=True,
    title="Average Forecast by Weekday"
)

fig3.update_layout(
    template="plotly_dark",
    height=450
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# ---------------------------------------------------
# 7 DAY MOVING AVERAGE
# ---------------------------------------------------

filtered = filtered.copy()

filtered["Moving_Average"] = (
    filtered["yhat"]
    .rolling(window=7)
    .mean()
)

fig4 = go.Figure()

fig4.add_trace(
    go.Scatter(
        x=filtered["ds"],
        y=filtered["yhat"],
        mode="lines",
        name="Forecast"
    )
)

fig4.add_trace(
    go.Scatter(
        x=filtered["ds"],
        y=filtered["Moving_Average"],
        mode="lines",
        name="7-Day Moving Average",
        line=dict(
            color="orange",
            width=3
        )
    )
)

fig4.update_layout(
    title="Forecast vs Moving Average",
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

# ---------------------------------------------------
# HIGHEST & LOWEST FORECAST
# ---------------------------------------------------

highest = filtered.loc[
    filtered["yhat"].idxmax()
]

lowest = filtered.loc[
    filtered["yhat"].idxmin()
]

left, right = st.columns(2)

with left:

    st.info(f"""
### Highest Predicted Revenue

**Date:** {highest['ds'].strftime('%d %B %Y')}

**Revenue:** ₹{highest['yhat']:,.2f}
""")

with right:

    st.warning(f"""
### Lowest Predicted Revenue

**Date:** {lowest['ds'].strftime('%d %B %Y')}

**Revenue:** ₹{lowest['yhat']:,.2f}
""")

st.divider()

# ---------------------------------------------------
# FORECAST TABLE
# ---------------------------------------------------

forecast_table = filtered[
    [
        "ds",
        "yhat",
        "yhat_lower",
        "yhat_upper"
    ]
].copy()

forecast_table.columns = [
    "Date",
    "Forecast",
    "Lower Bound",
    "Upper Bound"
]

st.subheader("Forecast Table")

st.dataframe(
    forecast_table,
    use_container_width=True,
    hide_index=True,
    height=400
)

st.divider()

# ---------------------------------------------------
# FORECAST STATISTICS
# ---------------------------------------------------

st.subheader("Forecast Statistics")

stats1, stats2, stats3 = st.columns(3)

stats1.metric(
    "Maximum Forecast",
    f"₹{filtered['yhat'].max():,.2f}"
)

stats2.metric(
    "Minimum Forecast",
    f"₹{filtered['yhat'].min():,.2f}"
)

stats3.metric(
    "Standard Deviation",
    f"₹{filtered['yhat'].std():,.2f}"
)

st.divider()

# ---------------------------------------------------
# AI BUSINESS INSIGHTS
# ---------------------------------------------------

trend = "Increasing"

if growth < 0:
    trend = "Decreasing"

confidence = (
    (
        filtered["yhat_upper"] -
        filtered["yhat_lower"]
    ).mean()
)

st.subheader("🤖 AI Forecast Insights")

st.success(f"""

### Forecast Summary

• Overall forecast trend is **{trend}**

• Predicted Growth : **{growth:.2f}%**

• Highest Revenue : **₹{highest['yhat']:,.2f}**

• Lowest Revenue : **₹{lowest['yhat']:,.2f}**

• Average Forecast Revenue : **₹{forecast_avg:,.2f}**

• Average Confidence Interval Width : **₹{confidence:,.2f}**

### Business Recommendations

 Increase inventory before high-demand periods.

 Schedule marketing campaigns during forecasted peak revenue.

 Allocate staff according to expected customer demand.

 Monitor revenue dips and investigate possible causes.

""")

st.divider()

# ---------------------------------------------------
# DOWNLOAD BUTTON
# ---------------------------------------------------

csv = forecast_table.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇ Download Forecast CSV",
    data=csv,
    file_name="Revenue_Forecast.csv",
    mime="text/csv"
)

st.divider()

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.caption(
    """
Retail Analytics & AI Powered Sales Forecasting System

"""
)