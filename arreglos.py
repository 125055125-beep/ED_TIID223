
 #Declarando un arreglo bien
numeros=[10,20,30,40,50]
""" 
# Imprime la posicion 30
print(numeros[2])

#Reasignar el valor de la pocision 3 a 15
numeros[3]= 15
print(numeros)

#Agregamos un valor nuevo al final nuestro arreglo
numeros.append(60)
print(numeros)

#manipulacion de arreglos

#eliminar un valor de un arreglo por pocisiones
numeros.pop(1)
print(numeros) 

#otra forma para eliminar con  remove por valor
numeros.remove(30)
print(numeros) """

frutas=["mango","Manzana,","uva", "pera", "Maracuya"]
frutas.remove("uva")
print(frutas)

frutas.pop(3)
print(frutas)

frutas.append("platano")
print(frutas)

frutas[2]= "fresa"
print(frutas)

#arreglo vacio
arreglo=[]
n = int(input("ingresa el tamaño del arreglo:"))
n1= int(input("ingresa valor 0"))
arreglo.append(n1)
print(arreglo)
#usuario diga la longitud del arreglo
#input imprimir en pantalla
#n para guardar el tamaño del arreglo
#int lo que hay dentro del arreglo
