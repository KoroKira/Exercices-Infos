# Affichage de la phrase à partir de la liste des mots :
ch = ['se', 'soigner', 'est', 'un', 'devoir', 'moral']
for mot in ch:
    print(mot, end=" ")
print()  # Pour un saut de ligne à la fin

# Afficher le texte à l'envers :
ch = ['se', 'soigner', 'est', 'un', 'devoir', 'moral']
for i in range(len(ch) - 1, -1, -1):
    print(ch[i], end=" ")
print()  # Pour un saut de ligne à la fin

# Afficher la phrase avec les mots dans le bon ordre et les caractères à l'envers :
ch = ['se', 'soigner', 'est', 'un', 'devoir', 'moral']
for mot in ch:
    print(mot[::-1], end=" ")
print()  # Pour un saut de ligne à la fin

# Afficher la phrase à l'envers et les lettres de chaque mot à l'envers :
ch = ['se', 'soigner', 'est', 'un', 'devoir', 'moral']
for i in range(len(ch) - 1, -1, -1):
    print(ch[i][::-1], end=" ")
print()  # Pour un saut de ligne à la fin


# Reprendre le programme de la question 4 en utilisant l'instruction while :
ch = ['se', 'soigner', 'est', 'un', 'devoir', 'moral']
i = len(ch) - 1
while i >= 0:
    print(ch[i][::-1], end=" ")
    i -= 1
print()  # Pour un saut de ligne à la fin

