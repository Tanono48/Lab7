"""Lab 07.02 - Binary Search Tree (Preorder, Insert)"""
class BSTNode:
    """BSTNode"""
    def __init__(self, data) -> None:
        """Initiation"""
        self.data = int(data)
        self.left = None
        self.right = None

    def set_data(self, data):
        """Setting Data"""
        self.data = int(data)

    def set_left(self, left_node):
        """Left Side"""
        self.left = left_node

    def set_right(self, right_node):
        """Right Side"""
        self.right = right_node

    def get_data(self):
        """Return Data"""
        return self.data

    def get_left(self):
        """Return Left"""
        return self.left

    def get_right(self):
        """Return Right"""
        return self.right

class BST:
    """BST"""
    def __init__(self) -> None:
        """Initiation"""
        self.root = None

    def get_root(self):
        """Getting Root"""
        return self.root

    def set_root(self, root):
        """Setting Root"""
        self.root = root

    def insert(self, data):
        """Insert"""
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        """Insertion"""
        if root is None:
            return BSTNode(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root

    def preorder(self):
        """Pre-Order"""
        self._preorder(self.root)
        print()

    def _preorder(self, root):
        """Showing Output"""
        if root:
            print("->", root.data, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

def main():
    """Data Structures and Algorithms Lab - Binary Search Tree"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()
