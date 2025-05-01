import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Caricamento del dataset preparato
df = pd.read_csv('spacex_launches_prepared.csv')

# Selezione delle feature e del target
X = df[['FlightNumber', 'PayloadMass', 'LaunchSite', 'Orbit', 'Outcome']]
y = df['Class']

# Divisione in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing
categorical_features = ['LaunchSite', 'Orbit', 'Outcome']
numerical_features = ['FlightNumber', 'PayloadMass']

# Configura ColumnTransformer con OneHotEncoder che gestisce categorie sconosciute
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features)
    ])

# Definizione dei modelli
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier()
}

# Addestramento e valutazione dei modelli
accuracies = {}
for name, model in models.items():
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('classifier', model)])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies[name] = accuracy
    print(f"Accuracy del modello {name}: {accuracy:.2f}")

# Visualizzazione delle accuratezze in un bar chart
plt.figure(figsize=(8, 5))
plt.bar(accuracies.keys(), accuracies.values(), color=['blue', 'green', 'orange'])
plt.title('Classification Model Accuracy Comparison')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.ylim(0, 1)
plt.savefig('model_accuracy_comparison.png')
plt.show()

# Identificazione del modello con la più alta accuratezza
best_model_name = max(accuracies, key=accuracies.get)
best_model_accuracy = accuracies[best_model_name]
print(f"Il modello con la più alta accuratezza è {best_model_name} con un'accuratezza di {best_model_accuracy:.2f}")

# Matrice di confusione per il miglior modello
best_model = models[best_model_name]
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', best_model)])
pipeline.fit(X_train, y_train)
y_pred_best = pipeline.predict(X_test)
cm = confusion_matrix(y_test, y_pred_best)

# Visualizzazione della matrice di confusione
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title(f'Confusion Matrix for {best_model_name}')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('model_confusion_matrix.png')
plt.show()