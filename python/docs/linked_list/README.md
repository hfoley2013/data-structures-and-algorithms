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
