import tkinter as tk
from tkinter import messagebox
import subprocess, sys, os

LISTE_TP = [
    ("TP1.1 – Convertisseur Celsius/Fahrenheit", "TP1.1/main.py"),
    ("TP1.2 – Somme et produit des nombres pairs", "TP1.2/main.py"),
    ("TP1.3 – Messages d'accueil", "TP1.3/main.py"),
    ("TP1.4 – Jeu de calcul mental", "TP1.4/main.py"),
    ("TP1.5 – Année bissextile", "TP1.5/main.py"),
]

def lancer(tp_relatif):
    python_exe = sys.executable
    chemin = os.path.join(os.path.dirname(__file__), tp_relatif)
    try:
        subprocess.Popen([python_exe, chemin])
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de lancer {tp_relatif}\n{e}")

def main():
    racine = tk.Tk()
    racine.title("Lanceur de TP Python")
    racine.geometry("520x340")
    racine.resizable(False, False)

    tk.Label(racine, text="Choisis le TP à lancer :", font=("Arial", 14, "bold")).pack(pady=16)

    cadre = tk.Frame(racine)
    cadre.pack(pady=8, fill="x")
    for libelle, chemin in LISTE_TP:
        bouton = tk.Button(cadre, text=libelle, command=lambda p=chemin: lancer(p))
        bouton.pack(pady=6, padx=24, fill="x")

    tk.Button(racine, text="Quitter", command=racine.destroy).pack(pady=8)

    racine.mainloop()

if __name__ == "__main__":
    main()
