from Model.fichier import est_bissextile

class ControllerBissextile:
    def __init__(self, vue):
        self.vue = vue

    def verifier(self, annee_brute: str):
        try:
            annee = int(annee_brute)
        except ValueError:
            return "Erreur"
        return f"{annee} est bissextile" if est_bissextile(annee) else f"{annee} n'est pas bissextile"
