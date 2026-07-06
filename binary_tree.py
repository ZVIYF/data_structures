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

    def search(self, val):

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
