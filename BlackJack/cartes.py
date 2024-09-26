def print_card(rang, suite):

    haut = "┌─────────┐"
    bas = "└─────────┘"
    cote = "│         │"

    if rang == "10":  
        rang_droit = rang
        rang_gauche = rang
    else:
        rang_droit = rang + " "
        rang_gauche = " " + rang

    suite_ligne = f"│    {suite}    │"
    rang_ligne_gauche = f"│{rang_gauche}       │"
    rang_ligne_droit = f"│       {rang_droit}│"

    print(haut)
    print(rang_ligne_gauche)
    print(cote)
    print(suite_ligne)
    print(cote)
    print(rang_ligne_droit)
    print(bas)

