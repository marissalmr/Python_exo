L =  [21,5,25,12,8] 
#print(len(L))
#L[3] = 13
#L[4] = L[4]-2
#print(L)
#L.append(17)
#print(L)
#del(L[2])
#print(L)

#Lt = sorted(L)
#print(Lt)
#P = ["Marie", "Lola" , "Nina"]
#pT = sorted(P)
#print(pT)

#Ecrire une fonction repatrtion qui prend en parametre une liste de nombres entiers et renvoie deux listes nommées pair et impair qui contiendront les nombres de la liste

def repartition(L):
    liste_pair = []
    liste_impair = []
    for i in L:
        if i % 2 == 0 :
            liste_pair.append(i)
        else :
            liste_impair.append(i)
    return liste_pair, liste_impair


#L=[12,34,56,23]
#print(repartition(L))

#Ecrire une fonction suppr qui prend en paramettres une liste L et elimine de cette liste tous les 0

def suppr(E):
    i = 0 #Permettra de parcourir la liste élément par élément
    while i<len(E) : #Tant que i n'a pas parcouru la liste en entière
        if E[i] == 0: #Si l'élement qui se trouve à la postion i dans la liste E est égal à 0
            del(E[i]) #Tu le supprime de la liste E
        else :
            i =  i+1 #Sinon tu continue à parcourir la liste
    return E #Quand la boucle est terminé tu m'affiche le résultat final avec la liste E

#E=[12,43,0,23,0,34,34,0]
#print(suppr(E))

#Ecrire une fonction lancers prenant en parametre un entier n qui permet de génerer une liste correspondant à n lancers d'un dé à 6 faces, ou n est un entier  
def lancers(n):
    resultat = [] #Création d'une liste vide ou on stockera les résultats des lancers
    from random import randint
    for i in range(n): #va permettre de répeter l'action n fois selon ce que la personne va insérer
        resultat.append(randint(1,6)) #Tirer un nombre aléatoire entre 1 et 6 et va l'ajouter dans resultat 
    return resultat

n = int(input("Entrer qlqc"))
print(lancers(n))
