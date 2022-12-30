# Stacks and Queues

Create a `Node`, `Stack`, and `Queue` class that allow for the full functionality of adding, removing, and inspecting a stack and queue of nodes.

## Challenge

* Node
  * Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
* Stack
  * Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    * This object should be aware of a default empty value assigned to top when the stack is created.
    * The class should contain the following methods:
    * push
      * Arguments: value
      * adds a new node with that value to the top of the stack with an O(1) Time performance.
    * pop
      * Arguments: none
      * Returns: the value from node from the top of the stack
      * Removes the node from the top of the stack
      * Should raise exception when called on empty stack
    * peek
      * Arguments: none
      * Returns: Value of the node located at the top of the stack
      * Should raise exception when called on empty stack
    * is empty
      * Arguments: none
      * Returns: Boolean indicating whether or not the stack is empty.
* Queue
  * Create a Queue class that has a front property. It creates an empty Queue when instantiated.
    * This object should be aware of a default empty value assigned to front when the queue is created.
    * The class should contain the following methods:
      * enqueue
        * Arguments: value
        * adds a new node with that value to the back of the queue with an O(1) Time performance.
      * dequeue
        * Arguments: none
        * Returns: the value from node from the front of the queue
        * Removes the node from the front of the queue
        * Should raise exception when called on empty queue
      * peek
        * Arguments: none
        * Returns: Value of the node located at the front of the queue
        * Should raise exception when called on empty stack
      * is empty
        * Arguments: none
        * Returns: Boolean indicating whether or not the queue is empty

## Approach & Efficiency

* Node
  * O(1)
    * All nodes will take the same time to create and occupy the same space independent of input
* Stack
  * O(1)
    * All operations in a stack only affect the `top` node, so the number of nodes in the stack does not affect performance
* Queue
  * O(1)
    * All operations in a queue only affect the `front` or `back` node, so the number of nodes in the stack does not affect performance

## API

* Stack
  * `push`
    * Arguments: value
    * adds a new node with that value to the top of the stack with an O(1) Time performance.
  * `pop`
    * Arguments: none
    * Returns: the value from node from the top of the stack
    * Removes the node from the top of the stack
    * Should raise exception when called on empty stack
  * `peek`
    * Arguments: none
    * Returns: Value of the node located at the top of the stack
    * Should raise exception when called on empty stack
  * `is_empty`
    * Arguments: none
    * Returns: Boolean indicating whether or not the stack is empty.
* Queue
  * `enqueue`
    * Arguments: value
    * adds a new node with that value to the back of the queue with an O(1) Time performance.
  * `dequeue`
    * Arguments: none
    * Returns: the value from node from the front of the queue
    * Removes the node from the front of the queue
    * Should raise exception when called on empty queue
  * `peek`
    * Arguments: none
    * Returns: Value of the node located at the front of the queue
    * Should raise exception when called on empty stack
  * `is_empty`
    * Arguments: none
    * Returns: Boolean indicating whether or not the queue is empty

## Tests

* Can successfully push onto a stack
* Can successfully push multiple values onto a stack
* Can successfully pop off the stack
* Can successfully empty a stack after multiple pops
* Can successfully peek the next item on the stack
* Can successfully instantiate an empty stack
* Calling pop or peek on empty stack raises exception
* Can successfully enqueue into a queue
* Can successfully enqueue multiple values into a queue
* Can successfully dequeue out of a queue the expected value
* Can successfully peek into a queue, seeing the expected value
* Can successfully empty a queue after multiple dequeues
* Can successfully instantiate an empty queue
* Calling dequeue or peek on empty queue raises exception

## Checklist

* [ ] Update root README
* Node
  * [ ] value
  * [ ] next
* [ ] Stack
  * [ ] `push`
  * [ ] `pop`
  * [ ] `peek`
  * [ ] `is_empty`
* [ ] Queue
  * [ ] `queue`
  * [ ] `dequeue`
  * [ ] `peek`
  * [ ] `is_empty`
* [ ] All tests passing
  * [ ] Happy Path - Expected Path
  * [ ] Expected Failure
  * [ ] Edge Cases
