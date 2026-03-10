import pandas as pd

print("Starting Data Cleaning Process...\n")

# Load raw dataset
df = pd.read_csv("data/raw/healthcare_raw.csv")

print("Dataset Loaded Successfully\n")

# Check missing values
print("Missing Values:")
print(df.isnull().sum(), "\n")

# Remove duplicate rows
initial_rows = df.shape[0]
df = df.drop_duplicates()
final_rows = df.shape[0]

print(f"Duplicates removed: {initial_rows - final_rows}\n")

# Display dataset info
print("Dataset Info:")
print(df.info())

# Save cleaned dataset
df.to_csv("data/processed/healthcare_cleaned.csv", index=False)

print("\nCleaned dataset saved to: data/processed/healthcare_cleaned.csv")
print("Data Cleaning Completed Successfully")