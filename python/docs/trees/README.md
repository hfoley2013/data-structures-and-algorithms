# Trees

Create a Binary Tree and Binary Search Tree, then traverse the tree using breadth-first-search.

## Challenge

* **Node**
  * Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
* **Binary Tree**
  * Create a Binary Tree class
    * Define a method for each of the depth first traversals:
      * pre order
      * in order
      * post order
    * Each depth first traversal method should return an array of values, ordered appropriately.
* **Binary Search Tree**
  * Create a Binary Search Tree class
    * This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    * Add
      * Arguments: value
      * Return: nothing
      * Adds a new node with that value in the correct location in the binary search tree.
    * Contains
      * Argument: value
      * Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

* `pre_order()`: The time complexity of this method is `O(n)`, where n is the number of nodes in the tree. This is because each node in the tree is visited exactly once.
* `in_order()`: The time complexity of this method is also `O(n)`. This is because each node in the tree is visited exactly once.
* `post_order()`: The time complexity of this method is also `O(n)`. This is because each node in the tree is visited exactly once.

**Note:** The space complexity of each of these methods is `O(n)` as well, since the maximum size of the stack will be the total number of nodes in the tree (in the worst case).

## API

* `pre_order()`: This method performs a pre-order traversal of the binary tree and returns a list of the values of the nodes in the tree. It uses a stack to store the nodes that are waiting to be visited. It first adds the current node to the list of values, then pushes the right and left child nodes onto the stack if they exist.
* `in_order()`: This method performs an in-order traversal of the binary tree and returns a list of the values of the nodes in the tree. It uses a stack to store the nodes that are waiting to be visited. It first pushes the current node and all of its left child nodes onto the stack, then adds the value of the current node to the list of values and sets the current node to its right child. If the current node has no right child, it pops the top node from the stack and repeats the process.
* `post_order()`: This method performs a post-order traversal of the binary tree and returns a list of the values of the nodes in the tree. It uses a stack to store the nodes that are waiting to be visited. It first pushes the current node and all of its child nodes onto the stack, then adds the value of the current node to the list of values and sets the current node to the top node of the stack. If the current node has no children, it pops the top node from the stack and repeats the process. The final list of values is reversed to achieve the correct order.
