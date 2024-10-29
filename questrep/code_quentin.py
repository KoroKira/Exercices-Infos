# Initialisation :

# Fonction pour lancer une partie

def jouer_partie(): # def permet de réutiliser le code (donc de relancer une partie)

    # Demander le 1er animal à l'utilisateur
    animal_1 = input("Saisie un premier animal : ")

    # Demander le second animal à l'utilisateur
    animal_2 = input("Saisie un second animal : ")

    # Boucler si les 2 animaux sont identique pour inviter l'utilisateur à prendre 2 animaux différents
    while animal_1 == animal_2:
        print("Choisis 2 animaux différents ")
        animal_1 = input("Saisie un premier animal ")
        animal_2 = input("Saisie un second animal ")

    # Demander à l'utilisateur de choisir une question permettant de différencier les 2 animaux
    distinguer = input("Saisie une question permettant de distinguer " + animal_1 + " de " + animal_2 + " : ")

    # Demander à l'utilisateur quel animal répond positivement à la question 
    animal_oui = input("Quel animal répond par oui à cette question ? ")

    # Par conséquent, si un animal répond positivement à la question, l'autre répondra négativement
    animal_non = animal_1 if animal_oui == animal_2 else animal_2

    # Jeu :

    #Première réponse à la question d'avant
    réponse_1 = input("L'animal auquel tu penses. " + distinguer + "(oui/non) : ").lower() # .lower() permet à l'utilisateur de répondre Oui ou OUI ou OUi et qu'il n'y est pas d'erreur

    oui = "oui"

    # Si la réponse est positive à la 1ère question
    if réponse_1 == "oui":
        # Demande si c'est l'animal déjà connu dans la banque de donnée
        réponse_oui = input("Est-ce " + animal_oui + " ? (oui/non) : ").lower()
        # Si la réponse est oui alors l'ordinateur à trouvé
        if réponse_oui == "oui":
            print ("J'ai trouvé, l'animal auquel tu penses est " + animal_oui)
        # Sinon il va falloir rentrer ce nouvel animal dans la banque de donnée
        else:
            solution_oui = input("Quel était l'animal ? ")
            différence_oui = input("Quelle question les différencie ? ")
            enregistre_solution_oui = input("Qui répond positivement à la question : " + différence_oui + " ? " + solution_oui + " (tapez 1) " + animal_oui + " (tapez 2) : ")

    # Si la réponse est négative à la 1ère question 
    else:
        # Demande si c'est l'animal déjà connu dans la banque de donnée
        reponse_non = input("Est-ce " + animal_non + " ? (oui/non) : ").lower()
        # Si la réponse est oui alors l'ordinateur à trouvé
        if reponse_non == oui:
            print ("J'ai trouvé, l'animal auquel tu penses est " + animal_non)
        # Sinon il va falloir rentrer ce nouvel animal dans la banque de donnée
        else:
            solution_non = input("Quel était l'animal ? ")
            différence_non = input("Quelle question les différencie ? ")
            enregistre_solution_non = input("Qui répond positivement à la question : " + différence_non + " ? " + solution_non + " (tapez 1) " + animal_non + " (tapez 2) : ")

# Boucle pour gérer les parties
def lancer_jeu():
    while True:
        jouer_partie()

        # Demander si l'utilisateur veux rejouer une partie
        rejouer = input("Veux-tu rejouer une partie ? (oui/non) : ").lower()
        if rejouer != "oui":
            print("Merci d'avoir joué !")
            break

# Appel initial pour démarrer le jeu
lancer_jeu()