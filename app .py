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
st.dataframe(filtered_df.head())

# 1. Survival Count by Gender
st.subheader("🔹 Survival Count by Gender")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x="Survived", hue="Sex", ax=ax1)
ax1.set_xticklabels(['Not Survived', 'Survived'])
st.pyplot(fig1)

# 2. Survival Count by Class
st.subheader("🔹 Survival Count by Class")
fig2, ax2 = plt.subplots()
sns.countplot(data=filtered_df, x="Survived", hue="Pclass", ax=ax2)
ax2.set_xticklabels(['Not Survived', 'Survived'])
st.pyplot(fig2)

# 3. Age Distribution by Survival
st.subheader("🔹 Age Distribution by Survival Status")
fig3, ax3 = plt.subplots()
sns.histplot(data=filtered_df, x="Age", hue="Survived", multiple="stack", bins=30, ax=ax3)
ax3.set_xlabel("Age")
st.pyplot(fig3)

# 4. Heatmap of Correlation
st.subheader("🔹 Heatmap of Feature Correlations")
numeric_cols = filtered_df.select_dtypes(include=["int64", "float64"]).dropna().copy()
fig4, ax4 = plt.subplots()
sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax4)
st.pyplot(fig4)

# 5. Pie Chart of Survival Rate
st.subheader("🔹 Survival Rate Pie Chart")
survival_counts = filtered_df["Survived"].value_counts()
fig5, ax5 = plt.subplots()
ax5.pie(survival_counts, labels=["Not Survived", "Survived"], autopct="%1.1f%%", startangle=90)
ax5.axis("equal")
st.pyplot(fig5)

# 6. Count of Passengers by Embarkation Port
st.subheader("🔹 Count of Passengers by Embarkation Port")
fig6, ax6 = plt.subplots()
sns.countplot(data=filtered_df, x="Embarked", palette="Set2", ax=ax6)
st.pyplot(fig6)

# Footer
st.markdown("---")
st.markdown("📊 **Built with Streamlit | Titanic Dataset EDA**")

