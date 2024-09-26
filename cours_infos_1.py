# Programme initial (nul)

nombre1 = input("Entrer nombre 1:")
nombre2 = input("Entrer nombre 2:")
print("nombre 1 + nombre 2 =",nombre1+nombre2)

## WOW ON A 12, PCQ ON CONCATÈNE DES STRINGS ENTRE EUX
## ON DOIT CONVERTIR LES STRINGS EN INT POUR FAIRE UNE ADDITION

# Programme 1
nombre1 = int(input("Entrer nombre 1:"))
nombre2 = int(input("Entrer nombre 2:"))
resultat = nombre1 + nombre2
print("nombre 1 + nombre 2 =",resultat)

## C'EST MIEUX MAINTENANT, C'EST PLUS CLAIR ET CA MARCHE

# Programme 2
nombre1 = int(input("Entrer nombre 1:"))
nombre2 = int(input("Entrer nombre 2:"))
resultat = nombre1 + nombre2
print(f"{nombre1} + {nombre2} = {resultat}")

# Programme 3
nombre1 = int(input("Entrer nombre 1:"))
nombre2 = int(input("Entrer nombre 2:"))
if nombre1 > nombre2:
    resultat = nombre1 - nombre2
    print(f"{nombre1} - {nombre2} = {resultat}")
else:
    resultat = nombre2 - nombre1
    print(f"{nombre2} - {nombre1} = {resultat}")
    
# Programme 4
# Ici ce qu'on nous demande, c'est de lire du float au lieu du int
nombre1 = float(input("Entrer nombre 1:"))
nombre2 = float(input("Entrer nombre 2:"))
resultat = nombre1 + nombre2
print(f"La somme des deux nombres = {resultat} et la partie entière de cette somme = {int(resultat)}")

# Programme 5
# Ici ce qu'on nous demande, c'est de remplacer le point par une virgule 
nombre1 = float(input("Entrer nombre 1:"))
nombre2 = float(input("Entrer nombre 2:"))
resultat = nombre1 + nombre2
print(f"{nombre1} + {nombre2} = {str(resultat).replace('.', ',')}")