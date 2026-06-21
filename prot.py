import pandas as pd

df = pd.read_csv('proteinas_test.csv')
print(df.head())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print(df.groupby("ID_Proteína")["Carga_Total"].value_counts())
print(df.dropna(subset=['Classe']))