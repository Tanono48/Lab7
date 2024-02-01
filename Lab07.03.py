"""Lab 07.03 - Binary Search Tree (Traversals)"""
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

    def is_empty(self):
        """Empty"""
        return self.root is None

    def inorder(self):
        """In-order"""
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        """Show-Output"""
        if root:
            self._inorder(root.left)
            print("->", root.data, end=" ")

            self._inorder(root.right)

    def postorder(self):
        """Post-Order"""
        self._postorder(self.root)
        print()

    def _postorder(self, root):
        """Show Output only Post-Order"""
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            print("->", root.data, end=" ")

    def traverse(self):
        """Traversing and Show Output"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder()
        print('Inorder: ', end='')
        self.inorder()
        print('Postorder: ', end='')
        self.postorder()

def main():
    """Data Structures and Algorithms Lab - Binary Search Tree"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

main()
