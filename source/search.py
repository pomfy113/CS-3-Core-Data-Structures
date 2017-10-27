#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # If you've gone too far, it's not in there
    if index >= len(array):
        return None
    # If it matches, return index
    if array[index] == item:
        return index
    # You uh... you add 1 to the index
    index += 1
    return linear_search_recursive(array, item, index)

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # Starting off with left and right as margins
    left = 0
    right = len(array)-1
    # Continue until return
    while True:
        # Cut it in half
        middle = left + ((right - left) // 2)
        # Item found!
        if item == array[middle]:
            return middle
        # If we're on the last two elements, check both if it matches
        # Otherwise, it's not going to be in there
        elif right - left <= 2:
            if item == array[left]:
                return left
            elif item == array[right]:
                return right
            return None
        # Check if it's left or right of the middle
        # If it's left, then we cut the right half and vice versa
        elif item > array[middle]:
            left = middle
        elif item < array[middle]:
            right = middle


def binary_search_recursive(array, item, left=None, right=None):
    # Only run at beginning
    if(left is None) and (right is None):
        left = 0
        right = len(array)-1
    # Index for the middle element
    middleindex = left + ((right - left) // 2)
    # If it's smack dab in the middle, return that
    if item == array[middleindex]:
        return middleindex
    # If it's down to the last two elements, check both
    # If it's not in either, then it's not there
    if right - left <= 2:
        if item == array[left]:
            return left
        elif item == array[right]:
            return right
        return None
    # Otherwise, we check if it's left/right of middle and cut where it's not
    elif item > array[middleindex]:
        return binary_search_recursive(array, item, middleindex, right)
    elif item < array[middleindex]:
        return binary_search_recursive(array, item, left, middleindex)
