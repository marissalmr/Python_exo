from random import*


somme_1 = 0
somme_2 = 0
compteur = 0
while True:

    de_1 = randint(1,6)
    de_2 = randint(1,6)
    somme_1 +=de_1
    somme_2 +=de_2
    compteur = compteur + 1
    if somme_1>21 or somme_2>21 :
        print("perdu")
        break
    elif somme_1 == 21 or somme_2 == 21 :
        print("Gagné")
        print(f"Joueur 1 : {somme_1}, Joueur 2 : {somme_2}")
        break

