import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Starting Exploratory Data Analysis...\n")

# Load processed dataset
df = pd.read_csv("data/processed/healthcare_cleaned.csv")

print("Dataset Loaded Successfully\n")

# Show dataset columns
print("Dataset Columns:")
print(df.columns, "\n")

# ---------------------------
# Summary Statistics
# ---------------------------
print("Dataset Summary:")
print(df.describe(), "\n")

# ---------------------------
# Average charges by smoker
# ---------------------------
print("Average Charges by Smoking Status:")
print(df.groupby("smoker")["charges"].mean(), "\n")

# ---------------------------
# Average charges by age group
# ---------------------------
print("Average Charges by Age Group:")
print(df.groupby("age_group")["charges"].mean(), "\n")

# ---------------------------
# Plot 1: Charges by Smoker
# ---------------------------
plt.figure(figsize=(6,4))
sns.barplot(x="smoker", y="charges", data=df)
plt.title("Average Charges by Smoking Status")
plt.xlabel("Smoker")
plt.ylabel("Average Charges")
plt.show()

# ---------------------------
# Plot 2: Charges by Age Group
# ---------------------------
plt.figure(figsize=(6,4))
sns.barplot(x="age_group", y="charges", data=df)
plt.title("Average Charges by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Charges")
plt.show()

# ---------------------------
# Plot 3: Charges by BMI Category
# ---------------------------
plt.figure(figsize=(6,4))
sns.barplot(x="bmi_category", y="charges", data=df)
plt.title("Average Charges by BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Average Charges")
plt.show()

# ---------------------------
# Plot 4: Charges by Region
# ---------------------------
plt.figure(figsize=(6,4))
sns.barplot(x="region", y="charges", data=df)
plt.title("Average Charges by Region")
plt.xlabel("Region")
plt.ylabel("Average Charges")
plt.show()

print("EDA Completed Successfully")