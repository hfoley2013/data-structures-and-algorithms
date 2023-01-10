# Breadth First Search

## Challenge Summary

* Do Breadth-first Traversal
* Write a function called `breadth_first`
  * Arguments: tree
  * Return: list of all values in the tree, in the order they were encountered
    * Will be numeric.

## Whiteboard Process

![Tree Breadth First](./tree_breadth_first_search.jpeg)


## Approach & Efficiency

* The `breadth_first_search` approach takes in a `tree` as an argument and then proceeds to visiting every node in the tree on the same level and proceeds downward.
* The algorithm utilizes a first-in, first-out queue to hold any unvisited nodes.
* On each loop, the algo removes the first item from teh queue and appends it's value to the `values` list.
* If that node has left and right nodes, those nodes are the added to the end of the queue and visited in order left to right.
* Big-O Notation
  * **Time:** O(n), where `n` is the number of nodes in the `tree`, because we must visit each node in the `tree` and get their values.
  * **Space:** O(n), where `n` is the number of nodes in the `tree`, because we must hold all nodes in the `tree` once the are evaluated and return them to the user.

## API

* Application contains the following function to be used with the `BinaryTree`class:
  * `breadth_first_search`
    * Inputs: `tree`
    * Returns: `list` of `numbers`; one for each value in the `tree` nodes

## Tests

* We tested the following circumstances with `pytest`:
  * Search a rootless tree
  * Search a tree with a single node
  * Search a tree with two nodes
  * Search a tree with four nodes
  * Search a tree with n nodes
