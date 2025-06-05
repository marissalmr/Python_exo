liste = ["chat", "chien", "chat", "oiseau", "chien", "chien", "oiseau"]
#Output attendu : ["chat", "chien", "__", "oiseau", "__"]
crochet = "__"
final_list = liste.copy()
for index, i in enumerate(liste):
    new_list = liste[index+1:]
    for indexx, j in enumerate(new_list):
        if i == j:
            liste[index] = crochet
print(liste)