import json
import os
import pandas as pd

class Node:
    def __init__(self, question=None, animal=None):
        self.question = question
        self.animal = animal
        self.yes = None
        self.no = None

    @staticmethod
    def from_dict(data):
        if "animal" in data:
            return Node(animal=data["animal"])
        node = Node(question=data["question"])
        node.yes = Node.from_dict(data["yes"]) if data["yes"] else None
        node.no = Node.from_dict(data["no"]) if data["no"] else None
        return node

def load_knowledge_base(filepath="knowledge_base.json"):
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            data = json.load(file)
            return Node.from_dict(data)
    else:
        print("Fichier de base de connaissances introuvable.")
        return None

def extract_questions_and_animals(node, current_questions=None, current_path=None, data=None):
    if data is None:
        data = {}
    if current_questions is None:
        current_questions = []
    if current_path is None:
        current_path = []

    if node.animal:
        animal_path = {question: ("oui" if answer else "non") for question, answer in zip(current_questions, current_path)}
        data[node.animal] = animal_path
    else:
        extract_questions_and_animals(node.yes, current_questions + [node.question], current_path + [True], data)
        extract_questions_and_animals(node.no, current_questions + [node.question], current_path + [False], data)

    return data

def generate_double_entry_table(data):
    all_questions = sorted({q for answers in data.values() for q in answers.keys()})
    df = pd.DataFrame(index=data.keys(), columns=all_questions)
    df = df.fillna("non")  # Fill missing values with "non"

    for animal, answers in data.items():
        for question, answer in answers.items():
            df.at[animal, question] = answer
    return df

def save_table_to_excel(df, filepath="animal_questions_table.xlsx"):
    """Enregistre le DataFrame dans un fichier Excel."""
    df.to_excel(filepath, index=True)
    print(f"Tableau enregistré sous '{filepath}'.")

def main():
    root = load_knowledge_base()
    if root:
        data = extract_questions_and_animals(root)
        df = generate_double_entry_table(data)
        save_table_to_excel(df)
        print("Tableau croisé des animaux et des questions :\n")
        print(df)

if __name__ == "__main__":
    main()
