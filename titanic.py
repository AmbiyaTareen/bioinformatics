import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print(df.groupby("Survived")["Pclass"].value_counts())
print(df.isnull().sum())