"""
Cavin Dsouza
dsouzac@indiana.edu
Python version 3.5.2

This code snippet performs Strassens matrix multiplication
on two files 'matRead1.txt' and 'matRead2.txt' and
creates a 'strassensMatMul.txt' output file at a fixed location.
"""

MATRIX_INPUT_1 = "matRead1.txt"
MATRIX_INPUT_2 = "matRead2.txt"
RESULT_MATRIX = "strassensMatMul.txt"

# Strassen's base case ==> Threshold = 2
THRESHOLD = 2


def naive_matrix_multiply(mat1, mat2):
    n = len(mat1)
    result = new_zeros_matrix(n)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result


def new_zeros_matrix(length):
    return [[0 for _ in range(length)] for _ in range(length)]


def add_matrix(mat1, mat2):
    l = len(mat1)
    mat3 = new_zeros_matrix(l)
    for i in range(l):
        for j in range(l):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
    return mat3


def subtract_matrix(_mat1, _mat2):
    l = len(_mat1)
    mat3 = new_zeros_matrix(l)
    for i in range(l):
        for j in range(l):
            mat3[i][j] = _mat1[i][j] - _mat2[i][j]
    return mat3


def strassen_matrix_multiply_recursive(a, b):
    n = len(a)

    if n > THRESHOLD:
        sub_matrix_size = n // 2

        a11 = new_zeros_matrix(sub_matrix_size)
        a12 = new_zeros_matrix(sub_matrix_size)
        a21 = new_zeros_matrix(sub_matrix_size)
        a22 = new_zeros_matrix(sub_matrix_size)

        b11 = new_zeros_matrix(sub_matrix_size)
        b12 = new_zeros_matrix(sub_matrix_size)
        b21 = new_zeros_matrix(sub_matrix_size)
        b22 = new_zeros_matrix(sub_matrix_size)

        for i in range(sub_matrix_size):
            for j in range(sub_matrix_size):
                a11[i][j] = a[i][j]
                a12[i][j] = a[i][j + sub_matrix_size]
                a21[i][j] = a[i + sub_matrix_size][j]
                a22[i][j] = a[i + sub_matrix_size][j + sub_matrix_size]

                b11[i][j] = b[i][j]
                b12[i][j] = b[i][j + sub_matrix_size]
                b21[i][j] = b[i + sub_matrix_size][j]
                b22[i][j] = b[i + sub_matrix_size][j + sub_matrix_size]

        # Intermediate P matrices
        p1 = strassen_matrix_multiply_recursive(add_matrix(a11, a22), add_matrix(b11, b22))
        p2 = strassen_matrix_multiply_recursive(add_matrix(a21, a22), b11)
        p3 = strassen_matrix_multiply_recursive(a11, subtract_matrix(b12, b22))
        p4 = strassen_matrix_multiply_recursive(a22, subtract_matrix(b21, b11))
        p5 = strassen_matrix_multiply_recursive(add_matrix(a11, a12), b22)
        p6 = strassen_matrix_multiply_recursive(subtract_matrix(a21, a11), add_matrix(b11, b12))
        p7 = strassen_matrix_multiply_recursive(subtract_matrix(a12, a22), add_matrix(b21, b22))

        # C matrix subdivisions
        c1 = subtract_matrix(add_matrix(add_matrix(p1, p4), p7), p5)
        c2 = add_matrix(p3, p5)
        c3 = add_matrix(p2, p4)
        c4 = subtract_matrix(add_matrix(add_matrix(p1, p3), p6), p2)

        # Recompiling matrix C
        c = new_zeros_matrix(n)
        for i in range(sub_matrix_size):
            for j in range(sub_matrix_size):
                c[i][j] = c1[i][j]
                c[i][j + sub_matrix_size] = c2[i][j]
                c[i + sub_matrix_size][j] = c3[i][j]
                c[i + sub_matrix_size][j + sub_matrix_size] = c4[i][j]
        return c

    return naive_matrix_multiply(a, b)


def read_matrix_from_file(filename):
    elements = []
    with open(filename, "r", encoding="utf8") as file_handle:
        for line in file_handle:
            elements.append(
                [
                    int(x) for x in line.split(",")
                ]
            )
    return elements


def write_matrix_to_file(filename, result):
    with open(filename, "w", encoding="utf8") as file_handle:
        for row in result:
            file_handle.write(",".join(str(element) for element in row))
            file_handle.write("\n")


def display_matrix(arr2d):
    print("\n".join(str(row) for row in arr2d))


def main():
    a = read_matrix_from_file(MATRIX_INPUT_1)
    b = read_matrix_from_file(MATRIX_INPUT_2)
    assert len(a) == len(a[0]) == len(b) == len(b[0])
    c = strassen_matrix_multiply_recursive(a, b)
    write_matrix_to_file(RESULT_MATRIX, c)
    print("Strassen's algorithm successfully applied.")


if __name__ == "__main__":
    main()
