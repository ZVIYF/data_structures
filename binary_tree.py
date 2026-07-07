class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def append(self, val):
        self.root = BinaryTree.insert(self.root, val)

    @staticmethod
    def list_to_binary_tree(my_list):
        my_tree = BinaryTree()
        for val in list:
            my_tree.append(val)
        return my_tree

    def search(self, val):
        return self.search_rec(self.root, val)

    def print_in_order(self):
        self.print_rec(self.root)

    @staticmethod
    def print_rec(node):
        if node is None:
            return
        BinaryTree.print_rec(node.left)
        print(node.data)
        BinaryTree.print_rec(node.right)

    @staticmethod
    def insert(node, val):
        if node is None:
            return Node(val)
        if node.data > val:
            node.left = BinaryTree.insert(node.left, val)
            return node
        else:
            node.right = BinaryTree.insert(node.right, val)
            return node

    @staticmethod
    def search_rec(node, val):
        if node is None:
            return False
        if node.data == val:
            return True
        if node.data > val:
            return BinaryTree.search_rec(node.left, val)
        return BinaryTree.search_rec(node.right, val)


arr1 = [9, 1, 7, 3, 5]
tree1 = BinaryTree.list_to_binary_tree(arr1)
BinaryTree.print_in_order(tree1)