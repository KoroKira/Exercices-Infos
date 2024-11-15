# blackjack.py

from cartes import Deck
from joueur_croupier import Joueur, Croupier

# Classe Blackjack
class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.joueur = Joueur("Joueur")
        self.croupier = Croupier()
        
    def distribuer_cartes(self):
        # Distribuer 2 cartes au joueur et au croupier
        for _ in range(2):
            self.joueur.hit(self.deck)
            self.croupier.hit(self.deck)

    def afficher_mains(self, show_croupier=False):
        self.joueur.afficher_main()
        if show_croupier:
            self.croupier.afficher_main()
        else:
            # Montrer une seule carte du croupier (une face cachée)
            print("Main du Croupier :")
            print("<Carte cachée>")
            self.croupier.main.cartes[1].afficher()

    def play_game(self):
        print("Début du jeu de Blackjack!")
        self.distribuer_cartes()

        # Afficher les mains initiales
        self.afficher_mains()

        # Tour du joueur
        while self.joueur.decide():
            self.joueur.hit(self.deck)
            if self.joueur.valeur_main() > 21:
                print("Le joueur a dépassé 21. Vous perdez !")
                return

        # Tour du croupier
        print("\nTour du croupier...")
        self.croupier.jouer(self.deck)

        # Afficher toutes les mains
        print("\nMains finales :")
        self.afficher_mains(show_croupier=True)

        # Comparer les mains pour déterminer le gagnant
        joueur_valeur = self.joueur.valeur_main()
        croupier_valeur = self.croupier.valeur_main()

        if croupier_valeur > 21:
            print("Le croupier a dépassé 21. Vous gagnez !")
        elif joueur_valeur > croupier_valeur:
            print("Vous gagnez !")
        elif joueur_valeur < croupier_valeur:
            print("Le croupier gagne !")
        else:
            print("Égalité !")

# Exemple d'utilisation
if __name__ == "__main__":
    jeu = Blackjack()
    jeu.play_game()
