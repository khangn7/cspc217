# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 217 Summer 2023
# INSTRUCTOR: Jonathan Hudson
# RNkY9dhladt8yUgc1WHi
# DO NOT EDIT THE ABOVE LINES

# TODO: INFORMATION FOR YOUR TA
'''
Name: Khang Ngo
UCID: 30237573
'''

# Constants for the game pieces
EMPTY = 0
X_PIECE = 1
O_PIECE = 2

DEFAULT_ROW = 3
DEFAULT_COL = 3
WIN_LENGTH = 3

#
#  TODO: Insert your implementation of create_board here (code and comments (in-line and above function))
#
def create_board(rows=DEFAULT_ROW, columns=DEFAULT_COL) -> list:
    """
    returns a 0-init 2d list representing a tictactoe board 

    :param rows: Number, height of board
    :param column: Number, width of board
    :return: list, described above
    """
    board = [0] * rows
    for row in range(rows):
        board[row] = [EMPTY] * columns
    return board


#
#  TODO: Insert your implementation of row_count here (code and comments (in-line and above function))
#
def row_count(board) -> int:
    """
    returns the amount of rows in a 2d list returned by create_board()
    :param board: list, the 2d list representing the tictactoe board
    :return: int, amount of rows
    """
    return len(board)

#
#  TODO: Insert your implementation of column_count here (code and comments (in-line and above function))
#
def column_count(board) -> int:
    """
    returns the amount of columns in a 2d list returned by create_board()
    :param board: list, the 2d list representing the tictactoe board
    :return: int, amount of columns
    """
    return len(board[0])

#
#  TODO: Insert your implementation of can_play here (code and comments (in-line and above function))
#
def can_play(board, row, column) -> bool:
    """
    returns whether there is board[row][column] has the value EMPTY constant
    :param board: list, 2d list representing board
    :param row: row the box chosen to check is in
    :param column: column the box is in
    :return: bool
    """
    return board[row][column] == EMPTY

#
#  TODO: Insert your implementation of play here (code and comments (in-line and above function))
#
def play(board, row, column, piece):
    """
    changes board[row][column] to piece
    :param board: list, 2d list representing board
    :param row: row the box chosen to check is in
    :param column: column the box is in
    :param piece: int, should be constant representing player's piece
    no return
    """
    # board passed by reference for list init'd in function bruh
    board[row][column] = piece

#
#  TODO: Replace this with your implementation of full here (code and comments (in-line and function))
#
def full(board) -> bool:
    """
    returns whether board[][] has no values that are EMPTY constant
    :param board: list, 2d list representing board
    :return: bool, described above
    """
    for row in board:
        for box in row:
            if box == EMPTY:
                return False
    return True


#
#  TODO: Insert your implementations of win_in_row (code and comments (in-line and function))
#
def win_in_row(board, row, piece) -> bool:
    """
    returns whether given piece won in given row
    check if there is the given piece in a row of WIN_LENGTH in given row
    :param board: list, 2d list representing board
    :param row: row the box chosen to check is in
    :param piece: int, should be constant representing player's piece
    :return: bool, True if given piece wins, else False
    """
    in_a_row = 0
    # each box in row
    for box in board[row]:
        if box == piece:
            in_a_row += 1 # record how many in a row so far
        else:
            in_a_row = 0 # reset 
        # if ever enough to win
        if in_a_row == WIN_LENGTH:
            return True
    return False

#
#  TODO: Insert your implementations of win_in_column here (code and comments (in-line and function))
#
def win_in_column(board, column, piece) -> bool:
    """
    returns whether given piece won in given column
    check if there is the given piece in a continuous sequence of WIN_LENGTH in given column
    :param board: list, 2d list representing board
    :param column: column the box chosen to check is in
    :param piece: int, should be constant representing player's piece
    :return: bool, True if given piece wins, else False
    """
    # works same as win_in_row()
    in_a_row = 0
    # each row
    for y in range(row_count(board)):
        # print(board[y][column])
        # same column each row
        if board[y][column] == piece:
            in_a_row += 1
        else:
            in_a_row = 0
        if in_a_row == WIN_LENGTH:
            return True
    return False

#
#  TODO: Insert your implementations of win_in_diagonal_backslash here (code and comments (in-line and function))
#
def win_in_diagonal_backslash(board, piece):
    """
    returns whether given piece won due to a "backslash" diagonal 
    backslash diagonal is sequence where every piece's row and column is 1 higher than previous piece
    function checks if any diagonal of WIN_LENGTH exists where every piece is given piece
    :param board: list, 2d list representing board
    :param piece: int, should be constant representing player's piece
    :return: bool, True if given piece wins, else False
    """
    ro_count = row_count(board)
    col_count = column_count(board)
    # range(ro_count - WIN_LENGTH + 1) and range(ro_count - WIN_LENGTH + 1) 
    # is so no indexing out of range
    # iterate all possible staring coords for diagonal
    for start_x in range(col_count - WIN_LENGTH + 1): 
        for start_y in range(ro_count - WIN_LENGTH + 1):
            # check diagonal
            in_a_row = 0
            box_x = start_x
            box_y = start_y
            for i in range(WIN_LENGTH):
                if board[box_y][box_x] == piece:
                    in_a_row += 1
                else:
                    in_a_row = 0
                if in_a_row == WIN_LENGTH:
                    return True
                # change to index next box
                box_x += 1
                box_y += 1
    return False


#
#  TODO: Insert your implementations of win_in_diagonal_forward_slash here (code and comments (in-line and function))
#
def win_in_diagonal_forward_slash(board, piece):
    """
    returns whether given piece won due to a "forward slash" diagonal 
    forward slash diagonal is sequence where every piece's row is 1 lower and column is 1 higher than previous piece
    function checks if any diagonal of WIN_LENGTH exists where every piece is given piece
    :param board: list, 2d list representing board
    :param piece: int, should be constant representing player's piece
    :return: bool, True if given piece wins, else False
    """
    # designed like win_in_diagonal_backslash()
    ro_count = row_count(board)
    col_count = column_count(board)
    # checks from left to right
    for start_x in range(col_count - WIN_LENGTH + 1):
        for start_y in range(ro_count - 1, WIN_LENGTH - 2, -1):
            # start_x and start_y here will be for the leftmost lowest box of diagonal
            in_a_row = 0
            box_x = start_x
            box_y = start_y
            # check this diagonal
            for i in range(WIN_LENGTH):
                if board[box_y][box_x] == piece:
                    in_a_row += 1
                else:
                    in_a_row = 0
                if in_a_row == WIN_LENGTH:
                    return True
                box_x += 1
                box_y -= 1
    return False


#
#  TODO: Replace this with your implementation of won here (code and comments (in-line and function))
#
def won(board, piece) -> bool:
    """
    returns whether given piece has won in the board using WIN_LENGTH
    :param board: list, 2d list representing board
    :param piece: int, should be constant representing player's piece
    :return: bool, True if given piece wins, else False
    """
    # check rows
    ro_count = row_count(board)
    for y in range(ro_count):
        if win_in_row(board, y, piece):
            return True
    # check columns
    col_count = column_count(board)
    for x in range(col_count):
        if win_in_column(board, x, piece):
            return True
    # check diagonal
    if win_in_diagonal_backslash(board, piece):
        return True
    if win_in_diagonal_forward_slash(board, piece):
        return True
    return False


#
#  TODO: Replace this with your implementation of hint here (code and comments (in-line and function))
#
def hint(board, piece):
    """
    returns row and column of of move to win given a board, if there is no such move returns (-1, -1)
    :param board: list, 2d list representing board
    :param piece: int, should be constant representing player's piece
    :return: tuple, described above
    """
    ro_count = row_count(board)
    col_count = column_count(board)
    # check horizontally
    for start_y in range(ro_count):
        for start_x in range(col_count - WIN_LENGTH + 1):
            first_y = start_y
            first_x = start_x
            win_coords = checkSequenceNearWin(board, piece, first_y, first_x, 0, 1)
            if win_coords[0] != -1:
                return win_coords
    # check vertically
    for start_x in range(col_count):
        for start_y in range(ro_count - WIN_LENGTH + 1):
            first_y = start_y
            first_x = start_x
            win_coords = checkSequenceNearWin(board, piece, first_y, first_x, 1, 0)
            if win_coords[0] != -1:
                return win_coords
    
    # note: 
    # both types of diagonals can be checked at the same time
    # because each diagonal has an opposite diagonal
    # think of checking as convoluting WIN_LENGTH * WIN_LENGTH grid over board
    # in that grid is two WIN_LENGTH diagonals

    # check all diagonals
    for start_x in range(col_count - WIN_LENGTH + 1): 
        for start_y in range(ro_count - WIN_LENGTH + 1):
            # check backwards slash
            first_y = start_y
            first_x = start_x
            win_coords = checkSequenceNearWin(board, piece, first_y, first_x, 1, 1)
            if win_coords[0] != -1:
                return win_coords
            # check forward slash
            first_y = start_y + WIN_LENGTH - 1
            first_x = start_x
            win_coords = checkSequenceNearWin(board, piece, first_y, first_x, -1, 1)
            if win_coords[0] != -1:
                return win_coords

    return (-1, -1)
            
def checkSequenceNearWin(board, piece, start_y:int, start_x:int, change_y:int, change_x:int) -> tuple:
    """
    give starting coords for a sequence defined by change_yx param, return coords needed to win
    if no win returns (-1, -1)
    :param start_y: int, row of first cell in sequence
    :param start_x: int, column of first cell in sequence
    :param change_y: described below
    :param change x: int, the difference in the coords between next cell and current cell in sequence
                     aka. change in coords per cell in sequence from left to right
    :return: tuple, described above in format (row, column)
    """
    check_y = start_y
    check_x = start_x
    pieces_found = 0
    empty = [0, 0]
    for i in range(WIN_LENGTH):
        if board[check_y][check_x] == piece:
            pieces_found += 1
        else:
            empty[0] = check_y
            empty[1] = check_x
        check_y += change_y
        check_x += change_x
    if pieces_found == (WIN_LENGTH - 1):
        return (empty[0], empty[1])

    return (-1, -1)



##############################################################################
#
# Code below is for testing student functions (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
#
##############################################################################
def game_over(board):
    """
    This function determines if the game is complete due to a win or tie by either player
    :param board: The 2D list board to check
    :return: True if game is complete, False otherwise
    """
    if full(board) or won(board, X_PIECE) or won(board, O_PIECE):
        return True
    return False



if __name__ == '__main__':
    print("File is being run directly so ask about running the tests.")

    if input("Enter Y to run tests:") == "Y":
        from CPSC217S23A3Test import *

    run_tests()
