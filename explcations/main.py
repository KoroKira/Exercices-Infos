# fais un programme qui appelera soit programme_1, soit programme_2, en fonction de la demande de l'utilisateur. Et ensuite ca devra demmander n

from programme_1 import affiche_programme as affiche_programme_1
from programme_2 import affiche_programme as affiche_programme_2

def main():
    choix = input("Quel programme voulez-vous exécuter (1 ou 2) ? ")
    n = int(input("Combien de fois voulez-vous exécuter le programme ? "))
    if choix == "1":
        affiche_programme_1(n)
    elif choix == "2":
        affiche_programme_2(n)
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")

if __name__ == "__main__":
    main()