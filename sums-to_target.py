#sums_to_target(lst: list[int], target: int) -> bool Retourne True si deux éléments de la liste s’additionnent pour donner target. Ex : [2, 7, 11, 15], target = 9 → True (car 2 + 7 = 9)
def sums_to_target(liste,chiffre_recherche):
    copie = []
    for index, i in enumerate(liste):
        copie = liste[index+1:]
        for j in copie:
            if i + j == chiffre_recherche:
                return chiffre_recherche

    return False


