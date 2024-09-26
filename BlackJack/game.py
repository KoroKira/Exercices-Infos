# game.py

from interface_utilisateur import BlackjackConsole

def main():
    print("Bienvenue au jeu de Blackjack !")
    jeu = BlackjackConsole()
    jeu.play_game()

if __name__ == "__main__":
    main()
