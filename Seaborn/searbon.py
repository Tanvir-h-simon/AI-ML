import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

# 1. Distribution of the target variable
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="charges", bins=40, kde=True, color="steelblue")
plt.title("Distribution of Medical Charges")
plt.xlabel("Charges")
plt.ylabel("Count")
plt.show()

# 2. Charges for smokers vs non-smokers
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="smoker", y="charges", palette="Set2")
plt.title("Charges by Smoking Status")
plt.show()

# 3. Age vs charges, colored by smoker
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="age", y="charges", hue="smoker", alpha=0.7)
plt.title("Age vs Charges")
plt.show()

# 4. BMI vs charges with a regression line for each group
sns.lmplot(data=df, x="bmi", y="charges", hue="smoker", height=5, aspect=1.5)
plt.title("BMI vs Charges")
plt.show()

# 5. Several categorical comparisons side by side
fig, axes = plt.subplots(1, 3, figsize=(16, 5))

sns.barplot(data=df, x="sex", y="charges", ax=axes[0])
axes[0].set_title("Average Charges by Sex")

sns.barplot(data=df, x="region", y="charges", ax=axes[1])
axes[1].set_title("Average Charges by Region")
axes[1].tick_params(axis="x", rotation=30)

sns.countplot(data=df, x="children", ax=axes[2])
axes[2].set_title("Number of Children")

plt.tight_layout()
plt.show()

# 6. Correlation heatmap of numeric features
plt.figure(figsize=(6, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Between Numeric Features")
plt.show()

# 7. Pairwise relationships between all numeric columns
sns.pairplot(df, hue="smoker", diag_kind="kde")
plt.show()