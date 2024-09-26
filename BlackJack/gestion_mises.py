# gestion_mises.py

from blackjack import Blackjack
from joueur_croupier import Joueur, Croupier

class JoueurAvecSolde(Joueur):
    def __init__(self, nom, solde_initial=100):
        super().__init__(nom)
        self.solde = solde_initial
        self.mise = 0

    def bet(self, montant):
        if montant > self.solde:
            print("Vous n'avez pas assez de solde pour miser cette somme.")
            return False
        else:
            self.mise = montant
            self.solde -= montant
            print(f"{self.nom} a misé {self.mise}. Solde restant : {self.solde}")
            return True

    def double_down(self):
        if self.mise * 2 > self.solde:
            print("Vous n'avez pas assez de solde pour doubler la mise.")
            return False
        else:
            self.solde -= self.mise
            self.mise *= 2
            print(f"{self.nom} a doublé la mise. Nouvelle mise : {self.mise}. Solde restant : {self.solde}")
            return True

    def gagner(self):
        gains = self.mise * 2
        self.solde += gains
        print(f"{self.nom} gagne {gains}. Nouveau solde : {self.solde}")

    def perdre(self):
        print(f"{self.nom} perd {self.mise}. Solde restant : {self.solde}")

    def egalite(self):
        self.solde += self.mise
        print(f"Égalité. {self.nom} récupère sa mise. Solde : {self.solde}")

# Exemple d'utilisation
if __name__ == "__main__":
    joueur = JoueurAvecSolde("Joueur", 100)
    joueur.bet(20)
    joueur.double_down()
    joueur.gagner()
