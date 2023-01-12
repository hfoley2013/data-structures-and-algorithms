from data_structures.kary_tree import Node, KaryTree

def fizz_buzz_tree(tree):
    def fizz_buzz(node):
        if node.value % 15 == 0:
            return Node("FizzBuzz", node.children)
        elif node.value % 3 == 0:
            return Node("Fizz", node.children)
        elif node.value % 5 == 0:
            return Node("Buzz", node.children)
        return Node(str(node.value), node.children)

    def traverse(node):
        if node is None:
            return None
        new_node = fizz_buzz(node)
        new_node.children = [traverse(child) for child in node.children]
        return new_node

    return KaryTree(traverse(tree.root))



if __name__ == '__main__':
    # Creating the tree structure
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

    one.children = [two, three]
    two.children = [four, five, six]
    three.children = [seven, eight, nine]
    four.children = [ten]
    five.children = [eleven]
    six.children = [twelve]
    seven.children = [thirteen]
    nine.children = [fourteen, fifteen]

    tree = KaryTree(one)

    fizz_tree = fizz_buzz_tree(tree)
    print(fizz_tree.breadth_first())
