def creer_noeud(donnees, bool_question=False): # Fonction pour créer un nœud
    return {
        "donnees": donnees, #les guillemets autour de "donnees", "bool_question", "oui", et "non" signifient  que ce sont des noms des clés dans le dictionnaire retourné par la fonction.
        "bool_question": bool_question,
        "oui": None,
        "non": None
    }