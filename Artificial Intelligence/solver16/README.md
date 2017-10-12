# 15-Puzzle Variant
Instead of sliding a single tile from one cell into an empty cell, in this variant, either one, two or three tiles may be
slid left, right, up or down in a single move.

### Heuristic used: 
Manhattan distance

### Search Algorithm:
A-star

#### Output is a representation of the solution path in the following format:
#### [move-1] [move-2] ... [move-n]


### Input puzzle:
1 7 2 3<br>
5 6 8 4<br>
9 14 10 11<br>
13 0 15 12<br>

### Output:
#### Explored states:
[[1, 7, 2, 3], [5, 6, 8, 4], [9, 14, 10, 11], [13, 0, 15, 12]] ==> (initial state)<br>
[[1, 0, 2, 3], [5, 7, 8, 4], [9, 6, 10, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 0], [5, 7, 8, 4], [9, 6, 10, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 7, 8, 11], [9, 6, 10, 12], [13, 14, 15, 0]]<br>
[[1, 2, 3, 4], [5, 7, 8, 0], [9, 6, 10, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 0, 7, 8], [9, 6, 10, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 11], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 12]]<br>
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] ==> (final state)<br>

#### SEQUENCE OF MOVES:<br>
D34 L22 U31 D24 R24 U12 L22 U13<br>

