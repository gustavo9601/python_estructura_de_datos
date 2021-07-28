"""
Nodes y singly linked list
Las estructuras linked consisten en nodos conectados a otros, los más comunes son sencillos o dobles.
No se accede por índice sino por recorrido. Es decir se busca en la lista de nodos hasta encontrar un valor.

Data: Será el valor albergado en un nodo.
Next: Es la referencia al siguiente nodo en la lista
Previous: Será el nodo anterior.
Head: Hace referencia al primer nodo en la lista
Tail: Hace referencia al último nodo.



Double Linked Structure.
Estos hacen que el nodo haga referencia al siguiente nodo y al anterior, es decir nos va a permitir ir en
ambas direcciones. También nos permitirá realizar “formas” y contextos circulares.

El ejemplo clave aquí será función de ctrl+z y ctrl+y Estas opciones nos permiten hacer y deshacer un
proceso en Windows.

El historial del navegador también es un buen ejemplo al permitirnos navegar entre el pasado y el presente.

"""


class Node(object):
    "Represents a single linked node."

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# Creating 3 differents nodes
node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)

# This causes an Atribute Error
# node1.next = node3

node1 = Node("C", node3)
print(node1.next.data)
