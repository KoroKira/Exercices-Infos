import random

# Fonction pour créer une liste de notes aléatoires
def creerNotes(nbnotes):
    listenotes = []
    for i in range(nbnotes):
        listenotes.append(random.randint(0, 20))
    return listenotes

# Fonction pour ajouter une matière et ses notes à l'ensemble
def ajouterNotesAEnsembleMatieres(matiere, nbnotes, ensembleMatieres):
    notes = creerNotes(nbnotes)
    ensembleMatieres[matiere] = notes

# Procédure pour afficher les matières et leurs notes
def obtenirNotesMatieres(ensembleMatieres):
    result = []
    for matiere, notes in ensembleMatieres.items():
        result.append((matiere, notes))
    return result

# Programme principal
ensembleMatieres = {}
ajouter = "oui"

# Boucle pour ajouter des matières tant que l'utilisateur le souhaite
while ajouter.lower() == "oui":
    matiere = input("Veuillez saisir le nom d'une matière : ")
    nbnotes = int(input(f"Combien de notes pour la matière {matiere} ? : "))
    ajouterNotesAEnsembleMatieres(matiere, nbnotes, ensembleMatieres)
    ajouter = input("Voulez-vous ajouter une autre matière ? (oui/non) : ")

# Affichage des matières et des notes
notes_matieres = obtenirNotesMatieres(ensembleMatieres)
for matiere, notes in notes_matieres:
    print(f"Matière : {matiere}")
    print(f"Notes : {notes}\n")