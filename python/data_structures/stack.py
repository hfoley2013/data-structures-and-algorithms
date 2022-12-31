from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)

        if self.top is None:
            self.top = new_node
            return

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if Stack.is_empty(self) is False:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            return temp.value
        else:
            raise InvalidOperationError

    def peek(self):
        if Stack.is_empty(self) is False:
            return self.top.value
        else:
            raise InvalidOperationError

    def is_empty(self):
        if self.top:
            return False
        return True
