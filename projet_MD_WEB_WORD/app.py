from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os
from convert import convert_to_web, convert_to_word

app = Flask(__name__)

# Dossiers de fichiers
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MD_FILES_DIR = os.path.join(BASE_DIR, 'md_files')
WEB_FILES_DIR = os.path.join(BASE_DIR, 'web_files')
WORD_FILES_DIR = os.path.join(BASE_DIR, 'word_files')

os.makedirs(MD_FILES_DIR, exist_ok=True)
os.makedirs(WEB_FILES_DIR, exist_ok=True)
os.makedirs(WORD_FILES_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html', file_link=None)

@app.route('/convert_to_web', methods=['POST'])
def convert_md_to_web():
    try:
        md_file = request.files['md_file']
        md_file_path = os.path.join(MD_FILES_DIR, md_file.filename)
        md_file.save(md_file_path)
        convert_to_web(md_file_path, WEB_FILES_DIR)
        file_link = url_for('download_file', filename=md_file.filename.replace('.md', '.html'), folder='web_files')
        return render_template('index.html', file_link=file_link, file_name=md_file.filename.replace('.md', '.html'))
    except Exception as e:
        return f"Erreur lors de la conversion : {e}", 500

@app.route('/convert_to_word', methods=['POST'])
def convert_md_to_word():
    try:
        md_file = request.files['md_file']
        md_file_path = os.path.join(MD_FILES_DIR, md_file.filename)
        md_file.save(md_file_path)
        convert_to_word(md_file_path, WORD_FILES_DIR)
        file_link = url_for('download_file', filename=md_file.filename.replace('.md', '.docx'), folder='word_files')
        return render_template('index.html', file_link=file_link, file_name=md_file.filename.replace('.md', '.docx'))
    except Exception as e:
        return f"Erreur lors de la conversion : {e}", 500

@app.route('/download/<folder>/<filename>')
def download_file(folder, filename):
    folder_path = os.path.join(BASE_DIR, folder)
    return send_from_directory(folder_path, filename)

if __name__ == '__main__':
    app.run(debug=True)
