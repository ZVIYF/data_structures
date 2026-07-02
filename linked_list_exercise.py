class LinkedLists:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def append(self, val):
        new_node = Node(val)
        temp = self.head
        if self.is_empty():
            return
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_first(self):
        if not self.is_empty():
            output = self.head.data
            self.head = self.head.next
            return output

    @staticmethod
    def delete_after(current: Node):
        if current.next:
            output = current.next.data
            current.next = current.next.next
            return output

    def find(self, value):
        temp = self.head
        if self.is_empty():
            return None
        while temp:
            if temp.data == value:
                break
            temp = temp.next
        return temp

    def length(self):
        count = 0
        if self.is_empty():
            return count
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def find_index(self, i):
        if i >= self.length():
            return None
        temp = self.head
        while i > 0:
            temp = temp.next
            i -= 1
        return temp

    def sum_linked_list(self):
        sum = 0
        temp = self.head
        while temp:
            if isinstance(temp.data, int | float):
                sum += temp.data
            temp = temp.next
        return sum

    def seperate_str_int(self):
        my_str = []
        my_int = []
        temp = self.head
        while temp:
            if isinstance(temp.data, int):
                my_int.append(temp.data)
            elif isinstance(temp.data, str):
                my_str.append(temp.data)
            temp = temp.next
        return my_str, my_int

    def link_linked_lists(self, other: LinkedLists):
        self.append(other.head)

    def is_sorted(self):
        if self.is_empty():
            return True
        temp = self.head
        while temp.next:
            if temp.data > temp.next:
                return False
            temp = temp.next
        return True

    def delete_value_from_list(self, value):
        if self.is_empty():
            return
        temp = self.head
        while temp.next:
            if temp.next.data == value:
                self.delete_after(temp)
            else:
                temp = temp.next
        if self.head.data == value:
            self.delete_first()

    def values_from_list(self):
        my_set = set()
        if self.is_empty():
            return list(my_set)
        temp = self.head
        while temp:
            my_set.add(temp.data)
            temp = temp.next
        return list(my_set)

    # def reverse(self):
    #     list_len = self.length()
    #     temp =


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    # def reverse_node(self):
    #     if self.next is None:
    #         return None
    #     self.next.next = self
    #
    #     return self.next 