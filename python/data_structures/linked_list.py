# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node

class Node:
  """
  Instantiates a class Node for use in Linked Lists.
  """
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


# Create a LinkedList class
class LinkedList:
  """
  Instantiates a Linked List class to which Nodes can be inserted, found, and their link chain returned as a string.
  """
  def __init__(self):
    self.head = None

  def insert(self, value):
    """
    Adds a new node with that value to the head of the list with an O(1) Time performance.
    """
    new_node = Node(value, self.head)
    self.head = new_node

  def includes(self, value):
    """
    Indicates whether that value exists as a Node’s value somewhere within the list.
    """
    node = self.head
    while node is not None:
        if node.value == value:
            return True
        node = node.next
    return False

  def __str__(self):
    """
    Returns a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"
    """
    values = []
    node = self.head
    while node is not None:
        values.append("{ " + str(node.value) +" }")
        node = node.next
    if len(values) == 0:
        return "NULL"
    return " -> ".join(values) + " -> NULL"
