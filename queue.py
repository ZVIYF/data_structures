class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        self.tail.next = Node(val)
        self.tail = self.tail.next
        if self.head is None:
            self.head = self.tail

    def removefirst(self):
        if self.head is None:
            return
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        return temp.data

    def peek(self):
        if self.head:
            return self.head.data

# # # # # # #

class Queue:
    def __init__(self):
        self.queue = LinkedList()
        self.len = -1

    def enqueue(self, val):
        self.queue.append(val)
        self.len += 1

    def dequeue(self):
        self.len -= 1
        return self.queue.removefirst()

    def is_empty(self):
        if self.len < 0:
            return True
        return False

    def peek(self):
        return self.queue.peek()

# # # # # # # # # #

class ClassifiedRequests(Queue):
    def is_full(self):
        if self.len >= 29:
            return True
        return False

    def is_late(self):
        """
        אם שעת סגירה - פחות דלתא של שעה < קטן מ זמן נוכחי:

        :return:
        """
        pass


    def enqueue(self, val):
        if self.is_full() and self.is_late():
            print("Queue if full. No more requests today!")
            return
        self.queue.append(val)
        self.len += 1

# # # # # # # # # #

def GapIntQueue(q:Queue):
    temp = Queue()
    q1 = Queue()
    temp_val = None
    while not q.is_empty():
        if temp_val:
            q1.enqueue(temp_val - q.peek())
        temp_val = q.dequeue()
        temp.enqueue(temp_val)
    q = temp
    return q1

def replace_values(q:Queue, value, replace):
    temp_q = Queue()
    while not q.is_empty():
        temp_val = q.dequeue()
        if temp_val == value:
            temp_val = replace
        temp_q.enqueue(temp_val)
    q = temp_q
    return q

def sort_queue(q:Queue):
    temp_q1 = Queue()
    temp_q2 = Queue()
    while not q.is_empty():
        if q.peek() < 0:
            temp_q2.enqueue(q.dequeue())
        else:
            temp_q1.enqueue(q.dequeue())
    while not temp_q2.is_empty():
        temp_q1.enqueue(temp_q2.dequeue())
    return temp_q1

