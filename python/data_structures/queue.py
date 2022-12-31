from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
        
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node



    def dequeue(self):
        if Queue.is_empty(self) is False:
            temp = self.front
            self.front = temp.next
            temp.next = None
            return temp.value
        else:
            raise InvalidOperationError
        
    def peek(self):
        if Queue.is_empty(self) is False:
            return self.front.value
        else:
            raise InvalidOperationError
            
    def is_empty(self):
        if self.front:
            return False
        return True
