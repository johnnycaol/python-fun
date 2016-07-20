class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
    # Utility function to print the stack
    def printStack(self):
        print(self.items)
    
stack = Stack()
stack.push('111')
stack.push('222')
stack.push('333')
stack.pop()
stack.printStack()
