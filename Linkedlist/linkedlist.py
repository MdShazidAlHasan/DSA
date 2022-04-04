class _Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._next = next
        self._element = element

class LinkedList:
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
            self._head = newest 
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def addfirst(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest 
            self._tail = newest
        else: 
            newest._next = self._head 
            self._head = newest 
        self._size += 1

    def addany(self, e, position): # indexing starts from 0 
        newest = _Node(e, None)
        p = self._head
        i = 0
        while i < position -1:
            p = p._next
            i = i + 1
        newest._next = p._next
        p._next = newest
        self._size += 1
    
    def removefirst(self):
        if self.isempty():
            print('LinkedList is empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._tail = None
        return e

    def removelast(self):
        if self.isempty():
            print("LinkedLists is empty")
            return
        p = self._head
        i = 0
        
        while i< self._size-2:
            p = p._next
            i += 1
        self._tail = p
        e = p._next._element
        p._next = None
        self._size -= 1
        return e

    def removeany(self, position):
        p = self._head
        i = 0
        while i<position -1:
            p = p._next
            i +=1
        e = p._next._element
        p._next = p._next._next
        self._size -= 1
        return e

    def search(self, key)-> int:
        p = self._head 
        index = 0
        while p:
            if p._element == key:
                return index 
            p = p._next
        
        return 'NOT FOUND!!'

    def display(self):
        p = self._head 
        while p:
            print(p._element, end = '-->')
            p = p._next
        print()
        
L = LinkedList()
L.addlast(2)
L.addlast('pi')
L.addlast(0)
