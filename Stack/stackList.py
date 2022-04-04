from exceptions import Empty

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, element):
        if element is None:
            return
        self.data.append(element)

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self.data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self.data[-1]

