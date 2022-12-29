from data_structures.linked_list import *

def zip_lists(list1, list2):
    """
    Takes two linked lists as arguments and returns a single list with the alternating values from the two lists in the order they appear in their original lists.

    Example:
    list1 = {1} -> {3} -> {2} -> null
    list2 = {5} -> {9} -> {4} -> null

    Expected Output: {1} -> {5} -> {3} -> {9} -> {2} -> {4} -> null
    """

    current1 = list1.head
    current2 = list2.head

    if current1 is None:
        return list2

    if current2 is None:
        return list1

    while current1 and current2:
        # store next values
        current1_next = current1.next
        current2_next = current2.next

        # insert second value after first value
        list1.insert_after(current1.value, current2.value)

        # move the pointers forward one
        current1 = current1_next
        current2 = current2_next

    # account for list2 being longer than list1
    while current2:
        list1.append(current2.value)
        current2 = current2.next
    
    return list1
