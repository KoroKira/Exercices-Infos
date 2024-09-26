# **Roadmap : Développement d'un Blackjack en Python**

## **Module 1 : Initialisation du Jeu**
### **Objectif** :
- Créer la structure de base du jeu (cartes, paquet, joueurs).

### **Tâches** :
1. **Classe `Carte`** :
   - Attributs : `suit` (couleur), `rank` (valeur).
   - Méthode : `__str__()` pour afficher la carte en chaîne de caractères.

   __**FAIT**__

2. **Classe `Deck`** :
   - Méthode pour créer un jeu de 52 cartes.
   - Méthode pour mélanger les cartes.
   - Méthode `draw()` pour tirer une carte.

   __**On a un générateur random des cartes (d'abord on a le créateur de carte et le tireur), il nous faut les stocker et les gérer entre elles, parce que lourd d'avoir 5 fois d'affilé de l'as de pique par malchance**__

3. **Classe `Main`** :
   - Attribut pour stocker les cartes du joueur.
   - Méthode pour ajouter une carte à la main.
   - Méthode pour calculer la valeur de la main (inclure la gestion de l'As : 1 ou 11).

---

## **Module 2 : Joueur et Croupier**
### **Objectif** :
- Implémenter la logique pour le joueur et le croupier.

### **Tâches** :
1. **Classe `Joueur`** :
   - Attribut pour la main du joueur.
   - Méthode `hit()` pour piocher une carte.
   - Méthode pour décider de "stand" ou continuer à jouer.

2. **Classe `Croupier`** (hérite de `Joueur`) :
   - Logique pour tirer automatiquement des cartes tant que la main est inférieure à 17.

---

## **Module 3 : Logique du Jeu**
### **Objectif** :
- Intégrer les composants pour jouer une partie complète.

### **Tâches** :
1. **Classe `Blackjack`** :
   - Initialiser un paquet de cartes mélangé.
   - Distribuer 2 cartes au joueur et 2 cartes au croupier (1 face cachée pour le croupier).
   - Gérer les actions du joueur : `hit()`, `stand()`, `double_down()`.
   - Implémenter les règles de victoire/défaite.

2. **Méthode `play_game()`** :
   - Gérer le tour par tour pour le joueur et le croupier.
   - Comparer les mains à la fin pour déterminer le gagnant.

---

## **Module 4 : Gestion des mises et du solde**
### **Objectif** :
- Ajouter la gestion des paris pour un jeu plus réaliste.

### **Tâches** :
1. Ajouter un attribut pour le solde des joueurs.
2. Implémenter la gestion des mises (`bet()`).
3. Gérer les gains et pertes selon le résultat (victoire, défaite, égalité).
4. Implémenter l'option de doubler la mise (`double_down()`).

---

## **Module 5 : Interface Utilisateur en Console**
### **Objectif** :
- Améliorer l’expérience avec une interface textuelle.

### **Tâches** :
1. Afficher les cartes du joueur et du croupier à chaque tour.
2. Demander à l'utilisateur de choisir une action : `hit()`, `stand()`, `double_down()`.
3. Afficher les résultats et mettre à jour le solde.

---

## **Module 6 : Améliorations et Options Avancées**
### **Objectif** :
- Ajouter des fonctionnalités avancées et des options supplémentaires.

### **Tâches** :
1. Implémenter une gestion de plusieurs joueurs.
2. Ajouter une option pour jouer plusieurs manches avec conservation du solde.
3. Ajouter des statistiques (nombre de victoires, défaites, égalités).
4. Implémenter une stratégie basique pour le croupier.

---

## **Module 7 : Tests Unitaires**
### **Objectif** :
- Assurer la robustesse du code via des tests automatisés.

### **Tâches** :
1. Écrire des tests unitaires pour les différentes classes :
   - Tests sur la création des cartes et paquets.
   - Tests du calcul des mains.
   - Tests des actions (`hit()`, `stand()`, etc.).

2. Créer un fichier `test_blackjack.py` et utiliser `unittest` ou `pytest`.

---

## **Module 8 : Optimisation et Extensibilité**
### **Objectif** :
- Examiner les possibilités d'optimisation et rendre le code flexible pour des améliorations futures.

### **Tâches** :
1. Optimiser la gestion des As pour éviter des recalculs inutiles.
2. Refactoriser pour permettre des variantes (ex. : Blackjack européen).
3. Documenter le code et ajouter des commentaires pour faciliter l’extensibilité.