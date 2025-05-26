#Crée une classe Animal avec : un nom une méthode parler() qui affiche : "Je suis un animal." Puis, crée une classe Chien qui hérite de Animal et redéfinit la méthode parler() pour dire : "Woof ! Je m'appelle [nom]".

class Animal :
    def __init__(self,nom):
        self.nom = nom

    def parler(self):
        print("Je suis un animal")

class Chien(Animal):
    def parler(self):
        print(f"Woof ! Je m'appelle {self.nom}")


chiwawa = Chien("Yeti")
chiwawa.parler()