# Singly Linked List

Goal is to create a program that allows us to create a linked list using a `Node` class to add to a `LinkedList` class

## Challenge

* **Node**
  * Create a `Node` class that has properties for the value stored in the `Node`, and a pointer to the next `Node`.

* **Linked List**
  * Create a `LinkedList` class
    * Within your `LinkedList` class, include a `head` property.
    * Upon instantiation, an empty Linked List should be created.
  * The class should contain the following methods
    * `insert`
      * Arguments: value
      * Returns: nothing
      * Function: Adds a new node with that value to the head of the list with an O(1) Time performance.
    * `includes`
      * Arguments: value
      * Returns: Boolean
      * Function: Indicates whether that value exists as a Node’s value somewhere within the list.
    * `to_string`
      * Arguments: none
      * Returns: a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"

## Approach & Efficiency

* The `Node` class is used to create a node for use in a singly linked list
* The `LinkedList` class is used to add nodes to our list using the `Node` class

## Tests

* We tested for the following with 11 tests total:
  1. The value added to `Node` returns the expected value
  2. Nodes added via `Node` have the value of the previous node assigned as their `next` property
  3. Tests that `insert` properly inserts values into the linked list using the `Node` class
  4. Tests that `insert` properly inserts one value into the linked list, linked list returns a list of one value, and the `next` property of the node is `None`
  5. Tests that if no nodes are added to the linked list using `insert`, the `head` returns the value `None`
  6. Tests that the `includes` method properly returns values inserted into the linked list using the `insert` method
  7. Tests that if one node is inserted only that value is found using `includes`
  8. If no nodes are insert then `includes` returns `False`
  9. Tests that multiple values added to the linked list are printed in the format "{a} -> {b} -> {c} -> NULL" when invoking the `to_string` method
  10. Tests that if there is only one node, `to_string` returns "{a} -> NULL"
  11. Tests that if there are no node in the linked list the `to_string` method returns "NULL"
