import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("esg_project_outputs/esg_processed_with_weights.csv")

st.title("ESG Investment Dashboard")
st.write("Portfolio Optimization & Company Clusters")


industry_filter = st.sidebar.multiselect("Industry", df["Industry"].unique())
country_filter = st.sidebar.multiselect("Country", df["Country"].unique())
cluster_filter = st.sidebar.multiselect("Cluster", df["cluster"].unique())

filtered = df.copy()
if industry_filter: filtered = filtered[filtered["Industry"].isin(industry_filter)]
if country_filter: filtered = filtered[filtered["Country"].isin(country_filter)]
if cluster_filter: filtered = filtered[filtered["cluster"].isin(cluster_filter)]

st.subheader("Top Companies by Optimized Weight")
st.dataframe(filtered.sort_values("opt_weight", ascending=False)[["Company","Ticker","Industry","Country","ROE","WACC","opt_weight"]].head(20))


st.subheader("Cluster Overview")
fig, ax = plt.subplots(figsize=(8,6))
scatter = ax.scatter(filtered["ROA"], filtered["ROE"], c=filtered["cluster"], cmap='tab10', s=50)
ax.set_xlabel("ROA")
ax.set_ylabel("ROE")
ax.set_title("Clusters by ROA vs ROE")
legend1 = ax.legend(*scatter.legend_elements(), title="Cluster")
ax.add_artist(legend1)
st.pyplot(fig)


st.subheader("Return/Risk Score Distribution")
fig2, ax2 = plt.subplots(figsize=(8,4))
ax2.hist(filtered["Return_Risk_Score"], bins=20, color='skyblue')
ax2.set_xlabel("Return/Risk Score")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)
