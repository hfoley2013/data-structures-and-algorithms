import pytest

from modules.linked_list import Node, LinkedList

# Tests
def test_node_value():
    node = Node(1)
    assert node.value == 1

def test_node_next():
    node1 = Node(1)
    node2 = Node(2, node1)
    assert node2.next == node1

def test_insert():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    assert linked_list.head.value == 3
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 1

def test_insert_one_node():
    linked_list = LinkedList()
    linked_list.insert(1)

    assert linked_list.head.value == 1
    assert linked_list.head.next is None

def test_insert_no_nodes():
    linked_list = LinkedList()

    assert linked_list.head is None

def test_includes():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    assert linked_list.includes(1) == True
    assert linked_list.includes(2) == True
    assert linked_list.includes(3) == True
    assert linked_list.includes(4) == False

def test_includes_one_node():
    linked_list = LinkedList()
    linked_list.insert(1)

    assert linked_list.includes(1) == True
    assert linked_list.includes(2) == False

def test_includes_no_nodes():
    linked_list = LinkedList()

    assert linked_list.includes(1) == False

def test_to_string():
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    assert linked_list.to_string() == "3 -> 2 -> 1 -> NULL"

def test_to_string_one_node():
    linked_list = LinkedList()
    linked_list.insert(1)

    assert linked_list.to_string() == "1 -> NULL"

def test_to_string_no_nodes():
    linked_list = LinkedList()

    assert linked_list.to_string() == "NULL"
