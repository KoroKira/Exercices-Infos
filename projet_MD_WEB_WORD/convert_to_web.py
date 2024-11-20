import markdown
import os

def convert_to_web(md_file_path, output_dir):
    """
    Convertit un fichier Markdown en une page HTML avec une mise en page améliorée et l'enregistre dans le dossier de sortie.
    """
    # Lire le contenu du fichier Markdown
    with open(md_file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Convertir le contenu Markdown en HTML
    html_content = markdown.markdown(text)
    
    # Ajouter du CSS pour une meilleure mise en page
    css = """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            color: #333;
            background-color: #f9f9f9;
            margin: 40px;
            line-height: 1.6;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #2c3e50;
        }
        p {
            font-size: 16px;
            margin-bottom: 20px;
        }
        pre {
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            font-family: 'Courier New', monospace;
            background-color: #e0e0e0;
            padding: 2px 5px;
            border-radius: 4px;
        }
        blockquote {
            background-color: #ecf0f1;
            border-left: 5px solid #3498db;
            margin-left: 0;
            padding: 10px 20px;
            font-style: italic;
        }
        ul, ol {
            padding-left: 20px;
        }
        ul li {
            margin-bottom: 10px;
        }
        ol li {
            margin-bottom: 10px;
        }
    </style>
    """
    
    # Créer le fichier HTML avec le contenu Markdown et le CSS
    html_page = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Page Web Convertie</title>
        {css}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Déterminer le nom du fichier HTML
    output_file_name = os.path.basename(md_file_path).replace('.md', '.html')
    output_file_path = os.path.join(output_dir, output_file_name)
    
    # Sauvegarder le contenu HTML dans un fichier
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(html_page)
    
    print(f"Fichier HTML converti et sauvegardé à : {output_file_path}")
