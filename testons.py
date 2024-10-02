import os
from datetime import datetime

def scan_directory_at_level(root_dir, level):
    """Scanner le contenu d'un dossier jusqu'à un certain niveau d'arborescence."""
    files = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Calculer le niveau de profondeur actuel
        depth = dirpath[len(root_dir):].count(os.sep)
        if depth > level:
            # Si on dépasse le niveau spécifié, arrêter
            dirnames[:] = []  # Ne pas entrer dans les sous-dossiers
            continue

        # Ajouter les fichiers du niveau en cours
        for filename in filenames:
            try:
                file_path = os.path.join(dirpath, filename)
                file_stats = os.stat(file_path)
                # Stocker le chemin relatif pour comparaison
                relative_path = os.path.relpath(file_path, root_dir)
                files[relative_path] = {
                    'path': file_path,
                    'size': file_stats.st_size,
                    'modified_time': file_stats.st_mtime
                }
            except Exception as e:
                with open('comparaison_fichiers.txt', 'a') as output_file:
                    output_file.write(f"Erreur lors de la lecture du fichier {filename} dans {dirpath}: {e}\n")
    return files

def comparer_dossiers(dossier_a, dossier_b, level=0):
    """Comparer les dossiers A et B niveau par niveau"""
    # Scanner tout le dossier A
    fichiers_a = scan_directory_at_level(dossier_a, level)
    
    # Scanner seulement le niveau actuel de B
    fichiers_b = scan_directory_at_level(dossier_b, level)

    # Préparation du fichier de sortie
    with open('comparaison_fichiers.txt', 'a') as output_file:
        # Comparer les fichiers au niveau actuel
        for fichier in fichiers_a:
            # Obtenir le dossier parent du fichier dans A
            dossier_parent_a = os.path.dirname(fichier)
            dossier_parent_b = os.path.join(dossier_b, dossier_parent_a)

            if os.path.exists(dossier_parent_b) and os.path.isdir(dossier_parent_b):
                # Scanner les fichiers du dossier correspondant dans B au niveau actuel
                if fichier in fichiers_b:
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
                else:
                    output_file.write(f"{fichier}: Présent dans {dossier_a} mais absent de {dossier_b} au niveau {level}\n")
            else:
                output_file.write(f"Dossier {dossier_parent_a}: Absent de {dossier_b} au niveau {level}\n")

        # Comparer les dossiers en commun pour aller plus en profondeur
        for fichier in fichiers_a:
            dossier_parent_a = os.path.dirname(fichier)
            dossier_parent_b = os.path.join(dossier_b, dossier_parent_a)

            # Si c'est un dossier dans les deux arborescences, on descend au niveau suivant
            if os.path.exists(dossier_parent_b) and os.path.isdir(dossier_parent_b):
                # Descendre dans l'arborescence pour les dossiers en commun
                comparer_dossiers(os.path.join(dossier_a, dossier_parent_a), os.path.join(dossier_b, dossier_parent_a), level + 1)

if __name__ == "__main__":
    # Chemins des dossiers à comparer
    dossier_a = r"\\eDossier\sdossier\tdossier\rdossier\Hdossier dossier dossier"
    dossier_b = r"\\eDossier\sdossier\tdossier\rdossier\Hdossier dossier dossier B"

    # Lancer la comparaison et écrire les résultats dans un fichier texte
    comparer_dossiers(dossier_a, dossier_b)

    print("Comparaison terminée ! Résultats enregistrés dans 'comparaison_fichiers.txt'.")