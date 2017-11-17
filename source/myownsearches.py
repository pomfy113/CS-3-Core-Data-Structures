import time

class Basic_Searches(object):
    def __init__(self, array=None):
        self.items = array
        self.sorted = sorted(array)

    def bubble_sort(self):
        """Do a bubble sort."""
        # For benchmarking
        array = self.items[:]

        iterations = 0
        start_time = time.time()
        # Initializing
        right = len(array)
        swapped = True

        while right != 0 and swapped is True:
            # For early exit
            swapped = False
            # Go through entire list
            for i in range(right-1):
                # Check early exit; if this doesn't change, we're done
                swapped = False
                # Compare the two elements
                # If it was swapped, we're not completely done yet
                if array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
                    swapped = True
            # Go through less of the array each time
            right -= 1
            # Benchmarking
            iterations += 1

        print("* * BUBBLE SORT * *")
        print("COMPLETE LOOPS:", iterations)
        print("\nTIME:", (time.time() - start_time)*1000, "ms\n")
        return array

    def insertion_sort1(self):
        # For benchmarking
        array = self.items[:]
        iterations = 0
        start_time = time.time()
        # Initializing

        for index in range(len(array)):
            item = index

            while array[index] < array[item-1] and index > 0:
                array[index], array[item-1] = array[item-1], array[index]
                index -= 1
                item -= 1

            # Benchmark
            iterations += 1
        print("* * INSERTION SORT-1 [constant swap] * *")
        print("COMPLETE LOOPS:", iterations)
        print("\nTIME:", (time.time() - start_time)*1000, "ms\n")
        return array

    def insertion_sort2(self):
        """Insertion sort."""
        # For benchmarking
        array = self.items[:]
        iterations = 0
        start_time = time.time()
        # Initializing

        for index in range(len(array)):
            item = index


            while array[index] < array[item-1] and item > 0:
                item -= 1

            newitem = array.pop(index)
            array.insert(item, newitem)

            # Benchmark
            iterations += 1
        print("* * INSERTION SORT-2 [find and insert] * *")
        print("COMPLETE LOOPS:", iterations)
        print("\nTIME:", (time.time() - start_time)*1000, "ms\n")
        return array

    def selection_sort(self):
        """Selection sort."""
        # For benchmarking
        array = self.items[:]
        iterations = 0
        start_time = time.time()

        newarray = []
        for index in range(len(array)):

            lowest = 0
            for item in range(len(array)):
                if array[item] < array[lowest]:
                    lowest = item

            newitem = array.pop(lowest)
            newarray.append(newitem)
            iterations += 1
        print("* * SELECTION SORT * *")
        print("COMPLETE LOOPS:", iterations)
        print("\nTIME:", (time.time() - start_time)*1000, "ms\n")
        return newarray


import random

randomlist = []
for i in range(500):
    randomlist.append(i)

random.shuffle(randomlist)
search = Basic_Searches(randomlist)

print("\n\n* * * * * * * * * * * * * * * * * * * * * * *")
print("* * * * * * * * * * * * * * * * * * * * * * *")
print("* * * * * * * STARTING SEARCHES * * * * * * *")
print("* * * * * * * * * * * * * * * * * * * * * * *")
print("* * * * * * * * * * * * * * * * * * * * * * *\n\n")

print("Randomized list:", search.items)
print("============================\n")
print(search.bubble_sort())
print("============================\n")
print(search.insertion_sort1())
print("============================\n")
print(search.insertion_sort2())
print("============================\n")
print(search.selection_sort())
