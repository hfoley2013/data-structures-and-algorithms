# Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node

class Node:
  """
  Instantiates a class Node for use in Linked Lists.
  """
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class TargetError(Exception):
  pass

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
    try:
      new_node = Node(value, self.head)
      self.head = new_node
    except TargetError:
      raise TargetError

  def includes(self, value):
    """
    Indicates whether that value exists as a Node’s value somewhere within the list.
    """
    try:
      current_node = self.head
      while current_node is not None:
          if current_node.value == value:
              return True
          current_node = current_node.next
      return False
    except TargetError:
      raise TargetError

  def append(self, value):
    """
    Takes a value as a parameter and appends it to the end of the list.
    """
    try:
      new_node = Node(value)
      current_node = self.head
      while current_node.next is not None:
        current_node = current_node.next
      current_node.next = new_node
    except TargetError:
      raise TargetError

  def insert_before(self, value, new_value):
    try:
      new_node = Node(new_value)
      current_node = self.head
      previous_node = None
      if current_node is None:
        raise TargetError
      if current_node.value is value:
        self.head = new_node
        new_node.next = current_node
        return
      while current_node is not None:
        if current_node.value is value:
          new_node.next = current_node
          previous_node.next = new_node
          return
        previous_node = current_node
        current_node = current_node.next
      raise TargetError
    except TargetError:
      raise TargetError

  def insert_after(self, value, new_value):
    try:
      new_node = Node(new_value)
      current_node = self.head
      while current_node is not None:
        if current_node.value is value:
          new_node.next = current_node.next
          current_node.next = new_node
          return
        current_node = current_node.next
      raise TargetError
    except TargetError:
      raise TargetError


  def kth_from_end(self, k):
    """
    Returns the value located at the kth position in the linked list.
    """

    steps_behind = 0
    leader = self.head
    follower = None

    if leader is None:
      raise TargetError

    while leader:
      leader = leader.next
      if follower:
        follower = follower.next
      elif steps_behind == k:
        follower = self.head
      else:
        steps_behind += 1

    if not follower:
      raise TargetError

    return follower.value




  def __str__(self):
    """
    Returns a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"
    """
    try:
      values = []
      node = self.head
      while node is not None:
          values.append("{ " + str(node.value) +" }")
          node = node.next
      if len(values) == 0:
          return "NULL"
      return " -> ".join(values) + " -> NULL"
    except TargetError:
      raise TargetError
