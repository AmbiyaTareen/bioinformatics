import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)
def explore (df):
    print(df.head())
    print(df.describe())
    print(df.shape)
    print(df.isnull().sum())

if  __name__== "__main__":
    df = load_data("proteinas_test.csv")
    explore(df)