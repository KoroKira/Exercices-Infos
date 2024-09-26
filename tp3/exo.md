Exercices
Exercice1 : listes de notes dans un dictionnaire de matières


Soit le programme suivant qui permet de créer (aléatoirement) 2 listes de notes pour 2 matières.

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 15:27:39 2016

@author: FRERE
"""
#import des librairies
import random

# variables
ensembleMatieres = {}
matiere =""
nbnotes = 0

#ajouter une premiere matiere
matiere = input("veuillez saisir le nom d une matiere  :  ")
#nombre de notes aléatoire
nbnotes = random.randint(2,10)

#nouvelle liste de notes
listenotes = []
#ajout des notes
for i in range(nbnotes):
    #ajout de
    listenotes.append(random.randint(0,20))

#ajout dans les matières
ensembleMatieres[matiere]=listenotes
    


#ajouter une deuxieme matiere
matiere = input("veuillez saisir le nom d une matiere  :  ")
#nombre de notes aléatoire
nbnotes = random.randint(2,10)

#nouvelle liste de notes
listenotes = []
#ajout des notes
for i in range(nbnotes):
    #ajout de
    listenotes.append(random.randint(0,20))

#ajout dans les matières
ensembleMatieres[matiere]=listenotes


#☻affichage (brut) des matières et de leurs notes
print(ensembleMatieres)


1) Testez le programme et comprenez comment il fonctionne et quel résultat il donne.



Remarque :

Les deux parties de codes sont des copies l'une de l'autre.

C'est le signe qu'une procédure ou une fonction peut remplacer ce code.



2) Modifiez le programme pour réaliser les procédures et fonctions suivantes :

fonction creerNotes (ou saisirNotes si nous voulions faire intervenir l'utilisateur dans un second temps)
notes.png

fonction ajouterNotesAEnsembleMatieres
ajoutnotesmatieres.png

procedure afficherNotesMatieres
affichernotesmatieres.png

3) Terminez le programme (en utilisant les procédures et fonctions réalisées) pour réaliser l'algorithme suivant :

