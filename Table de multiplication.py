from random import *
aleatoire = randint(1,101)
nomb_choisi = int(input("chiffre"))
while nomb_choisi !=aleatoire:
    if nomb_choisi < aleatoire :
         print("Prend un nombre plus grand")
         nomb_choisi = int(input("chiffre"))

    else :
        print("Prend un nombre plus petit")
        nomb_choisi = int(input("chiffre"))

print(f"Bravo le nombre est bien {nomb_choisi}")

