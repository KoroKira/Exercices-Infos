# Game.py 

import subprocess

def ask_and_run_script():
    choice = input("Voulez-vous lancer A.py ou B.py ? (A/B) : ").strip().upper()
    if choice == 'A':
        subprocess.run(["python", "A.py"])
    elif choice == 'B':
        subprocess.run(["python", "B.py"])
    else:
        print("Choix invalide. Veuillez entrer A ou B.")

def main():
    ask_and_run_script()

# Exécute le programme principal si le script est lancé directement
if __name__ == "__main__":
    main() 