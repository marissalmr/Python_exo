#Vérifie si la liste augmente puis diminue strictement, comme une montagne.
a = [5,8,13,16,8]
new_liste = []
for index, i in enumerate(a): 
    index_suivant = index + 1
    if index_suivant >= len(a): #Pour ne pas etre en dehors de la liste
        #print(False)
        break
    if i == a[index_suivant]:
        a.pop(index_suivant)
#print(a)

courbe = []

for index, i in enumerate(a) : #chiffre de la liste et leurs index 
    index_suivant = index + 1 #Pour comparer i et celui après lui
    liste_vide = []

    if index_suivant >= len(a): #Pour ne pas etre en dehors de la liste
        #print(False)
        continue
    if len(a)<3:
        #print("pas possible")
        break
    if a[0]>a[index_suivant] and index == 0:
        print("pas possible")
        break
    if  i < a[index_suivant] : #Si le premier chiffre (i) et supérieur à celui d'après (index_suivant)
        courbe.append("monte")
        continue
    if i > a[index_suivant]:
        courbe.append("descente")

print(courbe)
tmp = courbe.copy()
for index, i in enumerate(courbe): 
    index_suivant = index + 1
    if index_suivant >= len(courbe): #Pour ne pas etre en dehors de la liste
        #print(False)
        continue
    print(i)
    print(courbe[index_suivant])
    if i == courbe[index_suivant]:
        tmp.pop(index)




print(tmp)


    