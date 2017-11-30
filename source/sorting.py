#!python
import operator
# from pympler import tracker
# tr = tracker.SummaryTracker()
# Global var
from memory_profiler import profile

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
    ASSUMING n IS ORIGINAL LIST AND HALVES ARE (n/2)
    Running time: O(n); has to go through every element in both lists(n/2 * 2)
        Can be less if one list finishes first
    Memory usage: n + m"""
    # COMPARE default: (is [arg1] greater than [arg2])
    # KEY default: (do nothing to element)
    # NOTE: Please make sure that both lists are in order
    l_index = r_index = 0
    merged = []
    # Repeat until one list is empty
    while (l_index < len(left)) and (r_index < len(right)):
        left_item = left[l_index]
        right_item = right[r_index]
        # If right index is larger, append left[index]; increase l. index
        if COMPARE(KEY(right_item), KEY(left_item)):
            merged.append(left_item)
            l_index += 1
        # If left index is larger, append right[index]; increase r. index
        elif COMPARE(KEY(left_item), KEY(right_item)):
            merged.append(right_item)
            r_index += 1
        # If equal; jam em both in + increment both; no harm, no foul
        elif(KEY(left_item) == KEY(right_item)):
            merged.append(left_item)
            merged.append(right_item)
            l_index += 1
            r_index += 1
    # Add remains of other list via append
    if(l_index == len(left)):
        for index in range(r_index, len(right)):
            merged.append(right[index])
    elif(r_index == len(right)):
        for index in range(l_index, len(left)):
            merged.append(left[index])
    # Return list
    return merged

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(n^2) technically, but much lower in practice;
        Running cocktail twice which is O(n^2) on smaller lists is a tad better
        Assuming 100 items worst case:
            Cocktail: (100)^2 or 10,000
            Split-sort: 2(50^2) => 2*2500 => 5,000 operations
        But you pay for it in memory usage
    Memory usage: O(n);
        2n + merge; two halves 2(n/2) or (n) + sorted list (n)"""
    # COMPARE default: (is [arg1] greater than [arg2])
    # KEY default: (do nothing to element)

    # Pivot point; go to middle
    pivot = len(items) // 2
    # Init the two halves
    left = items[pivot:]
    right = items[:pivot]
    # Sort each half using any other sorting algorithm
    cocktail_sort(left)
    cocktail_sort(right)
    # Merging; [:] to mutate properly
    items[:] = merge(left, right)

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n log n)
        Depends on how many times we can split it in half.
        log n: With 256 items, we have to split it log(2)256 or 8 times
        n: After splitting it, we need to do a merge each time we do this func
        Which is why it's n * (log(2)n)
    Memory usage: 2(n * log n)?
        Despite splits, we still have size n each time we do an operations
        We do splits equal to log n, and they're mirrored (merge out, merge in)

        While it's 2(n * log n) + n when including the original list, we don't
        need to deal with that.
        """
    # Base case
    if (len(items)) > 1:
        # Pivot point/middle
        pivot = len(items) // 2
        # Recursive calls
        left = items[:pivot]
        right = items[pivot:]
        # Merging
        merge_sort(left)
        merge_sort(right)
        # Merging
        items[:] = merge(left, right)
        # items[:] = merge2(left, right, items)

def merge2(items, items_copy, start, middle, end):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    ASSUMING n IS ORIGINAL LIST AND HALVES ARE (n/2)
    Running time: O(n); has to go through every element in both lists(n/2 * 2)
        Can be less if one list finishes first
    Memory usage: n + m"""
    # COMPARE default: (is [arg1] greater than [arg2])
    # KEY default: (do nothing to element)
    """
    GENERAL IDEA:
        So the deal with this is that we're putting things in order inside
        the copy before copying them back to the items.

        Because we're using index and then changing the elements (no insert
        or delete whatsoever), there's no wasted space that I know of.
    """

    l_index = start
    r_index = middle
    # Use this for going through items
    index = start

    while (l_index < middle) and (r_index < end):
        l_item = items[l_index]
        r_item = items[r_index]
        # if the right item is larger, place left item into array
        if COMPARE(KEY(r_item), KEY(l_item)):
            items_copy[index] = l_item
            l_index += 1
        # if the left item is larger, place right into new array
        elif COMPARE(KEY(l_item), KEY(r_item)):
            items_copy[index] = r_item
            r_index += 1
        # Let's do both!
        elif KEY(r_item) == KEY(l_item):
            items_copy[index] = l_item
            l_index += 1
            index += 1
            items_copy[index] = r_item
            r_index += 1
        # Next!
        index += 1
        # Add remains of other list via append
    if(l_index == middle):
        for i in range(r_index, end):
            items_copy[index] = items[i]
            index += 1

    elif(r_index == end):
        for i in range(l_index, middle):
            items_copy[index] = items[i]
            index += 1

    # Updating only original copy!
    for i in range(start, end):
        items[i] = items_copy[i]

def merge_sort2(items, items_copy=[]):
    """See above merge for details; merge, but using the double buffer."""
    items_copy = items[:]
    start = 0
    end = len(items)
    # Hookay, let's get started with this mess
    mergehelper(items, items_copy, start, end)

def mergehelper(items, items_copy, start, end):
    # We've hit the end
    if end - start < 2:
        return
    else:
        # Settle the middle for future uses
        middle = (start+end) // 2
        # Recursive: give smaller and smaller lists
        mergehelper(items, items_copy, start, middle)
        mergehelper(items, items_copy, middle, end)
        # Time to do the merge!
        merge2(items, items_copy, start, middle, end)

def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]

def test_sorting(order, key, sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    import random
    items = random.sample(range(1, max_value + 1), num_items)
    # items = ["A", "b", "d", "E", "C"]
    # items = [('A', 1), ('B', 3), ('d', 4), ('e', 7), ('F', 9), ('C', 2)]
    # items = [5, 4, 3, 2, 1]
    # items = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # item_range = list(range(1, max_value + 1))
    # items = [random.choice(item_range for _ in range(num_items))]
    # print('Initial items: {!r}'.format(items))
    # print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    # print('Sorting items with {}(items)'.format(sort.__name__))

    global COMPARE
    global KEY
    KEY = key
    if order == "reverse":
        COMPARE = operator.lt
    elif order == "normal":
        COMPARE = operator.gt
    # Changed to make merge_sort possible
    sort(items)
    # print('Sorted items:  {!r}'.format(items))
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
