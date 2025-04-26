
class CompteBancaire:
    def __init__(self,nom,solde):
            self.nom = nom
            self._solde = solde

    def _getsolde(self):
        return self._solde

    def _setsolde(self,valeur):
        if valeur < 0 :
            print("Les valeurs négatifs ne sont pas autorisés")
        else :
            self._solde = valeur

    solde = property(_getsolde, _setsolde)


b1 = CompteBancaire("Marissa", 3453)
b1.solde = -12
print(b1.solde)
b1.nom = "Lili"
print(b1.nom)

class Portefeuille :
    def __init__ (self,nom,argent):
        self.nom = nom
        if argent < 0 :
            print ("Erreur doit etre positif")
            self.argent = 0
        else :
             self._argent = argent

    def _getargent(self):
        return self._argent


    def _setargent(self, valeur):
        if valeur < 0 :
            print("Le montant ne peut pas etre négatif")

    def _delargent(self):
        print("Argent supprimé pour : {}".format(self.nom))
        del self._argent
    methode = property(_getargent,_setargent, _delargent)

    def ajouter(self,montant):
        try:
             if montant<0 :
                raise ValueError("Il faut un montant positif"):
                    self.argent += montant

    def retirer(self,montant):
        if montant > self.argent :
            print("Vous n'avez pas assez d'argent pour retirer")
        else :
            self.argent -= montant

