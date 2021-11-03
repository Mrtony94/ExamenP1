"""

Hacer una clase student que contenga nombre y nota
-cuantos usuarios metes done
-Que te lea el nombre done
-que te lea la nota done
-estudiantes aprobados
-mayor nota

"""


class Student:
    def __init__(self, name, note):
        self.name = name
        self.note = note

    def __str__(self):
        return f"NAME: {self.name} | NOTE: {self.note}"

    def __repr__(self):
        return self.__str__()


def read_nstudent():
    correct = False

    while not correct:
        try:
            nstudent = int(input("¿Cuantos usuarios quieres meter?: "))
            if 0 < nstudent <= 100:
                correct = True
            else:
                raise ValueError
        except ValueError:
            print(f"El numero de estudiantes esta fuera de rango y/o "
                  f"has introducido un caracter, repite ")
    return nstudent


def read_name():
    correct = False
    while not correct:
        try:
            name = input("¿Cual es el nombre del usuario?: ").lower()
            if len(name) != 0 and len(name) < 15:
                correct = True
            else:
                raise ValueError
        except ValueError:
            print(f"El nombre que has introducido es erroneo ")
    return name


def read_nota():
    correct = False
    while not correct:
        try:
            nota = float(input("¿Que nota tiene el alumno?: "))
            if 0 < nota <= 10:
                correct = True
            else:
                raise ValueError
        except ValueError:
            print(f"La nota es erronea, vuelve a introducirla")
    return nota


def add_class(list_student):
    num_student = read_nstudent()
    for _ in range(num_student):
        name = read_name()
        nota = read_nota()
        s = Student(name, nota)
        list_student.append(s)
    return list_student


def pass_student(list_student):
    list_pass_student = []
    for s in list_student:
        if s.note >= 4.8:
            print(f"El estudiante {s} ha aprobado")
            list_pass_student.append(s)
        else:
            print(f"El estudiante {s} ha suspendido")
    return list_pass_student


def mayor_nota(lista):
    mayor = lista[0]
    for n in lista[1:]:
        if n.note > mayor.note:
            mayor = n
    return mayor

# Main
student_list = []
add_class(student_list)
print(pass_student(student_list))
print(mayor_nota(student_list))
