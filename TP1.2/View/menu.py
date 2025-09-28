import tkinter as tk

class VuePairs(tk.Frame):
    def __init__(self, maitre, action_calculer):
        super().__init__(maitre, padx=16, pady=16)
        self.action_calculer = action_calculer
        self.var_n = tk.StringVar()
        self.var_somme = tk.StringVar(value="—")
        self.var_detail_somme = tk.StringVar(value="—")
        self.var_produit = tk.StringVar(value="—")
        self.var_detail_produit = tk.StringVar(value="—")

        tk.Label(self, text="Somme et produit des nombres pairs", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0,12))

        tk.Label(self, text="Entier positif N :").grid(row=1, column=0, sticky="e")
        tk.Entry(self, textvariable=self.var_n).grid(row=1, column=1, sticky="we")

        tk.Button(self, text="Calculer", command=self._clic_calculer).grid(row=2, column=0, columnspan=2, sticky="we", pady=8)
        tk.Button(self, text="Réinitialiser", command=self._reinitialiser).grid(row=3, column=0, columnspan=2, sticky="we", pady=4)

        tk.Label(self, textvariable=self.var_somme).grid(row=4, column=0, columnspan=2, sticky="w", pady=(10,0))
        tk.Label(self, textvariable=self.var_detail_somme).grid(row=5, column=0, columnspan=2, sticky="w")
        tk.Label(self, textvariable=self.var_produit).grid(row=6, column=0, columnspan=2, sticky="w", pady=(10,0))
        tk.Label(self, textvariable=self.var_detail_produit).grid(row=7, column=0, columnspan=2, sticky="w")

        self.columnconfigure(1, weight=1)

    def _clic_calculer(self):
        try:
            n = int(self.var_n.get())
            if n < 0:
                raise ValueError
            lignes = self.action_calculer(n)
            self.var_somme.set(lignes['somme'])
            self.var_detail_somme.set(lignes['detail_somme'])
            self.var_produit.set(lignes['produit'])
            self.var_detail_produit.set(lignes['detail_produit'])
        except ValueError:
            self.var_somme.set("Erreur")
            self.var_detail_somme.set("—")
            self.var_produit.set("—")
            self.var_detail_produit.set("—")

    def _reinitialiser(self):
        self.var_n.set("")
        self.var_somme.set("—")
        self.var_detail_somme.set("—")
        self.var_produit.set("—")
        self.var_detail_produit.set("—")
