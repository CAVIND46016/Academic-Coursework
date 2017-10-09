import sys
import time

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] ) 
            
# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    str = ""
    for r in range(N):
        for c in range(N):
            # Unavailable position of the board
            if(r == x-1 and c == y-1):
                str+= "X "
                continue;
            
            if(board[r][c]):
                str+= sym + " ";
            else:
                str+= "_ ";
            
        str+= "\n"
    return str

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors2(board):
    successor_list = []
    if count_pieces(board) < N:
        valid_r = [r for r in range(N) if(count_on_row(board, r) < 1)]
        valid_c = [c for c in range(N) if(count_on_col(board, c) < 1)]
        for r in valid_r:
            for c in valid_c:
                # if position is unavailable, do not add to successor list.
                if(r == x-1 and c == y-1):
                    continue;
                successor_list.append(add_piece(board,r,c))
            break
    return successor_list

# to validate that given a queen, there is no other queen on its upper or lower diagonal conflicting with it.
def validate(board, row, col):
    for r in range(row+1,N):
        for c in range(N):
            if r-row==c-col or r+c==row+col:
                if board[r][c]:
                    return False
    return True;
    
# check if board is a goal state
def is_goal(board):
    if(count_pieces(board) == N and \
       all( [ count_on_row(board, r) <= 1 for r in range(N) ]) and \
       all( [ count_on_col(board, c) <= 1 for c in range(N) ])):
        if(type == 'nrook'):
            return True;
        else:
            for r in range(N):
                for c in range(N):
                    if board[r][c]:
                        x = validate(board,r,c)
                        if(not x):
                            return x
            return True
    return False;

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors2(fringe.pop()):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False

# This is N, the size of the board. It is passed through command line arguments.
type = 'nqueen'
N = 9;#int(sys.argv[1])
x = 1;#int(sys.argv[2])
y = 1;#int(sys.argv[3])

if(type not in ('nrook', 'nqueen') or x not in range(1, N+1) or y not in range(1, N+1)):
    print("Invalid Input")
    sys.exit(0)
    
if(type == 'nrook'):
    sym = 'R';
else:
    sym = 'Q';
    
# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
s = time.time()
solution = solve(initial_board)
print (printable_board(solution) + "\n" + "{} secs".format(time.time()-s) if solution else "Sorry, no solution found. :(")
