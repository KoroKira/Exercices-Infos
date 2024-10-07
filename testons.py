import requests
import json

# Remplace par tes informations Trello
API_KEY = "YOUR_TRELLO_API_KEY"
API_TOKEN = "YOUR_TRELLO_API_TOKEN"
WORKSPACE_ID = "YOUR_WORKSPACE_ID"  # ID du workspace à exporter

# URL de base de l'API Trello
BASE_URL = "https://api.trello.com/1"

# Fonction pour récupérer les informations d'un board
def get_board_data(board_id):
    url = f"{BASE_URL}/boards/{board_id}"
    query = {
        'key': API_KEY,
        'token': API_TOKEN,
        'lists': 'all',
        'cards': 'all',
        'members': 'all',
        'checklists': 'all',
    }
    response = requests.get(url, params=query)
    return response.json()

# Fonction pour récupérer tous les boards d'un workspace
def get_workspace_boards(workspace_id):
    url = f"{BASE_URL}/organizations/{workspace_id}/boards"
    query = {
        'key': API_KEY,
        'token': API_TOKEN,
    }
    response = requests.get(url, params=query)
    return response.json()

# Fonction principale pour exporter le workspace en JSON
def export_workspace_to_json(workspace_id, output_file="workspace_export.json"):
    # Récupération des boards du workspace
    boards = get_workspace_boards(workspace_id)
    workspace_data = {}

    # Boucle sur chaque board pour récupérer ses données
    for board in boards:
        board_id = board['id']
        board_data = get_board_data(board_id)
        workspace_data[board['name']] = board_data

    # Exportation des données au format JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(workspace_data, json_file, ensure_ascii=False, indent=4)
    
    print(f"Workspace exporté avec succès dans le fichier {output_file}")

# Appel de la fonction pour exporter les données
export_workspace_to_json(WORKSPACE_ID)