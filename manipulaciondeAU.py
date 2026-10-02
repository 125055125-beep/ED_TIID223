""" Consultar un elemento """

numeros = [10, 20, 30, 40, 50]

print(numeros[2])
print(f"Elemento en el indice 2: {numeros[2]}")

"""  Modificar un elemento """

numeros = [10, 20, 30, 40, 50]
print("Antes:  ", numeros)

numeros[2] = 100

print("Despues:", numeros)

"""  · append(60) """

numeros = [10, 20, 30, 40, 50]

numeros.append(60)

print(numeros)
print("Indice de 60:", len(numeros) - 1)


""" append([60, 70]) """

numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print(numeros)
print("Total de elementos:", len(numeros))
print("Tipo del indice 5:", type(numeros[5]).__name__)
print("El 70 esta en numeros[5][1]:", numeros[5][1])

""" append(60) y append(70) """


numeros = [10, 20, 30, 40, 50]

numeros.append(60)
numeros.append(70)

print(numeros)
print("Total de elementos:", len(numeros))
print("Indice de 70:", numeros.index(70))

""" · print(numeros[5]) e imprimir el 60 """

numeros = [10, 20, 30, 40, 50]

numeros.append([60, 70])

print("numeros[5]    ->", numeros[5])
print("numeros[5][0] ->", numeros[5][0])


"""  (insert) · insert(2, 25) """

numeros = [10, 20, 30, 40]
print("Antes:  ", numeros)

numeros.insert(2, 25)

print("Despues:", numeros)
print("25 -> indice", numeros.index(25))
print("30 -> indice", numeros.index(30))


""" · numeros = numeros + [50] """

numeros = [10, 20, 30, 40]

numeros = numeros + [50]

print(numeros)
print("50 -> indice", numeros.index(50))


""" numeros + [50, 60, 70] """

numeros = [10, 20, 30, 40]

numeros = numeros + [50, 60, 70]

print(numeros)
print("Total de elementos:", len(numeros))

""" · extend([40, 50, 60]) """

numeros = [10, 20, 30]

numeros.extend([40, 50, 60])

print(numeros)

""" extend(otros_numeros) """

numeros = [10, 20, 30]
otros_numeros = [40, 50, 60]

numeros.extend(otros_numeros)

print("numeros       :", numeros)
print("otros_numeros :", otros_numeros)

"""  numeros[len(numeros):] = [40] """

numeros = [10, 20, 30]
print("len(numeros) =", len(numeros))

numeros[len(numeros):] = [40]

print(numeros)
print("Igual que numeros[3:]? Si, ambos empiezan en el indice 3")

"""  Agregar 95 al final """

calificaciones = [70, 85, 90, 65]

calificaciones[len(calificaciones):] = [95]

print(calificaciones)


""" Agregar 80 entre 85 y 90 """

calificaciones = [70, 85, 90, 65]
calificaciones[len(calificaciones):] = [95]

calificaciones[2:2] = [80]

print(calificaciones)

"""  Arreglo completo """

calificaciones = [70, 85, 90, 65]
calificaciones[len(calificaciones):] = [95]
calificaciones[2:2] = [80]

print("Calificaciones:", calificaciones)
print("Total:", len(calificaciones))

""" Arreglo completo """

colores = ["Azul", "Amarillo", "Rosa"]
nuevos = ["Verde", "Morado", "Rojo"]

colores = colores + nuevos

print(colores)

""" Imprimir Negro """

colores = ["Azul", "Amarillo", "Rosa"]
colores = colores + ["Verde", "Morado", "Rojo"]

print("Esta Negro en la lista?", "Negro" in colores)

colores = colores + ["Negro"]

print(colores[len(colores) - 1])


""" Arreglo completo """

numeros = [10, 20, 30, 40]

numeros[2:2] = [95]
numeros = numeros + [50, 67]

print(numeros)


""" Imprimir 95 y 67 """

numeros = [10, 20, 30, 40]
numeros[2:2] = [95]
numeros = numeros + [50, 67]

print("Numero 95:", numeros[2])
print("Numero 67:", numeros[6])

""" Posiciones """

numeros = [10, 20, 30, 40]
numeros[2:2] = [95]
numeros = numeros + [50, 67]

for valor in (95, 67):
    print(f"El {valor} ocupa la posicion {numeros.index(valor)}")