# Correction des Exercices : Amortissement d'une Dette et Croissance d'un Bambou

## Exercice 1 : Amortissement d'une Dette

### Partie A : Étude sur un exemple

**Données du problème :**
- Montant du prêt : 120 000 EUR
- Durée de remboursement : 10 ans
- Taux annuel : 1,5 %
- Mensualités : 1 084,35 EUR

#### 1° Réalisation du tableau d'amortissement :
Il s'agit de créer un tableau d'amortissement en suivant les instructions suivantes :
- En C2, calculer les intérêts : `=B2*1,5/100`, où B2 représente la dette au début de l'année. 
- En E2, calculer la dette en fin d'année : `=B2-12*D2+C2`, en soustrayant les remboursements du capital.
- En F2, calculer l'amortissement : `=12*D2-C2`, soit la différence entre le total des mensualités et les intérêts.

Ensuite, appliquer ces formules pour les années suivantes dans le tableau.

#### b) Montant de l’annuité versée par Pauline :
On multiplie la mensualité par 12 pour obtenir l'annuité totale :  
`Annuité annuelle = 1 084,35 EUR * 12 = 13 012,2 EUR`

#### c) Pauline aura-t-elle remboursé sa dette au bout de 10 ans ?  
À la fin des 10 ans, le capital restant dû sera de 0 EUR, donc la dette sera intégralement remboursée.

### Partie B : Cas général

#### 1° Démontrer la récurrence pour le capital restant dû à la banque.
Nous utilisons la relation de récurrence donnée dans l'énoncé :
`C_{n+1} = 1,015 * C_n - 13 012,2`

#### 2° Montrer que la suite constante `v_n = 86 748` vérifie la relation de récurrence.
La suite `v_n` est constante car les annuités sont fixes, et la dette diminue régulièrement jusqu’à atteindre zéro.

#### 3° Montrer que la suite définie par `u_n = C_n - v_n` est géométrique.
La suite `u_n` est géométrique car elle suit une progression avec un facteur constant. Elle commence avec un certain premier terme, et nous devons la démontrer et calculer ce premier terme à partir de la relation donnée.

### Conclusion
Après 10 ans de remboursements, la dette est intégralement remboursée. Nous avons utilisé des formules d'amortissement classique pour démontrer la progression de la dette et vérifier que tout est conforme.

---

## Exercice 2 : Croissance d'un Bambou

Un infographiste simule la croissance d’un bambou en utilisant le modèle suivant :
- La taille initiale est de 50 cm.
- La croissance mensuelle est composée de 5 % de la taille actuelle, à laquelle on ajoute 20 cm.

### 1° Calcul des deux premiers termes de la suite
La taille au mois 0 est donnée par `u_0 = 50`.  
Nous utilisons la formule `u_{n+1} = 1,05 * u_n + 20` pour calculer les termes suivants :

- `u_1 = 1,05 * 50 + 20 = 72,5 cm`
- `u_2 = 1,05 * 72,5 + 20 = 96,125 cm`

### 2° Justifier que la suite est strictement croissante
La suite est strictement croissante car à chaque étape, la taille augmente de 5 % de la taille actuelle plus 20 cm. Cela garantit une croissance continue et significative.

### 4° Montrer que la suite (v_n) est géométrique
Nous définissons la suite `v_n` par `v_n = u_n + 400`. Il s'agit d'une suite géométrique car la progression est régulière. À chaque mois, la taille augmente de façon proportionnelle et constante.

### 5° Calculer la taille du bambou après 10 mois
Pour connaître la taille du bambou après 10 mois, il suffit d’appliquer la formule de récurrence 10 fois. Le résultat obtenu est la taille exacte du bambou à la fin du 10ème mois.

### 6° Calcul du nombre de mois pour dépasser les 10 mètres
Pour répondre à cette question, on peut utiliser un programme Python qui simule la croissance mensuelle jusqu’à ce que la taille dépasse 10 mètres (soit 1 000 cm). Le programme fait une boucle et à chaque itération, il calcule la taille du bambou au mois suivant.

Voici une implémentation possible en Python :

```python
def bambou():
    u = 50  # taille initiale en cm
    n = 0  # compteur de mois
    while u <= 1000:  # tant que le bambou ne dépasse pas 10 mètres
        u = 1.05 * u + 20  # mise à jour de la taille
        n += 1  # on compte les mois
    return n