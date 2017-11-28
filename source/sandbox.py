def insertion_sort(items, key):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""
    # if order == "reverse":
    #     compare = operator.lt
    # elif order == "normal":
    #     compare = operator.gt
    global COMPARE

    # Repeat until all items are in sorted order
    for index in range(len(items)):
        iterator = index

        # Take first unsorted item
        while COMPARE(key(items[iterator-1]), key(items[index])) and iterator > 0:
            iterator -= 1
    # Insert it in sorted order in front of items
        sorteditem = items.pop(index)
        items.insert(iterator, sorteditem)

    return items

def merge_sort(items, key):
    """Divide and conquer; split the items in the array, then sort."""
    # Check endcase
    if (len(items) / 2) > 1:
        global COMPARE
        # Pivot point/middle
        pivot = int(len(items) / 2)
        # Recursive call
        left = merge_sort(items[0:pivot], key)
        right = merge_sort(items[pivot:len(items)], key)
        # Init the variables
        l_index = r_index = 0
        merged = []
        # Merging
        while (l_index < len(left)) and (r_index < len(right)):
            # If right index is larger, append left[index]; increase l. index
            if COMPARE(right[r_index], left[l_index]):
                merged.append(left[l_index])
                l_index += 1
            # If left index is larger, append right[index]; increase r. index
            elif COMPARE(left[l_index], right[r_index]):
                merged.append(right[r_index])
                r_index += 1
        # Add remaining merge
        if(l_index == len(left)):
            merged.extend(right[r_index:])
        elif(r_index == len(left)):
            merged.extend(left[l_index:])
        # Return list
        return merged
    else:
        # End of the line!
        return bubble_sort(items, key)





def test_sorting(sort=bubble_sort, num_items=20, max_value=50, order="normal", key=None):
