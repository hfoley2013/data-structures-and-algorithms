# Blog Notes: Merge Sort

The merge sort algorithm is a popular sorting algorithm that is known for its efficiency and stability. It is a divide-and-conquer algorithm, which means that it breaks down the input array into smaller subarrays and then recombines them in a sorted order. In this blog post, we will be walking through the code for the merge sort algorithm using the example input of `[8, 4, 23, 42, 16, 15]`.

```py
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)
```

The first thing we see in the code is the `Mergesort` function, which takes in an input array `arr`. The variable `n` is then declared and assigned the length of the input array. If the length of the array is greater than 1, the code continues to execute.

The next step is to find the middle point of the array, which is done by declaring a variable `mid` and assigning it the value of `n/2`. This middle point is used to divide the input array into two subarrays, `left` and `right`. The `left` subarray is assigned the values of the input array from index 0 to the middle point, and the `right` subarray is assigned the values of the input array from the middle point to the end.

Now that we have our two subarrays, the next step is to sort them. This is done by calling the `Mergesort` function recursively on both the `left` and `right` subarrays. This is known as the **divide-and-conquer** step of the merge sort algorithm, where *the input array is continually broken down into smaller subarrays until they are all of length 1*.

Once the `left` and `right` subarrays are sorted, the final step is to merge them back together in a sorted order. This is done by implementing the merge process within the `Mergesort` function.

```py
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length
    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      DECLARE i <-- 0
      DECLARE j <-- 0
      DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
```

Let's walk through the first iteration of the merge sort algorithm using the example input of [8, 4, 23, 42, 16, 15].

When the `Mergesort` function is first called, the input array is assigned to the variable `arr` and the variable `n` is assigned the length of the array (6). Since the length of the array is greater than 1, the code continues to execute.

The next step is to find the middle point of the array, which is done by dividing `n` by 2. In this case, the middle point is 3. The input array is then divided into two subarrays, `left` and `right`. The `left` subarray is assigned the values of the input array from index 0 to the middle point (8, 4, 23), and the `right` subarray is assigned the values of the input array from the middle point to the end (42, 16, 15).

Now that we have our two subarrays, the next step is to sort them. This is done by calling the `Mergesort` function recursively on both the `left` and `right` subarrays.

For the `left` subarray, the `Mergesort` function is called again. The input array is now [8, 4, 23] and the middle point is 1. The `left` subarray is assigned the value [8], and the `right` subarray is assigned the value [4, 23]. The `Mergesort` function is called recursively on both subarrays.

For the `left` subarray, the `Mergesort` function is called again with an input of [8]. Since the length of the array is 1, the function stops executing and the array is returned as sorted.

For the `right` subarray, the `Mergesort` function is called again with an input of [4, 23]. The middle point is 1 and the `left` subarray is assigned [4] and the `right` subarray is assigned [23]. The `Mergesort` function is called recursively on both subarrays.

For the `left` subarray, the `Mergesort` function is called again with an input of [4]. Since the length of the array is 1, the function stops executing and the array is returned as sorted.

For the `right` subarray, the `Mergesort` function is called again with an input of [23]. Since the length of the array is 1, the function stops executing and the array is returned as sorted.

Now that the `left` and `right` subarrays are sorted, the next step is to merge them back together in a sorted order. This is done by implementing the merge process within the `Mergesort` function. The `i`, `j`, and `k` variables are declared and initialized to 0. These variables are used to keep track of the current index in the `left`, `right`, and `arr` arrays, respectively. The while loop compares the values of `left[i]` and `right[j]` and assigns the smaller value to the current index of the `arr` array. The `i`, `j`, and `k` variables are incremented for each iteration of the loop until one of the subarrays is fully merged into the `arr` array.

## Functional Code Example

```py
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

arr = [8, 4, 23, 42, 16, 15]
merge_sort(arr)
print(arr)
```
