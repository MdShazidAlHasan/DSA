class _Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next

class QueuesLinked:

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        newest = _Node(e, None)
        if self.is_empty():
            self._front = newest
            self._rear = newest
        else:
            self._rear._next = newest
            self._rear = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            print('This Queue is empty')
            return
        else:
            e = self._front._element
            self._front = self._front._next
        self._size -= 1
        return e

    def first(self):
        if self.is_empty():
            print('This Queue is empty')
            return
        else:
            return self._front._element
