from enum import Enum


class NodeColors(Enum):
    RED = 'RED'
    BLACK = 'BLACK'


class RedBlackNode:
    def __init__(self, value, parent = None):
        self.value = value
        self.right_child: RedBlackNode = None
        self.left_child: RedBlackNode = None
        self.color: NodeColors = NodeColors.RED
        self.parent: RedBlackNode = parent
        self.height = 1

    def recolor(self, new_color: NodeColors = None):
        if new_color is not None:
            self.color = new_color
            return
        if self.color == NodeColors.RED:
            self.color = NodeColors.BLACK
            return
        self.color = NodeColors.RED
