elementos = []
repetir = True

while repetir:
    print("\n--- PILA ---")
    print("1. Apilar")
    print("2. Desapilar")
    print("3. Mostrar elementos")
    print("4. Salir")

    while True:
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            valor = int(input("Numero que deseas guardar: "))
            elementos.append(valor)
            print("Elemento agregado.")

        elif opcion == "2":
            if len(elementos) == 0:
                print("La pila esta vacia.")
            else:
                print("Elemento eliminado:", elementos.pop())

        elif opcion == "3":
            print("Elementos de la pila:", elementos)

        elif opcion == "4":
            repetir = False
            break
        

        else:
            print("Opcion incorrecta.")

print("Programa finalizado.")