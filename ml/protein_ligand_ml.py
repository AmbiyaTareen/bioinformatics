# Protein-Ligand ML Pipeline
# Week 2 Day 8 - BBBP Dataset (Blood-Brain Barrier Permeability)

import pandas as pd
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np

#Loading the dataset
df =pd.read_csv('BBBP.csv')
print('Dataset Shape:',df.shape)
print(df[['name','p_np','smiles']].head())

# Converting SMILES to Molecular Fingerprints

def smiles_to_fingerprint(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    fingerprint= rdMolDescriptors.GetMorganFingerprintAsBitVect(mol, radius=2,nBits=2048)
    return list(fingerprint)

#Generating Fingerprints of all molecules
df = df.dropna(subset=['smiles'])
df['fingerprint'] = df['smiles'].apply(smiles_to_fingerprint)
df = df.dropna(subset=['fingerprint'])

print(f"Valid molecules : {len(df)}")

#Features and Labels

X=np.array(df['fingerprint'].tolist())
Y=df['p_np'].values

print(f'Feature Matrix Shape: {X.shape}')
print(f'Labels Shape: {Y.shape}')

# Training Random Forest Model
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(f"Training set: {X_train.shape[0]} molecules")
print(f"Test set: {X_test.shape[0]} molecules")

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)

print("Model trained!")

# Section 7 - Evaluate the Model
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(Y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(Y_test, y_pred))

# Ploting feature importances
importances = model.feature_importances_
plt.figure(figsize=(10, 4))
plt.plot(importances)
plt.title('Feature Importances - Morgan Fingerprint Bits')
plt.xlabel('Bit Position')
plt.ylabel('Importance')
plt.tight_layout()
plt.savefig('feature_importances.png')
print("Plot saved as feature_importances.png")