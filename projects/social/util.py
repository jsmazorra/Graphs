
class Queue():
    def __init__(self):
        self.list = []
    def __len__(self):
        return len(self.list)
    def __str__(self):
        return str(self.list)
    
    def enqueue(self, value):
        self.list.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.list.pop(0)
        else:
            return None
    def size(self):
        return len(self.list)
    def append(self, value):
        return len(self.append)

class Stack():
    def __init__(self):
        self.list = []
    def __len__(self):
        return len(self.list)
    def __str__(self):
        return str(self.list)

    def push(self, value):
        self.list.append(value)
    def pop(self):
        if self.size() > 0:
            return self.list.pop()
        else:
            return None
    def size(self):
        return len(self.list)
