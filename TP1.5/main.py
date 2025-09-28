import tkinter as tk
from View.menu import VueBissextile
from Controller.controller import ControllerBissextile

def main():
    racine = tk.Tk()
    racine.title("TP1.5 — Année bissextile")
    racine.geometry("420x200")
    vue = VueBissextile(racine, None)
    controleur = ControllerBissextile(vue)
    vue.action_verifier = controleur.verifier
    vue.pack(fill="both", expand=True)
    racine.mainloop()

if __name__ == "__main__":
    main()
