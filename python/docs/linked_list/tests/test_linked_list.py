import pytest

from modules.linked_list import Node

# Tests
def test_node_value():
    actual  = Node(1)
    expected = 1
    assert actual == expected

def test_node_next():
    node1 = Node(1)
    node2 = Node(2, node1)
    assert node2.next == node1
