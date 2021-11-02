class NegativeNumber(Exception):
    def __init__(self, num):
        self.num = num

min = 1
max = 5
num_list = []
correct = False
while not correct:
    try:
        for i in range(min, max + 1):
            i = int(input("introduce numero: "))
            if i < 0:
                raise NegativeNumber(i)
            else:
                correct = True
            num_list.append(i)
    except ValueError:
        print("ha introducido una letra introduzca una palabra")
    except NegativeNumber as e:
        print(f"has introducido un numero negativo {e.num}")

x = num_list

print(x)
