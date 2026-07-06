# # # # # # #

class Queue:
    def __init__(self):
        self.queue = Link
        self.len = -1

    def enqueue(self, val):
        self.queue.append(val)
        self.len += 1

    def dequeue(self):
        self.len -= 1
        return self.queue.pop(0)

    def is_empty(self):
        if self.len < 0:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return
        return self.queue[0]

# # # # # # # # # #

class ClassifiedRequests(Queue):
    def is_full(self):
        if self.len >= 29:
            return True
        return False

    def enqueue(self, val):
        if self.is_full():
            print("Queue if full. No more requests today!")
            return
        self.queue.append(val)
        self.len += 1

# # # # # # # # # #

def IntQueue(q:Queue):
    q1 = Queue()

    while not q2.is_empty():
