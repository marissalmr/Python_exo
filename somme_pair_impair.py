# Somme pair/impaire : Donne une liste d’entiers, retourne deux sommes : la somme des pairs et la somme des impairs
pair = 0
impair = 0

for i in range(101):
    if i%2 == 0:
        pair = pair + i
    else:
        impair = impair + i

print(pair)
print(impair)


