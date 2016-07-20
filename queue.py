from collections import deque

class Queue:
    def __init__(self):
        self.items = deque([])

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)
    
    # Utility function to print the queue
    def printQueue(self):
        print(self.items)
    
queue = Queue()
queue.enqueue('111')
queue.enqueue('222')
queue.enqueue('333')
queue.dequeue()
queue.printQueue()
print(queue.peek())
print(queue.size())