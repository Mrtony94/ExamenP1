"""
Antonio Andres Perez
DNI:47580369Q
"""
class Student:
    def __init__(self, nexp, course, score):
        self.course = course
        self.nexp = nexp
        self.score = score

    def __str__(self):
        return f"NEXP: {self.nexp} | COURSE: {self.course} | score: {self.score}"

    def __repr__(self):
        return self.__str__()


def read_nstudent():
    correct = False

    while not correct:
        try:
            nstudent = int(input("Please, enter the number of students you want to add: "))
            if nstudent >= 0:
                correct = True
            else:
                raise ValueError
        except ValueError:
            print(f"There are some error in the number of student ")
    return nstudent


def read_course():
    correct = False
    while not correct:
        try:
            course = input("Enter the course:").lower()
            if len(course) != 0:
                correct = True
        except ValueError:
            print("Incorrect value.", end=" ")
    return course


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

def average(list_student):
    average_score = 0
    count = 0
    for s in list_student:
        average_score += s.score
        count += 1
    average_total = average_score/count
    return average_total

def lower_score(lista):
    lower = lista[0]
    for n in lista[1:]:
        if n.score < lower.score:
            lower = n
    return lower

def add_class(list_student):
    num_student = read_nstudent()
    for _ in range(num_student):
        nexp = read_nexp(0)
        course = read_course()
        score = read_score(0,10)
        s = Student(nexp, course, score)
        list_student.append(s)
    return list_student


# Main
student_list = []
add_class(student_list)
print(f"Lower student: {lower_score(student_list)}")
print(f"Average: {average(student_list):.3}")
print(f"{student_list})


