import random


def choiix(utilisateur, aleatoire) :
    """
    :param utilisateur: ce parametre definit le choix de l'utilisateur'
    :param aleatoire: ce parametre definit le choix du pc'
    :return: string qui contient la reponse du fight
    """
    print(aleatoire)
    if aleatoire == "Pierre" and utilisateur == "Ciseau":
        return "Vous avez perdu"
    elif aleatoire == "Feuille" and utilisateur == "Ciseau":
        return "Vous avez gagner"

a = input("Choisisez Pierre, Feuille ou Ciseau")
choix = ["Pierre", "Feuille", "Ciseau"]
b = random.choice(choix)
resultat = choiix(utilisateur=a, aleatoire=b)
print(resultat)

