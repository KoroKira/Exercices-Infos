Nous voulons réaliser un programme qui permette de préparer la création d'un jeu de black jack (une définition du jeu ici : http://fr.wikipedia.org/wiki/Blackjack_%28jeu%29).



Deux structures de donnée ont été choisies pour représenter le jeu :

# 1) Structure de donnée jeu de 56 cartes : dictionnaire de 4 listes

jeu = {"trefle":["1","2","3","4","5","6","7","8","9","10","V","D","R","A"],"coeur": "1","2","3","4","5","6","7","8","9","10","V","D","R","A"],"carreau":["1","2","3","4","5","6","7","8","9","10","V","D","R","A"],"pique":["1","2","3","4","5","6","7","8","9","10","V","D","R","A"]}

# 2) Structures de données contenant les couleurs : liste

couleurs = ["coeur","pique","trefle","carreau"]



Proposez une solution où le joueur peut rejouer et réinitialiser le jeu autant de fois qu'il le désire