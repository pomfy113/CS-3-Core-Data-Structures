#!python

from sorting import is_sorted, bubble_sort, selection_sort, insertion_sort
import unittest


# Change this variable to the sort function you want to test
sort = bubble_sort


class IsSortedTest(unittest.TestCase):

    def test_is_sorted_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert is_sorted([]) is True  # Empty lists are vacuously sorted
        assert is_sorted([3]) is True  # Single item is trivially sorted
        assert is_sorted([3, 3]) is True  # Duplicate items are in order
        assert is_sorted([3, 5]) is True
        assert is_sorted([3, 5, 7]) is True
        # Write more positive test cases with assert is True statements
        # You'll need a lot more than this to test sorting algorithm robustness

        # Let's go for negatives
        assert is_sorted([-4, -3, -2, -1]) is True
        assert is_sorted([-4, -4, -4, -4]) is True
        assert is_sorted([-4, 0, 4]) is True
        assert is_sorted([-4, 0, -0, 4]) is True




    def test_is_sorted_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        assert is_sorted([5, 3]) is False
        assert is_sorted([3, 5, 3]) is False
        assert is_sorted([7, 5, 3]) is False
        # TODO: Write more negative test cases with assert is False statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # MORE negatives
        assert is_sorted([-11, 3, 2]) is False
        assert is_sorted([2, -1, 1, 1]) is False
        assert is_sorted([4, -3, 2, -1]) is False


    def test_is_sorted_on_sorted_strings(self):
        # Positive test cases (examples) with lists of sorted strings
        assert is_sorted(['A']) is True  # Single item is trivially sorted
        assert is_sorted(['A', 'A']) is True  # Duplicate items are in order
        assert is_sorted(['A', 'B']) is True
        assert is_sorted(['A', 'B', 'C']) is True
        # TODO: Write more positive test cases with assert is True statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # Multiple
        assert is_sorted(['AA', 'BB', 'CC']) is True
        assert is_sorted(['AA', 'BA', 'CA']) is True
        assert is_sorted(['AAAA', 'BB', 'CCC']) is True
        assert is_sorted(['AA', 'AAA', 'AAAA']) is True

        # lowercase
        assert is_sorted(['a', 'b', 'c']) is True
        assert is_sorted(['a', 'a', 'c']) is True
        # Mixed
        assert is_sorted(['A', 'a', 'b']) is True
        assert is_sorted(['C', 'a', 'b']) is True



    def test_is_sorted_on_unsorted_strings(self):
        # Negative test cases (counterexamples) with lists of unsorted strings
        assert is_sorted(['B', 'A']) is False
        assert is_sorted(['A', 'B', 'A']) is False
        assert is_sorted(['C', 'B', 'A']) is False
        # Write more negative test cases with assert is False statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # Multiple
        assert is_sorted(['CCC', 'BBB', 'AAA']) is False
        assert is_sorted(['CCCC', 'CCC', 'C']) is False
        # Lowercase
        assert is_sorted(['c', 'b', 'a']) is False
        assert is_sorted(['c', 'c', 'a']) is False


    def test_is_sorted_on_sorted_tuples(self):
        # Positive test cases (examples) with lists of sorted tuples
        assert is_sorted([(3, 5)]) is True  # Single item
        assert is_sorted([(3, 'A')]) is True  # Single item
        assert is_sorted([('A', 3)]) is True  # Single item
        assert is_sorted([('A', 'B')]) is True  # Single item
        assert is_sorted([(3, 5), (3, 5)]) is True  # Duplicate items
        assert is_sorted([(3, 'A'), (3, 'A')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('A', 3)]) is True  # Duplicate items
        assert is_sorted([('A', 'B'), ('A', 'B')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('B', 5)]) is True  # Both items sorted
        assert is_sorted([('A', 3), ('B', 3)]) is True  # First item sorted
        assert is_sorted([('A', 3), ('A', 5)]) is True  # Second item sorted
        assert is_sorted([(3, 'A'), (5, 'B')]) is True  # Both items sorted
        assert is_sorted([(3, 'A'), (5, 'A')]) is True  # First item sorted
        assert is_sorted([(3, 'A'), (3, 'B')]) is True  # Second item sorted
        # TODO: Write more positive test cases with assert is True statements
        # How do I even start

    def test_is_sorted_on_unsorted_tuples(self):
        # Negative test cases (counterexamples) with lists of unsorted tuples
        assert is_sorted([(5, 'B'), (3, 'A')]) is False  # Both items unsorted
        assert is_sorted([(5, 'A'), (3, 'B')]) is False  # First item unsorted
        assert is_sorted([(3, 'B'), (3, 'A')]) is False  # Second item unsorted
        assert is_sorted([('B', 5), ('A', 3)]) is False  # Both items unsorted
        assert is_sorted([('B', 3), ('A', 5)]) is False  # First item unsorted
        assert is_sorted([('A', 5), ('A', 3)]) is False  # Second item unsorted
        # TODO: Write more negative test cases with assert is False statements
        # HOW DO I EVEN START


class SortTest(unittest.TestCase):

    def test_sort_on_empty_list(self):
        items = []
        sort(items)
        assert items == []  # List should not be changed

    def test_sort_on_small_lists_of_integers(self):
        items1 = [3]
        sort(items1)
        assert items1 == [3]  # List should not be changed
        items2 = [5, 3]
        sort(items2)
        assert items2 == [3, 5]  # List should be in sorted order
        items3 = [5, 7, 3]
        sort(items3)
        assert items3 == [3, 5, 7]
        # TODO: Write more positive test cases with assert is True statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # ...

    def test_sort_on_small_lists_of_strings(self):
        items1 = ['A']
        sort(items1)
        assert items1 == ['A']  # List should not be changed
        items2 = ['B', 'A']
        sort(items2)
        assert items2 == ['A', 'B']  # List should be in sorted order
        items3 = ['B', 'C', 'A']
        sort(items3)
        assert items3 == ['A', 'B', 'C']
        # Write more positive test cases with assert is True statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # ...

    def test_sort_on_lists_of_random_integers(self):
        # TODO: Generate lists of random integers
        # TODO: Write more test cases with assert is True statements
        pass
        # ...


if __name__ == '__main__':
    unittest.main()
