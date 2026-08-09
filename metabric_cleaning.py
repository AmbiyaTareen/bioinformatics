import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix

df = pd.read_csv("metabric_clinical.csv")
print(df.shape)
print(df.duplicated().sum())
print(df['patient_id'].duplicated().sum())
print(df['death_from_cancer'].unique())
columns = df.select_dtypes(include='object').columns

for column in columns:
    print(column, ":", df[column].unique())

df['er_status_measured_by_ihc'] = df['er_status_measured_by_ihc'].replace('Positve', 'Positive')
print(df['er_status_measured_by_ihc'].unique())
print(df.dtypes)
print(df.describe())
pd.set_option('display.max_columns', None)
print(df.describe())
print(df[df['nottingham_prognostic_index'] == df['nottingham_prognostic_index'].min()])
print((df.isnull().sum() / len(df) * 100).sort_values(ascending=False))

df['tumor_stage_missing'] = df['tumor_stage'].isnull()
df['tumor_stage'] = df['tumor_stage'].fillna(df['tumor_stage'].median())

print(df['tumor_stage'].isnull().sum())

df['3-gene_classifier_subtype']=df['3-gene_classifier_subtype'].fillna('Unknown')
df['primary_tumor_laterality']=df['primary_tumor_laterality'].fillna('Unknown')

print(df['3-gene_classifier_subtype'].isnull().sum())
print(df['primary_tumor_laterality'].isnull().sum())

df['neoplasm_histologic_grade'] = df['neoplasm_histologic_grade'].fillna(df['neoplasm_histologic_grade'].mode()[0])
df['cellularity'] = df['cellularity'].fillna(df['cellularity'].mode()[0])
df['er_status_measured_by_ihc'] = df['er_status_measured_by_ihc'].fillna(df['er_status_measured_by_ihc'].mode()[0])
df['type_of_breast_surgery'] = df['type_of_breast_surgery'].fillna(df['type_of_breast_surgery'].mode()[0])

print(df['neoplasm_histologic_grade'].isnull().sum())
print(df['cellularity'].isnull().sum())
print(df['er_status_measured_by_ihc'].isnull().sum())
print(df['type_of_breast_surgery'].isnull().sum())

df['mutation_count'] = df['mutation_count'].fillna(df['mutation_count'].median())
df['tumor_size'] = df['tumor_size'].fillna(df['tumor_size'].median())

df['cancer_type_detailed'] = df['cancer_type_detailed'].fillna(df['cancer_type_detailed'].mode()[0])
df['tumor_other_histologic_subtype'] = df['tumor_other_histologic_subtype'].fillna(df['tumor_other_histologic_subtype'].mode()[0])
df['oncotree_code'] = df['oncotree_code'].fillna(df['oncotree_code'].mode()[0])
df['death_from_cancer'] = df['death_from_cancer'].fillna(df['death_from_cancer'].mode()[0])

print(df.isnull().sum())
print(df['inferred_menopausal_state'].unique())
print(df['pr_status'].unique())

print(df[['age_at_diagnosis', 'tumor_size', 'neoplasm_histologic_grade', 
    'lymph_nodes_examined_positive', 'mutation_count', 
    'nottingham_prognostic_index', 'tumor_stage', 
    'inferred_menopausal_state', 'pr_status', 
    '3-gene_classifier_subtype']].isnull().sum())

df['inferred_menopausal_state'] = df['inferred_menopausal_state'].map({'Pre': 0, 'Post': 1})
df['pr_status'] = df['pr_status'].map({'Negative': 0, 'Positive': 1})
df = df[df['3-gene_classifier_subtype'] != 'Unknown']

X = df[['age_at_diagnosis', 'tumor_size', 'neoplasm_histologic_grade', 
        'lymph_nodes_examined_positive', 'mutation_count', 
        'nottingham_prognostic_index', 'tumor_stage', 
        'inferred_menopausal_state', 'pr_status']]

y = df['3-gene_classifier_subtype']

print(X.shape)
print(y.shape)
print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(X_train.shape)
print(X_test.shape)

model = RandomForestClassifier(random_state=42, class_weight='balanced_subsample')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
print(cm)

print(X.columns)
print(df.groupby('3-gene_classifier_subtype').mean(numeric_only=True))