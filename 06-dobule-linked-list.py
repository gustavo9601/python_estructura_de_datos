"""
Code used for the class 'Double Linked List'.
"""

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class TwoWayNode(Node):
    def __init__(self, data, previous=None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous

# Create a doubly linked list with one node
head = TwoWayNode(1)
tail = head

# Add four node to the end of the linked list
for data in range(2, 6):
    tail.next = TwoWayNode(data, tail)
    tail = tail.next
