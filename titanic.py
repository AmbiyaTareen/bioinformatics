<<<<<<< HEAD
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print(df.groupby("Survived")["Pclass"].value_counts())
=======
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print(df.groupby("Survived")["Pclass"].value_counts())
>>>>>>> 6dd9691552871b3996124ea738570b6a08594b31
print(df.isnull().sum())