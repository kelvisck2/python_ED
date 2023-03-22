from Node import Node
#sequencial = []
#sequencial.append(7)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, elem):
        if self.head:
            #inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
            
        else:
            # primeira inserção
            self.head = Node(elem)
        self.size +=1

    def __len__(self):
        return self.size


    def get(self, index):
        #a = lista.get(6)
        pass

    def set(self, index, elem):
        #lista.set(5,9)
        pass

    def __getitem__(self, index):
        #a = lista[6]
        #a = lista.get(6)
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            return pointer.data
        raise IndentationError("ERRO")    

    def __setitem__(self, index, elem):
        #lista[5] = 9
        #lista.set(5,9)
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndentationError("ERRO")    
        

    def index(self, elem):
        """retorna o indice do elemento da lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} is not in list".format(elem))
    



"""lista = LinkedList()

print(lista.size)

lista.append(2)
lista.append(3)
lista.append(20)
lista.append(21)
lista.append(26)
lista.append(243)

#ponteiro2 = lista.head a"""

#while(ponteiro2):
 #   print(ponteiro2.data)
  #  ponteiro2 = ponteiro2.next

    

