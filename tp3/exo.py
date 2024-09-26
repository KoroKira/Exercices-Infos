import random

# Fonction pour créer une liste de notes aléatoires
def creerNotes(nbnotes):
    listenotes = []
    for i in range(nbnotes):
        listenotes.append(random.randint(0, 20))
    return listenotes

# Fonction pour ajouter une matière et ses notes à l'ensemble
def ajouterNotesAEnsembleMatieres(matiere, ensembleMatieres):
    nbnotes = random.randint(2, 10)
    notes = creerNotes(nbnotes)
    ensembleMatieres[matiere] = notes

# Procédure pour afficher les matières et leurs notes
def afficherNotesMatieres(ensembleMatieres):
    for matiere, notes in ensembleMatieres.items():
        print(f"Matière : {matiere}")
        print(f"Notes : {notes}\n")

# Programme principal
ensembleMatieres = {}

# Ajout d'une première matière
matiere = input("Veuillez saisir le nom d'une matière : ")
ajouterNotesAEnsembleMatieres(matiere, ensembleMatieres)

# Ajout d'une deuxième matière
matiere = input("Veuillez saisir le nom d'une autre matière : ")
ajouterNotesAEnsembleMatieres(matiere, ensembleMatieres)

# Affichage des matières et de leurs notes
afficherNotesMatieres(ensembleMatieres)
