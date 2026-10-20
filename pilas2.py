def pedir_numero():
    """Solicita un número al usuario y lo valida."""
    while True:
        try:
            return float(input("Ingresa un número: "))
        except ValueError:
            print("Entrada no válida. Debes ingresar un número.")


def mostrar_menu():
    print("\n===== MENÚ PILA =====")
    print("1. Insertar en pila")
    print("2. Borrar en pila")
    print("3. Listar pila")
    print("4. Salir")


def ejecutar_pila():
    pila = []

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            numero = pedir_numero()
            pila.append(numero)  # Se apila en la cima
            print(f"Se insertó {numero} en la pila.")

        elif opcion == "2":
            if pila:
                eliminado = pila.pop()  # Se quita el último (cima)
                print(f"Se eliminó el elemento de la cima: {eliminado}")
            else:
                print("La pila está vacía.")

        elif opcion == "3":
            if pila:
                print("Pila actual (base -> cima):", pila)
                print("Vista vertical:")
                for elemento in reversed(pila):
                    print(f"  | {elemento} |")
                print("  -------")
            else:
                print("La pila está vacía.")

        elif opcion == "4":
            print("Saliendo de la pila...")
            break

        else:
            print("Opción no válida. Elige entre 1 y 4.")


def main():
    while True:
        ejecutar_pila()
        respuesta = input("\n¿Deseas ejecutar el programa nuevamente? (s/n): ").strip().lower()
        if respuesta != "s":
            print("Programa finalizado.")
            break


if __name__ == "__main__":
    main()