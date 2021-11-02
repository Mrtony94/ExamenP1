### Ejercicio 3: Recibir un número del usuario e imprimir por pantalla si ese número se encuentra entre 0 y 100.


ok = False
while not ok:
    try:
        num = input("Introduce un numero: ")
        if len(num) == 1:
            num = int(num)
            if 0 <= num <= 100:
                print(f"El numero introducido es: {num}")
                ok = True
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("El Valor introducido es erroneo, por favor introduce otro")