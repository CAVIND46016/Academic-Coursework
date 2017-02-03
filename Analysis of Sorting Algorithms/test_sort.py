import sorting
import random
import time

tmp = [];
length = 25000;
for x in range(length):
    tmp.append(random.randint(-9999, 9999));

print("Sample array");
print(tmp)

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

assert(b1 == b2 == b3 == b4 == b5) #Ensuring array sorting correctness
print("b1 == b2 == b3 == b4 == b5"); 
