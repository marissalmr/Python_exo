#max_of_three(a, b, c) -> int Retourne le plus grand des trois nombres.
def max_of_three(a,b,c):
    stock_valeur = 0

    if a>b and b>c :
        return a
    elif b > c :
        return b

    return c

