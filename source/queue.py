#!python

from linkedlist import LinkedList


# Implement LinkedQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class LinkedQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) - just does prepend, which is O(1)"""
        self.list.prepend(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.tail.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) - since tail, it happens easily [TODO]"""
        if self.is_empty():
            raise ValueError
        return self.list.remove_tail()

class DeQueue(object):
    """Gee, it sure is easier to do this with a double linked list."""
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue_back(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue_back(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) - just does prepend, which is O(1)"""
        self.list.prepend(item)

    def enqueue_front(self, item):
        """Insert the given item at the front of this queue.
        Running time: O(1) - just does append, which is O(1)"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.tail.data

    def back(self):
        """Return the item at the back of this queue without removing it,
        or None if this queue is empty."""
        if self.is_empty():
            return None
        return self.list.head.data

    def dequeue_front(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) - since tail, it happens easily
        If this wasn't a double-linked list, it would take O(n)"""
        if self.is_empty():
            raise ValueError
        return self.list.remove_tail()

    def dequeue_back(self):
        """Remove and return the item at the back of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) - since head, it happens easily."""
        if self.is_empty():
            raise ValueError
        return self.list.remove_head()

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ListQueue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)
        # TODO: Count number of items

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: Depends on implementation.
        We can insert at 0, in which case, it's O(n), but pop is O(1)
        We can also insert at the top, in which case, O(1), but pop is O(n)"""
        self.list.insert(0, item)
        # TODO: Insert given item

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        size = self.length()
        if size == 0:
            return None
        return self.list[(size-1)]
        # TODO: Return front item, if any

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: see enqueue;
        Dequeue is always going to be the inverse of enqueue.
        """
        size = self.length()
        if size == 0:
            raise ValueError
        return self.list.pop((size-1))


# Implement LinkedQueue and ArrayQueue above, then change the assignment below
# to use each of your Queue implementations to verify they each pass all tests
Queue = LinkedQueue
# print(q.list)
# print(q.front())
# print(q.back())
# print(q.list)
# print(q.enqueue_back('E'))
# print(q.enqueue_front('A'))
# print(q.list)
# print(q.dequeue_back)
# print(q.list)
# print(q.dequeue_front)
# print(q.list)

# Queue = ArrayQueue
