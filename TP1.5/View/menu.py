import tkinter as tk

class VueBissextile(tk.Frame):
    def __init__(self, maitre, action_verifier):
        super().__init__(maitre, padx=16, pady=16)
        self.action_verifier = action_verifier
        self.var_annee = tk.StringVar()
        self.var_resultat = tk.StringVar(value="—")

        tk.Label(self, text="Année bissextile ?", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0,12))

        tk.Label(self, text="Entre une année :").grid(row=1, column=0, sticky="e")
        tk.Entry(self, textvariable=self.var_annee).grid(row=1, column=1, sticky="we")

        tk.Button(self, text="Vérifier", command=self._verifier).grid(row=2, column=0, columnspan=2, sticky="we", pady=8)

        tk.Label(self, textvariable=self.var_resultat, font=("Arial", 12, "bold")).grid(row=3, column=0, columnspan=2, sticky="w", pady=6)

        self.columnconfigure(1, weight=1)

    def _verifier(self):
        self.var_resultat.set(self.action_verifier(self.var_annee.get()))
