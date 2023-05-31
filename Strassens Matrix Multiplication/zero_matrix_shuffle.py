"""
Accepts two test matrices, varies the percentage of zeros in it as per user
specification and writes it into two text files ==> 'matReadZERO1.txt' and
'matReadZERO2.txt'.
"""
import random

MATRIX_INPUT_1 = "matRead1.txt"
MATRIX_INPUT_2 = "matRead2.txt"

MATRIX_OUTPUT_1 = "matReadZERO1.txt"
MATRIX_OUTPUT_2 = "matReadZERO2.txt"


def shuffle2d(arr):
    """
    Shuffles entries of 2-d array, preserving shape.
    Title: How do I shuffle a multidimensional list in Python
    Author: Mike Housky
    Date: 12/07/2014
    Availability: http://stackoverflow.com/questions/27337784/how-do-i-shuffle-a-multidimensional-list-in-python
    Shuffles entries of 2-d array, preserving shape.
    :param arr:
    :return:
    """

    reshape = []
    data = []
    end = 0
    for row in arr:
        data.extend(row)
        istart, end = end, end + len(row)
        reshape.append((istart, end))
    random.shuffle(data)
    return [data[istart:end] for (istart, end) in reshape]


def zero_matrix(_filename, mat_dim1, mat_dim2, perc):
    """
    Assigns a subset of the mat_dim1 * mat_dim2 matrix to 0
    :param _filename:
    :param mat_dim1:
    :param mat_dim2:
    :param perc:
    :return:
    """

    ctr = 0
    n_zeros = int(perc / 100 * (mat_dim1 * mat_dim2))
    num = []

    with open(_filename, "r", encoding="utf8") as _file:
        for each_line in _file:
            line = [int(x) for x in each_line.split(",")]
            num.append(line)

    for i in range(mat_dim1):
        for j in range(mat_dim2):
            num[i][j] = 0
            ctr += 1
            if ctr == n_zeros:
                break
        if ctr == n_zeros:
            break

    return shuffle2d(num)


def write_matrix_to_file(filename, result):
    """
    Writes matrix to file.
    :param filename:
    :param result:
    :return:
    """

    with open(filename, "w", encoding="utf8") as file:
        for row in result:
            file.write(",".join(str(element) for element in row))
            file.write("\n")


def main():
    rows1, columns1 = 512, 512
    rows2, columns2 = 512, 512

    perc = 75

    write_matrix_to_file(
        MATRIX_OUTPUT_1,
        zero_matrix(MATRIX_INPUT_1, rows1, columns1, perc)
    )
    write_matrix_to_file(
        MATRIX_OUTPUT_2,
        zero_matrix(MATRIX_INPUT_2, rows2, columns2, perc)
    )


if __name__ == "__main__":
    main()
