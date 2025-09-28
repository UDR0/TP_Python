def est_bissextile(annee: int) -> bool:
    "Renvoie True si l'année est bissextile, sinon False."
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)
