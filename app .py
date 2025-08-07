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

# Show Data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Sidebar Filters
st.sidebar.header("Filter Options")
gender = st.sidebar.selectbox("Select Gender", options=df["Sex"].unique())
pclass = st.sidebar.selectbox("Select Passenger Class", options=sorted(df["Pclass"].unique()))

# Apply filters
filtered_df = df[(df["Sex"] == gender) & (df["Pclass"] == pclass)]

st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head())

# 2-column layout for visualizations
col1, col2 = st.columns(2)

# --- Chart 1: Survival Count by Gender ---
with col1:
    st.subheader("Survival Count by Gender")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.countplot(data=filtered_df, x="Survived", hue="Sex", ax=ax1)
    ax1.set_title("Survival Count", fontsize=14)
    ax1.set_xlabel("Survived", fontsize=12)
    ax1.set_ylabel("Count", fontsize=12)
    st.pyplot(fig1)

# --- Chart 2: Age Distribution ---
with col2:
    st.subheader("Age Distribution")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.histplot(data=filtered_df, x="Age", bins=20, kde=True, ax=ax2)
    ax2.set_title("Age Histogram", fontsize=14)
    ax2.set_xlabel("Age", fontsize=12)
    ax2.set_ylabel("Frequency", fontsize=12)
    st.pyplot(fig2)

# --- Row 2 of charts ---
col3, col4 = st.columns(2)

# --- Chart 3: Passenger Class vs Survival ---
with col3:
    st.subheader("Passenger Class vs Survival")
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    sns.countplot(data=filtered_df, x="Pclass", hue="Survived", ax=ax3)
    ax3.set_title("Class-wise Survival", fontsize=14)
    ax3.set_xlabel("Passenger Class", fontsize=12)
    ax3.set_ylabel("Count", fontsize=12)
    st.pyplot(fig3)

# --- Chart 4: Fare Distribution ---
with col4:
    st.subheader("Fare Distribution")
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=filtered_df, y="Fare", ax=ax4)
    ax4.set_title("Fare Boxplot", fontsize=14)
    ax4.set_ylabel("Fare", fontsize=12)
    st.pyplot(fig4)

# --- Pie Chart: Survival Rate ---
st.subheader("Survival Rate Pie Chart")
surv_counts = filtered_df["Survived"].value_counts()
fig5, ax5 = plt.subplots(figsize=(6, 4))
ax5.pie(surv_counts, labels=["Not Survived", "Survived"], autopct="%1.1f%%", startangle=90)
ax5.axis("equal")
st.pyplot(fig5)

# --- Summary Stats ---
st.subheader("Summary Statistics")
st.write(filtered_df.describe(include="all"))

