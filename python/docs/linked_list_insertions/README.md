# Allow Insertions into Linked List

## Challenge

Write the following methods for the Linked List class:

* `append`
  * arguments: new value
  * adds a new node with the given value to the end of the list
* `insert_before`
  * arguments: value, new value
  * adds a new node with the given new value immediately before the first node that has the value specified
* `insert_after`
  * arguments: value, new value
  * adds a new node with the given new value immediately after the first node that has the value specified

## Approach & Efficiency

* `append`
  * Time: O(n)
  * Space: O(1)
* `insert_before`
  * Time: O(n)
  * Space: O(1)
* `insert_after`
  * Time: O(n)
  * Space: O(1)
* For each of the above functions, they will execute in linear time due the ever increasing time required to search ever-growing linked lists. As the length of the linked list grows, the time taken in the worst case to search the entire list will grow in direct proportion to the length of the list. However, each function will run in constant space since they iterate through one node at a time and the length of those nodes does not change.

## Tests

Tests conducted looked for the following:

1. Can successfully add a node to the end of the linked list
2. Can successfully add multiple nodes to the end of a linked list
3. Can successfully insert a node before a node located i the middle of a linked list
4. Can successfully insert a node before the first node of a linked list
5. Can successfully insert after a node in the middle of the linked list
6. Can successfully insert a node after the last node of the linked list
