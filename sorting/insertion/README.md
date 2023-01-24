# Blog Notes: Insertion Sort

Insertion Sort is a simple sorting algorithm that builds the final sorted list one item at a time. It compares each element in the list with the elements that come before it, and then inserts it into its correct position in the list.

The pseudocode for the Insertion Sort algorithm is as follows:

```py
InsertionSort(int[] arr)
  for i = 1 to arr.length
    int j <-- i - 1
    int temp <-- arr[i]
    while j >= 0 AND temp < arr[j]
      arr[j + 1] <-- arr[j]
      j <-- j - 1
    arr[j + 1] <-- temp
```

Let's go through an example of how this algorithm works using the list [8,4,23,42,16,15].

1. The algorithm starts by initializing a variable i to 1, and a variable j to i - 1, which is 0. It also creates a temporary variable called temp, and assigns it the value of the first element in the list, which is 8.

2. The first iteration of the outer FOR loop begins. Since i is currently 1, the algorithm enters the inner WHILE loop. Since j is currently 0, and temp (which is 8) is greater than the first element in the list (which is also 8), the WHILE loop is not executed and the algorithm proceeds to the next step.

3. The algorithm assigns the value of temp (which is 8) to the first element in the list. The list now becomes [8,4,23,42,16,15].

4. The outer FOR loop continues and i is incremented to 2. The inner WHILE loop is entered again, and j is set to 1. Since temp (which is 4) is less than the second element in the list (which is 8), the inner WHILE loop is executed.

5. The algorithm assigns the value of the second element in the list (which is 8) to the third element in the list (which is 23), and decrements j by 1. The list now becomes [8,8,23,42,16,15].

6. The inner WHILE loop is entered again, and j is set to 0. Since temp (which is 4) is less than the first element in the list (which is 8), the inner WHILE loop is executed.

7. The algorithm assigns the value of the first element in the list (which is 8) to the second element in the list (which is 8), and decrements j by 1. The list now becomes [8,8,23,42,16,15].

8. The inner WHILE loop is entered again, and j is set to -1. Since j is now less than 0, the inner WHILE loop is not executed.

9. The algorithm assigns the value of temp (which is 4) to the first element in the list. The list now becomes [4,8,23,42,16,15].

10. The outer FOR loop continues, and i is incremented to 3. The inner WHILE loop is entered again, and j is set to 2. Since temp (which is 23) is greater than the third element in the list (which is 23), the inner WHILE loop is not executed and the algorithm proceeds to the next step.

11. The algorithm assigns the value of temp (which is 23) to the third element in the list. The list now becomes [4,8,23,42]
