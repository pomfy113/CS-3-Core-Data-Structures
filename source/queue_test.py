#!python

from queue import Queue, DeQueue
import unittest


class QueueTest(unittest.TestCase):

    def test_init(self):
        q = Queue()
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = Queue(['A', 'B', 'C'])
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length(self):
        q = Queue()
        assert q.length() == 0
        q.enqueue('A')
        assert q.length() == 1
        q.enqueue('B')
        assert q.length() == 2
        q.dequeue()
        assert q.length() == 1
        q.dequeue()
        assert q.length() == 0

    def test_enqueue(self):
        q = Queue()
        q.enqueue('A')
        assert q.front() == 'A'
        assert q.length() == 1
        q.enqueue('B')
        assert q.front() == 'A'
        assert q.length() == 2
        q.enqueue('C')
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_front(self):
        q = Queue()
        assert q.front() is None
        q.enqueue('A')
        assert q.front() == 'A'
        q.enqueue('B')
        assert q.front() == 'A'
        q.dequeue()
        assert q.front() == 'B'
        q.dequeue()
        assert q.front() is None

    def test_dequeue(self):
        q = Queue(['A', 'B', 'C'])
        assert q.dequeue() == 'A'
        assert q.length() == 2
        assert q.dequeue() == 'B'
        assert q.length() == 1
        assert q.dequeue() == 'C'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.dequeue()

class DblQueueTest(unittest.TestCase):

    def test_init(self):
        q = DeQueue()
        assert q.front() is None
        assert q.length() == 0
        assert q.is_empty() is True

    def test_init_with_list(self):
        q = DeQueue(['A', 'B', 'C'])
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_length(self):
        q = DeQueue()
        assert q.length() == 0
        q.enqueue_back('A')
        assert q.length() == 1
        q.enqueue_front('B')
        assert q.length() == 2
        q.dequeue_front()
        assert q.length() == 1
        q.dequeue_back()
        assert q.length() == 0

    def test_enqueue(self):
        q = DeQueue()
        q.enqueue_back('B')
        assert q.front() == 'B'
        assert q.length() == 1
        q.enqueue_back('C')
        assert q.front() == 'B'
        assert q.length() == 2
        q.enqueue_front('A')
        assert q.front() == 'A'
        assert q.length() == 3
        assert q.is_empty() is False

    def test_front_back(self):
        q = DeQueue()
        assert q.front() is None
        q.enqueue_back('A')
        assert q.front() == 'A'
        q.enqueue_back('B')
        assert q.front() == 'A'
        q.dequeue_front()
        assert q.front() == 'B'
        q.dequeue_back()
        q.enqueue_front('C')
        assert q.front() == 'C'
        q.enqueue_front('B')
        assert q.front() == 'B'
        q.enqueue_front('A')
        assert q.front() == 'A'
        assert q.back() == 'C'
        q.dequeue_front()
        assert q.front() == 'B'
        assert q.back() == 'C'
        q.dequeue_front()
        q.dequeue_front()
        assert q.front() is None
        assert q.back() is None


    def test_dequeue(self):
        q = DeQueue(['A', 'B', 'C'])
        assert q.dequeue_front() == 'A'
        assert q.length() == 2
        assert q.dequeue_back() == 'C'
        assert q.length() == 1
        assert q.dequeue_back() == 'B'
        assert q.length() == 0
        assert q.is_empty() is True
        with self.assertRaises(ValueError):
            q.dequeue_front()


if __name__ == '__main__':
    unittest.main()
