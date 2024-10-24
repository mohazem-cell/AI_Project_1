from heapq import heappush,heappop


class heap_queue:
    def __init__(self):
        self.heap = []

    def push(self, puzzle):
        heappush(self.heap,puzzle)

    def pop(self):
        
        if self.is_empty():
            print("The queue is empty")
            return
        return heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if self.is_empty():
            print("The queue is empty")
            return
        return self.heap[0]

    def size(self):
        return len(self.heap)