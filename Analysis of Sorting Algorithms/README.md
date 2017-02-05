(Tested on a Windows x64 system, 8gb RAM i5-6200U CPU @ 2.40 GHz.)

#Average case analysis: 
Input ==> Randomly generated array of length 25000 elements <br />
<br />
Insertion sort: 42.576238870620734 secs <br />
Quick sort: 0.13081145286560059 secs <br />
Bubble sort: 52.32356381416321 secs <br />
Bubble sort (optimized): 0.005013227462768555 secs <br />
Merge sort: 0.21962261199951172 secs <br />

#Best case analysis:
Input ==> Randomly generated sorted array of length 25000 elements <br />
<br />
Insertion sort: 0.009023904800415039 secs<br />
Quick sort: 0.12733983993530273 secs<br />
Bubble sort: 52.047099113464355 secs<br />
Bubble sort (optimized): 0.004517555236816406 secs<br />
Merge sort: 0.22005343437194824 secs<br />

#Worst case analysis:
Input ==> Randomly generated reverse sorted array of length 25000 elements <br />
<br />
Insertion sort: 86.68600940704346 secs<br />
Quick sort: 0.12930798530578613 secs<br />
Bubble sort: 52.68231439590454 secs<br />
Bubble sort (optimized): 0.004010915756225586 secs<br />
Merge sort: 0.22008490562438965 secs<br />
