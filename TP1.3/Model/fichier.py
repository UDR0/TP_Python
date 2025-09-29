import random

SALUTATIONS_PAR_DEFAUT = ["Bonjour", "Salut", "Bienvenue"]

def decouper_noms(texte: str):
    morceaux = [p.strip() for p in texte.replace("\n", ",").split(",")]
    return [p for p in morceaux if p]

def generer_messages(noms, salutations=None):
    salutations = salutations or SALUTATIONS_PAR_DEFAUT
    return [f"{random.choice(salutations)} {nom} !" for nom in noms]
