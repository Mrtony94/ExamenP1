lo estoy haciendo, pero no consigo que me guarde el pokemon que busco
si tienes algo pásatelo

# Ejercicio 2 - PST
# Javier Zapatero Lera
# 54300753F

class Student:
    def __init__(self, asignatura, exp, nota):
        self.asignatura = asignatura
        self.exp = exp
        self.nota = nota

    def __str__(self):
        return f"Asignatura: {self.asignatura} Nexp: {self.exp} Score: {self.nota}"

    def __repr__(self):
        return self.__str__()


def read_n_student():
    exit = False
    while not exit:
        try:
            n = int(input("Please, enter the number of students you want to add: "))
            exit = True
        except ValueError:
            print("That wasn't a number")
    return n


def read_asignatura():
    asignatura = input("Enter de course: ")
    return asignatura


def read_nexp(min_value):
    correct = False
    while not correct:
        try:
            number = int(input("Please, enter nexp:"))
            if number > min_value:
                correct = True
        except ValueError:
            print("Incorrect value.", end=" ")
    return number


def read_score(min_value, max_value):
    correct = False
    while not correct:
        try:
            number = float(input("Please, enter score:"))
            if min_value <= number <= max_value:
                correct = True
        except ValueError:
            print("Incorrect value.", end=" ")
    return number


def add_student():
    for i in range(0, n):
        asignatura = read_asignatura()
        exp = read_nexp(0)
        nota = read_score(0, 10)
        estudiante = Student(asignatura, exp, nota)
        lista_estudiantes.append(estudiante)
    return lista_estudiantes


def menor_nota(lista):
    estudiante = lista_estudiantes[0]
    for s in lista:
        if s.nota < estudiante.nota:
            estudiante = s
    return f"Lower student: {estudiante}"


def media_notas(lista):
    total = 0
    contador = 0
    for s in lista:
        total += s.nota
        contador += 1
    return f"Average: {total/contador}"


def leer_encontrar_asignatura():
    asignatura = input("Enter a course: ")
    return asignatura


def encontrar_asignatura(lista, asignatura):
    lista_estudiantes_asignatura = []
    for s in lista:
        if s.asignatura.lower() == asignatura:
            lista_estudiantes_asignatura.append(s)
    if len(lista_estudiantes_asignatura) > 0:
        return lista_estudiantes_asignatura
    else:
        return f"No hay ninguna coincidencia"


lista_estudiantes = []
n = read_n_student()
print(add_student())
print(menor_nota(lista_estudiantes))
print(media_notas(lista_estudiantes))
asignatura = leer_encontrar_asignatura()
print(encontrar_asignatura(lista_estudiantes, asignatura))
