#Écris une fonction qui renvoie tous les sous-tableaux dont la somme est égale à target. [1, 2, 3, 4], target = 5 → sous-tableaux : [2, 3], [1, 4].


def find_subarrays(arr,target):
    liste_vide1=[]
    for i in range (len(arr)) :
            
        for j in range (i+1,len(arr)):
            if arr[i] + arr[j] == target :
                
                liste_vide1.append([arr[i], arr[j]]) #Création d'une liste de liste
    return liste_vide1
                
res = find_subarrays([5,18, 5, 4, 1,6,], 10)
print(res)
print(res[1][1]) #Affiche le numero 2 de la deuxieme liste


 