import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_csv("data/cleaned_shopping_data.csv")

print("Data loaded successfully")

# -------------------------------
# Basic EDA
# -------------------------------
print(df.info())
print(df.describe())

# -------------------------------
# Create plots folder
# -------------------------------
os.makedirs("plots", exist_ok=True)

# Age distribution
plt.figure()
sns.histplot(df["age"], bins=20)
plt.title("Age Distribution")
plt.savefig("plots/age_distribution.png")
plt.close()

# Gender distribution
plt.figure()
sns.countplot(data=df, x="gender")
plt.title("Gender Distribution")
plt.savefig("plots/gender_distribution.png")
plt.close()

# Category vs Purchase
plt.figure()
sns.boxplot(data=df, x="category", y="purchase_amount_usd")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/category_vs_purchase.png")
plt.close()

print("✅ EDA completed. Plots saved.")
