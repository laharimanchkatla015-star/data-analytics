import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load dataset
df = pd.read_csv("books_dataset.csv")
# Show first rows
print(df.head())

# =========================
# CLEAN PRICE COLUMN (FIXED)
# =========================
df["Price"] = df["Price"].apply(lambda x: re.sub(r"[^\d.]", "", str(x)))
df["Price"] = df["Price"].astype(float)

# =========================
# BASIC CHECKS
# =========================
print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nRating Count:")
print(df["Rating"].value_counts())

# =========================
# VISUALIZATION 1: Rating Count
# =========================
plt.figure(figsize=(6,4))
sns.countplot(x="Rating", data=df)
plt.title("Book Rating Distribution")
plt.show()

# =========================
# VISUALIZATION 2: Price Distribution
# =========================
plt.figure(figsize=(6,4))
sns.histplot(df["Price"], bins=10, kde=True)
plt.title("Price Distribution")
plt.show()

# =========================
# VISUALIZATION 3: Price vs Rating
# =========================
plt.figure(figsize=(6,4))
sns.boxplot(x="Rating", y="Price", data=df)
plt.title("Price vs Rating")
plt.show()

# =========================
# VISUALIZATION 4: Avg Price by Rating
# =========================
df.groupby("Rating")["Price"].mean().plot(kind="bar")
plt.title("Average Price by Rating")
plt.show()