# Create a Node class that has properties of the value stored in the Node and a pointer to the next Node

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
