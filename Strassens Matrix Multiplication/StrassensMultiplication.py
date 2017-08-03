
MATRIXINPUT1 = 'C:\\Workspace\\matRead1.txt'
MATRIXINPUT2 = 'C:\\Workspace\\matRead2.txt'
RESULTMATRIX = 'C:\\Workspace\\strassensMatMul.txt';

# MATRIXINPUT1 = 'C:\\Workspace\\matReadZERO1.txt'
# MATRIXINPUT2 = 'C:\\Workspace\\matReadZERO2.txt'
# RESULTMATRIX = 'C:\\Workspace\\strassensMatMulZERO.txt';

def add_matrix(_mat1, _mat2):
    assert(len(_mat1) == len(_mat2) and len(_mat1[0]) == len(_mat2[0]))
    l = len(_mat1);
    mat3 = [[0 for col in range(l)] for row in range(l)];
    for i in range(l):
        for j in range(l):
            mat3[i][j] = _mat1[i][j] + _mat2[i][j];
    return mat3;

def subtract_matrix(_mat1, _mat2):
    assert(len(_mat1) == len(_mat2) and len(_mat1[0]) == len(_mat2[0]))
    l = len(_mat1);
    mat3 = [[0 for col in range(l)] for row in range(l)];
    for i in range(l):
        for j in range(l):
            mat3[i][j] = _mat1[i][j] - _mat2[i][j];
    return mat3;

def new_zeros_matrix(_length):
    return _length*[_length*[0]];

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
        f.write('\n')
    f.close();
    
def main():
    X = read_Matrix_from_File(MATRIXINPUT1);
    Y = read_Matrix_from_File(MATRIXINPUT2);

    #Columns of first matrix must be equal to rows of the second matrix
    assert(len(X[0]) == len(Y))
    #Initialize the result matrix
    result = [[0 for col in range(len(Y[0]))] for row in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j];
        
    write_Matrix_to_file(RESULTMATRIX, result);
    
if (__name__ == "__main__"):
    main();
    