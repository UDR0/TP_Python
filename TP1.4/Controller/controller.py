from Model.fichier import generer_question

class ControllerJeuCalcul:
    def __init__(self, vue):
        self.vue = vue
        self.reponse_attendue = None
        self.bonnes = 0
        self.total = 0

    def nouvelle_question(self, type_operation: str):
        a, b, rep, texte = generer_question(type_operation)
        self.reponse_attendue = rep
        return texte

    def verifier_reponse(self, brut: str):
        if self.reponse_attendue is None:
            return ("Commence par générer une question.", f"Score : {self.bonnes} / {self.total}")
        self.total += 1
        try:
            utilisateur = int(brut)
        except ValueError:
            return ("Entrée invalide (entier attendu).", f"Score : {self.bonnes} / {self.total}")
        if utilisateur == self.reponse_attendue:
            self.bonnes += 1
            commentaire = "Correct tié le BOSS !"
        else:
            commentaire = f"Incorrect. Réponse attendue : {self.reponse_attendue}"
        return (commentaire, f"Score : {self.bonnes} / {self.total}")
