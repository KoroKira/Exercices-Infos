import random # Importer le module random

def deviner_nombre(): # Définition de la fonction deviner_nombre
    print("Bienvenue dans le jeu de deviner un nombre !") # Afficher un message de bienvenue
    mode = input("Voulez-vous deviner un nombre (1) ou faire deviner un nombre (2) ? ") # Demander à l'utilisateur de choisir un mode
    if mode == "1": # Si l'utilisateur choisit le mode 1
        deviner_nombre_utilisateur() # Appeler la fonction deviner_nombre_utilisateur
    elif mode == "2":  # Si l'utilisateur choisit le mode 2
        deviner_nombre_ordi() # Appeler la fonction deviner_nombre_ordi
    else: # Si l'utilisateur choisit un mode invalide
        print("Mode invalide. Veuillez choisir 1 ou 2.") # Afficher un message d'erreur

def deviner_nombre_utilisateur(): # Définition de la fonction deviner_nombre_utilisateur
    print("Vous devez deviner le nombre de l'ordinateur.") # Afficher un message
    min_val = int(input("Entrez la valeur minimale de l'intervalle : ")) # Demander à l'utilisateur de saisir la valeur minimale de l'intervalle
    max_val = int(input("Entrez la valeur maximale de l'intervalle : ")) # Demander à l'utilisateur de saisir la valeur maximale de l'intervalle
    nombre_secret = random.randint(min_val, max_val) # Générer un nombre aléatoire dans l'intervalle
    essais = int(input("Entrez le nombre d'essais : ")) # Demander à l'utilisateur de saisir le nombre d'essais
    print(f"L'ordinateur a choisi un nombre entre {min_val} et {max_val}.") # Afficher le message avec l'intervalle choisi
    for i in range(essais): # Boucle pour le nombre d'essais
        essais_restants = essais - i # Calculer le nombre d'essais restants
        devine = int(input(f"Devinez le nombre (il vous reste {essais_restants} essais) : ")) # Demander à l'utilisateur de deviner le nombre
        if devine == nombre_secret: # Si l'utilisateur devine le nombre
            print("Bravo ! Vous avez trouvé le nombre de l'ordinateur.") # Afficher un message de réussite
            return # Sortir de la fonction
        elif devine < nombre_secret: # Si la devine est inférieure au nombre secret
            print("Le nombre est plus grand.") # Afficher un message
        else: # Sinon
            print("Le nombre est plus petit.") # Afficher un message
    print(f"Vous avez épuisé tous vos essais. Le nombre de l'ordinateur était {nombre_secret}.") # Afficher un message d'échec

def deviner_nombre_ordi(): # Définition de la fonction deviner_nombre_ordi
    print("L'ordinateur doit deviner votre nombre.") # Afficher un message
    min_val = int(input("Entrez la valeur minimale de l'intervalle : ")) # Demander à l'utilisateur de saisir la valeur minimale de l'intervalle
    max_val = int(input("Entrez la valeur maximale de l'intervalle : ")) # Demander à l'utilisateur de saisir la valeur maximale de l'intervalle
    nombre_secret = int(input("Entrez votre nombre secret : ")) # Demander à l'utilisateur de saisir son nombre secret
    essais = int(input("Entrez le nombre d'essais de l'ordinateur : "))  # Demander à l'utilisateur de saisir le nombre d'essais de l'ordinateur
    print(f"Vous avez choisi le nombre {nombre_secret}.") # Afficher le nombre secret choisi par l'utilisateur
    for i in range(essais): # Boucle pour le nombre d'essais
        essais_restants = essais - i # Calculer le nombre d'essais restants
        devine = random.randint(min_val, max_val) # L'ordinateur devine un nombre aléatoire dans l'intervalle
        print(f"L'ordinateur devine le nombre {devine}.") # Afficher le nombre deviné par l'ordinateur
        if devine == nombre_secret: # Si l'ordinateur devine le nombre
            print("L'ordinateur a trouvé votre nombre.") # Afficher un message de réussite
            return # Sortir de la fonction
        elif devine < nombre_secret: # Si la devine est inférieure au nombre secret
            print("Le nombre est plus grand.") # Afficher un message
            min_val = devine + 1 # Mettre à jour la valeur minimale
        else: # Sinon
            print("Le nombre est plus petit.") # Afficher un message
            max_val = devine - 1 # Mettre à jour la valeur maximale
    print(f"L'ordinateur n'a pas réussi à trouver votre nombre. Le nombre était {nombre_secret}.") # Afficher un message d'échec

if __name__ == '__main__': # Si le script est exécuté directement
    deviner_nombre() # Appeler la fonction deviner_nombre