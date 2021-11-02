### Ejercicio 5: Escribe un script que reciba números ilimitados del usuario, pare cuando reciba 0, y escriba la media de los números recibidos.

# num = int
# average = 0
# count = 0
# while num != 0:
#     try:
#         num = int(input("Introduce un numero: "))
#         count += 1
#         average += num
#     except ValueError:
#         print("El Valor introducido es erroneo, por favor introduce otro")
#
# print(f"La media de los numeros introducidos es {average/(count-1)}")

# v2

num1 = int
average1 = 0
num_list = []
while num1 != 0:
    try:
        num1 = int(input("Introduce un numero: "))
        num_list.append(num1)
        average1 += num1
    except ValueError:
        print("El Valor introducido es erroneo, por favor introduce otro")

print(f"La media de los numeros introducidos es {average1/(len(num_list)-1)}")

