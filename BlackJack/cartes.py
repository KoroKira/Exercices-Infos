import random

# Fonction pour afficher la carte en ASCII
def print_card(rang, suite):
    haut = "┌─────────┐"
    bas = "└─────────┘"
    cote = "│         │"

    if rang == "10":  
        rang_droit = rang
        rang_gauche = rang
    else:
        rang_droit = rang + " "
        rang_gauche = " " + rang

    suite_ligne = f"│    {suite}    │"
    rang_ligne_gauche = f"│{rang_gauche}       │"
    rang_ligne_droit = f"│       {rang_droit}│"

    print(haut)
    print(rang_ligne_gauche)
    print(cote)
    print(suite_ligne)
    print(cote)
    print(rang_ligne_droit)
    print(bas)

# Classe Carte
class Carte:
    def __init__(self, suite, rang):
        self.suite = suite
        self.rang = rang

    def __str__(self):
        return f"{self.rang} de {self.suite}"

    def afficher(self):
        # Utilisation de la fonction ASCII pour afficher la carte
        print_card(self.rang, self.suite)

# Classe Deck (paquet de cartes)
class Deck:
    suites = ['♥', '♦', '♣', '♠']
    rangs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cartes = [Carte(suite, rang) for suite in self.suites for rang in self.rangs]
        self.melanger()

    def melanger(self):
        random.shuffle(self.cartes)

    def tirer(self):
        if len(self.cartes) > 0:
            return self.cartes.pop()
        else:
            return None

# Classe Main (main d'un joueur)
class Main:
    def __init__(self):
        self.cartes = []
    
    def ajouter_carte(self, carte):
        self.cartes.append(carte)

    def valeur(self):
        total = 0
        as_count = 0
        valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}

        for carte in self.cartes:
            total += valeurs[carte.rang]
            if carte.rang == 'A':
                as_count += 1

        # Ajustement si la valeur de l'As doit être 1
        while total > 21 and as_count:
            total -= 10
            as_count -= 1

        return total

    def afficher_main(self):
        for carte in self.cartes:
            carte.afficher()
            print()  # Ligne vide pour séparer les cartes visuellement

# Exemple d'utilisation
deck = Deck()
main_joueur = Main()

main_joueur.ajouter_carte(deck.tirer())
main_joueur.ajouter_carte(deck.tirer())

print("Main du joueur :")
main_joueur.afficher_main()
print("Valeur de la main :", main_joueur.valeur())
