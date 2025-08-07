import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(page_title="Titanic EDA Dashboard", layout="wide")

# Title
st.title("🚢 Titanic Data Analytics Dashboard")

# Load Data
df = pd.read_csv("cleaned_titanic.csv")

# Show Raw Data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Sidebar Filters
st.sidebar.header("Filter Options")
gender = st.sidebar.selectbox("Select Gender", options=["All"] + list(df["Sex"].unique()))
pclass = st.sidebar.selectbox("Select Passenger Class", options=["All"] + sorted(df["Pclass"].unique()))

# Apply filters
filtered_df = df.copy()
if gender != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == gender]
if pclass != "All":
    filtered_df = filtered_df[filtered_df["Pclass"] == pclass]

st.subheader("🎯 Filtered Data Preview")

