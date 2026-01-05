import pandas as pd
import os

# Load raw data
df = pd.read_csv("data/customer_shopping_behavior.csv")

# -------------------------------
# Clean column names
# -------------------------------
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

# -------------------------------
# Handle missing values
# -------------------------------
df["review_rating"].fillna(df["review_rating"].mean(), inplace=True)

# Convert Yes/No to 1/0
yes_no_cols = ["discount_applied", "promo_code_used"]
for col in yes_no_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0})

# -------------------------------
# Save cleaned data
# -------------------------------
os.makedirs("data", exist_ok=True)
df.to_csv("data/cleaned_shopping_data.csv", index=False)

print("✅ Data cleaning completed successfully!")
