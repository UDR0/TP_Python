from functools import reduce
import operator

def nombres_pairs_jusqua(n: int):
    return [i for i in range(2, n+1, 2)]

def somme_et_produit(n: int):
    pairs = nombres_pairs_jusqua(n)
    somme = sum(pairs)
    produit = reduce(operator.mul, pairs, 1) if pairs else 0
    return pairs, somme, produit
