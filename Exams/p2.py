class Student:
    def __init__(self, dni, exp, score):
        self.dni = dni
        self.exp = exp
        self.score = score

    def __str__(self):
        return f"DNI: {self.dni}, EXP: {self.exp}, SCORE: {self.score}"


def n_student(min):
    correct = False
    while not correct:
        try:
            student = int(input("Cuantos usuarios quieres introducir: "))
            if student >= min:
                correct = True
            else:
                raise ValueError
        except ValueError:
            print(f"Valor erroneo, mene un numero mayor a {min}")
    return student

def read_nexp(min_n):
    correct = False
    while not correct:
        try:
            number = int(input("Please, enter nexp:"))
            if number > min_n:
                correct = True
        except ValueError:
            print("Incorrect value.", end=" ")
    return number

def read_score(min_n, max_n):
    correct = False
    while not correct:
        try:
            number = float(input("Please, enter score:"))
            if min_n <= number <= max_n:
                correct = True
        except ValueError:
            print("Incorrect value.", end=" ")
    return number

def read_dni():
    correct = False
    while not correct:
        dni = input("Enter the DNI:")
        if len(dni) == 9 and dni[0:7].isdigit() and dni[-1].isalpha():
            correct = True
    return dni

students_list = []

students = n_student(3)
for i in range(1, students + 1):
    dni = read_dni()
    exp = read_nexp(0)
    score = read_score(0, 10)
    s = Student(dni, exp, score)
    students_list.append(s)

for s in students_list:
    print(s)

max_score = students_list[0]
min_core = students_list[0]
media = 0
for s in students_list:
    if s.score > max_score.score:
        max_score = s
    elif s.score < min_core.score:
        min_core = s
    media += s.score

print(f"max_score: {max_score}")
print(f"min_score: {min_core}")
print(f"MEDIA: {media/students}:.3f")











