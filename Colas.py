from  collections import deque

def pedir_numero():
    while True:
        try:
            return float(input("Ingrese un número: "))
        except ValueError:
            print("Error: debes ingresar otro numero.")


    
def mostrar_menu():

    print("========Menu colas========")
    print("1. Insertar en cola")
    print("2. Eliminar de cola")
    print("3. Mostrar cola")
    print("4. Salir")

def ejecutar_cola():
    cola = deque()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()


        if opcion == "1":
            numero = pedir_numero()
            cola.append(numero)
            print(f"se inserto {numero} en la cola.")

        elif opcion == "2":
            if cola:
                eliminado = cola.popleft()
                print(f"se elimino el primer elemento: {eliminado}")

            else: 
                print("la cola esta vacia")


        elif opcion == "3":
            if cola:
                print("cola actual (frente -> final):", list(cola))
            else:
                print("la cola esta vacia")

        elif opcion == "4":
            print("saliendo de la cola")
            break

        else:
            print("opcion no valida elige otra del 1 al 4")


            def main():
                while True:
                    ejecutar_cola()
                    respuesta = input ("¿desas ejecutar el programa nuevamente? (s/n):").strip().lower()
                    if respuesta !=  "s":
                        print("programa finalizado")
                        break

            if __name__ == "__main__":
                main()


                