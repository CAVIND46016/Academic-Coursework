"""
Creates two test matrices and writes it into 
two text files ==> 'matRead1.txt' and 'matRead2.txt'
"""
import random

MATRIXINPUT1 = 'matRead1.txt'
MATRIXINPUT2 = 'matRead2.txt'
    
def write_random_matrix_to_file(_filename, mat_dim1, mat_dim2, l_range, h_range):
    """
    Writes matrix to text file
    """
    with open(_filename, "w") as _file:
        for _ in range(mat_dim1):
            for j in range(mat_dim2):
                if j != mat_dim2 - 1:
                    _file.write(str(random.randint(l_range, h_range)) + ",")
                else:
                    _file.write(str(random.randint(l_range, h_range)))
            _file.write("\n") 
    
def main():
    """
    Entry-point for the function
    """
    rows1, columns1 = 512, 512
    rows2, columns2 = 512, 512
    assert columns1 == rows2
    
    num_low, num_high = 1, 9

    write_random_matrix_to_file(MATRIXINPUT1, rows1, columns1, num_low, num_high)
    write_random_matrix_to_file(MATRIXINPUT2, rows2, columns2, num_low, num_high)
    
    print("Matrices generated successfully.")

if __name__ == "__main__":
    main()
    
