### Ejercicio 6: Escribe una función que reciba una lista y devuelva una lista con los valores ordenados de manera ascendente.

def ordenar(n):
    n.sort()
    return n.pop(0)

num1 = int
num_list = []
while num1 != 0:
    try:
        num1 = int(input("Introduce un numero: "))
        num_list.append(num1)
    except ValueError:
        print("El Valor introducido es erroneo, por favor introduce otro")


ordenar(num_list)
print(num_list)


lista = [8, 23, 5, 2, 19, 25, 22]
ordenados = sorted(lista, reverse=True)

print(ordenados)
