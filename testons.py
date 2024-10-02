import os
from datetime import datetime

def scan_system_full(root_dir):
    """Scanner tout le contenu du dossier A, y compris les sous-dossiers"""
    files = {}

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            try:
                file_path = os.path.join(dirpath, filename)
                file_stats = os.stat(file_path)
                # Stocker le chemin relatif pour la comparaison
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

def scan_system_first_level(root_dir):
    """Scanner uniquement les fichiers et dossiers du premier niveau dans B"""
    files = {}
    for dirpath, _, filenames in os.walk(root_dir):
        # Ne traiter que les fichiers du premier niveau
        if dirpath == root_dir:
            for filename in filenames:
                try:
                    file_path = os.path.join(dirpath, filename)
                    file_stats = os.stat(file_path)
                    # Stocker le chemin relatif
                    relative_path = os.path.relpath(file_path, root_dir)
                    files[relative_path] = {
                        'path': file_path,
                        'size': file_stats.st_size,
                        'modified_time': file_stats.st_mtime
                    }
                except Exception as e:
                    with open('comparaison_fichiers.txt', 'a') as output_file:
                        output_file.write(f"Erreur lors de la lecture du fichier {filename} dans {dirpath}: {e}\n")
            break  # Sortir après avoir traité le premier niveau
    return files

def comparer_dossiers(dossier_a, dossier_b):
    # Scanner tout le dossier A
    fichiers_a = scan_system_full(dossier_a)

    # Préparation du fichier de sortie
    with open('comparaison_fichiers.txt', 'w') as output_file:
        # Parcourir les dossiers de premier niveau de A pour les comparer dans B
        for fichier in fichiers_a:
            # Obtenir le dossier parent du fichier dans A
            dossier_parent_a = os.path.dirname(fichier)
            
            # Comparer avec le premier niveau de B
            dossier_parent_b = os.path.join(dossier_b, dossier_parent_a)
            
            if os.path.exists(dossier_parent_b) and os.path.isdir(dossier_parent_b):
                # Scanner les fichiers de premier niveau dans le dossier correspondant de B
                fichiers_b = scan_system_first_level(dossier_parent_b)
                
                # Comparer les fichiers dans ce dossier
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
                    output_file.write(f"{fichier}: Présent dans {dossier_a} mais absent de {dossier_b} au premier niveau\n")
            else:
                output_file.write(f"Dossier {dossier_parent_a}: Absent de {dossier_b}\n")

if __name__ == "__main__":
    # Chemins des dossiers à comparer
    dossier_a = r"\\eDossier\sdossier\tdossier\rdossier\Hdossier dossier dossier"
    dossier_b = r"\\eDossier\sdossier\tdossier\rdossier\Hdossier dossier dossier B"

    # Lancer la comparaison et écrire les résultats dans un fichier texte
    comparer_dossiers(dossier_a, dossier_b)

    print("Comparaison terminée ! Résultats enregistrés dans 'comparaison_fichiers.txt'.")