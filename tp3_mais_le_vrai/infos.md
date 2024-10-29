Etape 1 : manipulation de liste au travers des chaînes de caractères
Exercice 1 : les chaînes de caractères et leurs opérations
En utilisant l'instruction while :

Sachant que

- l'élément de rang r (compté à partir de 0) d'une chaine de caractère "ch" est désigné par ch[r]

- et que la longueur de la chaine est donnée par len(ch)

Exemple:

[code python]

maChaine = 'Bonjour'
print("Longueur de la chaine : ", len(maChaine))

for i in range(0,len(maChaine)): #affichage des caractères 1 à longueur de la chaine : attention le 1er indice est 0 et pas 1
    print("Caractère ", i+1," : ", maChaine[i]) 

[/code]



1 - écrire le programme qui affiche les caractères d'une chaine dans l'ordre en insérant un espace entre tous les caractères consécutifs.

2 - Ecrire le programme qui affiche une chaîne à l'envers.

3 - Ecrire un programme qui détecte si une chaîne de caractères est un palindrome. Une chaîne de caractères est un palindrome si elle s'écrit de la même façon à l'endroit et à l'envers. (ex : laval)

4 - Écrire un programme qui détermine si une chaîne contient ou non le caractère « e ».

5 - Écrire un programme qui compte le nombre d’occurrences du caractère « e » dans une chaîne (combien de fois il apparait)





AIDE : La séquence ci-dessous peut vous aider pour la question 1 avec l'instruction for :

[code python]


ch = "Chateau"
for c in ch:
    print(c,end=",")
[/code]


Première liste Python : Remplacement de la chaine par une liste de caractères
L'utilisation de l'instruction for est plus adaptée pour des listes et tout ce qui s'y apparente.

Dans l'exemple ci-dessus le "mot" Chateau est construit avec une liste de caractères. Nous avons un résultat similaire au précédent.

[code python]

for c in ['C', 'h', 'a', 't', 'e', 'a', 'u'] :
    print (c, end=" ")
[/code]


Remarque : On peut également accéder aux éléments d'une liste par leurs indices comptés à partir de 0 (exactement comme pour les caractères d'une chaîne). La séquence ci-dessous affichera donc la même chose que les 2 précédentes.

[code python]

ch = ['C', 'h', 'a', 't', 'e', 'a', 'u']
for i in range(7):
    print(ch[i], end=" ")
[/code]


Exercice 2 : mise en pratique
1 - Compléter la séquence ci-dessous pour que le programme affiche la phrase "Se soigner est un devoir moral" à partir de la liste des mots "ch" et en utilisant l'instruction for.

[code python]

ch = ['se', 'soigner', 'est', 'un', 'devoir', 'moral']
    ....
[/code]
2 - Modifier le programme pour afficher le texte à l'envers en utilisant toujours l'instruction for. Pour vous aider exécuter le programme ci-dessous et essayer de comprendre son fonctionnement.

[code python]

ch = ['Se', 'soigner', 'est', 'un', 'devoir', 'moral']
for i in range(len(ch), -1, -1):
    print(i, end=" ")
[/code]
Pour aller plus loin (et vous faire des nœuds au cerveau)

3 - Ecrire le programme qui affiche la phrase avec les mots dans le bon ordre, mais avec l'ordre des caractères à l'envers pour chaque mot (en utilisant toujours l'instruction for).

4 - Ecrire le programme qui affiche la phrase à l'envers et les lettres de chaque mot à l'envers.

5 - Reprendre le programme de la question 4 en utilisant l'instruction while.


Etape 2 : approfondissements des notions déjà vues
Exercice 3 : suite de Fibonacci (structures répétitives)
 
Le petit programme ci-dessous permet d’afficher les dix premiers termes d’une suite appelée « Suite de Fibonacci ».

Il s’agit d’une suite de nombres dont chaque terme est égal à la somme des deux termes qui le précèdent.

Analysez ce programme et décrivez le mieux possible le rôle de chacune des instructions.

[code python]

a, b, c= 1, 1, 1
while c< 11 :
    print(b, end =" ")
    a, b, c= b, b+a, c+1

[/code]
1 - Qu'elles sont les valeurs affichées à l'exécution de ce programme ?

2 - Expliquer en particulier l'instruction a, b, c = 1, 1, 1 ainsi que a, b, c = b, a+b, c+1

3 - Modifier ce programme pour remplacer les espaces entre les nombres par des virgules.



Remarque : Bonnes pratiques

Pour avoir un programme propre, facile à comprendre, à partager et à relire il est important

- de choisir des noms de variables explicites (évitez tous les caractères spéciaux sauf le _)

- de clairement commenter (expliquer) votre code


Voici un programme plus propre :

[code python]

#création des variables et initialisation
nb1, nb2, compteur = 1, 1, 1

#boucle de calcul et affichage
while compteur < 11 :
    #affichage du 2nd nombre
    print(nb2, end =" ")
    #calculs et mise à jour des variables
    nb1, nb2, compteur = nb2, nb1+nb2, compteur+1
    """
    cette dernière ligne revient à remplacer d'un coup nb1 par nb2 nb2 par l'ancien nb1+l'ancien nb2, incrémenter compteur de 1
    """

[/code]

Exercice 4 : manipulation de listes et de structures répétitives et conditionnnelles
Des jeunes de 5 à 20 ans à classer par tranches d'âge (5 à 7 ans), (8 à 10 ans), (11 à 15 ans) et (16 à 20 ans)

L'opérateur ne sait pas non plus combien il y a de jeunes et le programme doit lire les âges tant qu'il y en a. L'opérateur devra par exemple rentrer un âge négatif pour indiquer au programme qu'il n'y a plus de jeune à classer.

Essayons de réaliser une programme petit bout par petit bout, étape par étape :

1) Saisir l'âge d'un jeune puis afficher "il est de la tranche (... à ...)"

2) En sachant qu'on a en tout 20 jeunes à classer par classe d'âge. Nous voulons compter le nombre de jeunes par tranche d'âge.

AIDE : nous voulons simplement ici gérer des compteurs pour chaque tranche d'âge.

Le programme doit demander : "l'âge du suivant ", lire l'âge, puis comptabiliser. Le programme doit afficher à la fin :

"Nombre de jeunes ages de 5 à 7 ans = ..."
"Nombre de jeunes ages de 8 à 10 ans = ..."
"Nombre de jeunes ages de 11 à 15 ans = ..."
"Nombre de jeunes ages de 16 à 20 ans = ..."
"Nombre de jeunes non classés = ..."       # les jeunes non classés sont des jeunes dont l'âge ne rentre pas dans les tranches ci-dessus
Remarque : pour réaliser le traitement ci-dessus, utiliser l'instruction "while" ; on peut définir une variable par tranche d'âge (On verra qu'on peut mieux faire).

3) On suppose qu'on ignore maintenant le nombre total de jeunes à classer.

Le programme doit demander au tout début de rentrer le nombre total de jeunes puis faire la même chose qu'à la question 2.


4) On suppose qu'on ignore maintenant le nombre total de jeunes à classer mais nous voulons demander à l'utilisateur s'il veut continuer ou non.

AIDE : nous pourrons utiliser une variable continuer qui prendra la valeur oui/non ou 0/1 ou qui soit booléenne.



Exercice 5 : Exercice de synthèse
Dans l'exercice 4, nous savons compter les jeunes de chaque tranche d'âge mais le programme ne peut pas dire "Dupont Joseph est dans la tranche de 8 à 10 ans".

Question : Imaginer un programme qui permet de saisir le nom, le prénom et l'âge d'un certain nombre de  personnes, et qui permettrait en fin de compte d'afficher les informations sur toutes ces personnes :

"Nombre total de personnes classées : ..."
"Liste par tranche d'âge"
"Nombre de personnes enregistrées dans la tranche 1 = ..."
"Prénom nom"
"....."
"Nombre de personnes enregistrées dans la tranche i = ..."
"Prénom nom"
"....."
"Nombre de personnes hors compétition = ..."


AIDE : nous pouvons utiliser un programme contenant une liste de personnes : nom, prénom, age. Une personne serait un dictionnaire.

Voici un programme permettant de créer une personne et une liste de personnes :

# -*- coding: utf-8 -*-
#import d'une bibliotheque de calculs aleatoires
import random


#variables
#creation d'une liste vide
maListe = []


#programme

#boucle de calcul et affichage
for i in range(10) :
    #strcuture personne : dictionnaire (creee à chaque passage dans le for)
    unePersonne = {"nom":"","prenom":"","age":0}
    #nombre aleatoire entre 0 et 20 mis dans l'age de unePersonne (et donc ecrase a chaque passage dans le for)
    unePersonne["age"] = random.randint(0,20)
    #ajout en fin de liste avec la fonction append
    maListe.append(unePersonne)

#affichage de la liste dans son ensemble via print, vous remarquerez que nous avons une liste de dictionnaires
print(maListe)
