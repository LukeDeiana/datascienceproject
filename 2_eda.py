import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caricamento del dataset preparato
df = pd.read_csv('spacex_launches_prepared.csv')

# Impostazione dello stile per le visualizzazioni
sns.set(style="whitegrid")

# 1. Flight Number vs. Launch Site (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='FlightNumber', y='LaunchSite')
plt.title('Flight Number vs. Launch Site')
plt.xlabel('Flight Number')
plt.ylabel('Launch Site')
plt.savefig('flight_number_vs_launch_site.png')
plt.show()

# 2. Payload vs. Launch Site (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PayloadMass', y='LaunchSite')
plt.title('Payload Mass vs. Launch Site')
plt.xlabel('Payload Mass (kg)')
plt.ylabel('Launch Site')
plt.savefig('payload_vs_launch_site.png')
plt.show()

# 3. Success Rate vs. Orbit Type (Bar Chart)
success_rate = df.groupby('Orbit')['Class'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(data=success_rate, x='Orbit', y='Class')
plt.title('Success Rate vs. Orbit Type')
plt.xlabel('Orbit Type')
plt.ylabel('Success Rate')
plt.savefig('success_rate_vs_orbit.png')
plt.show()

# 4. Flight Number vs. Orbit Type (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='FlightNumber', y='Orbit')
plt.title('Flight Number vs. Orbit Type')
plt.xlabel('Flight Number')
plt.ylabel('Orbit Type')
plt.savefig('flight_number_vs_orbit.png')
plt.show()

# 5. Payload vs. Orbit Type (Scatter Plot)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PayloadMass', y='Orbit')
plt.title('Payload Mass vs. Orbit Type')
plt.xlabel('Payload Mass (kg)')
plt.ylabel('Orbit Type')
plt.savefig('payload_vs_orbit.png')
plt.show()

# Controllo e conversione della colonna 'Date'
if 'Date' in df.columns:
    if not pd.api.types.is_datetime64_any_dtype(df['Date']):
        print("Colonna 'Date' non è in formato datetime. La converto ora...")
        try:
            df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
            print("Conversione completata con successo.")
        except Exception as e:
            print(f"Errore durante la conversione: {e}")
    else:
        print("Colonna 'Date' già in formato datetime.")
else:
    print("Errore: la colonna 'Date' non è presente nel dataset.")

# Esempio di visualizzazione: andamento del successo dei lanci per anno
if 'Date' in df.columns and pd.api.types.is_datetime64_any_dtype(df['Date']) and 'Class' in df.columns:
    df['Year'] = df['Date'].dt.year
    yearly_success = df.groupby('Year')['Class'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=yearly_success, x='Year', y='Class')
    plt.title('Andamento Annuale del Successo dei Lanci')
    plt.xlabel('Anno')
    plt.ylabel('Tasso di Successo')
    plt.savefig('yearly_success_trend.png')
    plt.show()
else:
    print("Non posso generare il grafico")