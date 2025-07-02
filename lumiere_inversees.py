#Tu as une rangée de n interrupteurs (ex : [False, False, False]).
#Chaque fois que tu appuies sur un interrupteur à la position i, il inverse son état ET celui juste après (i+1). Ton but est d’obtenir toutes les lumières allumées (True).
lumiere = [0,0,0,0,0,0]
nombre = 1
choix = int(input("1 pour le 1er interupteur, sinon 2 ou 3"))

while choix !=0:
        choix = choix - 1 

        if choix>len(lumiere):
             choix = choix % len(lumiere)
             print(choix)

        if lumiere[choix] == 0:
            lumiere[choix] = 1
        else:
            lumiere[choix] = 0    

        if lumiere[choix+1] == 0 :
            lumiere[choix+1] = 1
        else:
            lumiere[choix+1] = 0
        
   
        
        
        print(lumiere)
        print(10%6)
        choix = int(input("1 pour le 1er interupteur, sinon 2 ou 3"))


