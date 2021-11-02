def num_in():
    correct = False
    while not correct:
        try:
            primos = int(input(f"Please, enter an integer number (1-100): "))
            if 1 <= primos <= 100:
                correct = True
            else:
                raise ValueError
        except ValueError:
            print(f"Please, enter an integer number (1-100)", end=" ")
    return primos

def primos(n):
    primos_list = []
    for i in range(2, n + 1):
        primos_list.append(i)

    for i in primos_list:
        multiplo = i * 2
        while multiplo < n:
            if multiplo in primos_list:
                primos_list.remove(multiplo)
            multiplo += i
    return primos_list

n = num_in()
y = primos(n)
print(y)
