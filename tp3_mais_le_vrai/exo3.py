# Initialisation des variables pour la suite de Fibonacci
# premier_terme et second_terme représentent les deux premiers termes de la suite
# compteur permet de suivre le nombre de termes affichés
premier_terme, second_terme, compteur = 1, 1, 1

# La boucle while s'exécute jusqu'à ce que nous ayons affiché les dix premiers termes
while compteur <= 10:
    # Affiche le terme actuel (second_terme) suivi d'une virgule, sauf pour le dernier terme
    if compteur == 10:
        print(second_terme)  # Dernier nombre sans virgule
    else:
        print(second_terme, end=", ")
    
    # Mise à jour des valeurs pour le prochain terme
    # premier_terme prend la valeur de second_terme
    # second_terme prend la valeur de la somme des deux termes précédents
    # compteur est incrémenté de 1 pour suivre le nombre de termes affichés
    premier_terme, second_terme, compteur = second_terme, premier_terme + second_terme, compteur + 1
