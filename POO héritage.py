# Créé par melin, le 23/04/2025 en Python 3.7
class Vehicule : #class mere
    def __init__(self,nom_vehicule, quantite_essence):
        self.nom = nom_vehicule
        self.essence = quantite_essence

    def se_deplacer(self) :
        print("Le vehicule {} se déplace".format(self.nom))


#Class Fille

class Voiture(Vehicule):
    def __init__(self, nom_voiture,essence,puissance): # donc la en gros il a tout ce que le vehicule peut faire mais a&vec des chose en plus ça la complete un peu en attributr la classe fille c une sorte de la classe mere

        Vehicule.__init__(self,nom_voiture,essence) # expliuque moi ça a quoi ça sert

        self.puissance = puissance

    def se_deplacer(self):
        print("Je roule...")
#redefinir une methode qui exists deja dans la classe mere

class Avion(Vehicule):
    def __init__(self,nom,essence,marchandise):
        Vehicule.__init__(self,nom, essence) # expliuque moi ça a quoi ça sert

        self.marchandise = marchandise

    def se_deplacer(self):
        print("Je roule...")

#On peut faire de l'heritagr multiple :

class Etudiant :
    pass

class Enseignant:
    pass

class Doctorant(Etudiant,Enseignant):
    pass

voiture1 = Voiture("Toyota", 239, 234)
voiture1.se_deplacer()
av1 = Avion("F22", 2400, "Missiles")
av1.se_deplacer()

help(for)