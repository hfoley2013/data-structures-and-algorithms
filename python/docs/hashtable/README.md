# Hashtables

A HashTable is a data structure that stores key-value pairs and uses a hash function to map keys to indices in an array called a table. The goal of the hash function is to distribute the keys evenly across the indices of the table and to minimize the number of collisions, which occur when multiple keys map to the same index.

## Challenge

Implement a `Hashtable` Class with the following methods:

* `set`
  * Arguments: key, value
  * Returns: nothing
  * This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  * Should a given key already exist, replace its value from the `value` argument given to this method.
* `get`
  * Arguments: key
  * Returns: Value associated with that key in the table has
  * Arguments: key
  * Returns: Boolean, indicating if the key exists in the table already.
* `keys`
  * Returns: Collection of keys
* `hash`
  * Arguments: key
  * Returns: Index in the collection for that key

## Approach & Efficiency

The HashTable class uses an array as the underlying data structure to store key-value pairs. It uses a hash function to map each key to an index in the array, called the table. The goal of the hash function is to distribute the keys evenly across the indices of the table and to minimize the number of collisions, which occur when multiple keys map to the same index.

* `Hashtable`
  * Space complexity: `O(n)`, where n is the number of key-value pairs stored in the table
    * This is because the size of the table needs to be large enough to accommodate all the elements and handle collisions.
* `set`
  * Time: `O(1)`, as it uses a hash function to quickly find the appropriate index for the key-value pair.
    * NOTE: In the worst case scenario, where there are many collisions, the time complexity could be `O(n)` where n is the number of key-value pairs stored in the table.
* `get`
  * Time: `O(1)`, as it uses a hash function to quickly find the appropriate index for the key and retrieve the associated value.
    * NOTE: In the worst case scenario, where there are many collisions, the time complexity could be `O(n)` where n is the number of key-value pairs stored in the table.
* `has`
  * Time: `O(1)`, as it uses a hash function to quickly find the appropriate index for the key and check if it exists in the table.
  * NOTE: In the worst case scenario, where there are many collisions, the time complexity could be O(n) where n is the number of key-value pairs stored in the table.
* `keys`
  * Time: `O(n)` where n is the number of key-value pairs stored in the table, as it needs to iterate through all the key-value pairs to return a collection of keys.
* `hash`
  * Time: `O(1)` as it simply uses a hash function to quickly find the appropriate index for the key and returns the index.

## API

Here's an overview of how a `Hashtable` class:

1. `Hashtable` initializes an empty table with a fixed size and a load factor, which determines when the table should be resized to prevent it from becoming too full.
2. `set` is used to insert a new key-value pair into the table.
   * It first uses the hash function to map the key to an index in the table.
   * If the index is empty, the key-value pair is inserted. If the index is already occupied, the method uses a collision resolution technique to handle the collision, such as open addressing.
3. `get` method is used to retrieve the value associated with a given key.
   * It first uses the hash function to map the key to an index in the table, then it checks if the key exists in that index.
   * If the key does exist, it returns the associated value, else it returns `None`
4. `has` method is used to check if a key exists in the table.
   * It first uses the hash function to map the key to an index in the table and then it checks if the key exists in that index.
5. `keys` method returns a collection of all the keys in the table.
6. `hash` method is the function used to map a key to an index in the table.
