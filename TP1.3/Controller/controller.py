from Model.fichier import decouper_noms, generer_messages

class ControllerAccueil:
    def __init__(self, vue):
        self.vue = vue

    def generer(self, texte: str):
        noms = decouper_noms(texte)
        return generer_messages(noms)
