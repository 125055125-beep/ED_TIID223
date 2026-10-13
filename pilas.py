# 1. crear una pila vacia 
historial =[]

# apilar / push (agregar elementos)
historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")

print("historial:", historial)

#ver elemento 
pagina_actual = historial[2]
print("pagina actual:", pagina_actual)

#desapilar /pop (eliminar el ultimo elemento ingresado)

pagina_salida = historial.pop()
print("saliendo de:", pagina_salida)

print("historial actualizado:" , historial)
