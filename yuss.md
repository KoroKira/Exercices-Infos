# Documentation utilisateur

## Jeu de devinette d'animaux amélioré

Ce programme est un jeu de devinette d'animaux amélioré qui apprend de nouvelles informations sur les animaux en fonction des réponses de l'utilisateur. Le jeu fonctionne en posant des questions pour deviner l'animal auquel l'utilisateur pense, et en apprenant de nouvelles informations si la réponse est incorrecte.

### Comment jouer :
1. Pensez à un animal (sans le dire à l'ordinateur).
2. L'ordinateur posera des questions pour deviner l'animal.
3. Répondez aux questions par 'oui' ou 'non'.
4. Si l'ordinateur devine correctement, félicitations !
5. Sinon, l'ordinateur apprendra de nouvelles informations sur l'animal.

Le programme enregistre les nouvelles informations apprises pour améliorer ses capacités de devinette la prochaine fois que vous jouerez.

Amusez-vous à jouer et à apprendre de nouveaux animaux avec ce jeu de devinette amusant !

# Documentation technique

## Documentation technique

Ce programme est écrit en Python et utilise la sérialisation JSON pour stocker et charger les données de l'arbre de décision. Voici une description des différentes parties du code :

### 1. Classe Node :

- La classe Node représente un nœud dans l'arbre de décision. Chaque nœud peut contenir une question pour distinguer les animaux ou un animal (feuille de l'arbre).
- La méthode `to_dict` convertit un nœud en dictionnaire pour la sérialisation JSON.
- La méthode statique `from_dict` crée un nœud à partir d'un dictionnaire.

### 2. Fonctions :

- `load_knowledge_base(filepath)` : Charge l'arbre de décision depuis un fichier JSON.
- `save_knowledge_base(root, filepath)` : Sauvegarde l'arbre de décision dans un fichier JSON.
- `ask_yes_no(question)` : Demande une réponse 'oui' ou 'non' à l'utilisateur.
- `play_game(node)` : Fonction principale pour jouer au jeu de devinette.
- `learn_new_animal(node)` : Apprend de nouvelles informations sur un animal.
- `main()` : Fonction principale pour exécuter le jeu et gérer la base de connaissances.