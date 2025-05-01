import pandas as pd

# URL del dataset
URL1 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"

# Caricamento del dataset dall'URL
df = pd.read_csv(URL1)

# Visualizzazione delle prime righe per verificare il contenuto
print("Prime 5 righe del dataset:")
print(df.head())

# Controllo dei tipi di dati delle colonne
print("\nTipi di dati delle colonne:")
print(df.dtypes)

# Conversione della colonna 'Date' in formato datetime, se presente
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    print("\nColonna 'Date' convertita in datetime.")
else:
    print("\nNota: La colonna 'Date' non è presente nel dataset.")

# Salvataggio del DataFrame preparato in un file CSV locale
df.to_csv('spacex_launches_prepared.csv', index=False)
print("\nDataset preparato e salvato come 'spacex_launches_prepared.csv'")