import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


df = pd.read_csv("GDSC_DATASET.csv")
print(df.shape)
print(df.isnull().sum())
columns = df.select_dtypes(include='object').columns
print(df.groupby('DRUG_NAME').size().sort_values(ascending=False))

fulv_df = df[df['DRUG_NAME'] == 'Fulvestrant']
print(fulv_df.shape)
print(fulv_df['CNA'].isnull().sum())
print(fulv_df['Gene Expression'].isnull().sum())
print(fulv_df['Methylation'].isnull().sum())
print(fulv_df['Microsatellite instability Status (MSI)'].isnull().sum())
print(fulv_df[['CNA', 'Gene Expression', 'Methylation','Microsatellite instability Status (MSI)']].isnull().all(axis=1).sum())

fulv_df = fulv_df.dropna(subset=['CNA','Methylation','Gene Expression'])
print(fulv_df.shape)

fulv_df['Microsatellite instability Status (MSI)'] = fulv_df['Microsatellite instability Status (MSI)'].fillna('Unknown')
print(fulv_df['Microsatellite instability Status (MSI)'].value_counts(dropna=False))

print(fulv_df[['CNA','Gene Expression','Methylation']].dtypes)
print(fulv_df['CNA'].unique()[:10])
print(fulv_df['CNA'].unique()[:10])
print(fulv_df['Gene Expression'].unique()[:10])
print(fulv_df['Methylation'].unique()[:10])

fulv_df.columns = fulv_df.columns.str.replace('\n', ' ', regex=False)
print(fulv_df.columns.tolist())
print(fulv_df['Cancer Type (matching TCGA label)'].isnull().sum())

fulv_df['Cancer Type (matching TCGA label)'] = fulv_df['Cancer Type (matching TCGA label)'].fillna('Unknown')
print(fulv_df['Cancer Type (matching TCGA label)'].nunique())
print(fulv_df['Cancer Type (matching TCGA label)'].value_counts())

counts = fulv_df['Cancer Type (matching TCGA label)'].value_counts()
rare = counts[(counts < 20) & (~counts.index.isin(['Unknown', 'UNABLE TO CLASSIFY']))].index
fulv_df['Cancer Type (matching TCGA label)'] = fulv_df['Cancer Type (matching TCGA label)'].replace(rare, 'Other')
print(fulv_df['Cancer Type (matching TCGA label)'].value_counts())
print(fulv_df.groupby('Cancer Type (matching TCGA label)')['AUC'].agg(['count','mean','std']).sort_values('count', ascending=False).head(5))
       
X = pd.get_dummies(fulv_df[['CNA', 'Gene Expression', 'Methylation', 'Microsatellite instability Status (MSI)','Cancer Type (matching TCGA label)']])
y = fulv_df['AUC']
print(X.shape)
print(X.columns.tolist())

y = fulv_df['AUC']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
preds = model.predict(X_test)

print("R²:", r2_score(y_test, preds))
print("MSE:", mean_squared_error(y_test, preds))

baseline = DummyRegressor(strategy='mean')
baseline.fit(X_train, y_train)
base_preds = baseline.predict(X_test)
print("Baseline R²:", r2_score(y_test, base_preds))
print("Baseline MSE:", mean_squared_error(y_test, base_preds))

importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print(importances.head(10))


plt.figure(figsize=(6,6))
plt.scatter(y_test, preds, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label='Perfect prediction')
plt.xlabel('Actual AUC')
plt.ylabel('Predicted AUC')
plt.title('Predicted vs Actual AUC (Fulvestrant, v1 baseline)')
plt.legend()
plt.tight_layout()
plt.show()

