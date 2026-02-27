import pandas as pd
import matplotlib.pyplot as plt

# 1. Chargement des données

df = pd.read_csv("versailles_2020_2025.csv")

# 2. Préparation des données

# Conversion de la date
df['date'] = pd.to_datetime(df['date'])

# Création colonnes année et mois
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# Vérification valeurs manquantes
print("Valeurs manquantes :")
print(df.isnull().sum())

# 3. Analyse températures

# Température moyenne par année
temp_annuelle = df.groupby('year')['tavg'].mean()
print("\nTempérature moyenne annuelle :")
print(temp_annuelle)

# Température moyenne par mois (saisonnalité)
temp_mensuelle = df.groupby('month')['tavg'].mean()
print("\nTempérature moyenne mensuelle :")
print(temp_mensuelle)

# Jour le plus chaud
max_temp = df['tmax'].max()
jour_plus_chaud = df[df['tmax'] == max_temp]

print("\nTempérature maximale enregistrée :", max_temp)
print(jour_plus_chaud[['date', 'tmax']])

# Jour le plus froid
min_temp = df['tmin'].min()
jour_plus_froid = df[df['tmin'] == min_temp]

print("\nTempérature minimale enregistrée :", min_temp)
print(jour_plus_froid[['date', 'tmin']])

# 4. Graphiques températures

# Températures max/min dans le temps
plt.figure()
plt.plot(df['date'], df['tmax'], label="Température max")
plt.plot(df['date'], df['tmin'], label="Température min")
plt.legend()
plt.title("Températures max et min (2020-2025)")
plt.xlabel("Date")
plt.ylabel("Température (°C)")
plt.show()

# Moyenne annuelle
plt.figure()
temp_annuelle.plot(kind='bar')
plt.title("Température moyenne par année")
plt.xlabel("Année")
plt.ylabel("Température moyenne (°C)")
plt.show()

# Moyenne mensuelle
plt.figure()
temp_mensuelle.plot(kind='bar')
plt.title("Température moyenne par mois (2020-2025)")
plt.xlabel("Mois")
plt.ylabel("Température moyenne (°C)")
plt.show()

# 5. Analyse pluie

if 'prcp' in df.columns:
    pluie_annuelle = df.groupby('year')['prcp'].sum()
    print("\nPrécipitations totales par année :")
    print(pluie_annuelle)

    plt.figure()
    pluie_annuelle.plot(kind='bar')
    plt.title("Précipitations annuelles totales")
    plt.xlabel("Année")
    plt.ylabel("Pluie totale (mm)")
    plt.show()

# 6. Analyse vent

if 'wspd' in df.columns:
    vent_annuel = df.groupby('year')['wspd'].mean()
    print("\nVitesse moyenne du vent par année :")
    print(vent_annuel)

    plt.figure()
    vent_annuel.plot(kind='bar')
    plt.title("Vitesse moyenne du vent par année")
    plt.xlabel("Année")
    plt.ylabel("Vitesse moyenne du vent")
    plt.show()

print("\nAnalyse terminée.")
