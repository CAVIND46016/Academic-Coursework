#Cavin Dsouza
#dsouzac@indiana.edu
#Python version 3.5.2

#Accepts two test matrices, varies the percentage of zeros in it as per user specification and 
#writes it into two text files ==> 'matReadZERO1.txt' and 'matReadZERO2.txt'
#Directory created: C:\Workspace

import random;

MATRIXINPUT1 = 'C:\\Workspace\\matRead1.txt'
MATRIXINPUT2 = 'C:\\Workspace\\matRead2.txt'

MATRIXOUTPUT1 = 'C:\\Workspace\\matReadZERO1.txt'
MATRIXOUTPUT2 = 'C:\\Workspace\\matReadZERO2.txt'

def shuffle2d(arr2d, rand=random):
    #***************************************************************************************
    #*    Title: How do I shuffle a multidimensional list in Python
    #*    Author: Mike Housky
    #*    Date: 12/07/2014
    #*    Availability: http://stackoverflow.com/questions/27337784/how-do-i-shuffle-a-multidimensional-list-in-python
    #***************************************************************************************
    #Shuffes entries of 2-d array arr2d, preserving shape.
    reshape = []
    data = []
    iend = 0
    for row in arr2d:
        data.extend(row)
        istart, iend = iend, iend+len(row)
        reshape.append((istart, iend))
    rand.shuffle(data)
    return [data[istart:iend] for (istart,iend) in reshape]

def display_Matrix(arr2d):
    print("\n".join(str(row) for row in arr2d))
    
def zero_Matrix(_filename, _matDim1, _matDim2, _percent):
    f = open(_filename, 'r')
    counter = 0;
    nzeros = int(_percent / 100 * (_matDim1 * _matDim2)); 
    
    numbers = []
    for eachLine in f:
        line = [int(x) for x in eachLine.split(',')]
        numbers.append(line)
    f.close();
    
    for i in range(0, _matDim1):
        for j in range(0, _matDim2):
            numbers[i][j] = 0;
            counter += 1;
            if(counter == nzeros):
                break;
        if(counter == nzeros):
            break; 
    return (shuffle2d(numbers));

def write_Matrix_to_file(_filename, _result):
    f = open(_filename, 'w');
    for i in range(len(_result)):
        for j in range(len(_result[0])):
            if(j != len(_result[0]) - 1):
                f.write(str(_result[i][j]) + ",");
            else:
                f.write(str(_result[i][j]));
        f.write('\n')
    f.close();
    
def main():
    rows1       = 512;
    columns1    = 512;

    rows2       = 512;
    columns2    = 512;
    
    percentage  = 75;
    
    write_Matrix_to_file(MATRIXOUTPUT1, zero_Matrix(MATRIXINPUT1, rows1, columns1, percentage));
    write_Matrix_to_file(MATRIXOUTPUT2, zero_Matrix(MATRIXINPUT2, rows2, columns2, percentage));
    
if __name__ == "__main__":
    main();