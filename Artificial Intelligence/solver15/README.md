
### Input puzzle:
6 10 2 3<br>
1 14 8 4<br>
5 7 15 11<br>
9 0 13 12<br>

### Output:
#### Explored states:
[[6, 10, 2, 3], [1, 14, 8, 4], [5, 7, 15, 11], [9, 0, 13, 12]] ==> (initial state)<br>
[[6, 10, 2, 3], [1, 14, 8, 4], [5, 7, 15, 11], [9, 13, 0, 12]]<br>
[[6, 10, 2, 3], [1, 14, 8, 4], [5, 7, 0, 11], [9, 13, 15, 12]]<br>
[[6, 10, 2, 3], [1, 14, 8, 4], [5, 0, 7, 11], [9, 13, 15, 12]]<br>
[[6, 10, 2, 3], [1, 0, 8, 4], [5, 14, 7, 11], [9, 13, 15, 12]]<br>
[[6, 0, 2, 3], [1, 10, 8, 4], [5, 14, 7, 11], [9, 13, 15, 12]]<br>
[[0, 6, 2, 3], [1, 10, 8, 4], [5, 14, 7, 11], [9, 13, 15, 12]]<br>
[[1, 6, 2, 3], [0, 10, 8, 4], [5, 14, 7, 11], [9, 13, 15, 12]]<br>
[[1, 6, 2, 3], [5, 10, 8, 4], [0, 14, 7, 11], [9, 13, 15, 12]]<br>
[[1, 6, 2, 3], [5, 10, 8, 4], [9, 14, 7, 11], [0, 13, 15, 12]]<br>
[[1, 6, 2, 3], [5, 10, 8, 4], [9, 14, 7, 11], [13, 0, 15, 12]]<br>
[[1, 6, 2, 3], [5, 10, 8, 4], [9, 0, 7, 11], [13, 14, 15, 12]]<br>
[[1, 6, 2, 3], [5, 0, 8, 4], [9, 10, 7, 11], [13, 14, 15, 12]]<br>
[[1, 0, 2, 3], [5, 6, 8, 4], [9, 10, 7, 11], [13, 14, 15, 12]]<br>
[[1, 2, 0, 3], [5, 6, 8, 4], [9, 10, 7, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 0], [5, 6, 8, 4], [9, 10, 7, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 6, 8, 0], [9, 10, 7, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] ==> (final state)<br>

#### SEQUENCE OF MOVES:<br>
R2 U4 L3 U3 U2 L2 D1 D2 D3 R1 U4 U3 U2 R2 R3 D1 L4 D2 R3 D3<br>