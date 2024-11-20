import pandas as pd

# Charger le fichier CSV
input_file = "/Users/guilhem/Downloads/tp3-desarcy-fraissine-deligny.csv"  # Remplace par le chemin réel de ton fichier
output_file = "fichier_clean.csv"

# Chargement des données
df = pd.read_csv(input_file)

# Remplacement des virgules par des points dans les valeurs numériques
df = df.replace({',': '.'}, regex=True)

# Renommage des colonnes
df.columns = [
    "Temps",
    "T_air_int_brique",
    "T_paroi_int_brique",
    "T_paroi_ext_brique",
    "T_air_int_bois",
    "T_paroi_int_bois",
    "T_paroi_ext_bois",
    "T_air_ambiant",
]

# Conversion des colonnes en type float là où c'est pertinent
for col in df.columns[1:]:
    df[col] = df[col].astype(float)

# Sauvegarde du fichier nettoyé
df.to_csv(output_file, index=False)

print(f"Fichier nettoyé enregistré sous : {output_file}")
