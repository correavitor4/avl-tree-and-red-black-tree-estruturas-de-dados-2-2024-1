class AvlNode:
    def __init__(self, value=None):
        self.value = value
        self.right_child: AvlNode = None
        self.left_child: AvlNode = None
        self.parent: AvlNode = None
        self.height = 1
