#!python
import operator

# Global var
COMPARE = operator.gt
KEY = eval("lambda x: x")

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""
    for i in range(len(items)-1):
        # If the preceeding is larger, it's not sorted
        if COMPARE(KEY(items[i]), KEY(items[i+1])):
            return False
    # Got through all of it? It's sorted
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""
    # Repeat until all items are in sorted order
    limit = len(items)
    swapped = True

    # if order == "reverse":
    #     compare = operator.lt
    # elif order == "normal":
    #     compare = operator.gt
    global COMPARE
    global KEY

    while limit != 0 and swapped is True:
        # Early exit; if not changed, exit

        swapped = False

        for i in range(limit-1):
            # Swap adjacent items that are out of order
            # If there is a key, change those things around
            if COMPARE(KEY(items[i]), KEY(items[i+1])):
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        # We can go smaller each time we go through
        limit -= 1

    return items

def cocktail_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""
    # Repeat until all items are in sorted order
    limit = len(items)
    swapped = True

    # if order == "reverse":
    #     compare = operator.lt
    # elif order == "normal":
    #     compare = operator.gt
    global COMPARE
    global KEY

    while limit != 0 and swapped is True:
        # Early exit; if not changed, exit
        swapped = False

        for i in range(len(items)-limit, limit-1):
            # Swap adjacent items that are out of order
            # If there is a key, change those things around
            if COMPARE(KEY(items[i]), KEY(items[i+1])):
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        # Early exit going left to right
        if swapped is False:
            break

        # Now doing the reverse
        for i in range((limit-1), len(items)-limit, -1):
            if COMPARE(KEY(items[i-1]), KEY(items[i])):
                items[i], items[i-1] = items[i-1], items[i]
                swapped = True
        # Early exit going right to left
        if swapped is False:
            break

        # We can go smaller each time we go through
        limit -= 1

    return items
def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order."""
    # if order == "reverse":
    #     compare = operator.lt
    # elif order == "normal":
    #     compare = operator.gt
    global COMPARE
    global KEY

    # Repeat until all items are in sorted order
    for index in range(len(items)):
        # Will hold lowest number we found so far
        # Start with first unsorted number
        lowest_index = index

        # Find minimum item in unsorted items; go up slowly
        for check_index in range(index, len(items)):
            # If we find a new lowest number, save its index
            if COMPARE(KEY(items[lowest_index]), KEY(items[check_index])):
                lowest_index = check_index
        # Swap it with first unsorted item
        items[index], items[lowest_index] = items[lowest_index], items[index]

    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    global COMPARE
    global KEY

    # Repeat until all items are in sorted order
    for index in range(len(items)):
        iterator = index

        # Take first unsorted item
        while COMPARE(KEY(items[iterator-1]), KEY(items[index])) and iterator > 0:
            iterator -= 1
    # Insert it in sorted order in front of items
        sorteditem = items.pop(index)
        items.insert(iterator, sorteditem)

    return items

# Note; used to be items1/items2
def merge(left, right):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    l_index = r_index = 0
    merged = []
    while (l_index < len(left)) and (r_index < len(right)):
        # If right index is larger, append left[index]; increase l. index
        if COMPARE(KEY(right[r_index]), KEY(left[l_index])):
            merged.append(left[l_index])
            l_index += 1
        # If left index is larger, append right[index]; increase r. index
        elif COMPARE(KEY(left[l_index]), KEY(right[r_index])):
            merged.append(right[r_index])
            r_index += 1
    # Add remaining merge
    if(l_index == len(left)):
        merged.extend(right[r_index:])
    elif(r_index == len(left)):
        merged.extend(left[l_index:])
    # Return list
    return merged


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Pivot point/middle
    pivot = int(len(items) / 2)
    # Sort each half using any other sorting algorithm
    left = cocktail_sort(items[0:pivot])
    right = cocktail_sort(items[pivot:len(items)])
    # Merging; [:] to mutate properly
    items[:] = merge(left, right)
    return items


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if (len(items)/2) < 2:
        return bubble_sort(items)
    # TODO: Split items list into approximately equal halves
    else:
        # Pivot point/middle
        pivot = int(len(items) / 2)
        # Recursive call
        left = merge_sort(items[0:pivot])
        right = merge_sort(items[pivot:len(items)])
        # Merging; [:] to mutate properly
        items[:] = merge(left, right)
        return items


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(order, key, sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    import random
    # items = random.sample(range(1, max_value + 1), num_items)
    # items = ["A", "b", "d", "E", "C"]
    items = [('A', 1), ('B', 3), ('d', 4), ('e', 7), ('F', 9), ('C', 2)]
    # items = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # item_range = list(range(1, max_value + 1))
    # items = [random.choice(item_range for _ in range(num_items))]
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))

    global COMPARE
    global KEY
    KEY = key
    if order == "reverse":
        COMPARE = operator.lt
    elif order == "normal":
        COMPARE = operator.gt
    # Changed to make merge_sort possible
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))



def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    try:
        order = args[3] if len(args) >= 4 else "normal"
    except ValueError:
        print('Order (`reverse`/`normal`) required for command-line arguments')
        return
    try:
        key = eval(args[4]) if len(args) >= 5 else eval("lambda x: x")
    except ValueError:
        print('Function required for command-line arguments')
        return
    # Test sort function, but don't explode if sort function does not exist
    try:
        test_sorting(order, key, sort_function, num_items, max_value)
    except NameError:
        print("SOMETHING HAPPENED")
        script = sys.argv[0]  # Get script file name
        print('\nUsage: {} sort num max order key'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('\trandomly sampled from the range [1...`max`] (inclusive)')
        print('\tin the either "reverse" or "normal" `order`')
        print('\twith a `key` function (if available)')

        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')


if __name__ == '__main__':
    main()
