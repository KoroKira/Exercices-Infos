import markdown
from weasyprint import HTML
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import os

# Fonction de conversion de markdown en HTML
def markdown_to_html(md_text):
    # Conversion du markdown en HTML
    html = markdown.markdown(md_text)
    return html

# Fonction pour appliquer des styles au HTML
def apply_custom_styles(html_content):
    # Ici, tu peux ajouter des styles CSS spécifiques pour la mise en page
    # Exemple de CSS pour la couleur, marges, etc.
    css = """
    body {
        font-family: Arial, sans-serif;
        color: #333;
    }
    h1 {
        color: #FF5733;
    }
    h2 {
        color: #007BFF;
    }
    p {
        color: #555;
    }
    """
    return f"<style>{css}</style>{html_content}"

# Fonction pour générer un PDF à partir du HTML avec mise en page personnalisée
def generate_pdf_from_html(html_content, output_pdf):
    # Applique les styles à ton HTML
    styled_html = apply_custom_styles(html_content)
    
    # Convertir HTML en PDF via WeasyPrint
    HTML(string=styled_html).write_pdf(output_pdf)

# Fonction pour définir la mise en page personnalisée avec le nombre de pages
def create_custom_pdf(md_file_path, output_pdf, page_limit=10):
    # Lire le contenu du fichier markdown
    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_text = file.read()

    # Convertir markdown en HTML
    html_content = markdown_to_html(md_text)

    # Créer un PDF à partir du contenu HTML avec mise en page
    generate_pdf_from_html(html_content, output_pdf)

    # Ouvrir le PDF pour appliquer des réglages supplémentaires
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    # Exemple de mise en page avec ReportLab (ajustement des marges, couleurs)
    c.setFillColor(HexColor("#FF5733"))
    c.setFont("Helvetica", 12)

    # Ajouter du texte personnalisé (par exemple, un en-tête)
    c.drawString(100, height - 100, "En-tête personnalisé pour ton PDF")

    # Appliquer la limite de pages
    for page_num in range(1, page_limit):
        if page_num > 1:
            c.showPage()  # Crée une nouvelle page
        c.drawString(100, height - 100, f"Page {page_num} de {page_limit}")

    # Sauvegarder le PDF final
    c.save()

# Exemple d'utilisation
md_file_path = '/Users/guilhem/Documents/GitHub/Exercices-Infos/tesdt.md'  # Remplace par ton fichier .md
output_pdf = 'output.pdf'

create_custom_pdf(md_file_path, output_pdf)
