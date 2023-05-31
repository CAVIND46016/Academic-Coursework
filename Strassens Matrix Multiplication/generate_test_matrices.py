"""
Creates two test matrices and writes it into
two text files ==> 'matRead1.txt' and 'matRead2.txt'
"""
import random

MATRIX_INPUT_1 = 'matRead1.txt'
MATRIX_INPUT_2 = 'matRead2.txt'


def write_random_matrix_to_file(filename, mat_dim1, mat_dim2, l_range, h_range):
    """
    Writes matrix to text file
    :param filename:
    :param mat_dim1:
    :param mat_dim2:
    :param l_range:
    :param h_range:
    :return:
    """

    with open(filename, "w", encoding="utf8") as file:
        for _ in range(mat_dim1):
            for j in range(mat_dim2):
                if j != mat_dim2 - 1:
                    file.write(str(random.randint(l_range, h_range)) + ",")
                else:
                    file.write(str(random.randint(l_range, h_range)))
            file.write("\n")


def main():
    rows1, columns1 = 512, 512
    rows2, columns2 = 512, 512
    assert columns1 == rows2

    num_low, num_high = 1, 9

    for value in [
        (MATRIX_INPUT_1, rows1, columns1),
        (MATRIX_INPUT_2, rows2, columns2)
    ]:
        write_random_matrix_to_file(
            value[0],
            value[1],
            value[2],
            num_low,
            num_high
        )

    print("Matrices generated successfully.")


if __name__ == "__main__":
    main()
