class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre} -> Edad: {self.edad}"

    def __repr__(self):
        return self.__str__()


def pedir_n_personas():
    ok = False
    while not ok:
        try:
            n = int(input("Escribe cuántas personas quieres añadir: "))
            ok = True
        except ValueError:
            print("Introduce un número correcto")
    return n


def pedir_nombre():
    nombre = input("Introduce un nombre: ")
    return nombre


def pedir_edad():
    ok = False
    while not ok:
        try:
            edad = int(input("Introduce la edad: "))
            ok = True
        except ValueError:
            print("Introduce una edad correcta")
    return edad


def añadir_persona():
    for _ in range(0, n):
        nombre = pedir_nombre()
        edad = pedir_edad()
        p = Persona(nombre, edad)
        lista_personas.append(p)
    return lista_personas


def mas_18(lista_personas):
    lista_personas_mayores = []
    for persona in lista_personas:
        if persona.edad >= 18:
            lista_personas_mayores.append(persona)
        else:
            lista_personas_mayores = None
    return lista_personas_mayores


lista_personas = []
n = pedir_n_personas()
print(añadir_persona())
print(mas_18(lista_personas))
