# systeme pour suivre la positiion d'un poersonnage dans un jeu vidéo
from random import *
class Personnage :
    def __init__(self, nom, position):
        self.nom = nom
        self._position = position


    def _getposition(self):
        return self._position


    def _setposition(self, position):
        if position[0] < 0 or position[1]<0 :
            print("Erreur")
        else :
            self._position = position

  position = property(_getposition, _setposition)


    def afficher_position(self):
        print("Position actuelle de {} : {}".format(self.nom,self._position))


    def get_nouvelle_position(self):
        x = randint(1,300)
        y = randint(1,300)
        return (x,y) #tuple



class Guerrier(Personnage):
    def __init__(self,nom,position,force):
        Personnage.__init__(self,nom,position)
        self.force = force

    def afficher_position():
        print("Guerrie {} est à la position {} avec une force de {}".format(self.nom,self._position, self.force))


Papa = Personnage("Papa", "Algerie")
Maman = Guerrier("Maman" , "Paris" , "1080 xp")
print(isinstance(Papa,Personnage))


