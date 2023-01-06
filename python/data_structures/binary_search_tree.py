from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    def add(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        node = self.root
        while True:
            if value < node.value:
                if not node.left:
                    node.left = new_node
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = new_node
                    return
                node = node.right

    def contains(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False
