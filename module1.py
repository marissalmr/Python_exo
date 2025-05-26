#Un magasin vend 6 types de vis. Chaque type a un stock limité et un prix unitaire. Écris une fonction qui demande à l'utilisateur combien de vis il veut pour chaque type. Si la quantité dépasse le stock, on met 0. Écris une deuxième fonction qui calcule le prix total de la commande, en fonction des quantités et des prix.
def mystere(L):
    prix1 = [0.10,0.15,0.20,0.18,0.30,0.50]
    res = 0
    for i in range(0,6):
        res = res + prix1[i]*L[i]
    return res

def commande(L):
    quantite = [200,300,350,300,250,100]
    vis = ["type1", "type2", "type3", "type4", "type5", "type6"]
    commande = []
    for i in range(0,6):
        qte_comamnde = int(input(" Choisisez le nombre de vis que vous voulez"))
        if (qte_comamnde>quantite[i]):
            commande.append(0)
        else :
            commande.append(qte_comamnde)

    return commande



#qte_comamnde.append(L)


#quantite = [200,300,350,300,250,100]
#vis = ["type1", "type2", "type3", "type4", "type5", "type6"]

#for i in range(len(vis)) : #Il faut savoir combien de fois faire la boucle
    #print(f"Voici les de vis : {vis[i]} : et leurs quantité : {quantite[i]}")

#commande_pers = int(input("Quel est votre commande ? "))

#calcult_commande = commande(commande_pers)
#mys = mystere(calcult_commande)







