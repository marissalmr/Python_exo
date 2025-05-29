# Convertit "aaabbcccc" en "a3b2c4"
dic_vide = {}
chaine = "aabbcba"
lettre = ''
for i in chaine : 
    if i in dic_vide:
        dic_vide[i]+=1 #clé reste la meme valeur, et valeur gagne +1
    else :
        dic_vide[i] = 1 



#print(dic_vide)
for i in dic_vide:
    lettre += f"{i}{dic_vide[i]}"
    #print(f"{i}{dic_vide[i]}")
print(lettre)
    

    