import os
import subprocess

chercheur = r"/Users/guilhem/Documents/GitHub/Exercices-Infos/Pendu/pendu.py"
penseur = r"laurine.py"

def ask_and_run_script():
    choice = input("Voulez-vous lancer chercheur.py ou penseur.py ? (chercheur/penseur) : ").strip().lower()
    if choice == "chercheur":
        subprocess.run(["python", chercheur])
    elif choice == 'penseur':
        subprocess.run(["python", penseur])
    else:
        print("Choix invalide. Veuillez entrer chercheur ou penseur.")

def main():
    ask_and_run_script()

if __name__ == "__main__":
    main()