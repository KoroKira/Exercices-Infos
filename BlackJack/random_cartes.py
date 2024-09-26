import random
from cartes import print_card # ca appelle la fonction print_card du fichier cartes.py

def main():
    rangs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suites = ["♠", "♥", "♦", "♣"]

    for _ in range(2):  # modifier 2, ca permet de générer un nombre de cartes précises
        rang = random.choice(rangs)
        suite = random.choice(suites)
        print_card(rang, suite)
        print()

if __name__ == "__main__":
    main()