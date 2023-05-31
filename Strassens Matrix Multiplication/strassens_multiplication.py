MATRIX_INPUT_1 = 'matRead1.txt'
MATRIX_INPUT_2 = 'matRead2.txt'
RESULT_MATRIX = 'strassensMatMul.txt'


def add_matrix(mat1, mat2):
    assert len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])
    l = len(mat1)
    mat3 = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
    return mat3


def subtract_matrix(mat1, mat2):
    assert len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0])
    l = len(mat1)
    mat3 = [[0 for _ in range(l)] for _ in range(l)]
    for i in range(l):
        for j in range(l):
            mat3[i][j] = mat1[i][j] - mat2[i][j]
    return mat3


def new_zeros_matrix(_length):
    return _length * [_length * [0]]


def read_matrix_from_file(filename):
    elements = []
    with open(filename, 'r', encoding="utf8") as file_handle:
        for line in file_handle:
            elements.append(
                [
                    int(x) for x in line.split(',')
                ]
            )
    return elements


def write_matrix_to_file(filename, result):
    with open(filename, 'w') as file_handle:
        for i in range(len(result)):
            for j in range(len(result[0])):
                if j != len(result[0]) - 1:
                    file_handle.write(str(result[i][j]) + ",")
                else:
                    file_handle.write(str(result[i][j]))
            file_handle.write('\n')


def main():
    mat_1 = read_matrix_from_file(MATRIX_INPUT_1)
    mat_2 = read_matrix_from_file(MATRIX_INPUT_2)

    # Columns of the first matrix must be equal to rows of the second matrix
    assert len(mat_1[0]) == len(mat_2)
    # Initialize the result matrix
    result = [[0 for _ in range(len(mat_2[0]))] for _ in range(len(mat_1))]

    for i in range(len(mat_1)):
        for j in range(len(mat_2[0])):
            for k in range(len(mat_2)):
                result[i][j] += mat_1[i][k] * mat_2[k][j]

    write_matrix_to_file(RESULT_MATRIX, result)


if __name__ == "__main__":
    main()
