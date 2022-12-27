import pytest
from data_structures.linked_list import LinkedList, Node


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list.to_string()) == "NULL"


# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list.to_string()) == "{ apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list.to_string()) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list.to_string()) == "{ banana } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")

# def test_to_string():
#     linked_list = LinkedList()
#     linked_list.insert(1)
#     linked_list.insert(2)
#     linked_list.insert(3)

#     assert linked_list.to_string() == "3 -> 2 -> 1 -> NULL"

# def test_to_string_one_node():
#     linked_list = LinkedList()
#     linked_list.insert(1)

#     assert linked_list.to_string() == "1 -> NULL"

# def test_to_string_no_nodes():
#     linked_list = LinkedList()

#     assert linked_list.to_string() == "NULL"
