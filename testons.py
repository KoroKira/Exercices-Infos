import requests
import pandas as pd

# Fonction pour récupérer les workspaces via l'API de Kantree
def get_workspaces(api_key):
    url = "https://api.kantree.io/v1/me/projects"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Fonction pour récupérer les cartes d'un workspace
def get_workspace_cards(api_key, workspace_id):
    url = f"https://api.kantree.io/v1/projects/{workspace_id}/cards"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Fonction pour parcourir les champs de chaque carte et extraire tous les intitulés possibles
def extract_data_to_excel(api_key):
    workspaces = get_workspaces(api_key)
    
    # Une liste pour stocker toutes les données globales
    all_data = []
    
    # Ensemble pour stocker tous les intitulés de champs différents
    all_columns = set()

    # Parcours de tous les workspaces
    for workspace in workspaces:
        workspace_id = workspace['id']
        workspace_name = workspace['name']
        cards = get_workspace_cards(api_key, workspace_id)

        # Parcours de toutes les cartes dans le workspace
        for card in cards:
            card_data = {
                'Workspace': workspace_name,
                'Card ID': card['id'],
                'Card Title': card['title'],
            }
            
            # Parcourir les champs de la carte et les ajouter au dictionnaire
            for field in card.get('fields', []):
                field_name = field.get('label', 'Unknown Field')
                field_value = field.get('value', '')
                card_data[field_name] = field_value
                # Ajouter chaque intitulé de champ unique à l'ensemble des colonnes
                all_columns.add(field_name)
            
            all_data.append(card_data)
    
    # Convertir la liste des données en DataFrame pandas
    df = pd.DataFrame(all_data)

    # Ajouter toutes les colonnes manquantes à partir de l'ensemble all_columns
    for col in all_columns:
        if col not in df.columns:
            df[col] = ''

    # Exporter vers un fichier Excel
    df.to_excel('kantree_data_extract.xlsx', index=False)
    print("Extraction réussie dans kantree_data_extract.xlsx")

# Remplacer par ton propre token API de Kantree
API_KEY = 'TON_API_KEY_ICI'

# Appel de la fonction d'extraction
extract_data_to_excel(API_KEY)