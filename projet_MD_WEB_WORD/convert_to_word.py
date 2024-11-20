from docx import Document
import os

def convert_to_word(md_file_path, output_dir):
    """
    Convertit un fichier Markdown en un document Word (.docx) et l'enregistre dans le dossier de sortie.

    :param md_file_path: Chemin du fichier Markdown (.md) à convertir.
    :param output_dir: Dossier où le fichier Word converti sera enregistré.
    """
    # Lire le contenu du fichier Markdown
    with open(md_file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Créer un nouveau document Word
    doc = Document()
    
    # Ajouter le contenu ligne par ligne dans le document Word
    for line in text.split('\n'):
        doc.add_paragraph(line)
    
    # Déterminer le nom du fichier Word
    output_file_name = os.path.basename(md_file_path).replace('.md', '.docx')
    output_file_path = os.path.join(output_dir, output_file_name)
    
    # Sauvegarder le document Word
    doc.save(output_file_path)
    print(f"Fichier Word converti et sauvegardé à : {output_file_path}")
