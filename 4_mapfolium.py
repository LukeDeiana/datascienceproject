import folium
import pandas as pd
from geopy.distance import geodesic

# Passo 1: Carica il dataset preparato
df = pd.read_csv('spacex_launches_prepared.csv')

# Passo 2: Definisci le coordinate approssimative dei siti di lancio
launch_sites_coords = {
    'CCAFS SLC 40': [28.5623, -80.5774],
    'VAFB SLC 4E': [34.6321, -120.6107],
    'KSC LC 39A': [28.5733, -80.6469]
}

# Passo 3: Aggiungi le colonne di latitudine e longitudine al DataFrame in base al sito di lancio
df['Lat'] = df['LaunchSite'].map(lambda x: launch_sites_coords[x][0])
df['Long'] = df['LaunchSite'].map(lambda x: launch_sites_coords[x][1])

# Passo 4: Crea una mappa Folium centrata su un punto medio (ad esempio, USA centrale)
m = folium.Map(location=[30.0, -90.0], zoom_start=4)

# Passo 5: Aggiungi marcatori per ogni sito di lancio con colori basati sul risultato del lancio
for index, row in df.iterrows():
    color = 'green' if row['Class'] == 1 else 'red'  # Verde per successo, rosso per fallimento
    folium.Marker(
        location=[row['Lat'], row['Long']],
        popup=f"{row['LaunchSite']} - Outcome: {row['Outcome']}",
        icon=folium.Icon(color=color)
    ).add_to(m)

# Passo 6: Aggiungi cerchi di prossimità (ad esempio, raggio di 5 km) attorno a ogni sito di lancio
for site, coords in launch_sites_coords.items():
    folium.Circle(
        location=coords,
        radius=5000,  # 5 km
        color='blue',
        fill=True,
        fill_opacity=0.2
    ).add_to(m)

# Passo 7: Definisci le coordinate di una caratteristica vicina (ad esempio, costa per CCAFS SLC 40)
coast_coords = [28.5623, -80.5674]  # Costa approssimativa vicino a CCAFS SLC 40

# Passo 8: Aggiungi una linea che collega CCAFS SLC 40 alla costa
folium.PolyLine(
    locations=[launch_sites_coords['CCAFS SLC 40'], coast_coords],
    color='purple',
    weight=2,
    opacity=1
).add_to(m)

# Passo 9: Calcola la distanza da CCAFS SLC 40 alla costa
distance_to_coast = geodesic(launch_sites_coords['CCAFS SLC 40'], coast_coords).kilometers

# Passo 10: Aggiungi un marcatore per la costa con la distanza visualizzata
folium.Marker(
    location=coast_coords,
    popup=f"Costa - Distanza da CCAFS SLC 40: {distance_to_coast:.2f} km",
    icon=folium.Icon(color='blue')
).add_to(m)

# Passo 11: Salva la mappa come file HTML
m.save('launch_sites_map.html')
print("Mappa salvata come 'launch_sites_map.html'")