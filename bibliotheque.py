#Crée deux classes : Livre : avec un titre et un auteur, et une méthode pour afficher les infos du livre.
#Bibliotheque : qui peut contenir plusieurs livres, avec : une méthode pour ajouter un livre, une méthode pour afficher la liste des titres
#Ensuite : Crée un livre, Affiche ses infos, Ajoute-le dans la bibliothèque, Affiche les titres présents dans la bibliothèque


class livre:
    def __init__(self,titre,auteur):
        self.titre = titre
        self.auteur = auteur


    def afficher_info(self):
        print(f"Le titre du livre est {self.titre} et l'auteur est {self.auteur}")


class bibliotheque:
    def __init__(self):
        self.liste = []

    def ajouter_livre(self,livre):
        self.liste.append(livre)

    def afficher(self):
        for livre in self.liste:
            print(livre.titre)



livre1 = livre("Harry Potter", "")
livre1.auteur = "hjkgghjg"
livre1.afficher_info()
bibli = bibliotheque()
bibli.ajouter_livre(livre1)
bibli.afficher()

