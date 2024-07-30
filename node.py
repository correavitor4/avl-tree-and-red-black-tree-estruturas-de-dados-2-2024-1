class NODE:
    def __init__(self, value=None):
        self.value = value
        self.right_child: NODE = None
        self.left_child: NODE = None
        self.parent: NODE = None
        self.height = 1
