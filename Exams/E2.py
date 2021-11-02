class Students:
    def __init__(self, dni, exp, score):
        self.dni = dni
        self.exp = exp
        self.score = score

    def __str__(self):
        return f"DNI: {self.dni}, EXP: {self.exp}, SCORE: {self.score}"


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

def read_students(n):
    correct = False
    while not correct:
        try:
            number = int(input(" Please, enter the number of students you want to add: "))
            if number >= n:
                correct = True
            else:
                raise ValueError
        except ValueError:
            print("Incorrect value.", end=" ")
    return number

students_list = []

study = read_students(3)


for i in range(1, study + 1):
    dni = read_dni()
    exp = read_nexp(0)
    score = read_score(0, 10)
    s = Students(dni, exp, score)
    students_list.append(s)

for s in students_list:
    print(s)

higher_student = students_list[0]
lower_student = students_list[0]
average = 0

for s in students_list:
    if s.score > higher_student.score:
        higher_student = s
    elif s.score < lower_student.score:
        lower_student = s
    average += s.score


print(f"Higher student: {higher_student}")
print(f"Lower student: {lower_student}")
print(f"Average: {average/study}.3f")
