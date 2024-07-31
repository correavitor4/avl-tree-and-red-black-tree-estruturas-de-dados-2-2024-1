from avlnode import AvlNode


class AVLTree:
    def __init__(self):
        self.root: AvlNode = None

    @staticmethod
    def height(node):
        if node is None:
            return 0
        return node.height

    def heightConsideringLeftAndRight(self, node: AvlNode):
        return 1 + max(self.height(node.left_child), self.height(node.right_child))

    def getBalanceFactor(self, node):
        if not node:
            return 0
        return self.height(node.left_child) - self.height(node.right_child)

    def insert(self, root: AvlNode, value):
        if not root:
            return AvlNode(value)
        elif value < root.value:
            root.left_child = self.insert(root.left_child, value)
        else:
            root.right_child = self.insert(root.right_child, value)

        root.height = self.heightConsideringLeftAndRight(root)

        balance_factor = self.getBalanceFactor(root)

        # Left Rotation
        if balance_factor > 1 and value < root.left_child.value:
            return self.rightRotate(root)

        # Right rotation
        if balance_factor < -1 and root.right_child.value:
            return self.leftRotate(root)

        # Left-right rotation
        if balance_factor > 1 and value > root.left_child.value:
            root.left_child = self.leftRotate(root.left_child)
            return self.rightRotate(root)

        # Right-left Rotation
        if balance_factor < -1 and value < root.right_child.value:
            root.right_child = self.rightRotate(root.right_child)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z: AvlNode) -> AvlNode:
        y = z.right_child
        T2 = y.left_child

        y.left_child = z
        z.right_child = T2

        z.height = self.heightConsideringLeftAndRight(z)
        y.height = self.heightConsideringLeftAndRight(y)

        return y

    def rightRotate(self, z: AvlNode) -> AvlNode:
        y = z.left_child
        T3 = y.right_child

        y.right_child = z
        z.left_child = T3

        z.height = self.heightConsideringLeftAndRight(z)
        y.height = self.heightConsideringLeftAndRight(y)

        return y

    def insertValue(self, value):
        self.root = self.insert(self.root, value)

    def __repr__(self):
        if self.root is None:
            return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.root.height  # height of nodes at current level
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0:
                break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n is None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.value is not None:
                    buf = ' ' * ((5 - len(str(n.value))) // 2)
                    cur_row += '%s%s%s' % (buf, str(n.value), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left_child is not None:
                    next_nodes.append(n.left_child)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right_child is not None:
                    next_nodes.append(n.right_child)
                    next_row += ' \\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * (len(sep) // 2)  # cut separator size in half
        return content
