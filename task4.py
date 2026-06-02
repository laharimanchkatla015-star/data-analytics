import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("books_dataset.csv")

print(df.head())

# =========================
# SENTIMENT FUNCTION
# =========================
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# =========================
# CREATE SENTIMENT COLUMN
# =========================
df["Sentiment"] = df["Title"].apply(get_sentiment)

# NOW SAFE TO PRINT
print(df[["Title", "Sentiment"]].head())

# =========================
# SENTIMENT COUNT
# =========================
print(df["Sentiment"].value_counts())

# =========================
# VISUALIZATION
# =========================
plt.figure(figsize=(6,4))
sns.countplot(x="Sentiment", data=df)
plt.title("Sentiment Analysis of Book Titles")
plt.show()