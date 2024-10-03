import os
import filecmp
from datetime import datetime

def scan_directory(dir_path):
    files_dict = {}
    dirs_dict = set()
    for root, dirs, files in os.walk(dir_path):
        relative_dir = os.path.relpath(root, dir_path)
        dirs_dict.add(relative_dir)
        
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, dir_path)
            file_info = {
                'path': file_path,
                'mod_time': os.path.getmtime(file_path),
                'size': os.path.getsize(file_path)
            }
            files_dict[relative_path] = file_info
    return files_dict, dirs_dict

def compare_files(file_a, file_b):
    if file_a['mod_time'] != file_b['mod_time']:
        return 'Modification date differs'
    elif file_a['size'] != file_b['size']:
        return 'File size differs'
    else:
        return 'Files are identical'

def generate_report(dir_a, dir_b, report_file):
    files_a, dirs_a = scan_directory(dir_a)
    files_b, dirs_b = scan_directory(dir_b)

    with open(report_file, 'w') as report:
        # Comparer les fichiers
        for relative_path, file_info_a in files_a.items():
            if relative_path in files_b:
                file_info_b = files_b[relative_path]
                comparison_result = compare_files(file_info_a, file_info_b)
                report.write(f"File: {relative_path}\n")
                report.write(f" - {comparison_result}\n")
            else:
                report.write(f"File: {relative_path} is missing in {dir_b}\n")

        for relative_path, file_info_b in files_b.items():
            if relative_path not in files_a:
                report.write(f"File: {relative_path} is missing in {dir_a}\n")

        # Comparer les sous-dossiers manquants dans B mais présents dans A
        for relative_dir in dirs_a:
            if relative_dir not in dirs_b:
                report.write(f"Directory: {relative_dir} is missing in {dir_b}\n")

if __name__ == "__main__":
    directory_a = "dossier_a"
    directory_b = "dossier_b"
    report_path = "comparison_report.txt"

    generate_report(directory_a, directory_b, report_path)
