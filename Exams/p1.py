def introduce_numeros():
    ok = False
    while not ok:
        try:
            numero = int(input("Escriba un numero entero: "))
            if 1 <= numero <= 100:
                ok = True
            else:
                raise ValueError
        except ValueError:
            print("Introduce un numero correcto")
    return numero

def primos(numero):
    primos = []
    for i in range(2, numero + 1):
        primos.append(i)

    for i in primos:
        multiplo = i * 2
        while multiplo < numero:
            if multiplo in primos:
                primos.remove(multiplo)
            multiplo += i
    return primos

n = introduce_numeros()
y = primos(n)
print(f"P: {y}")
