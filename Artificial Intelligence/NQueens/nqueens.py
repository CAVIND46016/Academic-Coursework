import sys
import time


def count_on_row(board, row):
    """
    Count # of pieces in given row
    :param board: 
    :param row: 
    :return: 
    """

    return sum(board[row])


def count_on_col(board, col):
    """
    Count # of pieces in given column
    :param board: 
    :param col: 
    :return: 
    """

    return sum([row[col] for row in board])


def count_pieces(board):
    """
    Count total # of pieces on board
    :param board: 
    :return: 
    """

    return sum([sum(row) for row in board])


def printable_board(board):
    """
    Return a string with the board rendered in a human-friendly format
    :param board: 
    :return: 
    """

    text = ""
    for r in range(N):
        for c in range(N):
            # Unavailable position of the board
            if r == x - 1 and c == y - 1:
                text += "X "
                continue

            if board[r][c]:
                text += sym + " "
            else:
                text += "_ "

        text += "\n"
    return text


def add_piece(board, row, col):
    """
    Add a piece to the board at the given position, and return a new board (doesn't change original)
    :param board: 
    :param row: 
    :param col: 
    :return: 
    """

    return board[0:row] + [board[row][0:col] + [1, ] + board[row][col + 1:]] + board[row + 1:]


def successors2(board):
    """
    Retrieve a list of the successor states for a given board configuration.
    :param board: 
    :return: 
    """

    successor_list = []
    if count_pieces(board) < N:
        valid_r = [r for r in range(N) if (count_on_row(board, r) < 1)]
        valid_c = [c for c in range(N) if (count_on_col(board, c) < 1)]
        for r in valid_r:
            for c in valid_c:
                # if position is unavailable, do not add to the successor list.
                if r == x - 1 and c == y - 1:
                    continue
                successor_list.append(add_piece(board, r, c))
            break
    return successor_list


def validate(board, row, col):
    """
    to validate that given a queen, there is no other queen on its upper or lower diagonal conflicting with it.
    :param board: 
    :param row: 
    :param col: 
    :return: 
    """

    for r in range(row + 1, N):
        for c in range(N):
            if r - row == c - col or r + c == row + col:
                if board[r][c]:
                    return False
    return True


# check if board is a goal state
def is_goal(board):
    if (count_pieces(board) == N and
        all([count_on_row(board, r) <= 1 for r in range(N)]) and
        all([count_on_col(board, c) <= 1 for c in range(N)])):
        if type_ == "nrook":
            return True
        else:
            for r in range(N):
                for c in range(N):
                    if board[r][c]:
                        xx = validate(board, r, c)
                        if not xx:
                            return xx
            return True
    return False


def solve(board):
    """
    Solve n-rooks!
    :param board: 
    :return: 
    """

    fringe = [board]
    while len(fringe) > 0:
        for successor in successors2(fringe.pop()):
            if is_goal(successor):
                return successor
            fringe.append(successor)
    return False


# This is N, the size of the board. It is passed through command line arguments.
type_ = "nqueen"
N = 9
x = 1
y = 1

if type_ not in ("nrook", "nqueen") or x not in range(1, N + 1) or y not in range(1, N + 1):
    print("Invalid Input")
    sys.exit(0)

if type_ == "nrook":
    sym = "R"
else:
    sym = "Q"

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0] * N] * N
print("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
s = time.time()
solution = solve(initial_board)
print(printable_board(str(solution)) + "\n" + "{} secs".format(
    time.time() - s) if solution else "Sorry, no solution found. :(")
