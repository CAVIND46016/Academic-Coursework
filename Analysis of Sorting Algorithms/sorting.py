"""
References:
http://www.geeksforgeeks.org/fundamentals-of-algorithms/#SearchingandSorting
Algorithm Design and Analysis CLRS
"""
import random

def insertion_sort(arr):
    """
    Insertion sort (Time complexity = O(n*n))
    Max time taken to sort if elements are sorted in reverse order and 
    min time when elements are already sorted.
    Insertion sort is used when number of elements is small. 
    It can also be useful when input array is almost sorted, 
    only few elements are misplaced in complete big array.
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]    
            i = i - 1   
        arr[i + 1] = key

def quick_sort(arr):
    """
    Quick sort:
    Best = Average = O(n*log(n)), Worst = O(n*n)
    """
    def quick_sort_run(arr, _start, _end):
        def partition_fixed(arr, _start, _end):
            pivot = arr[_start]
            
            i = _start + 1
            j = _end
            
            loop_terminates = False
            while not loop_terminates:
                while i <= j and arr[i] <= pivot:
                    i = i + 1
                while arr[j] >= pivot and j >= i:
                    j = j - 1
                if j < i:
                    loop_terminates = True
                else:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        
            temp = arr[_start]
            arr[_start] = arr[j]
            arr[j] = temp
            
            return j
        
        def partition_randomized(arr, _start, _end):
            i = random.randrange(_start, _end)
            
            temp = arr[_start]
            arr[_start] = arr[i]
            arr[i] = temp
            
            return partition_fixed(arr, _start, _end)
        
        if _start < _end:
            split_element = partition_randomized(arr, _start, _end)
            quick_sort_run(arr, _start, split_element - 1)
            quick_sort_run(arr, split_element + 1, _end)
        
    return quick_sort_run(arr, 0, len(arr) - 1)

def bubble_sort(arr):
    """
    Bubble sort
    Max time taken to sort if elements are sorted in reverse order (O(n*n)) 
    and min time (O(n)) when elements are already sorted.
    """
    for i in range(len(arr)):    
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubble_sort_opt(arr):
    """
    optimized by stopping the algorithm if inner loop didn’t cause any swap. 
    """
    swapped = None
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True     
        if swapped == False:
            break

def merge_sort(_toBeSorted):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)
    
        for i in range(0, n1):
            L[i] = arr[l + i]
     
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
    
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
     
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
     
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            
    def merge_sort_run(arr, l, r):
        if l < r:
            m = (l+(r-1)) // 2
     
            merge_sort_run(arr, l, m)
            merge_sort_run(arr, m+1, r)
            merge(arr, l, m, r)
            
    return merge_sort_run(_toBeSorted, 0, len(_toBeSorted) - 1)

def descendingOrder(arr):
    """
    optimized by stopping the algorithm if inner loop didn’t cause any swap.
    """ 
    swapped = None
    for i in range(len(arr)):
        swapped = False     
        for j in range(0, len(arr) - i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
      
        if swapped == False:
            break
 
