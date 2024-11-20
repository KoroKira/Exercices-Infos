# Initialisation :
animaux = {}

def jouer_partie():
    global animaux

    # Si c'est la première partie, demander deux animaux pour initier le jeu
    if not animaux:
        initialiser_jeu()

    # Boucle de jeu
    while True:
        print("\nPense à un animal et je vais essayer de le deviner.")
        deviner_animal()

        # Demander si l'utilisateur veut rejouer
        rejouer = input("\nVeux-tu rejouer une partie ? (oui/non) : ").strip().lower()
        if rejouer != "oui":
            print("Merci d'avoir joué !")
            break

def initialiser_jeu():
    """Initialiser la première question pour démarrer le jeu."""
    animal_1 = input("Saisie un premier animal : ")
    animal_2 = input("Saisie un second animal : ")

    # Assurer que les deux animaux sont différents
    while animal_1 == animal_2:
        print("Choisis 2 animaux différents.")
        animal_1 = input("Saisie un premier animal : ")
        animal_2 = input("Saisie un second animal : ")

    # Demander une question pour différencier les deux animaux
    question = input(f"Saisie une question pour distinguer {animal_1} de {animal_2} : ")
    animal_oui = input(f"Quel animal répond par oui à la question ? ({animal_1}/{animal_2}) : ")

    # Ajouter la distinction à la mémoire
    animal_non = animal_1 if animal_oui == animal_2 else animal_2
    animaux["question"] = (question, {True: animal_oui, False: animal_non})

def deviner_animal():
    """Utiliser les questions pour deviner un animal."""
    noeud = "question"  # On commence toujours au premier niveau
    parent = None  # Garder une référence au parent pour ajouter une nouvelle distinction
    parent_chemin = None  # Garder le chemin (True/False) à modifier dans le parent
    réponse = None

    # Parcourir les questions jusqu'à deviner l'animal
    while isinstance(animaux[noeud], tuple):
        question, chemins = animaux[noeud]
        réponse = input(f"{question} (oui/non) : ").strip().lower() == "oui"

        # Si le chemin actuel n'existe pas encore, on interrompt la recherche
        if chemins[réponse] not in animaux:
            parent = noeud
            parent_chemin = réponse
            noeud = chemins[réponse]
            break

        parent = noeud  # Mémoriser le parent pour d'éventuelles modifications
        parent_chemin = réponse
        noeud = chemins[réponse]  # Descendre dans l'arbre

    # Vérifier si l'animal deviné est correct
    animal_trouvé = noeud
    confirmation = input(f"Est-ce que c'est {animal_trouvé} ? (oui/non) : ").strip().lower()
    if confirmation == "oui":
        print(f"J'ai trouvé, l'animal auquel tu penses est {animal_trouvé} !")
    else:
        ajouter_nouvelle_distinction(parent, parent_chemin, animal_trouvé)

def ajouter_nouvelle_distinction(parent, parent_chemin, animal_trouvé):
    """Ajouter une nouvelle question pour différencier un animal."""
    nouvel_animal = input("Quel était l'animal auquel tu pensais ? : ")
    nouvelle_question = input(f"Quelle question permet de différencier {animal_trouvé} de {nouvel_animal} ? : ")
    réponse_oui = input(f"Qui répond par oui à cette question ? ({nouvel_animal}/{animal_trouvé}) : ").strip().lower() == nouvel_animal.lower()

    # Ajouter la nouvelle question et les animaux à la mémoire
    animaux[nouvel_animal] = None
    animaux[animal_trouvé] = None
    animaux[parent] = (
        nouvelle_question,
        {True: nouvel_animal if réponse_oui else animal_trouvé,
         False: animal_trouvé if réponse_oui else nouvel_animal}
    )
    print(f"Merci, j'ai ajouté {nouvel_animal} et sa question à ma mémoire.")

# Appel initial pour démarrer le jeu
jouer_partie()
