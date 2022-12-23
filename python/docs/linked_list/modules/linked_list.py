# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


# Create a LinkedList class
class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, value):
    new_node = Node(value, self.head)
    self.head = new_node

  def includes(self, value):
    node = self.head
    while node is not None:
        if node.value == value:
            return True
        node = node.next
    return False

  def to_string(self):
    values = []
    node = self.head
    while node is not None:
        values.append(str(node.value))
        node = node.next
    if len(values) == 0:
        return "NULL"
    return " -> ".join(values) + " -> NULL"
