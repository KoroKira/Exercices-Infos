import os
from datetime import datetime

def scan_system(root_dir):
    # Initialize dictionary to store files with their relative paths and stats
    files = {}

    # Walk through the directory structure
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_stats = os.stat(file_path)
            # Store the relative path of the file to compare with the other directory
            relative_path = os.path.relpath(file_path, root_dir)
            files[relative_path] = {
                'path': file_path,
                'size': file_stats.st_size,
                'modified_time': file_stats.st_mtime
            }
    return files

def comparer_dossiers(dossier_a, dossier_b):
    # Scanner les deux dossiers
    fichiers_a = scan_system(dossier_a)
    fichiers_b = scan_system(dossier_b)

    # Préparation du fichier de sortie
    with open('comparaison_fichiers.txt', 'w') as output_file:
        # Vérification des fichiers présents dans A mais pas dans B
        for fichier in fichiers_a:
            if fichier not in fichiers_b:
                output_file.write(f"{fichier}: Présent dans {dossier_a} mais absent de {dossier_b}\n")
            else:
                # Comparaison des fichiers présents dans les deux dossiers
                stats_a = fichiers_a[fichier]
                stats_b = fichiers_b[fichier]

                date_a = datetime.fromtimestamp(stats_a['modified_time'])
                date_b = datetime.fromtimestamp(stats_b['modified_time'])
                taille_a = stats_a['size']
                taille_b = stats_b['size']

                if date_a < date_b:
                    output_file.write(f"{fichier}: Plus ancien dans {dossier_a} que dans {dossier_b}\n")
                elif date_a > date_b:
                    if taille_b > taille_a:
                        output_file.write(f"{fichier}: Plus récent dans {dossier_a} mais plus léger que dans {dossier_b}\n")
                    else:
                        output_file.write(f"{fichier}: Plus récent dans {dossier_a} et plus lourd ou égal que dans {dossier_b}\n")

        # Vérification des fichiers présents dans B mais pas dans A
        for fichier in fichiers_b:
            if fichier not in fichiers_a:
                output_file.write(f"{fichier}: Présent dans {dossier_b} mais absent de {dossier_a}\n")

if __name__ == "__main__":
    # Chemins des dossiers à comparer
    dossier_a = "/chemin/vers/dossier/A"
    dossier_b = "/chemin/vers/dossier/B"

    # Lancer la comparaison et écrire les résultats dans un fichier texte
    comparer_dossiers(dossier_a, dossier_b)

    print("Comparaison terminée ! Résultats enregistrés dans 'comparaison_fichiers.txt'.")