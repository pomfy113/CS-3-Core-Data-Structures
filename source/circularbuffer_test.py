from circularbuffer import CircularBuffer
import unittest


class CircularBufferTest(unittest.TestCase):
    def test_init(self):
        cb = CircularBuffer()
        assert cb.write == 0
        assert cb.read == 0
        assert cb._size() == 12

    def test_init_with_list(self):
        cb = CircularBuffer(['A', 'B', 'C'])
        assert cb.write == 3
        assert cb.read == 0
        assert cb.buffer[0] == 'A'
        assert cb.buffer[1] == 'B'
        assert cb.buffer[2] == 'C'

    def test_write_and_read_movement(self):
        cb = CircularBuffer(['A', 'B', 'C'])
        assert cb.write == 3
        assert cb.read == 0  # This better not be moving

        cb.queue('D')
        assert cb.write == 4
        assert cb.read == 0
        cb.dequeue()  # Should not do anything
        assert cb.write == 4
        assert cb.read == 1

        cb = CircularBuffer()  # Clearing
        for i in range(11):
            cb.queue(i)
        assert cb.write == 11
        assert cb.read == 0

        cb.queue(11)
        assert cb.write == 0
        assert cb.read == 0
        assert cb.dequeue() == 0

        # Should BOTH move
        cb.queue(12)
        assert cb.write == 1
        assert cb.read == 1
        assert cb.dequeue() == 1

    def test_queues(self):
        cb = CircularBuffer()
        for i in range(12):
            cb.queue(i)
        assert cb.read == 0
        assert cb.dequeue() == 0
        assert cb.read == 1
        assert cb.dequeue() == 1

        # Overwriting
        for i in range(12):
            cb.queue(i)
        assert cb.read == 0
        assert cb.dequeue() == 0
        assert cb.read == 1
        assert cb.dequeue() == 1



if __name__ == '__main__':
    unittest.main()
