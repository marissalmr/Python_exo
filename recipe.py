#Crée une classe Recipe représentant une recette de cuisine. Elle doit contenir : 
# un titre, une description, une liste d'ingrédients, des étapes, un utilisateur (auteur)
#Ajoute une méthode afficher_info() qui affiche le titre et le nom de l’auteur.
#Crée ensuite une instance de recette, affiche ses infos, puis modifie l’auteur et réaffiche les infos.
class recipe:
    def __init__(self,titre, desc, ingr, etapes, user):
        self.titre = titre
        self.desc = desc
        self.ingr = ingr
        self.etapes = etapes
        self.user = user


    def afficher_info(self):
        print(f"Le titre de la recipe est {self.titre} et l'auteur est {self.user}")


recipe1 = recipe("my recipe", "saleeee", "udfhyg", "etap1", "")
recipe1.afficher_info()
recipe1.user = "Marissa"
recipe1.afficher_info()

