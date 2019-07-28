#Creando la clase Nodo
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

#creando la lista enlazada
class ListaEnlzadaSimple:
    def __init__(self):
        self.head = None

        #metodo para aggrar de primero en la lista
        def agrearAlPrincipio(self, data):
            self.head = node(data = data, next = self.head)

        #metodo para verificar si esta vacia la lista
        def estaVacia()    


