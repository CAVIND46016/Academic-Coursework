import random

# References:
# http://www.geeksforgeeks.org/fundamentals-of-algorithms/#SearchingandSorting
# Algorithm Design and Analysis CLRS

"""
Insertion sort (Time complexity = O(n*n))
Max time taken to sort if elements are sorted in reverse order and min time when elements are already sorted.
Insertion sort is used when number of elements is small. 
It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.
"""
def insertion_sort(_toBeSorted):
    for j in range(1, len(_toBeSorted)):
        key = _toBeSorted[j];
        i = j - 1;
        while(i >= 0 and _toBeSorted[i] > key):
            _toBeSorted[i + 1] = _toBeSorted[i];    
            i = i - 1;    
        _toBeSorted[i + 1] = key;
    
    return _toBeSorted;

"""
Quick sort:
Best = Average = O(n*log(n)), Worst = O(n*n)
"""
def quick_sort(_toBeSorted):
    def quick_sort_run(_toBeSorted, _start, _end):
        def partition_fixed(_toBeSorted, _start, _end):
            pivot = _toBeSorted[_start];
            
            i = _start + 1;
            j = _end;
            
            loop_terminates = False;
            while not loop_terminates:
                while(i <= j and _toBeSorted[i] <= pivot):
                    i = i + 1;
                while(_toBeSorted[j] >= pivot and j >= i):
                    j = j - 1;
                if j < i:
                    loop_terminates = True;
                else:
                    temp = _toBeSorted[i];
                    _toBeSorted[i] = _toBeSorted[j];
                    _toBeSorted[j] = temp;
        
            temp = _toBeSorted[_start];
            _toBeSorted[_start] = _toBeSorted[j];
            _toBeSorted[j] = temp;
            
            return j;
        
        def partition_randomized(_toBeSorted, _start, _end):
            i = random.randrange(_start, _end);
            
            temp = _toBeSorted[_start];
            _toBeSorted[_start] = _toBeSorted[i];
            _toBeSorted[i] = temp;
            
            return partition_fixed(_toBeSorted, _start, _end);
        
        if (_start < _end):
            split_element = partition_randomized(_toBeSorted, _start, _end);
            quick_sort_run(_toBeSorted, _start, split_element - 1);
            quick_sort_run(_toBeSorted, split_element + 1, _end);
        
        return _toBeSorted;
    return quick_sort_run(_toBeSorted, 0, len(_toBeSorted) - 1);

"""
Bubble sort
Max time taken to sort if elements are sorted in reverse order (O(n*n)) and min time (O(n)) when elements are already sorted.
"""
def bubble_sort(_toBeSorted):
    for i in range(len(_toBeSorted)):    
        for j in range(0, len(_toBeSorted) - i - 1):
            if(_toBeSorted[j] > _toBeSorted[j+1]):
                _toBeSorted[j], _toBeSorted[j+1] = _toBeSorted[j+1], _toBeSorted[j];
        
    return _toBeSorted;

def bubble_sort_opt(_toBeSorted):
    swapped = None;
    for i in range(len(_toBeSorted)):
        swapped = False;     
        for j in range(0, len(_toBeSorted) - i - 1):
            if(_toBeSorted[j] > _toBeSorted[j+1]):
                _toBeSorted[j], _toBeSorted[j+1] = _toBeSorted[j+1], _toBeSorted[j];
                swapped = True;
        """optimized by stopping the algorithm if inner loop didn’t cause any swap."""       
        if(swapped == False):
            break;
        
    return _toBeSorted;


def merge_sort(_toBeSorted):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)
    
        for i in range(0 , n1):
            L[i] = arr[l + i]
     
        for j in range(0 , n2):
            R[j] = arr[m + 1 + j]
    
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
     
        while(i < n1 and j < n2):
            if(L[i] <= R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        while(i < n1):
            arr[k] = L[i]
            i += 1
            k += 1
     
        while(j < n2):
            arr[k] = R[j]
            j += 1
            k += 1
            
    def merge_sort_run(arr, l, r):
        if(l < r):
            m = (l+(r-1)) // 2
     
            merge_sort_run(arr, l, m)
            merge_sort_run(arr, m+1, r)
            merge(arr, l, m, r)
        
        return arr;
            
    return merge_sort_run(_toBeSorted, 0, len(_toBeSorted) - 1)
 
