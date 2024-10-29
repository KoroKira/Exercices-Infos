import random

# Fonction pour lire les visuels du pendu depuis un fichier
def read_hangman_pics(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # On sépare les visuels à chaque ligne vide (c'est de l'ascii art)
        return content.split("\n\n")

# Lire les visuels du fichier pendu.txt
HANGMAN_PICS = read_hangman_pics('/Users/guilhem/Documents/GitHub/Exercices-Infos/Pendu/pendu.txt')

# Liste de mots par difficulté
def read_words_from_file(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            words.extend(line.strip().split())
    return words

easy_words = read_words_from_file('/Users/guilhem/Documents/GitHub/Exercices-Infos/Pendu/easy.txt')
medium_words = read_words_from_file('/Users/guilhem/Documents/GitHub/Exercices-Infos/Pendu/medium.txt')
hard_words = read_words_from_file('/Users/guilhem/Documents/GitHub/Exercices-Infos/Pendu/hard.txt')

WORDS = {
    'easy': easy_words,
    'medium': medium_words,
    'hard': hard_words
}

# Choisir la difficulté (pour avoir essayé, le 3 est le plus simple à résoudre)
def choose_difficulty():
    while True:
        print("Choisissez une difficulté: (1) Facile, (2) Moyenne, (3) Difficile")
        choice = input("> ")
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print("Choix non valide.")

# Fonction pour afficher l'état actuel du mot deviné
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '.' for letter in word])

# Fonction principale du jeu du pendu
def play_hangman():
    difficulty = choose_difficulty()
    word = random.choice(WORDS[difficulty]).upper()
    guessed_letters = {word[0], word[-1]}  # On commence avec la première et la dernière lettre ainsi que toutes les lettres communes
    remaining_attempts = len(HANGMAN_PICS) - 1
    tried_letters = set()  # Lettres essayées

    while remaining_attempts > 0:
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - remaining_attempts])
        print(f"Mot à deviner: {display_word(word, guessed_letters)}")
        print(f"Lettres essayées: {', '.join(sorted(tried_letters))}")
        print(f"Essais restants: {remaining_attempts}")
        
        guess = input("Devinez une lettre: ").upper()

        if guess in tried_letters:
            print("Vous avez déjà essayé cette lettre.")
            continue
        
        tried_letters.add(guess)

        if guess in word:
            guessed_letters.add(guess)
            print(f"Bien joué ! La lettre {guess} est dans le mot.")
        else:
            remaining_attempts -= 1
            print(f"Raté ! La lettre {guess} n'est pas dans le mot.")
        
        # Si toutes les lettres du mot sont devinées
        if set(word) == guessed_letters:
            print(f"Félicitations ! Vous avez trouvé le mot : {word}")
            break
    else:
        print(HANGMAN_PICS[-1])
        print(f"Vous avez perdu ! Le mot était : {word}")

# Lancer le jeu
if __name__ == "__main__":
    play_hangman()
