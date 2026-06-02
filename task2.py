import pandas as pd
df = pd.read_csv("books_dataset.csv")
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nRatings Count:")
print(df["Rating"].value_counts())