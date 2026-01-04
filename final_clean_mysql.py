from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:Hema%40123@localhost:3306/customer_shopping_behavior"
)

# Load table with fixed columns
df = pd.read_sql("SELECT * FROM customer_shopping_cleaned;", engine)

# Rename column
df.rename(columns={
    "purchase_amount_(usd)": "purchase_amount_usd"
}, inplace=True)

# Convert Yes/No → 1/0
yes_no_cols = ["discount_applied", "promo_code_used"]
for col in yes_no_cols:
    df[col] = df[col].map({"Yes": 1, "No": 0})

print("Final Columns:")
print(df.columns)

# Save FINAL table
df.to_sql(
    "customer_shopping_final",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Final cleaned table saved as customer_shopping_final")
