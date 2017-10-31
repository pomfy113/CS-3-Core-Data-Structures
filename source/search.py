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
    # # 2
    # index = 0
    # for value in array:
    #     if item == value:
    #         return index  # found
    #     index += 1
    #     index = index+1
    # # 3
    # # for(int index = 0; index < len(array); index++)
    # for index in range(len(array)):
    #     if array[index] == item:
    #         return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # If you've gone too far, it's not in there
    if index >= len(array):
        return None
    # If it matches, return
    if array[index] == item:
        return index
    # You uh... you add 1 to the index
    return linear_search_recursive(array, item, index+1)
    # ^^^ SUPERIOR CODE ^^^

    # temparray = array[index:]
    # if len(array) == 0:
    #     return None
    # if array[0] == item:
    #     return 0
    #
    # return 1 + linear_search_recursive(array[1:], item)



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
    """Cuts array in half to check for item in array."""
    """Must be sorted; left/right are respective margins."""
    # Only run at beginning;
    if (left is None) and (right is None):
        left = 0
        right = len(array)-1
    # Index for the middle element
    if right < left:
        return None
    middleindex = (left + right) // 2
    middle_item = array[middleindex]
    # If it's the middle, return that
    if item == middle_item:
        return middleindex
    # = = = = = = ALTERNATE = = = = =
    # if right - left <= 2:
    #     if array[left] == item:
    #         return left
    #     elif array[right] == item:
    #         return right
    #     return None
    # = = = = = = ALTERNATE = = = = =

    # If it hasn't been found at this point, it's not there

    # If it's on the right half, cut the left half and vice versa
    # IF ALT: remove the +1 and -1 from middle index
    elif item > middle_item:
        return binary_search_recursive(array, item, middleindex+1, right)
    elif item < middle_item:
        return binary_search_recursive(array, item, left, middleindex-1)
