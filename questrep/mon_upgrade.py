import json
import os

# Définition de la classe Node pour représenter chaque nœud dans l'arbre de décision
class Node:
    def __init__(self, question=None, animal=None):
        self.question = question  # La question pour distinguer les animaux
        self.animal = animal      # L'animal à deviner (si le nœud est une feuille)
        self.yes = None           # Branche "oui" menant à un autre nœud ou animal
        self.no = None            # Branche "non" menant à un autre nœud ou animal

    # Méthode pour convertir un nœud en dictionnaire, facilitant la sérialisation JSON
    def to_dict(self):
        """Convertit le nœud en dictionnaire pour la sérialisation JSON."""
        # Si le nœud représente un animal (feuille), retourne simplement l'animal
        if self.animal:
            return {"animal": self.animal}
        # Sinon, retourne un dictionnaire contenant la question, la branche "oui" et la branche "non"
        return {
            "question": self.question,
            "yes": self.yes.to_dict() if self.yes else None,
            "no": self.no.to_dict() if self.no else None
        }

    # Méthode statique pour recréer un nœud à partir d'un dictionnaire
    @staticmethod
    def from_dict(data):
        """Crée un nœud à partir d'un dictionnaire."""
        # Si le dictionnaire contient un animal, crée un nœud avec cet animal
        if "animal" in data:
            return Node(animal=data["animal"])
        # Sinon, crée un nœud avec une question et charge récursivement les branches "oui" et "non"
        node = Node(question=data["question"])
        node.yes = Node.from_dict(data["yes"]) if data["yes"] else None
        node.no = Node.from_dict(data["no"]) if data["no"] else None
        return node

# Fonction pour charger la base de connaissances depuis un fichier JSON
def load_knowledge_base(filepath="knowledge_base.json"):
    # Vérifie si le fichier existe
    if os.path.exists(filepath):
        # Si oui, charge les données JSON et crée l'arbre en utilisant Node.from_dict
        with open(filepath, "r") as file:
            data = json.load(file)
            return Node.from_dict(data)
    else:
        # Sinon, initialise une base de connaissances minimale avec trois animaux/questions
        root = Node("Est-ce un mammifère?")
        root.yes = Node("Est-ce un carnivore?")
        root.yes.yes = Node(animal="lion")
        root.yes.no = Node(animal="gazelle")
        root.no = Node(animal="poisson")
        return root

# Fonction pour sauvegarder la base de connaissances dans un fichier JSON
def save_knowledge_base(root, filepath="knowledge_base.json"):
    # Ouvre le fichier en mode écriture et enregistre l'arbre en format JSON
    with open(filepath, "w") as file:
        json.dump(root.to_dict(), file, indent=4)

# Fonction pour demander une réponse oui/non à l'utilisateur
def ask_yes_no(question):
    answer = input(question + " (oui/non): ").strip().lower()  # Demande la réponse
    # Tant que la réponse n'est pas 'oui' ou 'non', redemande la question
    while answer not in ['oui', 'non']:
        answer = input("Merci de répondre par 'oui' ou 'non': ").strip().lower()
    return answer == 'oui'  # Retourne True pour 'oui' et False pour 'non'

# Fonction principale de jeu
def play_game(node):
    # Si le nœud représente un animal (feuille de l'arbre)
    if node.animal:  
        # Pose la question pour savoir si c'est le bon animal
        if ask_yes_no(f"Est-ce que l'animal est {node.animal}?"):
            print("Super ! J'ai trouvé !")
        else:
            # Si l'animal est incorrect, apprend le nouvel animal
            learn_new_animal(node)
    else:
        # Si le nœud contient une question, la pose et suit la branche "oui" ou "non" en fonction de la réponse
        if ask_yes_no(node.question):
            play_game(node.yes)
        else:
            play_game(node.no)

# Fonction pour apprendre un nouvel animal si la réponse est incorrecte
def learn_new_animal(node):
    # Demande le nom du nouvel animal auquel pensait l'utilisateur
    new_animal = input("Quel est l'animal auquel vous pensiez ? ").strip()
    # Demande une question pour distinguer le nouvel animal de l'animal proposé par l'ordinateur
    new_question = input(f"Quelle question permet de différencier {node.animal} et {new_animal} ? ").strip()
    # Pose la question pour savoir si le nouvel animal répond "oui" à cette question
    if ask_yes_no(f"Pour la question '{new_question}', {new_animal} répond-il oui ?"):
        # Si oui, crée le nœud "oui" pour le nouvel animal et "non" pour l'ancien
        new_yes_node = Node(animal=new_animal)
        new_no_node = Node(animal=node.animal)
    else:
        # Sinon, crée le nœud "non" pour le nouvel animal et "oui" pour l'ancien
        new_yes_node = Node(animal=node.animal)
        new_no_node = Node(animal=new_animal)
    
    # Remplace la feuille actuelle par une question et attache les nouveaux nœuds "oui" et "non"
    node.question = new_question
    node.animal = None
    node.yes = new_yes_node
    node.no = new_no_node
    print("Merci ! Je me souviendrai de cet animal.")

# Fonction principale exécutant le jeu et gérant la base de connaissances
def main():
    root = load_knowledge_base()  # Charge l'arbre de décision depuis le fichier
    # Boucle de jeu principal pour rejouer tant que l'utilisateur le souhaite
    while True:
        print("\nPensez à un animal, je vais essayer de le deviner !")
        play_game(root)  # Lance une partie
        if not ask_yes_no("Voulez-vous rejouer ?"):  # Demande si l'utilisateur veut rejouer
            print("Merci d'avoir joué !")
            break
    save_knowledge_base(root)  # Sauvegarde les nouvelles connaissances

# Exécute le programme principal si le script est lancé directement
if __name__ == "__main__":
    main()
