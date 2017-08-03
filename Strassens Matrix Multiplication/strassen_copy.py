from math import ceil, log
import time;

MATRIXINPUT1 = 'C:\\Workspace\\matRead1.txt'
MATRIXINPUT2 = 'C:\\Workspace\\matRead2.txt'
RESULTMATRIX = 'C:\\Workspace\\strassensMatMul.txt';
#Strassen's base case ==> Threshold = 2
THRESHOLD    = 32

def naiveMatrixMultiply(_mat1, _mat2):
    #Initialize the result matrix
    result = new_zeros_matrix(len(_mat1), len(_mat2[0])); 

    for i in range(len(_mat1)):
        for j in range(len(_mat2[0])):
            for k in range(len(_mat2)):
                result[i][j] += _mat1[i][k] * _mat2[k][j];
                
    return result;

def new_zeros_matrix(_row, _col):
    return [[0 for col in range(_col)] for row in range(_row)];

def add_matrix(_mat1, _mat2):
    l = len(_mat1);
    mat3 = [[0 for col in range(l)] for row in range(l)];
    for i in range(l):
        for j in range(l):
            mat3[i][j] = _mat1[i][j] + _mat2[i][j];
    return mat3;

def subtract_matrix(_mat1, _mat2):
    l = len(_mat1);
    mat3 = [[0 for col in range(l)] for row in range(l)];
    for i in range(l):
        for j in range(l):
            mat3[i][j] = _mat1[i][j] - _mat2[i][j];
    return mat3;

#http://stackoverflow.com/questions/3797575/find-largest-power-of-two-less-than-x-number
def next_power_of_two(n):
    return 2**int(ceil(log(n, 2)))

def recursive_strassen(A, B):
    n = len(A)

    if(n > THRESHOLD):
        sub_matrix_size = n//2
        start_time = time.time();
        A11 = [[0 for col in range(sub_matrix_size)] for row in range(sub_matrix_size)]
        A12 = [[0 for col in range(sub_matrix_size)] for row in range(sub_matrix_size)]
        A21 = [[0 for col in range(sub_matrix_size)] for row in range(sub_matrix_size)]
        A22 = [[0 for col in range(sub_matrix_size)] for row in range(sub_matrix_size)]

        B11 = [[0 for col in range(sub_matrix_size)] for row in range(sub_matrix_size)]
        B12 = [[0 for col in range(sub_matrix_size)] for row in range(sub_matrix_size)]
        B21 = [[0 for col in range(sub_matrix_size)] for row in range(sub_matrix_size)]
        B22 = [[0 for col in range(sub_matrix_size)] for row in range(sub_matrix_size)]
        print("sub matrix zeros creation: %s" % (time.time() - start_time))
      
        start_time = time.time();  
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
        print("sub matrix actual vals creation: %s" % (time.time() - start_time))
        start_time = time.time();
        H1 = recursive_strassen(add_matrix(A11, A22), add_matrix(B11, B22))
        H2 = recursive_strassen(add_matrix(A21, A22), B11)
        H3 = recursive_strassen(A11, subtract_matrix(B12, B22))
        H4 = recursive_strassen(A22, subtract_matrix(B21, B11))
        H5 = recursive_strassen(add_matrix(A11, A12) , B22)
        H6 = recursive_strassen(subtract_matrix(A21, A11), add_matrix(B11, B12))
        H7 = recursive_strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))
        print("7 multiplications: %s" % (time.time() - start_time))
        start_time = time.time();
        C1 = subtract_matrix(add_matrix(add_matrix(H1, H4), H7), H5)
        C2 = add_matrix(H3, H5)
        C3 = add_matrix(H2, H4)
        C4 = subtract_matrix(add_matrix(add_matrix(H1, H3), H6), H2)
        print("C1 C2 C3 C4: %s" % (time.time() - start_time))
        start_time = time.time();
        C = [[0 for col in range(n)] for row in range(n)]
        for i in range(sub_matrix_size):
            for j in range(sub_matrix_size):
                C[i][j] = C1[i][j]
                C[i][j + sub_matrix_size] = C2[i][j]
                C[i + sub_matrix_size][j] = C3[i][j]
                C[i + sub_matrix_size][j + sub_matrix_size] = C4[i][j]
        print("C full matrix: %s" % (time.time() - start_time))
        return C
    else:
        return naiveMatrixMultiply(A, B);

def Strassen_Matrix_Multiply_Recursive(_mat1, _mat2):
#     n = len(_mat1)
#     m = next_power_of_two(n)
#     m1 = [[0 for col in range(m)] for row in range(m)]
#     m2 = [[0 for col in range(m)] for row in range(m)]
#     for i in range(n):
#         for j in range(n):
#             m1[i][j] = _mat1[i][j]
#             m2[i][j] = _mat2[i][j]
#     m3 = recursive_strassen(m1, m2)
    m3 = recursive_strassen(_mat1, _mat2)
#     M = [[0 for col in range(n)] for row in range(n)]
#     for i in range(n):
#         for j in range(n):
#             M[i][j] = m3[i][j]
    return m3

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

if(__name__ == "__main__"):
    A = read_Matrix_from_File(MATRIXINPUT1);
    B = read_Matrix_from_File(MATRIXINPUT2);
    assert (len(A) == len(A[0]) == len(B) == len(B[0]))
#     start_time = time.time();
    C = Strassen_Matrix_Multiply_Recursive(A, B);
#     write_Matrix_to_file(RESULTMATRIX, C)
#     print("--- %s seconds ---" % (time.time() - start_time))
    print("done")