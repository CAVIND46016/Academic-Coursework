"""
Accepts two test matrices, varies the percentage of zeros in it as per user 
specification and writes it into two text files ==> 'matReadZERO1.txt' and 
'matReadZERO2.txt'.
"""
import random

MATRIXINPUT1 = 'matRead1.txt'
MATRIXINPUT2 = 'matRead2.txt'

MATRIXOUTPUT1 = 'matReadZERO1.txt'
MATRIXOUTPUT2 = 'matReadZERO2.txt'

def shuffle2d(arr2d, rand=random):
    """********************************************************************
    *    Title: How do I shuffle a multidimensional list in Python
    *    Author: Mike Housky
    *    Date: 12/07/2014
    *    Availability: http://stackoverflow.com/questions/27337784/how-do\
                        -i-shuffle-a-multidimensional-list-in-python
    ***********************************************************************
    Shuffes entries of 2-d array arr2d, preserving shape.
    """
    reshape = []
    data = []
    iend = 0
    for row in arr2d:
        data.extend(row)
        istart, iend = iend, iend+len(row)
        reshape.append((istart, iend))
    rand.shuffle(data)
    return [data[istart:iend] for (istart, iend) in reshape]
    
def zero_matrix(_filename, mat_dim1, mat_dim2, perc):
    """
    Assigns a 'perc'% of elements of the 
    mat_dim1 * mat_dim2 matrix to 0
    """
    ctr = 0
    nzeros = int(perc / 100 * (mat_dim1 * mat_dim2)) 
    num = []
    
    with open(_filename, 'r') as _file:
        for each_line in _file:
            line = [int(x) for x in each_line.split(',')]
            num.append(line)
    
    for i in range(mat_dim1):
        for j in range(mat_dim2):
            num[i][j] = 0
            ctr += 1
            if ctr == nzeros:
                break
        if ctr == nzeros:
            break
        
    return shuffle2d(num)

def write_matrix_to_file(_filename, _result):
    """
    Writes matrix to file.
    """
    with open(_filename, 'w') as _file:
        for i in range(len(_result)):
            for j in range(len(_result[0])):
                if j != len(_result[0]) - 1:
                    _file.write(str(_result[i][j]) + ",")
                else:
                    _file.write(str(_result[i][j]))
            _file.write('\n')
  
def main():  
    """
    Entry-point for the function.
    """
    rows1, columns1 = 512, 512
    rows2, columns2 = 512, 512

    perc = 75
    
    write_matrix_to_file(MATRIXOUTPUT1, zero_matrix(MATRIXINPUT1, rows1, columns1, perc))
    write_matrix_to_file(MATRIXOUTPUT2, zero_matrix(MATRIXINPUT2, rows2, columns2, perc))
    
if __name__ == "__main__":
    main()
    
