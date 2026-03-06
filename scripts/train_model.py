import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("data/processed/healthcare_cleaned.csv")

# Convert categorical features
df_encoded = pd.get_dummies(df, drop_first=True)

# Features and target
X = df_encoded.drop("charges", axis=1)
y = df_encoded["charges"]

# Save column names (IMPORTANT)
columns = X.columns

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
score = model.score(X_test, y_test)
print("Model Accuracy:", score)

# Save model and columns
joblib.dump(model, "models/cost_prediction_model.pkl")
joblib.dump(columns, "models/model_columns.pkl")

print("Model saved successfully")