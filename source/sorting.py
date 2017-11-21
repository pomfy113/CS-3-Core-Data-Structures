#!python
import operator

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""
    for i in range(len(items)-1):
        # If the preceeding is larger, it's not sorted
        if items[i] > items[i+1]:
            return False
    # Got through all of it? It's sorted
    return True


def bubble_sort(items, order, key):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""
    # Repeat until all items are in sorted order
    limit = len(items)
    swapped = True

    if order == "reverse":
        compare = operator.lt
    elif order == "normal":
        compare = operator.gt

    while limit != 0 and swapped is True:
        # Early exit; if not changed, exit

        swapped = False

        for i in range(limit-1):
            # Swap adjacent items that are out of order
            # If there is a key, change those things around
            if compare(key(items[i]), key(items[i+1])):
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        # We can go smaller each time we go through
        limit -= 1

    return items

def cocktail_sort(items, order, key):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""
    # Repeat until all items are in sorted order
    limit = len(items)
    swapped = True

    if order == "reverse":
        compare = operator.lt
    elif order == "normal":
        compare = operator.gt

    while limit != 0 and swapped is True:
        # Early exit; if not changed, exit
        swapped = False

        for i in range(len(items)-limit, limit-1):
            # Swap adjacent items that are out of order
            # If there is a key, change those things around
            if compare(key(items[i]), key(items[i+1])):
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        # Early exit going left to right
        if swapped is False:
            break

        # Now doing the reverse
        for i in range((limit-1), len(items)-limit, -1):
            if compare(key(items[i-1]), key(items[i])):
                items[i], items[i-1] = items[i-1], items[i]
                swapped = True
        # Early exit going right to left
        if swapped is False:
            break

        # We can go smaller each time we go through
        limit -= 1

    return items
def selection_sort(items, order, key):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order."""
    if order == "reverse":
        compare = operator.lt
    elif order == "normal":
        compare = operator.gt

    print(order)

    # Repeat until all items are in sorted order
    for index in range(len(items)):
        # Will hold lowest number we found so far
        # Start with first unsorted number
        lowest_index = index

        # Find minimum item in unsorted items; go up slowly
        for check_index in range(index, len(items)):
            # If we find a new lowest number, save its index
            if compare(key(items[lowest_index]), key(items[check_index])):
                lowest_index = check_index
        # Swap it with first unsorted item
        items[index], items[lowest_index] = items[lowest_index], items[index]

    return items


def insertion_sort(items, order, key):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""
    if order == "reverse":
        compare = operator.lt
    elif order == "normal":
        compare = operator.gt

    # Repeat until all items are in sorted order
    for index in range(len(items)):
        iterator = index

        # Take first unsorted item
        while compare(key(items[iterator-1]), key(items[index])) and iterator > 0:
            iterator -= 1
    # Insert it in sorted order in front of items
        sorteditem = items.pop(index)
        items.insert(iterator, sorteditem)

    return items


def test_sorting(sort=bubble_sort, num_items=20, max_value=50, order="normal", key=None):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of 8 or 16 items in arbitrary order
    # items = [3, 5, 4, 2, 6, 8, 1, 7]
    # items = [11, 13, 8, 4, 12, 2, 14, 3, 5, 18, 6, 10, 1, 7, 9, 15]

    # Create a list of items randomly sampled from range [1...max_value]
    import random
    # items = random.sample(range(1, max_value + 1), num_items)
    # items = ["A", "b", "d", "E", "C"]
    # items = [('A', 1), ('B', 3), ('d', 4), ('e', 7), ('F', 9), ('C', 2)]
    items = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # item_range = list(range(1, max_value + 1))
    # items = [random.choice(item_range for _ in range(num_items))]
    print('Initial items: {!r}'.format(items))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items, order, key)
    print('Sorted items:  {!r}'.format(items))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        sort = globals()[sort_name]
    else:
        sort = bubble_sort

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        order = args[3] if len(args) >= 4 else "normal"
        key = eval(args[4]) if len(args) >= 5 else eval("lambda x: x")
    except:
        print('Integer required for `num` and `max` command-line arguments')

    try:
        order = args[3] if len(args) >= 4 else "normal"
    except:
        print('Order (`reverse`/`normal`) required for command-line arguments')

    try:
        key = eval(args[4]) if len(args) >= 5 else eval("lambda x: x")
    except:
        print('Function required for command-line arguments')
    # Test sort function, but don't explode if sort function does not exist
    try:
        test_sorting(sort, num_items, max_value, order, key)
    except NameError:
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
