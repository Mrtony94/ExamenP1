#Ejercicio 1: Definir una función que reciba dos números y devuelva el mayor de ellos (Con su correspondiente prueba de que funciona).

def number(n1, n2):
    mayor = 0
    if n1 < n2:
        mayor = n2
        print(f"El mayor de los numeros es {mayor}")
    elif n2 < n1:
        mayor = n1
        print(f"El mayor de los numeros es {mayor}")
    else:
        print(f"Los numeros son iguales primer numero{n1}, segundo numero{n2}")


ok = False

try:
    n1 = int(input("introduce el 1º numero: "))
    n2 = int(input("Introduce el 2º numero: "))
    if n1 < 0 and n2 < 0:
        raise ValueError
    else:
        number(n1,n2)
except ValueError:
    print("El numero introducido es negativo vuelve a introducir el numero")

n = n1.isdigit()



