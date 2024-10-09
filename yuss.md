import requests  # pylint: disable = all
from requests.auth import HTTPBasicAuth
import pandas as pd
import os
import json
import time
from datetime import datetime
import urllib3
from flask import Flask, send_file
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Définir les variables d'environnement pour le proxy
os.environ['https_proxy'] = ''
os.environ['http_proxy'] = ''

# API Configuration
API_KEY = ''
BASE_URL = "https://thalesaleniaspace.kantree.io/"
API_URL = BASE_URL+"api/1.0/"

app = Flask(__name__)


def generate_timestamp():
    now = datetime.now()
    return now.strftime("%d-%m-%Y_%H-%M")


def essai_connexion(id_projet):
    """Essaye de se connecter à l'API d'un workspace et lève une erreur si besoin"""
    try:
        res = requests.get(
            API_URL + "projects/{}/board".format(id_projet),
            auth=HTTPBasicAuth(API_KEY, ''),
            verify=False
        )
    except Exception as e:
        raise Exception("Erreur de connexion à l'API : \n{}".format(e))

    if res.status_code != 200:
        raise Exception("Erreur lors de la connexion : {}".format(res.status_code))
    
    if not res.json().get('is_admin'):
        raise Exception("Erreur de permission")


def get_all_projects():
    """Obtenir tous les projets (workspaces)"""
    url = f'{API_URL}/projects'
    response = requests.get(url, auth=HTTPBasicAuth(API_KEY, ''), verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching projects: {response.status_code}")
        return []


def get_project_cards(project_id):
    """Obtenir les cartes d'un projet spécifique"""
    url = f'{API_URL}/projects/{project_id}/cards'
    response = requests.get(url, auth=HTTPBasicAuth(API_KEY, ''), verify=False)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching cards for project {project_id}: {response.status_code}")
        return []


def extraction(ID_PROJECT, workspace_name):
    """Extraction des workspaces et enregistrement dans le dossier correspondant"""
    # Test de connexion
    essai_connexion(ID_PROJECT)

    # Démarrage de l'export
    print("Request Download project ...")
    export = requests.post(
        API_URL + "projects/" + str(ID_PROJECT) + "/export",
        auth=HTTPBasicAuth(API_KEY, ''),
        verify=False
    )

    # Attente de l'exportation du fichier par Kantree
    inProgress = True
    while inProgress:
        time.sleep(10)
        print("Check if export is still running?")
        prog = requests.get(
            export.json()['result_url'],
            auth=HTTPBasicAuth(API_KEY, ''),
            verify=False
        )

        if prog.status_code != 200:
            inProgress = False
            print("Error while waiting...")
            break

        if prog.json()['done']:
            inProgress = False
            print("File is ready to download")

    # Création des dossiers
    chemin_absolu = os.path.dirname(os.path.dirname(__file__))
    chemin_relatif = "{}/".format(workspace_name)
    chemin_complet = os.path.join(chemin_absolu, chemin_relatif)
    os.makedirs(chemin_complet, exist_ok=True)

    xslx_name = "Extraction_Kantree_{}_{}.xlsx".format(workspace_name, generate_timestamp())
    file_path = os.path.join(chemin_complet, xslx_name)

    # Téléchargement du fichier
    download = requests.get(
        prog.json()['data'],
        auth=HTTPBasicAuth(API_KEY, ''),
        verify=False
    )

    # Ecriture du fichier
    open(file_path, 'wb').write(download.content)
    print("File written to", file_path)


# Extract data from all projects and save to Excel
def extract_data():
    projects = get_all_projects()
    all_data = []

    for project in projects:
        project_id = project['id']
        project_name = project['title']
        
        # Fetch project cards
        cards = get_project_cards(project_id)

        for card in cards:
            card_data = {
                'Project': project_name,
                'Card Name': card['title'],
                'Description': card.get('description', ''),
                'Due Date': card.get('due_date', ''),
                'Members': ', '.join([member['username'] for member in card.get('members', [])])
            }
            all_data.append(card_data)

    # Save data to Excel if there are any records
    if all_data:
        save_to_excel(all_data)


# Save extracted data to Excel
def save_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel('kantree_data.xlsx', index=False)
    print('Data saved to kantree_data.xlsx')


def save_to_excel(data):
    # Créer un nouveau workbook et une feuille active
    wb = Workbook()
    ws = wb.active
    ws.title = "Kantree Data"

    # Définir les en-têtes
    headers = ['Project', 'Card Name', 'Description', 'Due Date', 'Members']
    ws.append(headers)

    # Écrire les données
    for row in data:
        ws.append([row['Project'], row['Card Name'], row['Description'], row['Due Date'], row['Members']])

    # Appliquer du style aux en-têtes
    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Ajuster la largeur des colonnes
    for col in range(1, len(headers) + 1):
        ws.column_dimensions[get_column_letter(col)].width = 25  # Ajustez la largeur comme nécessaire

    # Sauvegarder le fichier Excel
    file_path = os.path.join(os.getcwd(), 'kantree_data.xlsx')  # Utiliser le chemin courant
    wb.save(file_path)
    print('Data saved to', file_path)

    return file_path

@app.route('/download')
def download_file():
    file_path = os.path.join(os.getcwd(), 'kantree_data.xlsx')  # Utiliser le chemin courant
    if not os.path.exists(file_path):
        return "Le fichier n'existe pas", 404  # Retourner une erreur si le fichier n'existe pas
    return send_file(file_path, as_attachment=True)

# Main script
if __name__ == "__main__":
    project_id = 1703  # Remplacez par votre ID de projet réel
    workspace_name = "Test_Kantree"  # Remplacez par votre nom de workspace réel
    extraction(project_id, workspace_name)  # Appeler la fonction d'extraction
    data = extract_data()  # Extraire les données des cartes et les sauvegarder dans Excel
    
    # Démarrer le serveur Flask après avoir enregistré le fichier
    app.run(debug=True)

'''
On ne récupère pas les datas, mais elles sont mises dans un fichier excel au vu des mails que je reçois de Kantree
Les datas dans l'excel fournis sont en bazar, elles sont inexploitables dans l'instant
Il faut que je vois pour faire un post traitement, peut etre un pré traitement des données avant le transfert ?
Openpyxl est la librairie sur laquelle focus car elle permet de traiter du excel
'''
