"""Here have a circular buffer."""

class CircularBuffer(object):
    def __init__(self, iterable=None, buffsize=12):
        """Initializes circular buffer."""
        self.buffer = [None for i in range(buffsize)]
        # For where the next node will appear
        self.write = 0
        # Eldest node; each dequeue moves it up
        self.read = 0
        self.counter = buffsize

        if iterable is not None:
            for item in iterable:
                self.queue(item)

    def __str__(self):
        """Print representation; reversed for ease of viewing."""
        items = []
        for i in reversed(range(len(self.buffer))):
            data = self.buffer[((self.write + i) % self._size())]
            items.append("[{}]".format(data))
        return(str(items))

# Note: Should ask about __iter__ later
    def _size(self):
        """It's how big the buffer is."""
        return len(self.buffer)

    def _writemove(self):
        """Move the write header; where queues happen."""
        # The read moves with the write if no dequeues.
        # Have to wait until a go around until this happens

        # Because of how _readmove works, no matter how many dequeues happen,
        # read will be at maximum be one behind the write
        if self.read == self.write and self.counter == 0:
            self.read += 1
            self.read = self.read % self._size()
        self.write += 1
        self.write = self.write % self._size()

    def _readmove(self):
        """Move the read header; where dequeues happen."""
        # Read can't get past the write head, that's just not **WRITE**
        if ((self.read+1) % self._size()) == self.write:
            # Print for debugging/visual rep purposes
            print("Error: Cannot move past write head.")
            return
        # If that's all good, we just move the read up
        else:
            self.read += 1
            self.read = self.read % self._size()

    def queue(self, item):
        """Write element at write head."""
        # Change whatever is in the write head into item
        # Counter is used for controlling the read head;
        # after buffersize amounts of moving, it can free itself
        if self.counter > 0:
            self.counter -= 1
        self.buffer[self.write] = item
        self._writemove()

    def dequeue(self):
        """Remove element from read head."""
        # Gets data from wherever read head is to return later
        # Replaces that with None, then moves read head
        data = self.buffer[self.read]
        self.buffer[self.read] = None
        self._readmove()
        return data

    def check(self, index=0):
        """Check data; index from newest to oldest."""
        """If no arguments, check newest."""
        return self.buffer[(self.write - (1 + index)) % self._size()]

    def orderedrep(self):
        """For debugging purposes."""
        return self.buffer

test = CircularBuffer()
for i in range(20):
    test.queue(i)
    print(test, "\n", test.write)

print("\nPREDEQUE: ORDERED REP\n", test.orderedrep(), "\nCURRENT READ/WRITE", test.buffer[test.read%12], test.buffer[test.write%12])
test.dequeue()
print(test)
test.dequeue()
print(test)
test.queue(20)
print(test)
test.queue(21)
print(test)
test.dequeue()
print(test)

print("Something completely different")
test2 = CircularBuffer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(test2, "\n\n dequeuing")

for i in range(10):
    test2.dequeue()
    print(test2)
print("LOOP OVER\n", test2.write, test2.read)
test2.dequeue()
print(test2.orderedrep())
print(test2)
test2.dequeue()
print(test2.orderedrep())
print(test2, test2.write, test2.read)
test2.dequeue()
test2.dequeue()
print(test2.orderedrep())
print(test2, test2.write, test2.read)

print("Teting ordered rep")
print(test2.orderedrep())
test2.queue(1)
print(test2.orderedrep())
test2.dequeue()
test2.dequeue()
test2.queue(2)
print(test2.orderedrep())

test2 = CircularBuffer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(test2)
print(test2.check())
print(test2.check(1))
print(test2.check(2))
print(test2.dequeue())
