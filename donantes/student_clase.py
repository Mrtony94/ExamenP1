class Student:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return f"{self.nombre}, {str(self.nota)}" #str por el float


def read_nstudent():
    exit = False
    while not exit:
        try:
            n = int(input("introduce numero de estudiantes: "))
            exit = True
        except ValueError:
            print("el numero no es numero ")
    return n


def read_note():
    exit = False
    while not exit:
        try:
            n = float(input("introduce numero de estudiantes: "))
            if 10 >= n >= 0:
                exit = True
        except ValueError:
            print("el numero no es numero ")
    return n

def estudiantes_aprobados(lista):
    lista_student = []
    for s in lista:
        if s.nota >= 4.8:
            lista_student.append(s.nombre)
    return lista_student

n = read_nstudent()
lista_student = []
for i in range(0, n):
    nombre = input("introduce el nombre: ")
    nota = read_note()
    s = Student(nombre, nota)
    lista_student.append(s)

aprobados = estudiantes_aprobados(lista_student)
if len(aprobados) == 0:
    print("No aprobo ningun estudiante ")
    for a in aprobados:
        print(a) # con str
else:
    print(f"Lista de estudiantes aprobados {aprobados}")

def mayor_note(lista):
    estudiante = None
    mayor_nota = -1
    for s in lista:
        if s.nota > mayor_nota:
            estudiante = s

    return estudiante
