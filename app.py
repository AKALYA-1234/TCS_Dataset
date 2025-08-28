import streamlit as st
import pandas as pd

# Title
st.title("🛒 Retail Transactions Dashboard")

# Load CSV
df = pd.read_csv("Retail_Transactions_2000.csv")

# Show first rows
st.subheader("📊 Preview of Data")
st.dataframe(df.head())

# Show basic stats
st.subheader("📈 Dataset Summary")
st.write(df.describe())

# Dropdown to explore columns
col = st.selectbox("🔍 Choose a column to explore", df.columns)

# Show selected column
st.write("You selected:", col)
st.write(df[col].head(20))
