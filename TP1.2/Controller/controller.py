from Model.fichier import somme_et_produit

class ControllerPairs:
    def __init__(self, vue):
        self.vue = vue

    def calculer(self, n: int):
        pairs, s, p = somme_et_produit(n)
        if not pairs:
            return {
                'somme': "0 = 0",
                'detail_somme': "0 = 0",
                'produit': "0 = 0",
                'detail_produit': "0 = 0",
            }
        somme_gauche = " + ".join(map(str, pairs))
        produit_gauche = " * ".join(map(str, pairs))
        return {
            'somme': f"{somme_gauche} = {s}",
            'detail_somme': f"{s} = {somme_gauche}",
            'produit': f"{produit_gauche} = {p}",
            'detail_produit': f"{p} = {produit_gauche}",
        }
