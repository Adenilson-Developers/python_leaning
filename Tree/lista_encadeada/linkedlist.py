from node import Node
#sequencial  = []
#sequencial.append(7)

class LinkedList: 
    def __init__(self):
        self.head = None
        self.size = 0
    def append(self, elem):
        if self.head:
            # inserção quando a lista jpa possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            #primeira inserção
            self.head = Node(elem)
        


lista = LinkedList()
lista.append(7)