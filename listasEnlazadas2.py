
#Clase que representa la estructura de un nodo
class Nodo:
    def __init__(self, numero):
        #Valor que tendrá el nodo
        self.numero = numero

        #Apunta a nuestro siguiente nodo
        self.siguiente = None

#Clase que va a administrar todos los nodos
class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None

    def Insertar_Nodo_Al_Inicio(self, numero):
        nuevo_nodo = Nodo(numero)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self, numero):
        nuevo_nodo = Nodo(numero)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        #Referencia temporal
        actual = self.cabeza

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def Eliminar_Nodo_Al_Inicio(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay nada que eliminar.")
            return

        #La cabeza pasa al segundo nodo; el primero queda sin referencias
        self.cabeza = self.cabeza.siguiente

    def Eliminar_Nodo_Al_Final(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay nada que eliminar.")
            return

        #Si solo hay un nodo, la lista queda vacía
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        #Buscamos el penúltimo nodo
        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente

        #El penúltimo nodo ahora apunta a None
        actual.siguiente = None

    def Imprimir_ListaEnlazada(self):
        actual = self.cabeza

        while actual:
            print(actual.numero, "->", end=" ")
            actual = actual.siguiente
        print("None")

Mi_lista = ListasEnlazadas()
Mi_lista.Insertar_Nodo_Al_Inicio(5)
Mi_lista.Insertar_Nodo_Al_Inicio(4)
Mi_lista.Insertar_Nodo_Al_Inicio(3)
Mi_lista.Imprimir_ListaEnlazada()       

Mi_lista.Eliminar_Nodo_Al_Inicio()
Mi_lista.Imprimir_ListaEnlazada()      

Mi_lista.Eliminar_Nodo_Al_Final()
Mi_lista.Imprimir_ListaEnlazada()