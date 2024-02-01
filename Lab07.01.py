"""Lab 07.01 - Create BSTNode"""
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

def main():
    """Main Function"""
    root_node = BSTNode(int(input()))
    print(root_node.get_data(), root_node.get_left(), root_node.get_right(), sep="\n")
main()
