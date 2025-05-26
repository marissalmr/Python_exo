# Dans une liste où chaque nombre apparaît deux fois sauf un seul, retrouve ce nombre. Ex : [2, 3, 2, 4, 3] → 4

def remove_items(test_list, item):

    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]
    return res

list = [8,5,6,5,8,3,6,7,7]
list_vide = []
trouve = []
for index, i in enumerate(list):
    list_vide = list[index+1:]
    for j in list_vide:
        if j == i:
            trouve.append(i)

for t in trouve:
    list = remove_items(list,t)

print(list)
