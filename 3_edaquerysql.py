import pandas as pd

# Caricamento del dataset preparato
df = pd.read_csv('spacex_launches_prepared.csv')

# Converti la colonna 'Date' in formato datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 24. All Launch Site Names
unique_launch_sites = df['LaunchSite'].unique()
print("Nomi dei siti di lancio univoci:")
print(unique_launch_sites)

# 25. Launch Site Names Begin with 'CCA'
cca_sites = df[df['LaunchSite'].str.startswith('CCA')].head(5)
print("\nPrimi 5 record con siti di lancio che iniziano con 'CCA':")
print(cca_sites[['FlightNumber', 'Date', 'LaunchSite']])

# 26. Total Payload Mass
total_payload_mass = df['PayloadMass'].sum()
print("\nMassa totale del payload (kg):")
print(total_payload_mass)

# 27. Average Payload Mass by F9 v1.1
# Nota: Il dataset non contiene la colonna 'BoosterVersion', quindi questa query non può essere eseguita
print("\nNota: La colonna 'BoosterVersion' non è presente nel dataset fornito.")

# 28. First Successful Ground Landing Date
first_success_ground = df[df['Outcome'] == 'True RTLS'].sort_values('Date').iloc[0]['Date']
print("\nData del primo atterraggio di successo su piattaforma terrestre:")
print(first_success_ground)

# 29. Successful Drone Ship Landing with Payload between 4000 and 6000
successful_drone_ship = df[(df['Outcome'] == 'True ASDS') & 
                          (df['PayloadMass'] > 4000) & 
                          (df['PayloadMass'] < 6000)][['FlightNumber', 'Date', 'PayloadMass']]
print("\nLanci con atterraggio su drone ship e payload tra 4000 e 6000 kg:")
print(successful_drone_ship)

# 30. Total Number of Successful and Failure Mission Outcomes
success_failure_counts = df['Class'].value_counts()
print("\nConteggio totale di successi (1) e fallimenti (0):")
print(success_failure_counts)

# 31. Boosters Carried Maximum Payload
max_payload = df['PayloadMass'].max()
boosters_max_payload = df[df['PayloadMass'] == max_payload][['FlightNumber', 'Date', 'PayloadMass']]
print("\nLanci con la massa massima del payload:")
print(boosters_max_payload)

# 32. 2015 Launch Records (Failed Drone Ship Landings)
df['Year'] = df['Date'].dt.year
launches_2015 = df[(df['Year'] == 2015) & (df['Outcome'].str.contains('False'))][['FlightNumber', 'Date', 'LaunchSite', 'Outcome']]
print("\nRecord dei lanci falliti su drone ship nel 2015:")
print(launches_2015)

# 33. Rank Landing Outcomes Between 2010-06-04 and 2017-03-20
date_filtered = df[(df['Date'] >= '2010-06-04') & (df['Date'] <= '2017-03-20')]
outcome_counts = date_filtered['Outcome'].value_counts().sort_values(ascending=False)
print("\nClassifica degli esiti di atterraggio tra 2010-06-04 e 2017-03-20:")
print(outcome_counts)