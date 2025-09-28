import tkinter as tk
from View.menu import VueAccueil
from Controller.controller import ControllerAccueil

def main():
    racine = tk.Tk()
    racine.title("TP1.3 — Messages d'accueil")
    racine.geometry("520x420")
    vue = VueAccueil(racine, None)
    controleur = ControllerAccueil(vue)
    vue.action_generer = controleur.generer
    vue.pack(fill="both", expand=True)
    racine.mainloop()

if __name__ == "__main__":
    main()
