import tkinter as tk
from View.menu import VuePairs
from Controller.controller import ControllerPairs

def main():
    racine = tk.Tk()
    racine.title("TP1.2 — Pairs")
    racine.geometry("560x340")
    vue = VuePairs(racine, None)
    controleur = ControllerPairs(vue)
    vue.action_calculer = controleur.calculer
    vue.pack(fill="both", expand=True)
    racine.mainloop()

if __name__ == "__main__":
    main()
