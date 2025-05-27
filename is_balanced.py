#Vérifie que les parenthèses sont bien fermées et imbriquées.
def is_balanced(a):
    liste_ouverte=[]
    liste_fermer=[]
    for i in a :
        if i == "(":
            liste_ouverte.append(i)
        elif i == ")":
            liste_fermer.append(i)
    if len(liste_fermer) == len(liste_ouverte):
        return True
    else :
        return False
