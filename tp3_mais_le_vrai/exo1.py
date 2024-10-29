# Afficher les caractères d'une chaîne avec un espace entre eux :

maChaine = 'Bonjour'
i = 0
while i < len(maChaine):
    print(maChaine[i], end=" ")
    i += 1
print()  # Pour un saut de ligne à la fin

# Afficher une chaîne à l'envers :

maChaine = 'Bonjour'
i = len(maChaine) - 1
while i >= 0:
    print(maChaine[i], end="")
    i -= 1
print()  # Pour un saut de ligne à la fin

# Détecter si une chaîne est un palindrome :

maChaine = 'laval'
i = 0
est_palindrome = True
while i < len(maChaine) // 2:
    if maChaine[i] != maChaine[len(maChaine) - 1 - i]:
        est_palindrome = False
        break
    i += 1
print("Palindrome :", est_palindrome)

# Déterminer si une chaîne contient le caractère « e » :

maChaine = 'Bonjour'
i = 0
contient_e = False
while i < len(maChaine):
    if maChaine[i] == 'e':
        contient_e = True
        break
    i += 1
print("Contient 'e' :", contient_e)

# Compter le nombre d’occurrences du caractère « e » :

maChaine = 'Bonjour'
i = 0
compteur_e = 0
while i < len(maChaine):
    if maChaine[i] == 'e':
        compteur_e += 1
    i += 1
print("Occurrences de 'e' :", compteur_e)
