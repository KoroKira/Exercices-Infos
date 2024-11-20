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

   __**FAIT**__

3. **Classe `Main`** :
   - Attribut pour stocker les cartes du joueur.
   - Méthode pour ajouter une carte à la main.
   - Méthode pour calculer la valeur de la main (inclure la gestion de l'As : 1 ou 11).

    __**FAIT**__

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

   __**FAIT**__

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

   __**FAIT**__

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
2. Ajouter une option pour jouer plusieurs manches avec conservation du solde.
3. Ajouter des statistiques (nombre de victoires, défaites, égalités).
4. Implémenter une stratégie basique pour le croupier.
5. Faire une page pour lancer le jeu, un fichier game.py
