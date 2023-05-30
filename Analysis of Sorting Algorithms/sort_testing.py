"""
Test script that implements sorting algorithms defined
in sorting.py
"""

import sorting
import random
import time
import copy


def timing_function(sort_type):
    def real_timing_function(sort_tasks):
        def wrapper():
            t1 = time.time()
            sort_tasks()
            t2 = time.time()
            return "{}: {} secs.".format(sort_type, t2 - t1)

        return wrapper

    return real_timing_function


def print_results(length, sort_case):
    """
    Implements sorting definitions on a list of
    given 'length' in the best, average or worst case.
    """

    temp = []
    for _ in range(length):
        temp.append(random.randint(-9999, 9999))

    if sort_case == -1:
        temp.sort(reverse=True)
    elif sort_case == 1:
        temp.sort()

    tmp = copy.deepcopy(temp)

    @timing_function("Insertion sort")
    def task1():
        sorting.insertion_sort(tmp)

    print(task1())
    tmp = copy.deepcopy(temp)

    @timing_function("Quick sort")
    def task2():
        sorting.quick_sort(tmp)

    print(task2())
    tmp = copy.deepcopy(temp)

    @timing_function("Bubble sort")
    def task3():
        sorting.bubble_sort(tmp)

    print(task3())
    tmp = copy.deepcopy(temp)

    @timing_function("Bubble sort (optimized)")
    def task4():
        sorting.bubble_sort_opt(tmp)

    print(task4())
    tmp = copy.deepcopy(temp)

    @timing_function("Merge sort")
    def task5():
        sorting.merge_sort(tmp)

    print(task5())


def main():
    # Worst case = -1, Avg. case = 0, Best Case = 1
    sort_case = -1
    length = 8000
    print_results(length, sort_case)


if __name__ == "__main__":
    main()
