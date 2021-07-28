"""
Code used for the class 'Circular Linked List'.

Las listas enlazadas circulares son un tipo de lista enlazada en la que el último nodo apunta hacia el
headde la lista en lugar de apuntar None. Esto es lo que los hace circulares.

"""


class Node(object):
    "Represents a single linked node."
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


index = 1
new_item = "ham"

head = Node(None, None)
head.next = head

# Search for node at position index - 1 or the last position
probe = head

while index > 0 and probe.next != head:
    probe = probe.next
    index -= 1

# Insert new node after node at position index - 1 or last position
probe.next = Node(new_item, probe.next)

print(probe.next.data)