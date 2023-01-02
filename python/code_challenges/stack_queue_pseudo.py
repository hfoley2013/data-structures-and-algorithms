from data_structures.stack import Stack
from data_structures.invalid_operation_error import InvalidOperationError

class PseudoQueue:
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        while self.stack_1.is_empty() is False:
            node = self.stack_1.pop()
            self.stack_2.push(node)
        self.stack_2.push(value)


    def dequeue(self):
        while self.stack_2.is_empty() is False:
            node = self.stack_2.pop()
            self.stack_1.push(node)
        result = self.stack_1.pop()
        return result
