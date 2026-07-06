# # # # # # # # # # # # # #

class ListStack:
    def __init__(self):
        self.data = list()
        self.top = -1

    def push(self, value):
        self.data.insert(0, value)
        self.top += 1

    def pop(self):
        if self.is_empty():
            return
        self.top -= 1
        return self.data[self.top + 1]

    def is_empty(self):
        return self.top < 0


# # # # # # # # # # # # # #
class ArrayStack:
    def __init__(self, length):
        self.array = [None] * length
        self.top = -1

    def push(self, value):
        if self.is_full():
            print("Stack overflow!")
            return
        self.data.insert(0, value)
        self.top += 1

    def pop(self):
        if self.is_empty():
            return
        self.top -= 1
        return self.data[self.top + 1]

    def is_empty(self):
        return self.top < 0

    def is_full(self):
        if self.top == len(self.array):
            return True
        return False

# # # # # # # # # # # # # # #

class LinkedListStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head:
            return True
        return False

    def push(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp

    def pop(self):
        if self.is_empty():
            return
        temp = self.head.data
        self.head = self.head.next
        return temp


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# # # # # # # # # # # # # #

class LimitedListStack:
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
        self.length = -1

    def is_empty(self):
        if self.head:
            return True
        return False

    def is_full(self):
        if self.length >= self.capacity:
            return True
        return False


    def push(self, val):
        if self.is_full():
            print("Stack overflow!")
            return
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        temp = self.head.data
        self.head = self.head.next
        self.length -= 1
        return temp

# # # # # # # # # # # # # # #
