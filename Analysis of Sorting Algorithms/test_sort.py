"""
Test script that implements sorting algorithms defined
in sorting.py
"""
import sorting
import random
import time
import copy

def print_results(length, sort_case):
    """
    Implements sorting definitions on array of given 'length'
    in best, average or worst case.
    """     
    temp = []
    for _ in range(length):
        temp.append(random.randint(-9999, 9999))
       
    if sort_case == -1: #Worst Case
        sorting.descendingOrder(temp) #taking as input an array that is reverse sorted
    elif sort_case == 1: #Best case
        sorting.quick_sort(temp) #taking a sorted array as input
  
    tmp = copy.deepcopy(temp)
    s_t = time.time() 
    sorting.insertion_sort(tmp)
    print("Insertion sort: {} secs".format(time.time() - s_t))
    
    tmp = copy.deepcopy(temp)
    s_t = time.time()
    sorting.quick_sort(tmp)
    print("Quick sort: {} secs".format(time.time() - s_t))
    
    tmp = copy.deepcopy(temp)
    s_t = time.time()
    sorting.bubble_sort(tmp)
    print("Bubble sort: {} secs".format(time.time() - s_t))
    
    tmp = copy.deepcopy(temp)
    s_t = time.time()
    sorting.bubble_sort_opt(tmp)
    print("Bubble sort (optimized): {} secs".format(time.time() - s_t))
    
    tmp = copy.deepcopy(temp)
    s_t = time.time()
    sorting.merge_sort(tmp)
    print("Merge sort: {} secs".format(time.time() - s_t))
    
def main():
    """
    Entry-point for the function.
    """
    # Worst case = -1, Avg. case = 0, Best Case = 1
    sort_case = -1
    length = 25000
    print_results(length, sort_case)

if __name__ == "__main__":
    main()
