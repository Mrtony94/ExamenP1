import json


def find_donnors(donnors, person):
    list_donnors = donnors["donantes"]
    posible = []
    gs = person["grupo"]
    for d in list_donnors:
        if gs in d["dona_a"] and d["name"] != person["name"]:
            posible.append(d["name"])
    return posible


def is_posible_donnor(group, p):
    found = False
    i = 0
    while i < len(group) and not found:
        if group[i] in p["dona_a"]:
            found = True
    return found


def find_donnors_change(donnors, person): # meter a grupo mas de 1 elemento
    list_donnors = donnors["donantes"]
    posible = []
    gs = person["grupo"]
    for d in list_donnors:
        if is_posible_donnor(gs,d) and d["name"] != person["name"]:
            posible.append(d["name"])
    return posible


def find_person(dict_donnors, name):
    list_donnors = dict_donnors["donantes"]
    i = 0
    found = False
    result_dict = {}
    while i < len(list_donnors) and not found:
        person_dict = list_donnors[i]
        if person_dict["name"].lower() == name.lower():
            found = True
        i += 1
        if found:
            return person_dict
        else:
            return None
    return result_dict


with open("./donantes.json", "r") as f:
    str_data = f.read()
    dict_donnors = json.loads(str_data)

# print(dict_donnors)
name = input("A quien estas buscando: ")
find_person(dict_donnors, name)
dict_person = find_person(dict_donnors, name)
if dict_person:
    list_possible_donnors = find_donnors(dict_donnors, dict_person)
    print("continuo")
    print(list_possible_donnors)
    if len(list_possible_donnors) > 0:
        print(list_possible_donnors)
    else:
        print("no hay posibles donantes")
else:
    print("no se encontro a la persona")