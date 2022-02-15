"""
Python Stack Class
"""


class Stack:
    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)



if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(3)
    s.push(2)
    s.pop()
    print(s.peek())
    print(s)