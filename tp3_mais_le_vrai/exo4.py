# Étape 1
age = int(input("Entrez l'âge du jeune (ou un nombre négatif pour arrêter) : "))

if 5 <= age <= 7:
    print("Il est de la tranche 5 à 7 ans")
elif 8 <= age <= 10:
    print("Il est de la tranche 8 à 10 ans")
elif 11 <= age <= 15:
    print("Il est de la tranche 11 à 15 ans")
elif 16 <= age <= 20:
    print("Il est de la tranche 16 à 20 ans")
else:
    print("Âge non classé")


# Étape 2
count_5_7 = 0
count_8_10 = 0
count_11_15 = 0
count_16_20 = 0
count_non_classe = 0

for _ in range(20):
    age = int(input("Entrez l'âge du suivant jeune : "))
    
    if 5 <= age <= 7:
        count_5_7 += 1
    elif 8 <= age <= 10:
        count_8_10 += 1
    elif 11 <= age <= 15:
        count_11_15 += 1
    elif 16 <= age <= 20:
        count_16_20 += 1
    else:
        count_non_classe += 1

print(f"Nombre de jeunes ages de 5 à 7 ans = {count_5_7}")
print(f"Nombre de jeunes ages de 8 à 10 ans = {count_8_10}")
print(f"Nombre de jeunes ages de 11 à 15 ans = {count_11_15}")
print(f"Nombre de jeunes ages de 16 à 20 ans = {count_16_20}")
print(f"Nombre de jeunes non classés = {count_non_classe}")


# Étape 3
count_5_7 = 0
count_8_10 = 0
count_11_15 = 0
count_16_20 = 0
count_non_classe = 0

total_jeunes = int(input("Entrez le nombre total de jeunes à classer : "))

for _ in range(total_jeunes):
    age = int(input("Entrez l'âge du suivant jeune : "))
    
    if 5 <= age <= 7:
        count_5_7 += 1
    elif 8 <= age <= 10:
        count_8_10 += 1
    elif 11 <= age <= 15:
        count_11_15 += 1
    elif 16 <= age <= 20:
        count_16_20 += 1
    else:
        count_non_classe += 1

print(f"Nombre de jeunes ages de 5 à 7 ans = {count_5_7}")
print(f"Nombre de jeunes ages de 8 à 10 ans = {count_8_10}")
print(f"Nombre de jeunes ages de 11 à 15 ans = {count_11_15}")
print(f"Nombre de jeunes ages de 16 à 20 ans = {count_16_20}")
print(f"Nombre de jeunes non classés = {count_non_classe}")


# Étape 4
count_5_7 = 0
count_8_10 = 0
count_11_15 = 0
count_16_20 = 0
count_non_classe = 0
continuer = True

while continuer:
    age = int(input("Entrez l'âge du jeune (ou un nombre négatif pour arrêter) : "))
    
    if age < 0:
        continuer = False
    else:
        if 5 <= age <= 7:
            count_5_7 += 1
        elif 8 <= age <= 10:
            count_8_10 += 1
        elif 11 <= age <= 15:
            count_11_15 += 1
        elif 16 <= age <= 20:
            count_16_20 += 1
        else:
            count_non_classe += 1

print(f"Nombre de jeunes ages de 5 à 7 ans = {count_5_7}")
print(f"Nombre de jeunes ages de 8 à 10 ans = {count_8_10}")
print(f"Nombre de jeunes ages de 11 à 15 ans = {count_11_15}")
print(f"Nombre de jeunes ages de 16 à 20 ans = {count_16_20}")
print(f"Nombre de jeunes non classés = {count_non_classe}")
