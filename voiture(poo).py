#Crée une classe Voiture avec deux attributs : marque et modèle. Elle doit avoir deux méthodes :
# demarrer() : affiche un message indiquant que la voiture démarre. arreter() : affiche un message indiquant qu'elle s'arrête.
#Ensuite, crée deux objets Voiture, appelle les méthodes et observe les messages affichés.

class Voiture :
    def __init__(self,marque,modele):
        self.marque = marque
        self.modele = modele

    def demarrer(self):
        print(f"la voiture {self.marque}, demarre")

    def arreter(self):
        print(f"la voiture {self.marque} s'arrete")

voiture1 = Voiture(marque="Renault", modele="29")
voiture2 = Voiture("Clio", "26")


voiture1.demarrer()
voiture2.demarrer()
voiture1.arreter()















