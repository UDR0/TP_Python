import tkinter as tk
from View.menu import VueJeuCalcul
from Controller.controller import ControllerJeuCalcul

def main():
    racine = tk.Tk()
    racine.title("TP1.4 — Calcul mental")
    racine.geometry("520x320")
    controleur = ControllerJeuCalcul(None)
    vue = VueJeuCalcul(racine, controleur.nouvelle_question, controleur.verifier_reponse)
    controleur.vue = vue
    vue.pack(fill="both", expand=True)
    racine.mainloop()

if __name__ == "__main__":
    main()
