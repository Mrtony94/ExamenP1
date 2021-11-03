# ---------------------------------------------------------------------------------------- #
                                    # Diccionario
# ---------------------------------------------------------------------------------------- #

dic = {"nombre": "Javi", "edad": 23, "aficiones": ["deporte", "dibujar", "cerveza"]}

print(dic.keys())   # Claves del diccionario

print(dic.values())   # Valores del diccionario

print(dic["nombre"])    # Acceder al valor de una clave
print(dic["edad"])
print(dic["aficiones"])
print(dic["aficiones"][0])      # Si el valor es una lista, acceder a una posición

for key in dic:                 # Recorrer todo el diccionario e imp clave y valor
    print(key, ":", dic[key])

print(dic.clear())    # Borrar un diccionario

dic.pop("edad")    # Elimina una clave y devuelve su valor
print(len(dic))    # Longitud de un diccionario


# ---------------------------------------------------------------------------------------- #
                                    # Listas
# ---------------------------------------------------------------------------------------- #

dic1 = {"nombre": "Javi", "edad": 23, "aficiones": ["deporte", "dibujar", "cerveza"]}
dic2 = {"nombre": "Tony", "edad": 26, "aficiones": ["estudiar", "programar", "limonada"]}

lista = [dic1, dic2, 2, 3, 4, 5, "hola", "que", "haces"]

print(lista)        # Imprimir lista todo seguido
print(lista[1])     # Imprimir un elemento de la lista
print(lista[1]["nombre"])     # Imprimir un valor de un diccionario dentro de una lista
print(lista[len(lista)-1])      # Imprimir último valor

for i in lista:       # Recorrer una lista e imprimir sus elementos
    print(i)

lista.append("nada")      # Añadir al final de una lista
lista.append(dic1)

lista.remove("hola")      # Eliminar un elemnto de la lista

print(lista.index("que"))       # Imprimir el íncide de un elemento de la lista

lista.count(dic1)        # Te devuelve el numero de veces que hay repetido un elemento de la lista

lista.sort()       # Ordenar una lista de menor a mayor

lista.sort(reverse=True)        # Ordenar una lista de mayor a menor
