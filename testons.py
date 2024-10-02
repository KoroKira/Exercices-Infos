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

def comparer_dossiers_iteratif(dossier_a, dossier_b):
    """Comparer les dossiers A et B niveau par niveau de manière itérative."""
    
    # Pile de dossiers à comparer sous forme de tuples (dossier_A, dossier_B, niveau)
    pile = [(dossier_a, dossier_b, 0)]
    
    # Préparation du fichier de sortie
    with open('comparaison_fichiers.txt', 'a') as output_file:
        output_file.write("Début de la comparaison\n\n")

    while pile:
        current_a, current_b, level = pile.pop()
        
        # Scanner le niveau courant de A et B
        fichiers_a = scan_directory_at_level(current_a, level)
        fichiers_b = scan_directory_at_level(current_b, level)

        # Comparer les fichiers au niveau actuel
        with open('comparaison_fichiers.txt', 'a') as output_file:
            for fichier in fichiers_a:
                # Comparer les fichiers de A avec ceux de B
                if fichier in fichiers_b:
                    stats_a = fichiers_a[fichier]
                    stats_b = fichiers_b[fichier]

                    date_a = datetime.fromtimestamp(stats_a['modified_time'])
                    date_b = datetime.fromtimestamp(stats_b['modified_time'])
                    taille_a = stats_a['size']
                    taille_b = stats_b['size']

                    if date_a < date_b:
                        output_file.write(f"{fichier}: Plus ancien dans {current_a} que dans {current_b}\n")
                    elif date_a > date_b:
                        if taille_b > taille_a:
                            output_file.write(f"{fichier}: Plus récent dans {current_a} mais plus léger que dans {current_b}\n")
                        else:
                            output_file.write(f"{fichier}: Plus récent dans {current_a} et plus lourd ou égal que dans {current_b}\n")
                else:
                    output_file.write(f"{fichier}: Présent dans {current_a} mais absent de {current_b} au niveau {level}\n")

            # Ajouter les sous-dossiers communs pour une future comparaison au prochain niveau
            for fichier in fichiers_a:
                dossier_parent_a = os.path.dirname(os.path.join(current_a, fichier))  # Correction ici pour obtenir le chemin complet
                dossier_parent_b = os.path.join(current_b, os.path.basename(dossier_parent_a))  # Correction ici pour éviter os.path.relpath

                # Vérification avant d'ajouter à la pile
                if os.path.exists(dossier_parent_b) and os.path.isdir(dossier_parent_b):
                    # Ajouter les sous-dossiers dans la pile pour la prochaine itération
                    pile.append((dossier_parent_a, dossier_parent_b, level + 1))

if __name__ == "__main__":
    # Chemins des dossiers à comparer
    dossier_a = r"\\eDossier\sdossier\tdossier\rdossier\Hdossier dossier dossier"
    dossier_b = r"\\eDossier\sdossier\tdossier\rdossier\Hdossier dossier dossier B"

    # Lancer la comparaison et écrire les résultats dans un fichier texte
    comparer_dossiers_iteratif(dossier_a, dossier_b)

    print("Comparaison terminée ! Résultats enregistrés dans 'comparaison_fichiers.txt'.")