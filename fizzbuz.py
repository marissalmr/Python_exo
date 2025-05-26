#Affiche les nombres de 1 à 100, mais pour les multiples de 3 affiche « Fizz », pour les multiples de 5 affiche « Buzz », et pour les deux affiche « FizzBuzz ».



for i in range (101):
    if i%3==0 and i%5==0:
        print(f"{i} :Fizzbuzz")
    elif i%3==0:
        print(f"{i} : Fizz")
    elif i%5==0:
        print(f"{i} :Buzz")

