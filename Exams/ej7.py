### Ejercicio 7: Escribe una función que reciba una lista de números y devuelva la suma de todos esos números.

def sum(n):
    sum = 0
    for i in n:
        sum += i
    return sum

num1 = int
num_list = []
while num1 != 0:
    try:
        num1 = int(input("Introduce un numero: "))
        num_list.append(num1)
    except ValueError:
        print("El Valor introducido es erroneo, por favor introduce otro")


x = sum(num_list)
print(x)