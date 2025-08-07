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

# Gender Filter
gender = st.sidebar.selectbox("Select Gender", options=df["Sex"].unique())

# Passenger Class Filter
pclass = st.sidebar.selectbox("Select Passenger Class", options=sorted(df["Pclass"].unique()))

# Age Slider Filter
min_age, max_age = int(df["Age"].min()), int(df["Age"].max())
age_range = st.sidebar.slider("Select Age Range", min_value=min_age, max_value=max_age, value=(min_age, max_age))

# Apply Filters
filtered_df = df[
    (df["Sex"] == gender) &
    (df["Pclass"] == pclass) &
    (df["Age"] >= age_range[0]) &
    (df["Age"] <= age_range[1])
]

# Show Filtered Data
st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head())

# Visualizations
st.subheader("🧾 Data Visualizations")

# Column Layout for Charts
col1, col2 = st.columns(2)

# Chart 1: Survival Count by Gender
with col1:
    st.markdown("### ✅ Survival Count by Gender")
    fig1, ax1 = plt.subplots()
    sns.countplot(data=filtered_df, x="Survived", hue="Sex", ax=ax1)
    ax1.set_title("Survival Count")
    st.pyplot(fig1)

# Chart 2: Survival Count by Passenger Class
with col2:
    st.markdown("### 🎫 Survival by Passenger Class")
    fig2, ax2 = plt.subplots()
    sns.countplot(data=filtered_df, x="Survived", hue="Pclass", ax=ax2)
    ax2.set_title("Survival by Class")
    st.pyplot(fig2)

# Chart 3: Age Distribution by Survival
with col1:
    st.markdown("### 👶 Age Distribution by Survival")
    fig3, ax3 = plt.subplots()
    sns.histplot(data=filtered_df, x="Age", hue="Survived", kde=True, bins=30, ax=ax3)
    ax3.set_title("Age Distribution by Survival")
    st.pyplot(fig3)

# Chart 4: Fare Distribution
with col2:
    st.markdown("### 💸 Fare Distribution")
    fig4, ax4 = plt.subplots()
    sns.boxplot(data=filtered_df, x="Survived", y="Fare", ax=ax4)
    ax4.set_title("Fare by Survival")
    st.pyplot(fig4)

