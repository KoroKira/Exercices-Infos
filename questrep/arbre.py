import json
import os
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, question=None, animal=None):
        self.question = question
        self.animal = animal
        self.yes = None
        self.no = None

    @staticmethod
    def from_dict(data):
        """Créé un noeud à partir d'un dictionnaire."""
        if "animal" in data:
            return Node(animal=data["animal"])
        node = Node(question=data["question"])
        node.yes = Node.from_dict(data["yes"]) if data["yes"] else None
        node.no = Node.from_dict(data["no"]) if data["no"] else None
        return node

def load_knowledge_base(filepath="knowledge_base.json"):
    """Charge la base de connaissances JSON en arbre de noeuds."""
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            data = json.load(file)
            return Node.from_dict(data)
    else:
        print("Fichier de base de connaissances introuvable.")
        return None

def build_graph(node, graph=None, parent=None, answer=None):
    """Construit un graphique de l'arbre avec NetworkX."""
    if graph is None:
        graph = nx.DiGraph()
    current = f"{node.animal}" if node.animal else f"Q: {node.question}"
    
    if parent:
        graph.add_edge(parent, current)
    
    if node.animal is None:
        build_graph(node.yes, graph, current, "Oui")
        build_graph(node.no, graph, current, "Non")
    
    return graph

def visualize_tree(graph):
    """Affiche l'arbre sans texte de questions, juste les animaux."""
    pos = nx.spring_layout(graph)  # Utilise un layout en arbre
    plt.figure(figsize=(12, 8))
    
    # Colorie les feuilles (animaux) différemment
    node_colors = ["lightgreen" if "Q:" not in node else "lightblue" for node in graph.nodes]
    nx.draw(graph, pos, with_labels=True, labels={node: node.split(":")[-1] for node in graph.nodes},
            node_color=node_colors, node_size=1000, font_size=10, font_weight="bold", font_color="black",
            edge_color="gray", arrows=False)
    
    plt.title("Arbre de connaissances des animaux")
    plt.show()

def main():
    root = load_knowledge_base()
    if root:
        graph = build_graph(root)
        visualize_tree(graph)

if __name__ == "__main__":
    main()
