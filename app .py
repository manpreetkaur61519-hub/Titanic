# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(page_title="Titanic EDA Dashboard", layout="wide")

# Title and Image
st.title("🚢 Titanic Data Analytics Dashboard")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg",
    caption="RMS Titanic",
    use_column_width=True,
)

# Load Data
df = pd.read_csv("cleaned_titanic.csv")

# Show Data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Sidebar Filters
st.sidebar.header("Filter Options")

gender = st.sidebar.selectbox("Select Gender", options=df["Sex"].unique())
pclass = st.sidebar.selectbox("Select Passenger Class", options=sorted(df["Pclass"].unique()))
age_slider = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (0, 80))
fare_slider = st.sidebar.slider("Select Fare Range", float(df["Fare"].min()), float(df["Fare"].max()), (0.0, 250.0))

# Apply Filters
filtered_df = df[
    (df["Sex"] == gender) &
    (df["Pclass"] == pclass) &
    (df["Age"] >= age_slider[0]) & (df["Age"] <= age_slider[1]) &
    (df["Fare"] >= fare_slider[0]) & (df["Fare"] <= fare_slider[1])
]

# Show Filtered Data
st.subheader("🎯 Filtered Data Preview")
st.write(filtered_df.head())

# Layout for Visuals
col1, col2 = st.columns(2)

# Chart 1: Survival by Gender
with col1:
    st.subheader("🧍‍♂️ Survival Count by Gender")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=filtered_df, x="Survived", hue="Sex", ax=ax1)
    ax1.set_title("Survival Distribution")
    st.pyplot(fig1)

# Chart 2: Age Distribution
with col2:
    st.subheader("📊 Age Distribution")
    fig2, ax2 = plt.subplots()
    sns.histplot(filtered_df["Age"], kde=True, bins=30, ax=ax2)
    ax2.set_title("Age Histogram")
    st.pyplot(fig2)

# Row 2 Layout
col3, col4 = st.columns(2)

# Chart 3: Fare Distribution
with col3:
    st.subheader("💰 Fare Distribution")
    fig3, ax3 = plt.subplots()
    sns.histplot(filtered_df["Fare"], kde=True, bins=30, ax=ax3)
    ax3.set_title("Fare Histogram")
    st.pyplot(fig3)

# Chart 4: Survival by Embarkation Port
with col4:
    st.subheader("🚢 Survival by Embarkation Port")
    fig4, ax4 = plt.subplots()
    sns.countplot(data=filtered_df, x="Embarked", hue="Survived", ax=ax4)
    ax4.set_title("Embarked vs Survival")
    st.pyplot(fig4)




