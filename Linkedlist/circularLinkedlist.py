class _Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._next = next
        self._element = element

class CircularLinkedList:
    def __init__(self):
        self._head = None 
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size 

    def isempty(self):
        return self._size == 0

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            newest._next = newest
            self._head = newest 
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def display(self):
        p = self._head
        i = 0
        while i < self._size:
            print(p._element, end = "-->")
            p = p._next
            i = i + 1
        print()

    def addfirst(self, e):
        newest = _Node(e, None)
        if self.isempty():
            newest._next = newest
            self._head = newest
        else:
            self._tail._next = newest
            newest._next = self._head
            self._head = newest
        
        self._size += 1

    def addany(self, e, position):
        newest = _Node(e, None)
        p = self._head
        i = 0
        while i < position - 1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1
    
    def removefirst(self):
        if self.isempty():
            print('NOT FOUND ANY ELEMENT')
            return
        e = self._head._element
        self._tail._next = self._head._next
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._head = None 
            self._tail = None
        return e

    def removelast(self):
        if self.isempty():
            print('NOT FOUND ANY ELEMENT')
            return
        i = 0
        p = self._head
        while i<self._size -2:
            p = p._next
            i += 1      
        e = self._tail._element
        self._tail = p
        p._next = self._head
        self._size -= 1

        if self.isempty():
            self._head = None 
            self._tail = None
        return e
    def removeany(self, position):
        p = self._head
        i = 0
        while i < position- 1:
            p = p._next
            i += 1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e

L = CircularLinkedList()
L.addlast(2)
L.addlast('pi')
L.addlast(0)
