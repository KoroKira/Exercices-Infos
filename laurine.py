import random #Fait que python choisisse un nombre

# L'ordinateur pense à un nombre, le joueur doit le deviner
# Le joueur donne une intervalle sur laquelle deviner 
# Le joueur donne un nombre de tentative qu'il a pour deviner
while True : #tant que...
    val_min = int(input("Entrez la borne minimum : "))
    val_max = int(input("Entrez la borne maximum : "))
    rmd = random.randint(val_min, val_max) # Python choisis un nombre entre entre min et max
    tentatives = int(input("En combien de tentatives voulez-vous jouer : ")) # Nombre de tentatives
    essai = 0 # début à 0 tentatives
    
    while essai < tentatives :
        question = int(input(f"Quel est mon nombre sachant qu'il est compris entre {val_min} et {val_max} : ")) #Demande le nombre choisis suivant la valeur :min et max
        essai += 1
        if rmd < question :
            print("trop grand")
        elif rmd > question :
            print("trop petit")
        else : 
            print("gagné !")
            break
    else :
        print(f"Le nombre de tentatives est épuisé. Le nombre était : {rmd}") # Si le nombre n'a pas été trouvé suivant le nombres de tentatives choisis

    programme = input("Voulez-vous rejouer oui ou non : ") # Si je veux rejouer ?
    if programme != "oui" :
        print("Merci et au revoir !")
        break