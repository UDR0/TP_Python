import tkinter as tk

class VueConvertisseur(tk.Frame):
    def __init__(self, maitre, action_convertir):
        super().__init__(maitre, padx=16, pady=16)
        self.action_convertir = action_convertir
        self.var_mode = tk.StringVar(value="C2F")
        self.var_entree = tk.StringVar()
        self.var_resultat = tk.StringVar(value="—")

        tk.Label(self, text="Convertisseur C° - F°", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0,12))

        tk.Radiobutton(self, text="Celsius -> Fahrenheit", variable=self.var_mode, value="C2F").grid(row=1, column=0, sticky="w")
        tk.Radiobutton(self, text="Fahrenheit -> Celsius", variable=self.var_mode, value="F2C").grid(row=1, column=1, sticky="w")

        tk.Label(self, text="Température :").grid(row=2, column=0, sticky="e", pady=8)
        tk.Entry(self, textvariable=self.var_entree).grid(row=2, column=1, sticky="we", pady=8)

        tk.Button(self, text="Convertir", command=self._clic_convertir).grid(row=3, column=0, columnspan=2, pady=8, sticky="we")

        tk.Label(self, text="Résultat :").grid(row=4, column=0, sticky="e", pady=(8,0))
        tk.Label(self, textvariable=self.var_resultat, font=("Arial", 12, "bold")).grid(row=4, column=1, sticky="w", pady=(8,0))

        self.columnconfigure(1, weight=1)

    def _clic_convertir(self):
        mode = self.var_mode.get()
        try:
            valeur = float(self.var_entree.get())
            resultat = self.action_convertir(mode, valeur)
            self.var_resultat.set(resultat)
        except ValueError:
            self.var_resultat.set("Erreur")
