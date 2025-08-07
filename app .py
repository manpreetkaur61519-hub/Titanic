# Age Distribution
st.subheader("Age Distribution of Passengers")
fig, ax = plt.subplots()
sns.histplot(filtered_df["Age"].dropna(), kde=True, bins=30, ax=ax)
ax.set_xlabel("Age")
st.pyplot(fig)

# Survival Rate by Passenger Class
st.subheader("Survival Rate by Passenger Class")
fig, ax = plt.subplots()
sns.barplot(data=df, x="Pclass", y="Survived", ci=None, ax=ax)
ax.set_ylabel("Survival Rate")
st.pyplot(fig)

# Embarked Distribution
st.subheader("Embarkation Port Distribution")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x="Embarked", ax=ax)
st.pyplot(fig)

# Survival by Age and Sex
st.subheader("Survival by Age and Sex")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="Survived", y="Age", hue="Sex", ax=ax)
st.pyplot(fig)

# Fare Distribution
st.subheader("Fare Distribution")
fig, ax = plt.subplots()
sns.histplot(data=filtered_df, x="Fare", kde=True, ax=ax)
st.pyplot(fig)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
corr = df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)


