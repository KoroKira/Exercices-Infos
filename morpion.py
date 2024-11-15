import random

def afficher_grille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 5)

def verifier_victoire(grille, symbole):
    for ligne in grille:
        if all([case == symbole for case in ligne]):
            return True

    for col in range(3):
        if grille[0][col] == grille[1][col] == grille[2][col] == symbole:
            return True

    if grille[0][0] == grille[1][1] == grille[2][2] == symbole:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == symbole:
        return True

    return False

def jouer(grille, symbole, joueur):
    print(f"Tour du joueur {joueur} ({symbole})")
    while True:
        try:
            x, y = [int(i) for i in input("Entrez les coordonnées x et y (entre 0 et 2, séparées par un espace) : ").split()]
            if 0 <= x < 3 and 0 <= y < 3:
                if grille[x][y] == " ":
                    grille[x][y] = symbole
                    break
                else:
                    print("Case déjà occupée. Veuillez réessayer.")
            else:
                print("Coordonnées hors limites. Veuillez entrer des valeurs entre 0 et 2.")
        except (ValueError, IndexError):
            print("Coordonnées invalides. Veuillez entrer deux nombres entre 0 et 2.")

    afficher_grille(grille)
    return verifier_victoire(grille, symbole)

def jouer_contre_joueur():
    grille = [[" " for _ in range(3)] for _ in range(3)]
    symboles = ["X", "O"]
    joueur = 0

    while True:
        if jouer(grille, symboles[joueur], joueur + 1):
            print(f"Le joueur {joueur + 1} a gagné !")
            break
        if all([case != " " for ligne in grille for case in ligne]):
            print("Match nul !")
            break
        joueur = (joueur + 1) % 2

def ordinateur_aleatoire(grille, symbole):
    while True:
        x, y = random.randint(0, 2), random.randint(0, 2)
        if grille[x][y] == " ":
            grille[x][y] = symbole
            break

def ordinateur_intelligent(grille, symbole_ordi, symbole_joueur):
    # Vérifier si l'ordinateur peut gagner en un coup
    for x in range(3):
        for y in range(3):
            if grille[x][y] == " ":
                grille[x][y] = symbole_ordi
                if verifier_victoire(grille, symbole_ordi):
                    return
                grille[x][y] = " "

    # Vérifier si le joueur peut gagner en un coup et bloquer
    for x in range(3):
        for y in range(3):
            if grille[x][y] == " ":
                grille[x][y] = symbole_joueur
                if verifier_victoire(grille, symbole_joueur):
                    grille[x][y] = symbole_ordi
                    return
                grille[x][y] = " "

    # Sinon, jouer aléatoirement
    ordinateur_aleatoire(grille, symbole_ordi)

def jouer_contre_ordinateur(intelligence_avancee=False):
    grille = [[" " for _ in range(3)] for _ in range(3)]
    symboles = ["X", "O"]

    while True:
        # Tour du joueur
        if jouer(grille, symboles[0], 1):
            print("Vous avez gagné !")
            break
        if all([case != " " for ligne in grille for case in ligne]):
            print("Match nul !")
            break

        # Tour de l'ordinateur
        print("Tour de l'ordinateur...")
        if intelligence_avancee:
            ordinateur_intelligent(grille, symboles[1], symboles[0])
        else:
            ordinateur_aleatoire(grille, symboles[1])

        afficher_grille(grille)

        if verifier_victoire(grille, symboles[1]):
            print("L'ordinateur a gagné !")
            break

def main():
    print("Bienvenue dans le jeu du Morpion !")
    while True:
        choix = input("Voulez-vous jouer contre un autre joueur (1), contre un ordinateur aléatoire (2) ou contre un ordinateur intelligent (3) ? ")
        if choix == "1":
            jouer_contre_joueur()
        elif choix == "2":
            jouer_contre_ordinateur(intelligence_avancee=False)
        elif choix == "3":
            jouer_contre_ordinateur(intelligence_avancee=True)
        else:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")

        rejouer = input("Voulez-vous rejouer ? (Oui/Non) : ")
        if rejouer.lower() != "oui":
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    main()
