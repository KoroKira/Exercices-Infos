from apprendre_nouvel_animal import apprendre_nouvel_animal

# Fonction pour poser une question
def poser_question(noeud):
    if noeud["bool_question"]:
        reponse = input(f"{noeud['donnees']} (oui/non) : ").strip().lower() #La méthode strip() supprime tous les espaces (et certains caractères spéciaux comme \n, \t) au début et à la fin d'une chaîne. Elle est utile pour nettoyer une entrée utilisateur ou une chaîne de caractères.
        if reponse == "oui":                                                #Les deux méthodes sont souvent utilisées ensemble pour nettoyer et uniformiser une entrée utilisateur.
            poser_question(noeud["oui"])
        else:
            poser_question(noeud["non"])
    else:
        reponse = input(f"Est-ce que c'est {noeud['donnees']}? (oui/non) : ").strip().lower()
        if reponse == "oui":
            print("J'ai deviné votre animal !")
        else:
            apprendre_nouvel_animal(noeud)