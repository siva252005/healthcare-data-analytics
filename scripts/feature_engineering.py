import pandas as pd

print("Starting Feature Engineering...\n")

# Load cleaned dataset
df = pd.read_csv("data/processed/healthcare_cleaned.csv")

# ---------------------------
# Age Group
# ---------------------------
def age_group(age):
    if age < 30:
        return "Young"
    elif age < 50:
        return "Middle Age"
    else:
        return "Senior"

df["age_group"] = df["age"].apply(age_group)

# ---------------------------
# BMI Category
# ---------------------------
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

df["bmi_category"] = df["bmi"].apply(bmi_category)

# ---------------------------
# Risk Level
# ---------------------------
def risk_level(row):

    if row["smoker"] == "yes" and row["bmi"] > 30:
        return "High Risk"

    elif row["smoker"] == "yes":
        return "Medium Risk"

    else:
        return "Low Risk"

df["risk_level"] = df.apply(risk_level, axis=1)

# Show new columns
print("New Features Created:")
print(df[["age_group", "bmi_category", "risk_level"]].head())

# Save updated dataset
df.to_csv("data/processed/healthcare_cleaned.csv", index=False)

print("\nFeature Engineering Completed Successfully")