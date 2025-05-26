#Crée une classe CompteBancaire avec : -un titulaire (nom) , -un solde initial, -une méthode deposer(montant), -une méthode retirer(montant), -une méthode afficher_solde() qui affiche le solde.
#Crée un compte, fais des dépôts et retraits, puis affiche le solde.

class Comptebancaire:
    def __init__(self,nom,solde):
        self.nom = nom
        self.solde = solde

    def deposer(self,montant):
        self.solde = self.solde + montant


    def retirer(self,montant):
        self.solde = self.solde - montant

    def afficher_solde(self):
        print(f"Le solde actuel est de {self.solde}")

compte1 = Comptebancaire("Marie", 13643)
compte1.afficher_solde()
compte1.deposer(10)
compte1.afficher_solde()
compte1.retirer(15)
compte1.afficher_solde()
