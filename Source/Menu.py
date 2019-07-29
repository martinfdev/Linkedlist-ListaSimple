#!/usr/bin/python3
#import Source.ListaSimple

#definiendo metodo para hacer el ciclo de perdir un numero entero en la opcion del menu
def pedir_numero_entero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Introduce una opcion: "))
            correcto = True
        except ValueError:
            ("Introduce la opcion correcta! ")      
    return num
salir = False
opcion = 0


#cilo de opciones dependiente de la opcion a elegir  
while not salir:
    print("1    Insertar al inicio")
    print("2    Insertar al final")
    print("3    Buscar Elemento")
    print("4    Eliminar Elemento")
    print("5    Imprimir la lista")
    print("6    Salir")
    print("Elige una opcion")
    opcion =  pedir_numero_entero()

    if opcion == 1:
        print("Insertar al inicio")
    elif opcion == 2:
        print("Insertar al final")
    elif opcion == 3:
        print("Buscar Elemento")
    elif opcion == 4:
        print("Eliminar Elemento")
    elif opcion == 5:
        print("Motrar Todos los Elementos de la lista")     
    elif opcion == 6:
        salir = True    

    else:                   
        print("Introduce un numero entre 1 y 5")
print("fin de menu")

#Creando la clase Nodo
#class node:
#    def __init__(self, data = None, next = None):
#        self.data = data
#        self.next = next

#creando la lista enlazada
class ListaSimple:
    def __init__(self):
        self.head = None

    #metodo para agregar al principio en la lista
    def agrearAlPrincipio(self, data):
        self.head = node(data = data, next = self.head)

    #metodo para verificar si esta vacia la lista
    def estaVacia(self):
        return self.head == None

    #metodo para agregar al final de la lista
    def agregarAlFinal(self, data):
        if not self.head:
            self.head = node(data = data)
            return
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node(data =data)

    #metodo para eliminar nodos
    def eliminarNodo(self, key):
        curr = self.head
        prev = None

        while curr and curr.data != key:
            prev =  curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.nex = None
        
    #metodo para obtener el ultlmo nodo
    def devolverUltimoNodo(self):
        temp = self.head
        while (temp.next is not None):
            temp =  temp.next
        return temp.data

    #metodo para imprimir la lista
    def iprimirLista(self):
        node = self.head
        while  node != None:
            print(node.data)
            node = node.next
