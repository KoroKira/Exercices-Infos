import pandas as pd

# Charger le fichier CSV brut
input_file = "/Users/guilhem/Downloads/tp3-desarcy-fraissine-deligny.csv"  # Remplace par le nom de ton fichier CSV
output_file = "data_cleaned.xlsx"  # Nom du fichier Excel de sortie

# Lire le CSV en tant que DataFrame
df = pd.read_csv(input_file)

# Supprimer les guillemets superflus et convertir les virgules en points pour les nombres
df = df.applymap(lambda x: float(str(x).replace(',', '.').replace('"', '').strip()) if isinstance(x, str) and ',' in x else x)

# Sauvegarder le DataFrame nettoyé dans un fichier Excel
df.to_excel(output_file, index=False)

print(f"Fichier nettoyé sauvegardé sous {output_file}")
