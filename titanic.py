import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

df =pd.read_csv('Titanic-Dataset.csv')
print(df.shape)
print(df.head)
print(df.isnull().sum())

df['Sex']=df['Sex'].map({'male': 0 , 'female': 1})
print(df['Sex'].unique())
print(df['Sex'].dtype)

df['Age'] = df['Age'].fillna(df['Age'].median())
print(df['Age'].isnull().sum())

X= df[['Pclass', 'Sex', 'Age', 'Fare']]
y = df['Survived']

print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)

model=RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
print(accuracy)
print(classification_report(y_test,y_pred))

comparison = X_test.copy()
comparison['Actual'] = y_test
comparison['Predicted'] = y_pred
comparison['Correct?'] = comparison['Actual'] == comparison['Predicted']
print(comparison.head(10))


