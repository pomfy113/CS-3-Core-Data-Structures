"""Here have a circular buffer."""

class CircularBuffer(list):
    def __init__(self, iterable=None, buffsize=12):
        """Initializes circular buffer."""
        self.buffer = [None for i in range(buffsize)]
        self.write = 0
        self.read = 0

        if iterable is not None:
            for item in iterable:
                self.queue(item)


    def __str__(self):
        """Print representation"""
        items = []
        for i in range(len(self.buffer)):
            items.append("[{}: {}]".format(i, self.buffer[i]))
        return(str(items))

    def _pointmove(self):
        if self.read == self.write:
            self.read += 1
            self.read = self.read % len(self.buffer)
        self.write += 1
        self.write = self.write % len(self.buffer)

    def queue(self, item):
        self.buffer[self.write] = item
        self._pointmove()

    def dequeue(self):
        self.buffer[self.read] = None
        self.read += 1




test = CircularBuffer()
for i in range(20):
    test.queue(i)
    print(test, "\n", test.write)

print("\nPREDEQUE\n", test, "\nCURRENT READ", test.buffer[test.read])
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

test2 = CircularBuffer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(test2)
