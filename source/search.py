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
    # TODO: implement linear search recursively here
    if index >= len(array):
        return None
    if array[index] == item:
        return index

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
    left = 0
    right = len(array)-1
    print("====================================")
    print(array)
    print("Looking for", item)

    while True:
        search = int((left+right) / 2)
        # It's not pretty. I need to fix this.
        print("Searching,", search, ". Left is", left, "right is", right)

        if item == array[search]:
            print("Found", item, "in", right)
            return search
        elif item == array[left]:
            print("Found", item, "in", left)
            return left
        elif item == array[right]:
            print("Found", item, "in", right)
            return right

        elif item > array[search]:
            print("It's on the right side!\n\n")
            left = search
        elif item < array[search]:
            print("It's on the left side!\n\n")
            right = search

        if (right-left) // 2 == 0:
            print("Not found")
            return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    print(array)
    if(left is None) and (right is None):
        left = 0
        right = len(array)-1
    middle = (right - left) // 2
    middleindex = left + middle
    print("Searching for", item, "at index", middleindex, ".", "Left is:", left, ", right is:", right)
    if item == array[left]:
        print("Found at", left, "\n===========================")
        return left
    elif item == array[right]:
        print("Found at", right, "\n===========================")
        return right
    elif item == array[middleindex]:
        print("Found at", middleindex, "\n===========================")
        return middleindex

    elif(right-left) == 1:
        print("Not here.")
        return None

    elif item > array[middleindex]:
        return binary_search_recursive(array, item, left=middleindex, right=right)
    elif item < array[middleindex]:
        return binary_search_recursive(array, item, left=left, right=middleindex)




    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
