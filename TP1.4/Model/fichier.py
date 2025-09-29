import operator, random

OPERATIONS = {
    "addition": ("+", operator.add, 0, 20),
    "soustraction": ("-", operator.sub, 0, 20),
    "multiplication": ("×", operator.mul, 0, 12),
    "division": ("÷", operator.floordiv, 1, 12),
}

def generer_question(type_operation: str):
    symbole, fonction, bas, haut = OPERATIONS[type_operation]
    a = random.randint(bas, haut)
    b = random.randint(bas if type_operation != "division" else 1, haut)
    if type_operation == "division":
        a = a * b  # pour que la division tombe juste
    reponse = fonction(a, b)
    texte = f"Combien fait {a} {symbole} {b} ?"
    return (a, b, reponse, texte)
