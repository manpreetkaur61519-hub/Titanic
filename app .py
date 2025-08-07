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
st.sidebar.header("🔎 Filter Options")

# Gender Filter
gender = st.sidebar.selectbox("Select Gender", options=["All"] + list(df["Sex"].unique()))
# Passenger Class Filter
pclass = st.sidebar.selectbox("Select Passenger Class", options=["All"] + sorted(df["Pclass"].unique()))

# Age Filter using Slider
min_age, max_age = int(df["Age"].min()), int(df["Age"].max())
age_range = st.sidebar.slider("Select Age Range", min_age, max_age, (min_age, max_age))

# Fare Filter using Slider
min_fare, max_fare = int(df["Fare"].min()), int(df["Fare"].max())
fare_range = st.sidebar.slider("Select Fare Range", min_fare, max_fare, (min_fare, max_fare))

# Apply filters
filtered_df = df[
    (df["Age"].between(age_range[0], age_range[1])) &
    (df["Fare"].between(fare_range[0], fare_range[1]))
]

if gender != "All":
    filtered_df = filtered_df[filtered_df["Sex"] == gender]

if pclass != "All":
    filtered_df = filtered_df[filtered_df["Pclass"] == pclass]

# Filtered Data Preview
st.subheader("📊 Filtered Data Preview")
st.dataframe(filtered_df.head(20))

# ========================== #
# 🧠 Visualization Section
# ========================== #

st.subheader("📈 Visualizations")

# Layout with columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Survival Count by Gender")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=filtered_df, x="Survived", hue="Sex", ax=ax1)
    st.pyplot(fig1)

with col2:
    st.markdown("### Age Distribution")
    fig2, ax2 = plt.subplots()
    sns.histplot(filtered_df["Age"], kde=True, ax=ax2, bins=20)
    st.pyplot(fig2)

col3, col4 = st.columns(2)

with col3:
    st.markdown("### Fare Distribution")
    fig3, ax3 = plt.subplots()
    sns.histplot(filtered_df["Fare"], kde=True, ax=ax3, bins=20)
    st.pyplot(fig3)

with col4:
    st.markdown("### Class Distribution")
    fig4, ax4 = plt.subplots()
    sns.countplot(data=filtered_df, x="Pclass", hue="Sex", ax=ax4)
    st.pyplot(fig4)

# Optional Pie Chart
st.markdown("### 🥧 Pie Chart of Survival")
survived_counts = filtered_df["Survived"].value_counts()
fig5, ax5 = plt.subplots()
ax5.pie(survived_counts, labels=["Not Survived", "Survived"], autopct="%1.1f%%", startangle=90)
ax5.axis("equal")
st.pyplot(fig5)



