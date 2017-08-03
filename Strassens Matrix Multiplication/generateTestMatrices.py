#Cavin Dsouza
#dsouzac@indiana.edu
#Python version 3.5.2

#Creates two test matrices and writes it into two text files ==> 'matRead1.txt' and 'matRead2.txt'
#Directory created: C:\Workspace

import random;

MATRIXINPUT1 = 'C:\\Workspace\\matRead1.txt'
MATRIXINPUT2 = 'C:\\Workspace\\matRead2.txt'
    
def write_Random_Matrix_to_file(_filename, matDim1, matDim2, lRange, hRange):
    fh = open(_filename, "w");
    for i in range(matDim1):
        for j in range(matDim2):
            if(j != matDim2 - 1):
                fh.write(str(random.randint(lRange, hRange)) + ",")
            else:
                fh.write(str(random.randint(lRange, hRange)))
        fh.write("\n") 
          
    fh.close();
    
def main():
    rows1       = 512;
    columns1    = 512;

    rows2       = 512;
    columns2    = 512;
  
    #to multiply matrices
    assert(columns1 == rows2)  
    
    numLow      = 1;
    numHigh     = 9;
    
    write_Random_Matrix_to_file(MATRIXINPUT1, rows1, columns1, numLow, numHigh);
    write_Random_Matrix_to_file(MATRIXINPUT2, rows2, columns2, numLow, numHigh);
    print("Matrices generated successfully.")

if __name__ == "__main__":
    main();