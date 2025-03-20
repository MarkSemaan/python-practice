#The error being that it's popping the last item rather than the first, since in a queue, you should pop the first item since it works on a FIFO principle, so add a 0 to the pop.
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop(0)