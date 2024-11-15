# triangle de pascal
# demander à l'utilisateur un nombre de lignes N
# afficher les N premières lignes du triangle de Pascal
# bonus: si l'utilisateur dit "ligne X", imprimer ligne X du triangle de Pascal

# on veut que ca soit des * pour le triangle de pascal. On veut qu'il soit centré aussi
# au lieu que ca soit des chiffres, mettre un *

def triangle_pascal(n):
    # On initialise le triangle de Pascal avec la première ligne contenant un seul élément '1'
    triangle = [[1]]
    # Boucle pour générer chaque ligne du triangle de Pascal
    for i in range(1, n):
        # On commence chaque ligne avec un '1'
        ligne = [1]
        # Boucle pour calculer les valeurs intermédiaires de la ligne
        for j in range(1, i):
            # Chaque élément est la somme des deux éléments situés au-dessus dans le triangle
            ligne.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # On termine chaque ligne avec un '1'
        ligne.append(1)
        # On ajoute la ligne complète au triangle
        triangle.append(ligne)
    return triangle

def imprimer_ligne(triangle, x):
    # Vérifie si la ligne demandée est dans les limites du triangle
    if 0 <= x < len(triangle):
        print(triangle[x])
    else:
        print(f"Ligne {x} n'existe pas dans le triangle de Pascal généré.")

def main():
    # Demande à l'utilisateur de saisir un nombre de lignes pour le triangle de Pascal
    n = int(input("Veuillez saisir un nombre de lignes : "))
    # Génère le triangle de Pascal
    triangle = triangle_pascal(n)
    
    # Affiche le triangle de Pascal
    for i in range(n):
        print(" " * (n - i), end="")
        for j in range(i + 1):
            print("*", end=" ")
        print()
    
    # Demande à l'utilisateur s'il veut imprimer une ligne spécifique
    ligne_specifique = input("Si vous voulez imprimer une ligne spécifique, entrez 'ligne X' (par exemple, 'ligne 3') : ")
    if ligne_specifique.startswith("ligne "):
        try:
            x = int(ligne_specifique.split()[1])
            imprimer_ligne(triangle, x)
        except ValueError:
            print("Entrée invalide. Veuillez entrer 'ligne X' avec X comme un nombre entier.")

if __name__ == '__main__':
    # Exécute la fonction main si le script est exécuté directement
    main()