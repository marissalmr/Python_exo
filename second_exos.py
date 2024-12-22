# second exos file
from itertools import count


phrase = input("Donnez moi une phrase: ")
voyelles = ["a","e","i","o","u","y"]

count = 0
for car in count:
    if car in voyelles:
        count = count + 1
print(count)