# Crée une classe Vehicule avec un nom et une quantité d’essence. Elle contient une méthode se_deplacer() qui affiche un message générique.
#Puis, crée deux classes qui héritent de Vehicule : Voiture, qui a en plus une puissance, et redéfinit la méthode se_deplacer() pour afficher "Je roule..."
#Avion, qui a en plus une marchandise transportée, et redéfinit aussi se_deplacer() avec un message personnalisé.
#Enfin, crée un objet Voiture et un objet Avion, puis appelle leur méthode se_deplacer() pour tester le comportement de chaque classe.


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

