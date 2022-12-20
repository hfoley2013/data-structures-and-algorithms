# Insert to Middle of an Array

Write a function called `insert_shift_array` which takes in an array and a value to be added. Without utilizing any of the built-in methods available to your language, return an array with the new value added at the middle index.

## Whiteboard Process

![Insert Shift Array](../img/insert_array_shift.png)

## Approach & Efficiency

* I approached this problem by starting with thinking through how I was going to get the index of the middle of the provided list.
* Knowing that in its simplest form, the middle of a list will be the length of the list divided by 2, the trick was now to determine whether to round up or round down for any odd number length lists.
* Based on the sample inputs and outputs provided, I determined that in the case of odd number lists I would need to insert the value to the right of the middle value. This means that I would need to round up.
* Since I could not use built-in methods in the function, I needed to find a way to round up without using math.ceil().
* Taking advantage of the fact that `//` rounds down, we can do division of a negative numerator divided by 2, then negate the result.
* This has the advantage of allowing us to use one line of code to handle both even and odd length lists.
* Now that we've identified the middle index number, we can now think through how to modify the list without using any built-in methods.
* We can use concatenation to put together a new list that places the new value in the middle.
* We do this by creating part 1 of the new list by telling Python to create a list from the beginning of the list to the index value `list[:idx]`
* We then add the insertion value in with concatenation `list[:idx] + [num]`
* We then finish off the new list be telling Python to create a list from the index value to the end of the provided list `list[:idx] + [num] + list[idx:]`
* For Big O notation:
  * Time: O(n), runs in linear time
    * As the input list grows so does our execution time
  * Space: O(n), runs in linear space
    * As the input list grows so does the space required to hold the variables for the length of the input list and the index value.
