from creer_noeud import creer_noeud

# Fonction pour apprendre un nouvel animal
def apprendre_nouvel_animal(noeud):
    nouvel_animal = input("Quel était l'animal auquel vous pensiez ? : ")
    nouvelle_question = input(f"Quelle question permet de différencier {nouvel_animal} de {noeud['donnees']} ? : ")
    reponse = input(f"Qui répond 'oui' à cette question ? ({nouvel_animal}/{noeud['donnees']}) : ").strip().lower()

    nouveau_noeud = creer_noeud(nouvelle_question, bool_question=True)
    if reponse == nouvel_animal.lower():
        nouveau_noeud["oui"] = creer_noeud(nouvel_animal)
        nouveau_noeud["non"] = noeud.copy()
    else:
        nouveau_noeud["oui"] = noeud.copy()
        nouveau_noeud["non"] = creer_noeud(nouvel_animal)

    # Mise à jour du noeud courant avec le nouveau noeud
    noeud["donnees"] = nouveau_noeud["donnees"]
    noeud["bool_question"] = nouveau_noeud["bool_question"]
    noeud["oui"] = nouveau_noeud["oui"]
    noeud["non"] = nouveau_noeud["non"]