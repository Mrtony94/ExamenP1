### Ejercicio 4: Recibe una cadena de texto del usuario y determina si un carácter, escrito también por el usuario, se encuentra en dicha cadena.

def cadena(char):
    return char.isdigit()

ok = False

while not ok:
    try:
        char = input("introduce una frase: ")
        n = cadena(char)
        if len(char) > 1:
            if n:
                raise ValueError
            else:
                a = input("introduce el caracter que quieres buscar: ")
                if len(a) == 1:
                    if a in char:
                        print(f"El caracter que buscabas --> {a} se encuenta dentro de la cadena --> {char}")
                    ok = True
                else:
                    raise ValueError
        else:
            raise ValueError
    except ValueError:
        print(f"El valor introducido debe contener una cadena de texto, intentelo de nuevo")