# #07 - Python -> Jesus Antonio Escamilla

"""
EJERCIÓ
"""
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not len(self.stack) == 0:
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not len(self.stack) == 0:
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")

    def show(self):
        return self.stack

print("STACKS - PILAS - LIFO")
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.show())
print(stack.pop())
print(stack.peek())
print(stack.show())


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not len(self.queue) == 0:
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def front(self):
        if not len(self.queue) == 0:
            return self.queue[0]
        else:
            raise IndexError("front from an empty queue")

    def show(self):
        return self.queue

print("QUEUE - COLAS - FIFO")
queue = Queue()
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
print(queue.show())
print(queue.dequeue())
print(queue.front())
print(queue.show())



"""
EXTRA
"""
# Pendiente