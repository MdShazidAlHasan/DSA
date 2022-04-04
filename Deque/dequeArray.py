from exceptions import Empty

class ArrayDeque:
    def __init__(self):
        self._data = []
        self._font = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty('DEQUE is empty')
        return self._data[self._font]

    def add_first(self, e):
        self._data.insert(self._font, e)

    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Empty('DEQUE is empty')
        return self._data.pop(self._font)

    def delete_last(self):
        if self.is_empty():
            raise Empty('DEQUE is empty')
        return self._data.pop()

Q = ArrayDeque()
