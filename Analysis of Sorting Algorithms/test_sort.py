import sorting
import random
import time

def printResults(length, sort_case):     
    temp = [];
    tmp = [];
    for x in range(length):
        temp.append(random.randint(-9999, 9999));
        
    if(sort_case == -1): #Worst Case
        tmp = sorting.descendingOrder(temp); #taking as input an array that is reverse sorted
    elif(sort_case == 1): #Best case
        tmp = sorting.bubble_sort_opt(temp); #taking a sorted array as input
    else:
        tmp = temp; #randomly generated array
    
    s_t = time.time(); 
    b1 = sorting.insertion_sort(tmp)
    print("Insertion sort: {} secs".format(time.time() - s_t))
    
    s_t = time.time();
    b2 = sorting.quick_sort(tmp)
    print("Quick sort: {} secs".format(time.time() - s_t))
    
    s_t = time.time();
    b3 = sorting.bubble_sort(tmp)
    print("Bubble sort: {} secs".format(time.time() - s_t))
    
    s_t = time.time();
    b4 = sorting.bubble_sort_opt(tmp)
    print("Bubble sort (optimized): {} secs".format(time.time() - s_t))
    
    s_t = time.time();
    b5 = sorting.merge_sort(tmp)
    print("Merge sort: {} secs".format(time.time() - s_t))
    
    assert(b1 == b2 == b3 == b4 == b5)
    print("b1 == b2 == b3 == b4 == b5"); #Ensuring array sorting correctness
    
def main():
    # Worst case = -1, Avg. case = 0, Best Case = 1
    sort_case = 0
    length = 25000
    printResults(length, sort_case);

if(__name__ == "__main__"):
    main();
