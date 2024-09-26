# interface_utilisateur.py

from blackjack import Blackjack
from gestion_mises import JoueurAvecSolde

class BlackjackConsole(Blackjack):
    def __init__(self):
        super().__init__()
        self.joueur = JoueurAvecSolde("Joueur", 100)  # Le joueur avec solde

    def demander_mise(self):
        while True:
            try:
                montant = int(input("Entrez votre mise : "))
                if self.joueur.bet(montant):
                    break
            except ValueError:
                print("Veuillez entrer un montant valide.")

    def demander_action(self):
        actions = {"1": "hit", "2": "stand", "3": "double_down"}
        while True:
            print("\nChoisissez une action :")
            print("1. Tirer une carte (hit)")
            print("2. Rester (stand)")
            print("3. Doubler la mise (double_down)")

            choix = input("Votre choix : ")
            if choix in actions:
                return actions[choix]
            else:
                print("Choix invalide. Veuillez réessayer.")

    def play_game(self):
        print("Début du jeu de Blackjack avec gestion des mises !")
        self.demander_mise()
        self.distribuer_cartes()

        # Tour du joueur
        while True:
            self.afficher_mains()
            action = self.demander_action()
            if action == "hit":
                self.joueur.hit(self.deck)
                if self.joueur.valeur_main() > 21:
                    print("Le joueur a dépassé 21. Vous perdez !")
                    self.joueur.perdre()
                    return
            elif action == "stand":
                break
            elif action == "double_down":
                if not self.joueur.double_down():
                    continue  # Si on ne peut pas doubler, re-demander l'action
                self.joueur.hit(self.deck)
                if self.joueur.valeur_main() > 21:
                    print("Le joueur a dépassé 21 après avoir doublé la mise. Vous perdez !")
                    self.joueur.perdre()
                    return
                break

        # Tour du croupier
        print("\nTour du croupier...")
        self.croupier.jouer(self.deck)

        # Afficher toutes les mains
        print("\nMains finales :")
        self.afficher_mains(show_croupier=True)

        # Comparer les mains pour déterminer le gagnant
        joueur_valeur = self.joueur.valeur_main()
        croupier_valeur = self.croupier.valeur_main()

        if croupier_valeur > 21 or joueur_valeur > croupier_valeur:
            print("Vous gagnez !")
            self.joueur.gagner()
        elif joueur_valeur < croupier_valeur:
            print("Le croupier gagne !")
            self.joueur.perdre()
        else:
            print("Égalité !")
            self.joueur.egalite()

# Exemple d'utilisation
if __name__ == "__main__":
    jeu = BlackjackConsole()
    jeu.play_game()
