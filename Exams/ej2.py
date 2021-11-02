# Ejercicio 2: Definir una función que reciba un caracter escrito por el usuario y devuelva True si ese carácter es un número y False en caso contrario.

def numero(char):
    return char.isdigit()

ok = False

while not ok:
    try:
        char = input("introduce un caracter: ")
        n = numero(char)
        if len(char) == 1:
            if not n:
                print(f"El Valor introducido es una letra: {char} --> {numero(char)}")
            else:
                print(f"El Valor introducido es un numero: {char} --> {numero(char)}")
            ok = True
        else:
            raise ValueError
    except ValueError:
        print(f"El valor introducido debe contener solo 1 caracter, intentelo de nuevo")
