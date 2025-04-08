from creer_noeud import creer_noeud
from initialiser_jeu import initialiser_jeu
from poser_question import poser_question

# Fonction principale pour jouer au jeu
def jouer(racine):
    while True:
        print("\nPensez à un animal, et je vais essayer de le deviner.")
        poser_question(racine)
        rejouer = input("Voulez-vous jouer à nouveau ? (oui/non) : ").strip().lower()
        if rejouer != "oui":
            print("Merci d'avoir joué !")
            break

# Lancer le jeu
racine = initialiser_jeu()
jouer(racine)
