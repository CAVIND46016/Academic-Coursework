(Tested on a Windows 10 x64 system, 8gb RAM i5-6200U CPU @ 2.40 GHz.)

#Average case analysis: 
Input ==> Randomly generated array of length 25000 elements <br />
<br />
Insertion sort: 42.43400502204895 secs<br />
Quick sort: 0.16643190383911133 secs<br />
Bubble sort: 90.29240274429321 secs<br />
Bubble sort (optimized): 91.07437491416931 secs<br />
Merge sort: 0.2461543083190918 secs<br />

#Best case analysis:
Input ==> Randomly generated sorted array of length 25000 elements <br />
<br />
Insertion sort: 0.009023904800415039 secs<br />
Quick sort: 0.131850004196167 secs<br />
Bubble sort: 53.24405026435852 secs<br />
Bubble sort (optimized): 0.004010677337646484 secs<br />
Merge sort: 0.21661996841430664 secs<br />

#Worst case analysis:
Input ==> Randomly generated reverse sorted array of length 25000 elements <br />
<br />
Insertion sort: 86.30279755592346 secs<br />
Quick sort: 0.1429133415222168 secs<br />
Bubble sort: 127.06997394561768 secs<br />
Bubble sort (optimized): 128.17605638504028 secs<br />
Merge sort: 0.21707701683044434 secs<br />
