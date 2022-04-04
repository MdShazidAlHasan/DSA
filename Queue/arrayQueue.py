from exceptions import Empty
class ArrayQueue:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def __repr__(self):
        return f"{self._data}"

    def is_empty(self):
        return len(self._data) == 0

    def enqueue(self, element):
        self._data.append(element)

    def dequeue(self):
        if self.is_empty():
            print('This queqe is empty')
            return
        return self._data.pop()

    def first(self):
        if self.is_empty():
            print('This queqe is empty')
            return
        return self._data[0]

Q = ArrayQueue()
