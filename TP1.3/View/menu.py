import tkinter as tk

class VueAccueil(tk.Frame):
    def __init__(self, maitre, action_generer):
        super().__init__(maitre, padx=16, pady=16)
        self.action_generer = action_generer

        tk.Label(self, text="Messages d'accueil personnalisés", font=("Arial", 14, "bold")).pack(pady=(0,12))

        tk.Label(self, text="Entre une liste de noms (séparés par des virgules ou des retours à la ligne) :").pack(anchor="w")
        self.zone_texte = tk.Text(self, height=6, width=40)
        self.zone_texte.pack(fill="both", expand=False, pady=6)

        tk.Button(self, text="Générer", command=self._generer).pack(fill="x", pady=6)

        self.liste_resultats = tk.Listbox(self, height=8)
        self.liste_resultats.pack(fill="both", expand=True, pady=6)

    def _generer(self):
        brut = self.zone_texte.get("1.0", "end").strip()
        messages = self.action_generer(brut)
        self.liste_resultats.delete(0, "end")
        for m in messages:
            self.liste_resultats.insert("end", m)
