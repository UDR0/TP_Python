import tkinter as tk

class VueJeuCalcul(tk.Frame):
    def __init__(self, maitre, action_nouvelle_question, action_verifier):
        super().__init__(maitre, padx=16, pady=16)
        self.action_nouvelle_question = action_nouvelle_question
        self.action_verifier = action_verifier

        self.var_type = tk.StringVar(value="addition")
        self.var_question = tk.StringVar(value="Clique sur « Nouvelle question »")
        self.var_reponse = tk.StringVar()
        self.var_commentaire = tk.StringVar(value="—")
        self.var_score = tk.StringVar(value="Score : 0 / 0")

        tk.Label(self, text="Jeu de calcul mental", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0,12))

        tk.Label(self, text="Opération :").grid(row=1, column=0, sticky="e")
        ops = ["addition", "soustraction", "multiplication", "division"]
        tk.OptionMenu(self, self.var_type, *ops).grid(row=1, column=1, sticky="we")

        tk.Button(self, text="Nouvelle question", command=self._nouvelle_question).grid(row=2, column=0, columnspan=2, sticky="we", pady=6)

        tk.Label(self, textvariable=self.var_question, font=("Arial", 12)).grid(row=3, column=0, columnspan=2, sticky="w", pady=6)

        tk.Entry(self, textvariable=self.var_reponse).grid(row=4, column=0, sticky="we", pady=4)
        tk.Button(self, text="Valider", command=self._verifier).grid(row=4, column=1, sticky="we", pady=4)

        tk.Label(self, textvariable=self.var_commentaire, font=("Arial", 11, "bold")).grid(row=5, column=0, columnspan=2, sticky="w", pady=8)
        tk.Label(self, textvariable=self.var_score, fg="gray").grid(row=6, column=0, columnspan=2, sticky="w", pady=(4,0))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def _nouvelle_question(self):
        texte_q = self.action_nouvelle_question(self.var_type.get())
        self.var_question.set(texte_q)
        self.var_reponse.set("")
        self.var_commentaire.set("—")

    def _verifier(self):
        commentaire, score = self.action_verifier(self.var_reponse.get())
        self.var_commentaire.set(commentaire)
        self.var_score.set(score)
