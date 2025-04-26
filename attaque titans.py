from random import *
joueur1 = input("Choisisez votre pseudo")
print(joueur1)
joueur2= input("Choisisez votre pseudo")
print(joueur2)
joueur1.points = 250
joueur2.points = 250
nb_degats_1 = 0
nb_degats_2 = 0
random_attack = randint(0,100)

attaque = True
for combat in range(0,5):
    if attaque == True :
        nb_degats_1 += random_attack or nb_degats_2 += random_attack



