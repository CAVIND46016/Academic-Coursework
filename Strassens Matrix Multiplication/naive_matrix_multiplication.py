"""
Cavin Dsouza
dsouzac@indiana.edu
Python version 3.5.2

This code snippet performs naive matrix multiplication
(or i-k-j matrix multiplication). Accepts two files
'matRead1.txt' and 'matRead2.txt' and creates a
'naiveMatMul.txt' output file at a fixed location.
"""

MATRIX_INPUT_1 = "matRead1.txt"
MATRIX_INPUT_2 = "matRead2.txt"
RESULT_MATRIX = "naiveMatMul.txt"


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


def write_matrix_to_file(_filename, _result):
    with open(_filename, "w", encoding="utf8") as file_handle:
        for _, row in enumerate(_result):
            for jdx, value in enumerate(row):
                if jdx != len(_result[0]) - 1:
                    file_handle.write(str(value) + ",")
                else:
                    file_handle.write(str(value))
            file_handle.write("\n")


def naive_matrix_multiply(mat1, mat2):
    # Columns of the first matrix must be equal to rows of the second matrix
    assert len(mat1[0]) == len(mat2)
    # Initialize the result matrix
    result = [
        [
            0 for _ in range(len(mat2[0]))
        ] for _ in range(len(mat1))
    ]

    for idx, _ in enumerate(mat1):
        for jdx, _ in enumerate(mat2[0]):
            for kdx, _ in enumerate(mat2):
                result[idx][jdx] += mat1[idx][kdx] * mat2[kdx][jdx]

    return result


def main():
    result = naive_matrix_multiply(
        read_matrix_from_file(MATRIX_INPUT_1),
        read_matrix_from_file(MATRIX_INPUT_2)
    )
    write_matrix_to_file(RESULT_MATRIX, result)
    print("Naive matrix multiplication completed successfully.")


if __name__ == "__main__":
    main()
