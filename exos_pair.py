def is_pair(n) :
    if n % 2 == 0 :
        return True

    return False


for i in range(2,21) :
    result = is_pair(i)
    if result is True :
        print(f"{i} il est pair")