matriz=[
    [1,2,3],
    [4,5,6]
]

print("mostrar la matriz")
for fila in matriz:
    print(fila)

""" un valor en especifico """

print("muestra el 6")
print(matriz[1][2])


""" mostrar la fila 0 """

print(matriz[0])

""" reasignando un valor """

matriz[1][1] = 8
print(matriz)

""" arreglo de tres filas """

matriz.append([7,8,9])
print(matriz)
print("")                           

matriz[0].pop(2)
print("Eliminar el ultimo de la primera fila")
for fila in matriz:
    print(fila)