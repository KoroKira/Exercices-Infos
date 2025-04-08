from creer_noeud import creer_noeud

def initialiser_jeu(): # Initialiser l'arbre avec deux animaux de base
    animal1 = input("Pensez à un premier animal : ")
    animal2 = input("Pensez à un second animal : ")
    question = input(f"Quelle question permet de distinguer {animal1} de {animal2} ? ")
    animal_oui = input(f"Quel animal répond 'oui' à cette question ? ({animal1}/{animal2}) : ")

    racine = creer_noeud(question, bool_question=True)
    if animal_oui.lower() == animal1.lower(): #La méthode lower() convertit tous les caractères alphabétiques d'une chaîne en minuscules. Elle est utile pour uniformiser les comparaisons de texte, car les majuscules et les minuscules ne sont pas égales en Python.
        racine["oui"] = creer_noeud(animal1)
        racine["non"] = creer_noeud(animal2)
    else:
        racine["oui"] = creer_noeud(animal2)
        racine["non"] = creer_noeud(animal1)
    
    return racine