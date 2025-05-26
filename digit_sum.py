# Somme des chiffres, Implémente digit_sum(n: int) -> int qui calcule la somme des chiffres de n. : Ex. digit_sum(2729) == 2+7+2+9 == 19.
import math
def digit_sum(chiffre_from_user):
    somme1=0
    extraction = chiffre_from_user / 1000
    arrondi = math.floor(extraction)
    print(arrondi)
    multiple_extraction = arrondi * 1000
    reste = chiffre_from_user - multiple_extraction
    somme1 += arrondi
    #print(somme1)


    extraction = reste / 100
    arrondi = math.floor(extraction)
    print(arrondi)
    multiple_extraction = arrondi * 100
    restee = reste - multiple_extraction
    somme1 += arrondi
    #print(somme1)
    #print(restee)

    extraction = restee / 10
    arrondi = math.floor(extraction)
    print(arrondi)
    multiple_extraction = arrondi * 10
    resteee = restee - multiple_extraction
    somme1 += arrondi
    #print(somme1)

    #print(resteee)

    extraction = resteee / 1
    arrondi = math.floor(extraction)
    print(arrondi)
    multiple_extraction = arrondi * 1
    resteeee = resteee - multiple_extraction
    somme1 += arrondi
    print(somme1)

    #print(resteeee)

