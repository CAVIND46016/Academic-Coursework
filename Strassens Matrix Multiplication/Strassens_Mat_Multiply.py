#Cavin Dsouza
#dsouzac@indiana.edu
#Python version 3.5.2

#This code snippet performs Strassens matrix multiplication on two files 'matRead1.txt' and 'matRead2.txt' 
#and creates a 'strassensMatMul.txt' output file at a fixed location
#Directory created: C:\Workspace

from math import ceil, log
import time;

MATRIXINPUT1 = 'C:\\Workspace\\matRead1.txt'
MATRIXINPUT2 = 'C:\\Workspace\\matRead2.txt'
RESULTMATRIX = 'C:\\Workspace\\strassensMatMul.txt';

# MATRIXINPUT1 = 'C:\\Workspace\\matReadZERO1.txt'
# MATRIXINPUT2 = 'C:\\Workspace\\matReadZERO2.txt'
# RESULTMATRIX = 'C:\\Workspace\\strassensMatMulZERO.txt';
#Strassen's base case ==> Threshold = 2
THRESHOLD    = 2

def naiveMatrixMultiply(_mat1, _mat2):
    n = len(_mat1);
    result = new_zeros_matrix(n); 

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += _mat1[i][k] * _mat2[k][j];
                
    return result;

def new_zeros_matrix(_length):
    return [[0 for col in range(_length)] for row in range(_length)];

def add_matrix(_mat1, _mat2):
    l = len(_mat1);
    mat3 = new_zeros_matrix(l); 
    for i in range(l):
        for j in range(l):
            mat3[i][j] = _mat1[i][j] + _mat2[i][j];
    return mat3;

def subtract_matrix(_mat1, _mat2):
    l = len(_mat1);
    mat3 = new_zeros_matrix(l);
    for i in range(l):
        for j in range(l):
            mat3[i][j] = _mat1[i][j] - _mat2[i][j];
    return mat3;

def Strassen_Matrix_Multiply_Recursive(A, B):
    n = len(A)

    if(n > THRESHOLD):
        sub_matrix_size = n//2

        A11 = new_zeros_matrix(sub_matrix_size);
        A12 = new_zeros_matrix(sub_matrix_size);
        A21 = new_zeros_matrix(sub_matrix_size);
        A22 = new_zeros_matrix(sub_matrix_size);

        B11 = new_zeros_matrix(sub_matrix_size);
        B12 = new_zeros_matrix(sub_matrix_size);
        B21 = new_zeros_matrix(sub_matrix_size);
        B22 = new_zeros_matrix(sub_matrix_size);

        for i in range(sub_matrix_size):
            for j in range(sub_matrix_size):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][j + sub_matrix_size]
                A21[i][j] = A[i + sub_matrix_size][j]
                A22[i][j] = A[i + sub_matrix_size][j + sub_matrix_size]

                B11[i][j] = B[i][j]
                B12[i][j] = B[i][j + sub_matrix_size]
                B21[i][j] = B[i + sub_matrix_size][j]
                B22[i][j] = B[i + sub_matrix_size][j + sub_matrix_size]

        #Intermediate P matrices
        P1 = Strassen_Matrix_Multiply_Recursive(add_matrix(A11, A22), add_matrix(B11, B22))
        P2 = Strassen_Matrix_Multiply_Recursive(add_matrix(A21, A22), B11)
        P3 = Strassen_Matrix_Multiply_Recursive(A11, subtract_matrix(B12, B22))
        P4 = Strassen_Matrix_Multiply_Recursive(A22, subtract_matrix(B21, B11))
        P5 = Strassen_Matrix_Multiply_Recursive(add_matrix(A11, A12) , B22)
        P6 = Strassen_Matrix_Multiply_Recursive(subtract_matrix(A21, A11), add_matrix(B11, B12))
        P7 = Strassen_Matrix_Multiply_Recursive(subtract_matrix(A12, A22), add_matrix(B21, B22))

        #C matrix subdivisions
        C1 = subtract_matrix(add_matrix(add_matrix(P1, P4), P7), P5)
        C2 = add_matrix(P3, P5)
        C3 = add_matrix(P2, P4)
        C4 = subtract_matrix(add_matrix(add_matrix(P1, P3), P6), P2)
        
        #Recompiling matrix C
        C = new_zeros_matrix(n);
        for i in range(sub_matrix_size):
            for j in range(sub_matrix_size):
                C[i][j] = C1[i][j]
                C[i][j + sub_matrix_size] = C2[i][j]
                C[i + sub_matrix_size][j] = C3[i][j]
                C[i + sub_matrix_size][j + sub_matrix_size] = C4[i][j]
        return C
    else:
        return naiveMatrixMultiply(A, B);

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

def display_Matrix(arr2d):
    print("\n".join(str(row) for row in arr2d))
    
def main():
    A = read_Matrix_from_File(MATRIXINPUT1);
    B = read_Matrix_from_File(MATRIXINPUT2);
    assert (len(A) == len(A[0]) == len(B) == len(B[0]))
    start_time = time.time();
    C = Strassen_Matrix_Multiply_Recursive(A, B);
    print("--- %s seconds ---" % (time.time() - start_time))
    write_Matrix_to_file(RESULTMATRIX, C)
    print("Strassen's algorithm successfully applied.")

if(__name__ == "__main__"):
    main();