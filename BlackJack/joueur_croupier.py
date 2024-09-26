# joueur_croupier.py

from cartes import Carte, Deck, Main

# Classe Joueur
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = Main()

    def hit(self, deck):
        carte = deck.tirer()
        if carte:
            self.main.ajouter_carte(carte)
            print(f"{self.nom} a tiré : {carte}")
        else:
            print("Le deck est vide !")

    def afficher_main(self):
        print(f"Main de {self.nom} :")
        self.main.afficher_main()

    def valeur_main(self):
        return self.main.valeur()

    def decide(self):
        # Exemple simple : Demander à l'utilisateur s'il veut continuer ou non
        decision = input(f"{self.nom}, voulez-vous tirer une autre carte ? (oui/non): ").lower()
        return decision == "oui"

# Classe Croupier (hérite de Joueur)
class Croupier(Joueur):
    def __init__(self):
        super().__init__("Croupier")

    def jouer(self, deck):
        while self.valeur_main() < 17:
            self.hit(deck)
        print(f"Le croupier s'arrête avec une main de valeur {self.valeur_main()}.")
