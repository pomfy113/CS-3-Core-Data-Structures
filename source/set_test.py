"""You know, hashtables are peculiar."""
"""If you put in numbers, they're JUST in the right order."""
"""Pretty funky, huh?"""

from set import Set
import unittest

class SetTest(unittest.TestCase):
    def test_init(self):
        test1 = Set(['A', 'B', 'C', 'E'])
        assert test1.size() == 4

        test1 = Set([])
        assert test1.size() == 0

    def test_add(self):
        test1 = Set(['A', 'B', 'C', 'E'])
        assert test1.size() == 4
        test1.add('D')
        assert test1.size() == 5
        test1.add('D')
        assert test1.size() == 5
        test1.add('B')
        assert test1.size() == 5
        test1.remove('B')
        assert test1.size() == 4
        test1.add('B')
        assert test1.size() == 5


    def test_remove(self):
        # Test basic
        test1 = Set(['A', 'B', 'C', 'E'])
        assert test1.contains('B') is True
        assert test1.size() == 4
        test1.remove('B')
        assert test1.contains('B') is False
        assert test1.size() == 3

        with self.assertRaises(ValueError):
            test1.remove('B')

    def test_contains(self):
        test1 = Set(['A', 'B', 'C', 'E'])
        assert test1.contains('A') is True
        assert test1.contains('B') is True
        assert test1.contains('C') is True
        assert test1.contains('D') is False
        assert test1.contains('E') is True
        assert test1.contains('F') is False
        test1.remove('E')
        assert test1.contains('A') is True
        assert test1.contains('B') is True
        assert test1.contains('C') is True
        assert test1.contains('D') is False
        assert test1.contains('E') is False
        assert test1.contains('F') is False
        test1.add('F')
        assert test1.contains('A') is True
        assert test1.contains('B') is True
        assert test1.contains('C') is True
        assert test1.contains('D') is False
        assert test1.contains('E') is False
        assert test1.contains('F') is True
        test1.add('E')
        assert test1.contains('A') is True
        assert test1.contains('B') is True
        assert test1.contains('C') is True
        assert test1.contains('D') is False
        assert test1.contains('E') is True
        assert test1.contains('F') is True

    def test_intersection(self):
        # Typical test, should just have two elements
        test1 = Set([1, 2, 3, 4, 5])
        test2 = Set([4, 5, 6, 7, 8])
        result = test1.intersection(test2)
        assert result.contents() == [4, 5]
        # If same, just in case
        test1 = Set([1, 2, 3, 4, 5])
        test2 = Set([1, 2, 3, 4, 5])
        result = test1.intersection(test2)
        assert result.contents() == [1, 2, 3, 4, 5]
        # If none match
        test1 = Set([1, 2, 3, 4, 5])
        test2 = Set([6, 7, 8, 9, 10])
        result = test1.intersection(test2)
        assert result.contents() == []
        # If both empty
        test1 = Set([])
        test2 = Set([])
        result = test1.intersection(test2)
        test1 = Set(['A', 'B', 'C', 'E'])
        test2 = Set(['A', 'B', 'C', 'D'])
        result = test1.intersection(test2)
        assert result.contains('A') is True
        assert result.contains('B') is True
        assert result.contains('C') is True
        assert result.contains('D') is False
        assert result.contains('E') is False


    def test_union(self):
        # Typical use; should be all the way to 8, skip 4, 5
        test1 = Set([1, 2, 3, 4, 5])
        test2 = Set([4, 5, 6, 7, 8])
        result = test1.union(test2)
        assert result.contents() == [1, 2, 3, 4, 5, 6, 7, 8]
        # Exact same copies, should be no prob
        test1 = Set([1, 2, 3, 4, 5])
        test2 = Set([1, 2, 3, 4, 5])
        result = test1.union(test2)
        assert result.contents() == [1, 2, 3, 4, 5]
        # No overlap
        test1 = Set([1, 2, 3, 4, 5])
        test2 = Set([6, 7, 8, 9, 10])
        result = test1.union(test2)
        assert result.contents() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # Let's try it with letters now
        test1 = Set(['A', 'B', 'C'])
        test2 = Set(['A', 'B', 'C', 'D'])
        result = test1.union(test2)
        assert result.contains('A') is True
        assert result.contains('B') is True
        assert result.contains('C') is True
        assert result.contains('D') is True
        assert result.contains('E') is False

    def test_subset(self):
        # Should be false; two overlapping
        test1 = Set([1, 2, 3, 4, 5])
        test2 = Set([4, 5, 6, 7, 8])
        assert test1.is_subset(test2) is False
        # Should be true; set A within set B
        test1 = Set([1, 2, 3])
        test2 = Set([1, 2, 3, 4, 5, 6, 7, 8])
        assert test1.is_subset(test2) is True
        # Should be true; set A same as set B
        test1 = Set([1, 2, 3])
        test2 = Set([1, 2, 3])
        assert test1.is_subset(test2) is True
        # Should be false; set A bigger than set B
        test1 = Set([1, 2, 3, 4])
        test2 = Set([1, 2, 3])
        assert test1.is_subset(test2) is False
        # Should be false; set A not sharing anything with B
        test1 = Set([1, 2, 3])
        test2 = Set([4, 5, 6])
        assert test1.is_subset(test2) is False
        # Doing the same, but with characters
        # Should be false; two overlapping
        # Should be true; set A within set B
        test1 = Set(['A', 'B', 'C'])
        test2 = Set(['A', 'B', 'C', 'D'])
        assert test1.is_subset(test2) is True
        # Should be true; set A same as set B
        test1 = Set(['A', 'B', 'C'])
        test2 = Set(['A', 'B', 'C'])
        assert test1.is_subset(test2) is True
        # Should be false; set A bigger than set B
        test1 = Set(['A', 'B', 'C', 'D'])
        test2 = Set(['A', 'B', 'C'])
        assert test1.is_subset(test2) is False
        # Should be false; set A not sharing anything with B
        test1 = Set(['A', 'B', 'C', 'D'])
        test2 = Set(['X', 'Y', 'Z'])
        assert test1.is_subset(test2) is False

if __name__ == '__main__':
    unittest.main()
