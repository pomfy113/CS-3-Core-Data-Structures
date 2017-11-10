# __init__(elements=None) - initialize a new empty set structure, and add each element if a sequence is given
# size - property that tracks the number of elements in constant time
# contains(element) - return a boolean indicating whether element is in this set
# add(element) - add element to this set, if not present already
# remove(element) - remove element from this set, if present, or else raise KeyError
# union(other_set) - return a new set that is the union of this set and other_set
# intersection(other_set) - return a new set that is the intersection of this set and other_set
# difference(other_set) - return a new set that is the difference of this set and other_set
# is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set

from linkedlist import Node, LinkedList
from hashtable import HashTable


class Set(object):
    def __init__(self, elements=None):
        # If I want a perfect O(n), I'll need... linear collision check?
        if elements is None:
            initsize = 5
        else:
            initsize = len(elements)
        self.data = HashTable(initsize)
        for item in elements:
            if self.data.contains(item):
                continue
            else:
                self.data.set(item, None)

    def __str__(self):
        return str(self.data.keys())

    def contents(self):
        return self.data.keys()

    def size(self):
        """Find size."""
        return self.data.size

    def contains(self, element):
        return self.data.contains(element)

    def add(self, element):
        if self.contains(element):
            return
        else:
            self.data.set(element, None)

    def remove(self, element):
        if self.contains(element):
            self.data.delete(element)
        else:
            raise ValueError
    def union(self, other_set):
        """Return a new set that is a union of this set and other_set"""
        newset = self.contents()
        for item in other_set.contents():
            if self.contains(item):
                continue
            else:
                newset.append(item)
        return Set(newset)

    def intersection(self, other_set):
        """Return a new set that is an intersection of this set + other_set."""
        newset = []
        for item in other_set.contents():
            if self.contains(item):
                newset.append(item)
        return Set(newset)

    def is_subset(self, other_set):
        """Return a boolean whether other set is a subset of this set."""

        # Check to make sure if everything in THIS set is in the other
        if self.size() <= other_set.size():
            for item in self.contents():
                if other_set.contains(item):
                    continue
                else:
                    return False
            return True
        else:
            return False

test1 = Set([6, 7, 8, 9, 10])
test2 = Set([1, 2, 3, 4, 5])
result = test1.intersection(test2)
print(result)
# test2 = Set([4, 5, 6, 7, 8])
#
# print(test)
# print(test2)
# test.add(1)
# print(test)
# print(test.intersection(test2))
# print(test.union(test2))
#
# print(test.is_subset(test2))
#
# test = Set([1, 2, 3])
# test2 = Set([1, 2, 3, 4, 5, 6, 7, 8])
# print(test.is_subset(test2))
#
# test = Set([1, 2, 3])
# test2 = Set([1, 2, 3])
# print(test.is_subset(test2))
#
# test = Set([1, 2, 3, 4])
# test2 = Set([1, 2, 3])
# print(test.is_subset(test2))
#
# test = Set([1, 2, 3, 4, 5])
# test2 = Set([4, 5, 6, 7, 8])
# print(test.is_subset(test2))
