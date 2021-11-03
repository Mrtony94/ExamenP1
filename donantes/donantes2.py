'''

-abrir fichero
-buscamos un nombre dentro de la lista de dicccionarios (vamos a comparar con ese si alguien le puede donar a el)
- añadir los posibles donantes a la lista

'''

import json


def read_name():
    ok = False
    while not ok:
        try:
            name = input("Introduce el nombre: ")
            if len(name) != 0:
                ok = True
            else:
                raise ValueError
        except ValueError:
            print("El nombre es erroneo")
    return name


def find_person(diccionario, person):
    list_donnor = diccionario['donantes']
    found = False
    i = 0
    person_dic = {}
    while i < len(list_donnor) and not found:
        person_dic = list_donnor[i]
        if person.lower() == person_dic['name'].lower():
            found = True
        i += 1
    if found:
        return person_dic
    else:
        return None


def find_possible_donante(diccionario, person):
    list_donnor = diccionario['donantes']
    grupo_donante = person['grupo']
    possible_donante = []
    for d in list_donnor:
        if grupo_donante in d['dona_a'] and person['name'] != d['name']:
            possible_donante.append(d['name'])
    return possible_donante


with open("donantes.json") as f:
    str_data = f.read()
    diccionario_donantes = json.loads(str_data)

name = read_name()
datos_donado = find_person(diccionario_donantes, name)


if datos_donado:
    posibles_donante = find_possible_donante(diccionario_donantes, datos_donado)
    if len(posibles_donante) > 0:
        print(posibles_donante)
    else:
        print("no hay donantes")
else:
    print("no hay donante")