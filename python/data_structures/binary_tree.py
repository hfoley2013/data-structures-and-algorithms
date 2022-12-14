class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        values = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            values.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return values

    def in_order(self):
        values = []
        stack = []
        node = self.root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.value)
            node = node.right
        return values

    def post_order(self):
        values = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            values.append(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return values[::-1]

    def find_maximum_value(self):
        values = self.in_order()
        values.sort(reverse=True)
        return values[0]

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
