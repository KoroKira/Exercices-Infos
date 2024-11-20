import json
import os
from blackjack import Blackjack
from gestion_mises import JoueurAvecSolde
from leaderboard import afficher_leaderboard  # Importer la fonction leaderboard

class BlackjackConsole(Blackjack):
    def __init__(self):
        super().__init__()
        self.nom_joueur, self.joueur = self.menu_principal()

    def menu_principal(self):
        """Menu principal pour choisir de jouer, afficher le leaderboard ou gérer les joueurs."""
        while True:
            print("\n1. Jouer avec un joueur existant ou créer un nouveau joueur")
            print("2. Afficher le leaderboard")
            print("3. Quitter")
            choix = input("Votre choix : ")

            if choix == "1":
                return self.gestion_joueurs()
            elif choix == "2":
                afficher_leaderboard()  # Appeler la fonction pour afficher le leaderboard
            elif choix == "3":
                print("Au revoir!")
                exit()
            else:
                print("Choix invalide, veuillez réessayer.")

    def gestion_joueurs(self):
        """Gestion du choix de joueur : charger, créer ou supprimer un joueur."""
        while True:
            print("\n1. Jouer avec un joueur existant")
            print("2. Créer un nouveau joueur")
            print("3. Supprimer un joueur")
            choix = input("Votre choix : ")

            if choix == "1":
                return self.charger_joueur()
            elif choix == "2":
                return self.creer_nouveau_joueur()
            elif choix == "3":
                self.supprimer_joueur()
            else:
                print("Choix invalide, veuillez réessayer.")

    def charger_joueur(self):
        """Charge un joueur existant depuis le fichier JSON."""
        joueurs = self.lire_joueurs()
        if not joueurs:
            print("Aucun joueur trouvé. Veuillez créer un nouveau joueur.")
            return self.creer_nouveau_joueur()

        print("\nJoueurs disponibles :")
        for i, joueur in enumerate(joueurs):
            print(f"{i + 1}. {joueur['nom']} (Solde: {joueur['solde']} jetons)")
        
        choix = int(input("Choisissez un joueur par numéro : ")) - 1
        if 0 <= choix < len(joueurs):
            joueur_data = joueurs[choix]
            print(f"Bienvenue de retour, {joueur_data['nom']}! Solde actuel : {joueur_data['solde']} jetons")
            return joueur_data['nom'], JoueurAvecSolde(joueur_data['nom'], joueur_data['solde'])
        else:
            print("Choix invalide.")
            return self.charger_joueur()

    def creer_nouveau_joueur(self):
        """Crée un nouveau joueur avec un solde de départ de 100 jetons."""
        nom = input("Entrez le nom du nouveau joueur : ")
        joueur = JoueurAvecSolde(nom, 100)
        self.sauvegarder_joueur(joueur)
        print(f"Bienvenue, {nom}! Vous commencez avec 100 jetons.")
        return nom, joueur

    def supprimer_joueur(self):
        """Supprime un joueur enregistré."""
        joueurs = self.lire_joueurs()
        if not joueurs:
            print("Aucun joueur à supprimer.")
            return

        print("\nJoueurs disponibles pour suppression :")
        for i, joueur in enumerate(joueurs):
            print(f"{i + 1}. {joueur['nom']}")

        choix = int(input("Choisissez un joueur à supprimer par numéro : ")) - 1
        if 0 <= choix < len(joueurs):
            joueur_supprime = joueurs.pop(choix)
            print(f"Le joueur {joueur_supprime['nom']} a été supprimé.")
            self.ecrire_joueurs(joueurs)
        else:
            print("Choix invalide.")

    def lire_joueurs(self):
        """Lit tous les joueurs à partir du fichier JSON."""
        if os.path.exists("joueur_donnees.json"):
            with open("joueur_donnees.json", "r") as f:
                return json.load(f)
        return []

    def ecrire_joueurs(self, joueurs):
        """Écrit la liste de tous les joueurs dans le fichier JSON."""
        with open("joueur_donnees.json", "w") as f:
            json.dump(joueurs, f)

    def sauvegarder_joueur(self, joueur):
        """Sauvegarde un joueur dans le fichier JSON."""
        joueurs = self.lire_joueurs()
        for j in joueurs:
            if j["nom"] == joueur.nom:
                j["solde"] = joueur.solde
                break
        else:
            joueurs.append({"nom": joueur.nom, "solde": joueur.solde})
        
        self.ecrire_joueurs(joueurs)

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
        while True:
            print("\nDébut du jeu de Blackjack avec gestion des mises !")
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
                        self.sauvegarder_joueur(self.joueur)
                        break
                elif action == "stand":
                    break
                elif action == "double_down":
                    if not self.joueur.double_down():
                        continue  # Si on ne peut pas doubler, re-demander l'action
                    self.joueur.hit(self.deck)
                    if self.joueur.valeur_main() > 21:
                        print("Le joueur a dépassé 21 après avoir doublé la mise. Vous perdez !")
                        self.joueur.perdre()
                        self.sauvegarder_joueur(self.joueur)
                        break
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

            # Sauvegarde des données après la partie
            print("Partie terminée. Au revoir, {} !".format(self.joueur.nom))
            self.sauvegarder_joueur(self.joueur)

            # Demander si le joueur veut rejouer
            rejouer = input("Pour récupérer vos gains, faites o : ")
            if rejouer.lower() != 'o':
                print("Merci d'avoir joué ! L'addiction au jeu est dangereuse pour la santé.")
                break

# Exemple d'utilisation
#if __name__ == "__main__":
#    jeu = BlackjackConsole()
#    jeu.play_game()
