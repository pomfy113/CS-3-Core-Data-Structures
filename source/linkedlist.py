# #!python
#
# class Node(object):
#
#     def __init__(self, data):
#         """Initialize this node with the given data."""
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         """Return a string representation of this node."""
#         return 'Node({!r})'.format(self.data)
#
#
# class LinkedList(object):
#     """SINGLE linked list."""
#     def __init__(self, iterable=None):
#         """Initialize this linked list and append the given items, if any."""
#         self.head = None  # First node
#         self.tail = None  # Last node
#         self.size = 0  # Number of nodes
#         # Append the given items
#         if iterable is not None:
#             for item in iterable:
#                 self.append(item)
#
#     def __str__(self):
#         """Return a formatted string representation of this linked list."""
#         items = ['({!r})'.format(item) for item in self.items()]
#         return '[{}]'.format(' -> '.join(items))
#
#     def __repr__(self):
#         """Return a string representation of this linked list."""
#         return 'LinkedList({!r})'.format(self.items())
#
#     def items(self):
#         """Return a list of all items in this linked list.
#         Best and worst case running time: Theta(n) for n items in the list
#         because we always need to loop through all n nodes."""
#         # Create an empty list of results
#         result = []  # Constant time to create a new list
#         # Start at the head node
#         node = self.head  # Constant time to assign a variable reference
#         # Loop until the node is None, which is one node too far past the tail
#         while node is not None:  # Always n iterations because no early exit
#             # Append this node's data to the results list
#             result.append(node.data)  # Constant time to append to a list
#             # Skip to the next node
#             node = node.next  # Constant time to reassign a variable
#         # Now result contains the data from all nodes
#         return result  # Constant time to return a list
#
#     def is_empty(self):
#         """Return True if this linked list is empty, or False."""
#         return self.head is None
#
#     def length(self):
#         """Return the length of this linked list by traversing its nodes.
#         Best and worst case running time: ??? under what conditions? [TODO]"""
#         # Node counter initialized to zero
#         node_count = 0
#         # Start at the head node
#         node = self.head
#         # Loop until the node is None, which is one node too far past the tail
#         while node is not None:
#             # Count one for this node
#             node_count += 1
#             # Skip to the next node
#             node = node.next
#         # Now node_count contains the number of nodes
#         return node_count
#
#     def get_at_index(self, index):
#         """Return the item at the given index in this linked list, or
#         raise ValueError if the given index is out of range of the list size.
#         Best case running time: ??? under what conditions? [TODO]
#         Worst case running time: ??? under what conditions? [TODO]"""
#         # Check if the given index is out of range and if so raise an error
#         if not (0 <= index < self.size):
#             raise ValueError('List index out of range: {}'.format(index))
#
#         counter = self.head
#         for i in range(index):
#             counter = counter.next
#         return counter.data
#
#         # TODO: Find the node at the given index and return its data
#
#     def insert_at_index(self, index, item):
#         """Insert the given item at the given index in this linked list, or
#         raise ValueError if the given index is out of range of the list size.
#         Best case running time: ??? under what conditions? [TODO]
#         Worst case running time: ??? under what conditions? [TODO]"""
#         # Check if the given index is out of range and if so raise an error
#         if not (0 <= index <= self.size):
#             raise ValueError('List index out of range: {}'.format(index))
#         if index == 0:
#             self.prepend(item)
#         elif index == self.size:
#             self.append(item)
#         else:
#             new_node = Node(item)
#             node = self.head
#             previous = None
#             for i in range(index):
#                 previous = node
#                 node = node.next
#
#             previous.next = new_node
#             new_node.next = node
#             self.size += 1
#         # TODO: Find the node before the given index and insert item after it
#
#     def append(self, item):
#         """Insert the given item at the tail of this linked list.
#         Best and worst case running time: ??? under what conditions? [TODO]"""
#         # Create a new node to hold the given item
#         new_node = Node(item)
#         # Check if this linked list is empty
#         if self.is_empty():
#             # Assign head to new node
#             self.head = new_node
#         else:
#             # Otherwise insert new node after tail
#             self.tail.next = new_node
#         # Update tail to new node regardless
#         self.tail = new_node
#         self.size += 1
#
#     def prepend(self, item):
#         """Insert the given item at the head of this linked list.
#         Best and worst case running time: ??? under what conditions? [TODO]"""
#         # Create a new node to hold the given item
#         new_node = Node(item)
#         # Check if this linked list is empty
#         if self.is_empty():
#             # Assign tail to new node
#             self.tail = new_node
#         else:
#             # Otherwise insert new node before head
#             new_node.next = self.head
#         # Update head to new node regardless
#         self.head = new_node
#         self.size += 1
#
#     def find(self, quality):
#         """Return an item from this linked list satisfying the given quality.
#         Best case running time: Omega(1) if item is near the head of the list.
#         Worst case running time: O(n) if item is near the tail of the list or
#         not present and we need to loop through all n nodes in the list."""
#         # Start at the head node
#         node = self.head  # Constant time to assign a variable reference
#         # Loop until the node is None, which is one node too far past the tail
#         while node is not None:  # Up to n iterations if we don't exit early
#             # Check if this node's data satisfies the given quality function
#             if quality(node.data):  # Constant time to call quality function
#                 # We found data satisfying the quality function, so exit early
#                 return node.data  # Constant time to return data
#             # Skip to the next node
#             node = node.next  # Constant time to reassign a variable
#         # We never found data satisfying quality, but have to return something
#         return None  # Constant time to return None
#
#     def replace(self, old_item, new_item):
#         """Replace the given old_item in this linked list with given new_item
#         using the same node, or raise ValueError if old_item is not found.
#         Best case running time: ??? under what conditions? [TODO]
#         Worst case running time: ??? under what conditions? [TODO]"""
#
#         # Why replace if it's the same
#         if old_item == new_item:
#             return
#         node = self.head
#         while node is not None:
#             if node.data == old_item:
#                 node.data = new_item
#                 return
#             node = node.next
#         raise ValueError('Item not found: {}'.format(old_item))
#
#     def delete(self, item):
#         """Delete the given item from this linked list, or raise ValueError.
#         Best case running time: ??? under what conditions? [TODO]
#         Worst case running time: ??? under what conditions? [TODO]"""
#         # Start at the head node
#         node = self.head
#         # Keep track of the node before the one containing the given item
#         previous = None
#         # Create a flag to track if we have found the given item
#         found = False
#         # Loop until we have found the given item or the node is None
#         while not found and node is not None:
#             # Check if the node's data matches the given item
#             if node.data == item:
#                 # We found data matching the given item, so update found flag
#                 found = True
#             else:
#                 # Skip to the next node
#                 previous = node
#                 node = node.next
#         # Check if we found the given item or we never did and reached the tail
#         if found:
#             self.size -= 1
#             # Check if we found a node in the middle of this linked list
#             if node is not self.head and node is not self.tail:
#                 # Update the previous node to skip around the found node
#                 previous.next = node.next
#                 # Unlink the found node from its next node
#                 node.next = None
#             # Check if we found a node at the head
#             if node is self.head:
#                 # Update head to the next node
#                 self.head = node.next
#                 # Unlink the found node from the next node
#                 node.next = None
#             # Check if we found a node at the tail
#             if node is self.tail:
#                 # Check if there is a node before the found node
#                 if previous is not None:
#                     # Unlink the previous node from the found node
#                     previous.next = None
#                 # Update tail to the previous node regardless
#                 self.tail = previous
#         else:
#             # Otherwise raise an error to tell the user that delete has failed
#             raise ValueError('Item not found: {}'.format(item))
#
class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class LinkedList(object):
    """DOUBLE linked list."""
    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def rev_items(self):
        """Return a list of all items in this linked list. BUT REVERSED
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.tail  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.prev  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best case: Constant time; if empty, just returns 0
        Worst case: Theta(n). Goes through entire list and adds 1 per n
        """
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        node = self.head
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            node = node.next
        # Now node_count contains the number of nodes
        return node_count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case (error): Theta(2); after comparison, raise Value
        Best case (success): Constant; it's at the 0th index or tail
            No for loop; just goes to returns immediately.
        Worst case: Theta(n-1); near end of index.
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # if it's at the end, just return it. Might as well, right?
        if index == self.size:
            return self.tail.data

        counter = self.head
        # Otherwise, let's go through the list unless it's you're
        # Looking at the tip; if so, well, it's the head, return that.
        for i in range(index):
            counter = counter.next
        return counter.data

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case (Success): Constant; if head/tail, it's just append/prepend
        Worst case: Theta(n-1) and assignments.
        """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # This is just putting it at the beginning; prepend it
        if index == 0:
            self.prepend(item)
        # Just putting it at the end? It's an append
        elif index == self.size:
            self.append(item)
        # For everything else...
        else:
            new_node = Node(item)
            old_node = self.head
            # We loop through till we find index
            for i in range(index):
                old_node = old_node.next
            # Previous node's next node becomes this one
            # This one's previous node is now the next node
            old_node.prev.next = new_node
            new_node.prev = old_node.prev
            # Node we moved up is now new node's next node
            # New node is also that node's previous node
            old_node.prev = new_node
            new_node.next = old_node
            # Can't forget that it got bigger
            self.size += 1

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best: Constant; if empty, 1 comparison, 4 assignments
        Worst: Constant; if not empty, 1 comparison, 5 assignments
        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
            new_node.prev = self.tail
        # Update tail to new node regardless
        self.tail = new_node
        self.size += 1


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best: Constant; if empty, 1 comparison, 4 assignments
        Worst: Constant; if not empty, 1 comparison, 5 assignments
        """
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
            self.head.prev = new_node
        # Update head to new node regardless
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case: O(1), replacing the same thing is pointless
        Worst case: T(n), we go through entire list until we find a match
        """

        # Why replace if it's the same
        if old_item == new_item:
            return

        node = self.head
        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return
            node = node.next
        raise ValueError('Item not found: {}'.format(old_item))

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case: @head, O(1); if it's at the head, you shred right through
        Worst case: @tail, O(n); n operations for finding, then delete
            Also case for not finding it; still n operations.
        """
        # Start at the head node
        node = self.head

        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            self.size -= 1
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                node.prev.next = node.next
                node.next.prev = node.prev
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                if node.next is not None:
                    node.next.prev = None
                # Unlink the found node from the next node
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if node.prev is not None:
                    # Unlink the previous node from the found node
                    node.prev.next = None
                # Update tail to the previous node regardless
                self.tail = node.prev
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    ll = LinkedList(['A', 'B', 'C'])
    print(ll)
    print('size: {}'.format(ll.size))
    ll.insert_at_index(0, 'AA')
    print(ll)
    ll.insert_at_index(2, 'BB')
    print(ll)
    ll.insert_at_index(5, 'CC')
    print(ll)
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print("\n\nDouble Linked List")
    ll = LinkedList(['A', 'B', 'C'])
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    ll.prepend('A')
    print(ll)
    ll.append('C')
    print(ll)
    ll.delete('B')
    print(ll)
    print("Doing insert at index")
    ll.insert_at_index(1, 'B')
    print(ll)
    ll.insert_at_index(0, 'AA')
    print(ll)
    ll.insert_at_index(4, 'CC')
    print(ll)
    print(ll.rev_items()[1])



if __name__ == '__main__':
    test_linked_list()
