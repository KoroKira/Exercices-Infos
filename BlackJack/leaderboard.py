import json
import os

def afficher_leaderboard():
    """Affiche un classement des joueurs basé sur leur solde."""
    if not os.path.exists("joueur_donnees.json"):
        print("Aucun joueur enregistré pour le moment.")
        return

    # Charger les joueurs depuis le fichier JSON
    with open("joueur_donnees.json", "r") as f:
        joueurs = json.load(f)

    # Trier les joueurs par solde de manière décroissante
    joueurs = sorted(joueurs, key=lambda x: x["solde"], reverse=True)

    # Afficher le leaderboard
    print("\n--- Leaderboard des Joueurs ---")
    for i, joueur in enumerate(joueurs, start=1):
        print(f"{i}. {joueur['nom']} - {joueur['solde']} jetons")
    print("-------------------------------")

if __name__ == "__main__":
    afficher_leaderboard()
