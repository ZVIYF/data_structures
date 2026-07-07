class TreeNode:
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
        for val in my_list:
            my_tree.append(val)
        return my_tree

    def search(self, val):
        return self.search_rec(self.root, val)

    def print_pre_order(self):
        self.print_pre_order_rec(self.root)
        print()

    def print_in_order(self):
        self.print_in_order_rec(self.root)
        print()

    @staticmethod
    def print_pre_order_rec(node):
        if node is None:
            return
        print(node.data, end=", ")
        BinaryTree.print_pre_order_rec(node.left)
        BinaryTree.print_pre_order_rec(node.right)

    @staticmethod
    def print_in_order_rec(node):
        if node is None:
            return
        BinaryTree.print_in_order_rec(node.left)
        print(node.data, end=", ")
        BinaryTree.print_in_order_rec(node.right)

    @staticmethod
    def insert(node, val):
        if node is None:
            return TreeNode(val)
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

    def nodes_count(self):
        return self.nodes_count_rec(self.root)

    @staticmethod
    def nodes_count_rec(node):
        if node is None:
            return 0
        return 1 + BinaryTree.nodes_count_rec(node.left) + BinaryTree.nodes_count_rec(node.right)

    def leafs_count(self):
        return self.leafs_count_rec(self.root)

    @staticmethod
    def leafs_count_rec(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        else:
            return 0 + BinaryTree.leafs_count_rec(node.left) + BinaryTree.leafs_count_rec(node.right)

    def levels_count(self):
        return self.levels_count_rec(self.root)

    @staticmethod
    def levels_count_rec(node):
        if node is None:
            return 0
        left = 1 + BinaryTree.levels_count_rec(node.left)
        right = 1 + BinaryTree.levels_count_rec(node.right)
        level = max(left, right)
        return level




arr1 = [9, 1, 7, 3, 5]
tree1 = BinaryTree.list_to_binary_tree(arr1)
tree1.print_in_order()
tree1.print_pre_order()
print(tree1.nodes_count())