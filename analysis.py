import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# 1️⃣ Load cleaned data
# -------------------------------
df = pd.read_csv("data/cleaned_shopping_data.csv")

# Quick look at data
print(df.head())
print(df.info())
print(df.describe())

# -------------------------------
# 2️⃣ Create plots folder if it doesn't exist
# -------------------------------
os.makedirs("plots", exist_ok=True)  # changed "../plots" to "plots" for consistency

# Set Seaborn style for nicer plots
sns.set(style="whitegrid")

# -------------------------------
# 3️⃣ Distribution of purchase amounts
# -------------------------------
plt.figure(figsize=(8,5))
sns.histplot(df['purchase_amount_usd'], bins=20, kde=True, color='skyblue')  # added KDE & color
plt.title("Purchase Amount Distribution")
plt.xlabel("Purchase Amount (USD)")
plt.ylabel("Count")
plt.tight_layout()  # prevents label cutoff
plt.savefig("plots/purchase_distribution.png")
plt.show()

# -------------------------------
# 4️⃣ Count of items purchased by category
# -------------------------------
plt.figure(figsize=(8,5))
category_count = df['category'].value_counts()
sns.barplot(x=category_count.index, y=category_count.values, palette="viridis")
plt.xticks(rotation=45)
plt.title("Number of Purchases per Category")
plt.xlabel("Category")
plt.ylabel("Number of Purchases")
plt.tight_layout()
plt.savefig("plots/purchases_by_category.png")
plt.show()

# -------------------------------
# 5️⃣ Average purchase by subscription status
# -------------------------------
plt.figure(figsize=(8,5))
avg_purchase = df.groupby('subscription_status')['purchase_amount_usd'].mean().reset_index()
sns.barplot(x='subscription_status', y='purchase_amount_usd', data=avg_purchase, palette="magma")
plt.title("Average Purchase by Subscription Status")
plt.xlabel("Subscription Status")
plt.ylabel("Average Purchase Amount (USD)")
plt.tight_layout()
plt.savefig("plots/avg_purchase_by_subscription.png")
plt.show()
