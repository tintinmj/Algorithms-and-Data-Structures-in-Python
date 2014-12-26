class Stack():
    def __init__(self):
        """Initializes an empty stack"""
        self.items=[]
    def pop(self):
        """Pops out the element from top of the stack"""
        self.items.pop()
    def push(self,item):
        """Pushes an item on the top of the stack"""
        self.items.append(item)
    def isEmpty(self):
        """Returns True if the stack is empty else False"""
        return self.items == []
    def peek(self):
        """Returns the element at the top of the Stack """
        return self.items[-1]
    def clear(self):
        """Clear the Stack """
        return self.items = []


s = Stack()
s.push(2)
s.push("Diljit")
s.push("Avirup")
s.pop()
print s.peek()
print s.isEmpty()
s.pop()
print s.peek()
s.pop()
print s.isEmpty()
