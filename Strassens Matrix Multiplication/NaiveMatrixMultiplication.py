#Cavin Dsouza
#dsouzac@indiana.edu
#Python version 3.5.2

#This code snippet performs naive matrix multiplication (or i-k-j matrix multiplication)
#Accepts two files 'matRead1.txt' and 'matRead2.txt' and creates a 'naiveMatMul.txt' output file
#at a fixed location
#Directory created: C:\Workspace
import time

MATRIXINPUT1 = 'C:\\Workspace\\matRead1.txt'
MATRIXINPUT2 = 'C:\\Workspace\\matRead2.txt'
RESULTMATRIX = 'C:\\Workspace\\naiveMatMul.txt';

# MATRIXINPUT1 = 'C:\\Workspace\\matReadZERO1.txt'
# MATRIXINPUT2 = 'C:\\Workspace\\matReadZERO2.txt'
# RESULTMATRIX = 'C:\\Workspace\\naiveMatMulZERO.txt';

def read_Matrix_from_File(_filename):
    f = open(_filename, 'r');
    elements = [];
    for eachLine in f:
        line = [int(x) for x in eachLine.split(',')];
        elements.append(line);
    f.close();
    return elements;

def write_Matrix_to_file(_filename, _result):
    f = open(_filename, 'w');
    for i in range(len(_result)):
        for j in range(len(_result[0])):
            if(j != len(_result[0]) - 1):
                f.write(str(_result[i][j]) + ",");
            else:
                f.write(str(_result[i][j]));
        f.write('\n');
    f.close();
    
def naiveMatrixMultiply(_mat1, _mat2):
    #Columns of first matrix must be equal to rows of the second matrix
    assert(len(_mat1[0]) == len(_mat2))
    #Initialize the result matrix
    result = [[0 for col in range(len(_mat2[0]))] for row in range(len(_mat1))]

    for i in range(len(_mat1)):
        for j in range(len(_mat2[0])):
            for k in range(len(_mat2)):
                result[i][j] += _mat1[i][k] * _mat2[k][j];
                
    return result;
    
def main():
    X       = read_Matrix_from_File(MATRIXINPUT1);
    Y       = read_Matrix_from_File(MATRIXINPUT2);

    start_time = time.time();
    result  = naiveMatrixMultiply(X, Y);
    print("--- %s seconds ---" % (time.time() - start_time))   
    write_Matrix_to_file(RESULTMATRIX, result);
    print("Naive matrix multiplication completed successfully.")
    
if(__name__ == "__main__"):
    main();
    