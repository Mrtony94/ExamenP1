import json

with open("pokedex.json") as f:
    str_data = f.read()
    diccionario_pokemones = json.loads(str_data)


def read_pokemon():
    ok = False
    while not ok:
        try:
            name_pokemon = input("Enter pokemon name: ").lower()
            if len(name_pokemon) != 0:
                ok = True
            else:
                raise ValueError
        except ValueError:
            print("the name is incorrect")
    return name_pokemon


def find_pokemon(diccionario, pokemon):
    list_pokemon = diccionario['pokemon']
    found = False
    i = 0
    pokemon_dic = {}
    while i < len(list_pokemon) and not found:
        pokemon_dic = list_pokemon[i]
        if pokemon == pokemon_dic['name'].lower():
            found = True
        i += 1
    if found:
        return pokemon_dic
    else:
        return None


def find_possible_pokemon(diccionario, pokemon):
    list_pokemon = diccionario['pokemon']
    possible_pokemon = []
    for d in list_pokemon:
        if d['type'] in pokemon['weaknesses']:
            possible_pokemon.append(d['name'])
    return possible_pokemon


name = read_pokemon()
datos_pokemon = find_pokemon(diccionario_pokemones, name)
print(datos_pokemon)
posibles_pokemon = find_possible_pokemon(diccionario_pokemones, datos_pokemon)
print(posibles_pokemon)

'''
if datos_pokemon:
    posibles_pokemon = find_possible_pokemon(diccionario_pokemones, datos_pokemon)
    if len(posibles_pokemon) > 0:
        print(posibles_pokemon)
    else:
        print("no hay pokemon")
else:
    print("no hay pokemon")

'''
