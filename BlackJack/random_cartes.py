import random
from cartes import print_card

def main():
    rangs = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suites = ["♠", "♥", "♦", "♣"]

    for _ in range(2):  
        rang = random.choice(rangs)
        suite = random.choice(suites)
        print_card(rang, suite)
        print()

if __name__ == "__main__":
    main()