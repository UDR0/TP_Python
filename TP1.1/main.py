import tkinter as tk
from View.menu import VueConvertisseur
from Controller.controller import ControllerConvertisseur

def main():
    racine = tk.Tk()
    racine.title("TP1.1 — Convertisseur")
    racine.geometry("400x220")
    vue = VueConvertisseur(racine, None)
    controleur = ControllerConvertisseur(vue)
    vue.action_convertir = controleur.convertir_temperature
    vue.pack(fill="both", expand=True)
    racine.mainloop()

if __name__ == "__main__":
    main()
