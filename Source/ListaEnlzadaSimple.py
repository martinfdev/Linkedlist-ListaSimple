
#!/usr/bin/python3
import sys
#Creando la clase Nodo
class node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

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
            self.head = node(data=data)
            return
           
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)

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
        
    #metodo buscar nodo
    def buscarNodo(self, key):
        temp = self.head
        while temp != None and temp.data != key:
            temp =  temp.next 
        return temp

    #metodo para imprimir la lista
    def iprimirLista(self):
        node = self.head
        while  node != None:
            
            print(node.data, end="-> ")
            node = node.next

    #metodo modicar valor
    def modificarNodo(self, key):
        auxNodo = buscarNodo(key)
        auxNodo = node(input("Ingrese el nuevo valor: "))





ls = ListaSimple() #instanciando la lista

#definiendo metodo para hacer el ciclo de perdir un numero entero en la opcion del menu
def pedir_numero_entero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(input("Elige la opcion: "))
            correcto = True
        except:
            ("Introduce la opcion correcta! ")      
    return num
salir = False
opcion = 0


#ciclo de opciones dependiente de la opcion a elegir  
while not salir:
    
    print("")
    print ("-----------------Menu------------------")
    print("1    Insertar al inicio")
    print("2    Insertar al final")
    print("3    Buscar Elemento")
    print("4    Modificar")
    print("5    Eliminar Elemento")
    print("6    Ver lista")
    print("7    Salir")
    opcion =  pedir_numero_entero()

    if opcion == 1:
       ls.agrearAlPrincipio(input("Ingrese Valor: ")) 
    elif opcion == 2:
        ls.agregarAlFinal(input("Ingrese Valor entero: "))
    elif opcion == 3:
        dato = ls.buscarNodo(input("Ingrese el valor a buscar: "))
        print("El valor es: ", dato.data)
    elif opcion == 4:
        mod = ls.buscarNodo(input("Ingrese el valor a modificar: "))
        mod.data = input("Ingres el nuevo valor: ")
    elif opcion == 5:
        ls.eliminarNodo(input("Ingrese Valor a eliminar: "))
    elif opcion == 6:
        ls.iprimirLista()
    elif opcion == 7:
        salir = True    

    else:                   
        print("Introduce un numero entre 1 y 5")
print("Programa terminado!!")