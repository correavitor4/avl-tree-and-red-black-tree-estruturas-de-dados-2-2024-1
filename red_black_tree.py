from RedBlackNode import RedBlackNode, NodeColors


class RedBlackTree:
    def __init__(self):
        self.root: RedBlackNode = None

    @staticmethod
    def left_rotation(node_to_be_rotated: RedBlackNode) -> RedBlackNode:
        newTop = node_to_be_rotated.right_child
        node_to_be_rotated.right_child = newTop.left_child
        newTop.left_child = node_to_be_rotated

        return newTop

    @staticmethod
    def right_rotation(node_to_be_rotated: RedBlackNode) -> RedBlackNode:
        new_top = node_to_be_rotated.left_child
        node_to_be_rotated.left_child = new_top.right_child
        new_top.right_child = node_to_be_rotated

        return new_top

    def insert(self, value: int):

        root = self.root
        if root is None:
            new_node = RedBlackNode(value)
            new_node.recolor()
            self.root = new_node
            return

        new_node = self.find_node_place(root, value)
        self.post_insert_algorithm(new_node)

    def find_node_place(self, curr_node: RedBlackNode, value) -> RedBlackNode:
        if value == curr_node.value:
            raise Exception("Value already inserted on red-black tree")

        if value > curr_node.value:
            if curr_node.right_child is not None:
                return self.find_node_place(curr_node.right_child, value)

            new_node = RedBlackNode(value, parent=curr_node)
            curr_node.right_child = new_node
            return new_node

        if curr_node.left_child is not None:
            return self.find_node_place(curr_node.left_child, value)

        new_node = RedBlackNode(value, parent=curr_node)
        curr_node.left_child = new_node
        return new_node

    #TODO: O problema está aqui: por algum motivo, está fazendo os elementos sumirem após a inserção
    def post_insert_algorithm(self, new_node: RedBlackNode):
        while new_node.parent is not None and new_node.parent.color == NodeColors.RED:
            parent: RedBlackNode = new_node.parent
            grand_parent = parent.parent
            if grand_parent is None:
                return

            # Check if parent is the left child of grandparent
            if grand_parent.left_child is not None and grand_parent.left_child.value == parent.value:
                uncle = grand_parent.right_child

                if uncle is not None and uncle.color == NodeColors.RED:
                    uncle.recolor()
                    parent.recolor()
                    grand_parent.recolor()
                    new_node = grand_parent
                elif new_node.parent.right_child is not None and new_node.parent.right_child.value == new_node.value:
                    new_node = parent
                    self.left_rotation(new_node)
                else:
                    parent.recolor()
                    self.right_rotation(grand_parent)

            else:
                uncle = grand_parent.left_child
                if uncle is not None and uncle.color == NodeColors.RED:
                    grand_parent.left_child.recolor()
                    grand_parent.right_child.recolor()
                    grand_parent.recolor()
                    new_node = grand_parent
                elif parent.left_child is not None and parent.left_child.value == new_node.value:
                    new_node = parent
                    self.right_rotation(new_node)
                else:
                    parent.recolor()
                    grand_parent.recolor()
                    self.left_rotation(grand_parent)

            self.root.recolor(new_color=NodeColors.RED)

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
