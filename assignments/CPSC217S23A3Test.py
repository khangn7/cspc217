# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 217 Summer 2023
# INSTRUCTOR: Jonathan Hudson
# RNkY9dhladt8yUgc1WHi
# DO NOT EDIT THE ABOVE LINES (OR BELOW LINES UNLESS THIS IS YOUR BONUS VERSION OF FILE) (TAs will use their own version of this file for grading)

import inspect
import sys
import traceback
from copy import deepcopy
from pprint import pprint, pformat
# TODO: You will have to rename this if you rename your CPSC217S23A3Board file (note you cannot use hyphens in your filename)
from CPSC217S23A3Board import *

# Constants to turn off tests for parts of assignment
TEST_PART_1 = True
TEST_PART_2 = True
TEST_PART_3 = True
TEST_PART_4 = True
TEST_PART_5 = True
TEST_PART_6 = True
TEST_PART_7 = True
TEST_PART_8 = True
STOP_FIRST_FAIL = True


##############################################################################
#
# Code below is for testing student functions 
# (IF YOU ARE READING THIS YOU BETTER NO BE CHANGING CODE DOWN HERE)
#
##############################################################################


def run_tests() -> bool:
    """
    Runner for tests
    :return: Boolean True if all test sub-functions pass, otherwise False
    """
    if not test_create_board():
        return False
    if not test_play():
        return False
    if not test_full() and STOP_FIRST_FAIL:
        return False
    if not test_win_in_row() and STOP_FIRST_FAIL:
        return False
    if not test_win_in_column() and STOP_FIRST_FAIL:
        return False
    if not test_win_in_diagonal_backslash() and STOP_FIRST_FAIL:
        return False
    if not test_win_in_diagonal_forward_slash() and STOP_FIRST_FAIL:
        return False
    if not test_won() and STOP_FIRST_FAIL:
        return False
    if not test_hint() and STOP_FIRST_FAIL:
        return False
    return True


def function_exists(name):
    """
    Determine whether a function exists in the namespace at the time this function is called
    :param name: The name of the function to check the existence of
    :return: True if the function exists, False otherwise
    """
    members = inspect.getmembers(sys.modules[__name__])
    for (n, m) in members:
        if n == name and inspect.isfunction(m):
            return True
    return False


def test_create_board() -> bool:
    """
    Run a series of tests on the create_board, row_count, column_count functions
    :return: True if all tests passed.  False if any test fails.
    """
    # IS THIS TEST ON?
    if not TEST_PART_1:
        return True

    print("Testing create_board...")

    # Does function exist?
    try:
        if not ("create_board" in globals() and function_exists("create_board")):
            print("  create_board is not a function.")
            print("Failed test_create_board!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  The create_board function doesn't seem to exist.")
        print("Failed test_create_board!!!!!")
        return False

    print("  create_board function seems to exist.")

    # Is the argument count correct?
    if len(inspect.getfullargspec(create_board).args) != 2:
        print("  create_board should have 2 other arguments.")
        print("Failed test_create_board!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(create_board).args != ['rows', 'columns']:
        print("  create_board should have arguments 'rows','columns'.")
        print("Failed test_create_board!!!!!")
        return False

    print("  create_board parameters appear correct.")

    # Does function run on basic input with exception?
    try:
        create_board(3, 3)
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("An exception occurred during create_board(3,3).")
        print("Failed test_create_board!!!!!")
        return False

    print("  create_board(3,3) ran successfully.")

    # Does function run with default arguments?
    try:
        create_board()
    except Exception as ex:
        #print(str(ex) + "\n")
        #traceback.print_exc(file=sys.stderr)
        print("  An exception occurred during create_board().")
        print("  create_board() may not have defaults for 'rows' and 'columns' parameters.")
        print("Failed test_create_board!!!!!")
        return False

    print("  create_board appears to have default parameters.")

    # Does function return something?
    x = create_board(3, 3)
    if x is None:
        print("  create_board is returning None.")
        print("Failed test_create_board!!!!!")
        return False

    # Does function return a list
    board = create_board(3, 3)
    if type(board) != list:
        print("  create_board return type should be type list.")
        print("Failed test_create_board!!!!!")
        return False

    print("  create_board returns the right type.")

    # Check function correctness on all sizes
    for (row, col) in [(3, 3), (3, 4), (4, 3), (4, 4), (3, 5), (5, 3), (4, 5), (5, 4), (5, 5)]:
        # Does function run without exception on size?
        try:
            print(f"  Attempting to examine 2d list made by create_board({row}, {col})...")
            test_board = create_board(row, col)
        except Exception as ex:
            print(str(ex) + "\n")
            traceback.print_exc(file=sys.stderr)
            print("    An exception occurred during create_board.")
            print("Failed test_create_board!!!!!")
            return False

        # Is the return type list?
        if type(test_board) is not list:
            print(f"    The return type was {type(test_board)} which is not a list.")
            print("Failed test_create_board!!!!!")
            return False

        # Does the list have the correct number of elements?
        if len(test_board) != row:
            print(f"    The board had {len(test_board)} rows when {row} were expected.")
            print("Failed test_create_board!!!!!")
            return False

        # Is each row a list?  Does each row have the correct length?
        for test_row in range(len(test_board)):
            if type(test_board[test_row]) is not list:
                print(f"    The row at index {test_row} is a {test_board[test_row]}, not a list.")
                print("Failed test_create_board!!!!!")
                return False
            if len(test_board[test_row]) != col:
                print(
                    f"    The row at index {test_row} had {len(test_board[test_row])} elements when {col} were expected.")
                print("Failed test_create_board!!!!!")
                return False

        # Is each row unique?
        for test_row in range(len(test_board)):
            for test_col in range(len(test_board)):
                if test_row != test_col:
                    if test_board[test_row] is test_board[test_col]:
                        print(
                            f"    The row at index {test_row} is pointing to the same row as the row at index {test_col}.")
                        print("Failed test_create_board!!!!!")
                        return False

        # Is every space on the board populated with an integer value 0?
        for test_row in range(0, len(test_board)):
            for test_col in range(0, len(test_board[test_row])):
                if type(test_board[test_row][test_col]) is not int:
                    print(
                        f"    The value in row {test_row}, column {test_col} is a {type(test_board[test_row][test_col])}, not an integer.")
                    print("Failed test_create_board!!!!!")
                    return False
                if test_board[test_row][test_col] != 0:
                    print(
                        f"    The integer in row {test_row} column {test_col} is a {test_board[test_row][test_col]} which is not EMPTY==0.")
                    print("Failed test_create_board!!!!!")
                    return False

    # Check board made with default parameters
    try:
        print(f"  Attempting to examine 2d list made by create_board() with default values... ")
        test_board = create_board()
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("    An exception occurred during the attempt.")
        print("Failed test_create_board!!!!!")
        return False

    # Does it have the set the board field to a correct type?
    if type(test_board) is not list:
        print(f"    The value of board was a {type(test_board)} not a list.")
        print("Failed test_create_board!!!!!")
        return False

    # Does the list have the correct number of elements?
    if len(test_board) != 3:
        print(f"    The board had {len(test_board)} rows when 3 were expected.")
        print("Failed test_create_board!!!!!")
        return False

    # Is each row a list?  Does each row have the correct length?
    for test_row in range(len(test_board)):
        if type(test_board[test_row]) is not list:
            print(f"    The row at index {test_row} is a {test_board[test_row]}, not a list.")
            print("Failed test_create_board!!!!!")
            return False
        if len(test_board[test_row]) != 3:
            print(
                f"    The row at index {test_row} had {len(test_board[test_row])} elements when 3 were expected.")
            print("Failed test_create_board!!!!!")
            return False

    # Is each row unique
    for test_row in range(len(test_board)):
        for test_col in range(len(test_board)):
            if test_row != test_col:
                if test_board[test_row] is test_board[test_col]:
                    print(
                        f"    The row at index {test_row} is pointing to the same row as the row at index {test_col}.")
                    print("Failed test_create_board!!!!!")
                    return False

    # Is every space on the board populated with an integer value 0
    for test_row in range(0, len(test_board)):
        for test_col in range(0, len(test_board[test_row])):
            if type(test_board[test_row][test_col]) is not int:
                print(
                    f"    The value in row {test_row}, column {test_col} is a {type(test_board[test_row][test_col])}, not an integer.")
                print("Failed test_create_board!!!!!")
                return False
            if test_board[test_row][test_col] != 0:
                print(
                    f"    The integer in row {test_row} column {test_col} is a {test_board[test_row][test_col]} which is not EMPTY==0.")
                print("Failed test_create_board!!!!!")
                return False

    # Does row_count function exist?
    try:
        if not ("row_count" in globals() and function_exists("row_count")):
            print("  row_count is not a function.")
            print("Failed test_create_board!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  row_count function doesn't seem to exist.")
        print("Failed test_create_board!!!!!")
        return False

    print("  row_count function seems to exist.")

    # Is the argument count correct?
    if len(inspect.getfullargspec(row_count).args) != 1:
        print("  row_count should have 1 argument.")
        print("Failed test_create_board!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(row_count).args != ['board']:
        print("  row_count should have argument 'board'.")
        print("Failed test_create_board!!!!!")
        return False

    print("  row_count parameters appear correct.")

    # Does row_count seem to be defined correctly?
    if type(row_count(create_board(3, 4))) is not int:
        print("  row_count function should return int.")
        print("Failed test_create_board!!!!!")
        return False
    # Does row_count seem to be defined correctly?
    if row_count(create_board(4, 5)) != 4:
        print("  row_count function does not return right size.")
        print("Failed test_create_board!!!!!")
        return False

    print("  row_count return type appears correct.")

    # Does column_count function exist?
    try:
        if not ("column_count" in globals() and function_exists("column_count")):
            print("  column_count is not a function.")
            print("Failed test_create_board!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  column_count function doesn't seem to exist.")
        print("Failed test_create_board!!!!!")
        return False

    print("  column_count function seems to exist.")

    # Is the argument count correct?
    if len(inspect.getfullargspec(column_count).args) != 1:
        print("  column_count should have 1 argument.")
        print("Failed test_create_board!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(column_count).args != ['board']:
        print("  column_count should have argument 'board'.")
        print("Failed test_create_board!!!!!")
        return False

    print("  column_count parameters appear correct.")

    # Does column_count seem to be defined correctly?
    if type(column_count(create_board(3, 4))) is not int:
        print("  column_count function does not return an int.")
        print("Failed test_create_board!!!!!")
        return False
    # Does column_count seem to be defined correctly?
    if column_count(create_board(4, 5)) != 5:
        print("  column_count function does not return the right size.")
        print("Failed test_create_board!!!!!")
        return False

    print("  column_count return type appears correct.")

    print("Passed test_create_board.")
    print()
    return True


def test_play() -> bool:
    """
    Run a series of tests on the play, can_play function
    :return: True if all tests passed.  False if any test fails.
    """
    # IS THIS TEST ON?
    if not TEST_PART_2:
        return True

    print("Testing play, can_play...")

    # Does function exist?
    try:

        if "can_play" in globals() and function_exists("can_play"):
            print("  can_play function seems to exist.")
        else:
            print("  can_play is not a function.")
            print("Failed test_play!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  can_play function doesn't seem to exist.")
        print("Failed test_play!!!!!")
        return False
    try:

        if "play" in globals() and function_exists("play"):
            print("  play function seems to exist.")
        else:
            print("  play is not a function.")
            print("Failed test_play!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  play function doesn't seem to exist!")
        print("Failed test_play!!!!!")
        return False

    # Is the argument count correct?
    if len(inspect.getfullargspec(can_play).args) != 3:
        print("  can_play should have 3 arguments.")
        print("Failed test_play!!!!!")
        return False

    # Is the argument count correct?
    if len(inspect.getfullargspec(play).args) != 4:
        print("  play should have 4 arguments.")
        print("Failed test_play!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(can_play).args != ['board', 'row', 'column']:
        print("  can_play should have arguments 'board', 'row', 'column'.")
        print("Failed test_play!!!!!")
        return False
    if inspect.getfullargspec(play).args != ['board', 'row', 'column', 'piece']:
        print("  play should have arguments 'board', 'row', 'column', 'piece'.")
        print("Failed test_play!!!!!")
        return False

    # Can I run the function?
    try:
        can_play(create_board(3, 3), 0, 0)
        print("  can_play(board,0,0) function execution ran without exception.")
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  An exception occurred during can_play(board,0,0).")
        print("Failed test_play!!!!!")
        return False
    try:
        play(create_board(3, 3), 0, 0, 0)
        print("  The play(board,0,0,EMPTY) function execution ran without exception.")
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  An exception occurred during play(board,0,0,EMPTY).")
        print("Failed test_play!!!!!")
        return False

    # Does function return something?
    if can_play(create_board(3, 3), 0, 0) is None:
        print("  can_play is returning None!")
        print("Failed test_play!!!!!")
        return False

    # Does function return right type?
    if type(can_play(create_board(3, 3), 0, 0)) != bool:
        print("  can_play should return a bool type!")
        print("Failed test_play!!!!!")
        return False
    if not play(create_board(3, 3), 0, 0, 1) is None:
        print("  play is not returning None!")
        print("Failed test_play!!!!!")
        return False

    for test_rows in [3, 4]:
        for test_cols in [3, 4]:
            test_board = create_board(test_rows, test_cols)

            print(f"  can_play test for size ({test_rows}, {test_cols}).")
            for test_row in range(test_rows):
                for test_col in range(test_cols):
                    can_play_result = can_play(test_board, test_row, test_col)
                    # Check return type and value? Should be able to play everywhere.
                    if type(can_play_result) is not bool:
                        print(f"    The value returned was a {type(can_play_result)}, not a boolean.")
                        print("Failed test_play!!!!!")
                        return False
                    if can_play_result is False:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        print(
                            f"    The board \n{test_board_str}\n is empty but can_play(board, {test_row}, {test_col}) was False.")
                        print("Failed test_play!!!!!")
                        return False
                    test_board[test_row][test_col] = X_PIECE
                    can_play_result = can_play(test_board, test_row, test_col)
                    # Check return type and value? Should not be able to play here now.
                    if type(can_play_result) is not bool:
                        print(f"    The value returned was a {type(can_play_result)}, not a boolean.")
                        print("Failed test_play!!!!!")
                        return False
                    if can_play_result is True:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        print(
                            f"    The board \n{test_board_str}\n has piece at this spot but can_play(board, {test_row}, {test_col}) was True.")
                        print("Failed test_play!!!!!")
                        return False
                    test_board[test_row][test_col] = EMPTY
            copy = deepcopy(test_board)
            # Change a copy of the board and check if result of play, can_play matches changes expected
            print(
                f"  play/can_play before and after playing at every location in {test_rows}x{test_cols} empty board")
            for test_row in range(test_rows):
                for test_col in range(test_cols):
                    test_can_play_result0 = can_play(test_board, test_row, test_col)
                    if test_can_play_result0 is False:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        print(
                            f"   The board \n{test_board_str}\n is empty but can_play(board, {test_row}, {test_col}) was False.")
                        print("Failed test_play!!!!!")
                        return False
                    # Play an X. Should not be able to play in this spot now.
                    test_can_play_result1 = play(test_board, test_row, test_col, X_PIECE)
                    if test_can_play_result1 is not None:
                        print(
                            f"    The value returned by play(board, {test_row}, {test_col}, {X_PIECE}) was a {test_can_play_result1}, not None.")
                        print("Failed test_play!!!!!")
                        return False
                    copy[test_row][test_col] = X_PIECE
                    if copy != test_board:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        copy_str = pformat(copy, width=len(copy[0]) * 3 + 2)
                        print(
                            f"    The board \n{test_board_str}\n returned by play(board, {test_row}, {test_col}, {X_PIECE}) was not the expected\n{copy_str}")
                        print("Failed test_play!!!!!")
                        return False
                    test_can_play_result2 = can_play(test_board, test_row, test_col)
                    if test_can_play_result2 is True:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        print(
                            f"   The board \n{test_board_str}\n is occupied but can_play(board, {test_row}, {test_col}) was True.")
                        return True
                    # Play an EMPTY. Should be able to play in this spot now.
                    test_can_play_result3 = play(test_board, test_row, test_col, EMPTY)
                    if test_can_play_result3 is not None:
                        print(
                            f"    The value returned by play(board, {test_row}, {test_col}, {EMPTY}) was a {test_can_play_result3}, not None.")
                        print("Failed test_play!!!!!")
                        return False
                    copy[test_row][test_col] = EMPTY
                    if copy != test_board:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        copy_str = pformat(copy, width=len(copy[0]) * 3 + 2)
                        print(
                            f"    The board \n{test_board_str}\n returned by play(board, {test_row}, {test_col}, {EMPTY}) was not the expected\n{copy_str}")
                        print("Failed test_play!!!!!")
                        return False
                    test_can_play_result4 = can_play(test_board, test_row, test_col)
                    if test_can_play_result4 is False:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        print(
                            f"   The board \n{test_board_str}\n is empty but can_play(board, {test_row}, {test_col}) was False.")
                        print("Failed test_play!!!!!")
                        return False
                    # Play an O. Should not be able to play in this spot now.
                    test_can_play_result5 = play(test_board, test_row, test_col, O_PIECE)
                    if test_can_play_result5 is not None:
                        print(
                            f"    The value returned by play(board, {test_row}, {test_col}, {0}) was a {test_can_play_result5}, not None.")
                        print("Failed test_play!!!!!")
                        return False
                    copy[test_row][test_col] = O_PIECE
                    if copy != test_board:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        copy_str = pformat(copy, width=len(copy[0]) * 3 + 2)
                        print(
                            f"    The board \n{test_board_str}\n returned by play(board, row, col, 0) was not the expected\n{copy_str}")
                        print("Failed test_play!!!!!")
                        return False
                    test_can_play_result6 = can_play(test_board, test_row, test_col)
                    if test_can_play_result6 is True:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        print(
                            f"   The board \n{test_board_str}\n is occupied but can_play(board, {test_row}, {test_col}) was True.")
                        return True
                    # Play an EMPTY. Should be able to play in this spot now.
                    test_can_play_result7 = play(test_board, test_row, test_col, EMPTY)
                    if test_can_play_result7 is not None:
                        print(
                            f"    The value returned by play(board, {test_row}, {test_col}, {EMPTY}) was a {test_can_play_result7}, not None.")
                        print("Failed test_play!!!!!")
                        return False
                    copy[test_row][test_col] = EMPTY
                    if copy != test_board:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        copy_str = pformat(copy, width=len(copy[0]) * 3 + 2)
                        print(
                            f"    The board \n{test_board_str}\n returned by play(board, {test_row}, {test_col}, {EMPTY}) was not the expected\n{copy_str}")
                        print("Failed test_play!!!!!")
                        return False
                    test_can_play_result8 = can_play(test_board, test_row, test_col)
                    if test_can_play_result8 is False:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        print(
                            f"   The board \n{test_board_str}\n is empty but can_play(board, {test_row}, {test_col}) was False.")
                        print("Failed test_play!!!!!")
                        return False
    print("Passed test_play.")
    print()
    return True


def test_full() -> bool:
    """
    Run a series of tests on the full function
    :return: True if all tests passed.  False if any test fails.
    """
    # IS THIS TEST ON?
    if not TEST_PART_3:
        return True

    print("Testing full...")

    # Does function exist?
    try:

        if "full" in globals() and function_exists("full"):
            print("  full function seems to exist.")
        else:
            print("  full is not a function.")
            print("Failed test_full!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  full function doesn't seem to exist.")
        print("Failed test_full!!!!!")
        return False

    # Is the argument count correct?
    if len(inspect.getfullargspec(full).args) != 1:
        print("  full should have 1 argument!")
        print("Failed test_full!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(full).args != ['board']:
        print("  full should have arguments 'board'!")
        print("Failed test_full!!!!!")
        return False

    # Can I run the function?
    try:
        full(create_board(3, 3))
        print("  full(board) function execution ran without exception...")
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  An exception occurred during full(board).")
        print("Failed test_full!!!!!")
        return False

    # Does function return something?
    if full(create_board(3, 3)) is None:
        print("  full is returning None!")
        print("Failed test_full!!!!!")
        return False

    # Does function return right type?
    if type(full(create_board(3, 3))) != bool:
        print("  full should return a bool type!")
        print("Failed test_full!!!!!")
        return False

    for test_rows in [3, 4]:
        for test_cols in [3, 4]:
            print(f"  Testing full for a board of size {test_rows}x{test_cols}")
            test_board = create_board(test_rows, test_cols)
            # Does full return right for empty board?
            print("  Testing call to full for empty board.")
            full_result = full(test_board)
            if type(full_result) is not bool:
                print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                print("Failed test_full!!!!!")
                return False
            if full_result:
                test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"    The board \n{test_board_str}\n is empty but full returned True.")
                print("Failed test_full!!!!!")
                return False
            for row in range(test_rows):
                for col in range(test_cols):
                    test_board[row][col] = X_PIECE
            full_result = full(test_board)
            # Does full return right for full board?
            print("  Testing call to full for board full of Xs.")
            if type(full_result) is not bool:
                print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                print("Failed test_full!!!!!")
                return False
            if not full_result:
                test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"    The board \n{test_board_str}\n is full but full returned False.")
                print("Failed test_full!!!!!")
                return False
            # Does full return right if we selectively remove single piece from anywhere on board?
            print("  Testing full for almost full board of Xs with one EMPTY spot")
            for row in range(test_rows):
                for col in range(test_cols):
                    test_board[row][col] = EMPTY
                    full_result = full(test_board)
                    if type(full_result) is not bool:
                        print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                        print("Failed test_full!!!!!")
                        return False
                    if full_result:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        print(f"    The board \n{test_board_str}\n is not full returned True.")
                        print("Failed test_full!!!!!")
                        return False
                    test_board[row][col] = X_PIECE
            for row in range(test_rows):
                for col in range(test_cols):
                    test_board[row][col] = O_PIECE
            full_result = full(test_board)
            # Does full return right for full board?
            print("  Testing call to full for board full of Os.")
            if type(full_result) is not bool:
                print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                print("Failed test_full!!!!!")
                return False
            if not full_result:
                test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"    The board \n{test_board_str}\n is full but full returned False.")
                print("Failed test_full!!!!!")
                return False
            # Does full return right if we selectively remove single piece from anywhere on board?
            print("  Testing full for almost full board of Os with one EMPTY spot")
            for row in range(test_rows):
                for col in range(test_cols):
                    test_board[row][col] = EMPTY
                    full_result = full(test_board)
                    if type(full_result) is not bool:
                        print(f"    The value returned by full(board) was a {type(full_result)}, not a boolean.")
                        print("Failed test_full!!!!!")
                        return False
                    if full_result:
                        test_board_str = pformat(test_board, width=len(test_board[0]) * 3 + 2)
                        print(f"    The board \n{test_board_str}\n is not full returned True.")
                        print("Failed test_full!!!!!")
                        return False
                    test_board[row][col] = O_PIECE
    print("test_full Passed..")
    print()
    return True


def test_win_in_row() -> bool:
    """
    Run a series of tests on the win_in_row function
    :return: True if all tests passed.  False if any test fails.
    """
    # IS THIS TEST ON?
    if not TEST_PART_4:
        return True

    print("Testing win_in_row...")

    # Does function exist?
    try:

        if "win_in_row" in globals() and function_exists("win_in_row"):
            print("  win_in_row function seems to exist.")
        else:
            print("  win_in_row is not a function.")
            print("Failed test_win_in_row!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  win_in_row function doesn't seem to exist.")
        print("Failed test_win_in_row!!!!!")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(win_in_row).args) != 3:
        print("  win_in_row should have 3 arguments.")
        print("Failed test_win_in_row!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(win_in_row).args != ['board', 'row', 'piece']:
        print("  win_in_row should have arguments 'board', 'row', 'piece'.")
        print("Failed test_win_in_row!!!!!")
        return False

    # Can I run the function?
    try:
        win_in_row(create_board(3, 3), 0, 1)
        print("  win_in_row(board,0,1) function execution ran without exception.")
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  An exception occurred during win_in_row(board,0, 1).")
        print("Failed test_win_in_row!!!!!")
        return False

    # Does function return something?
    if win_in_row(create_board(3, 3), 0, 1) is None:
        print("  win_in_row is returning None.")
        print("Failed test_win_in_row!!!!!")
        return False

    # Does function return right type?
    if type(win_in_row(create_board(3, 3), 0, 1)) != bool:
        print("  win_in_row should return a bool type.")
        print("Failed test_win_in_row!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_row, test_piece, test_exp_result) in [
        # Board sizes with wins
        ([[1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]], 0, 1, True),
        ([[1, 1, 1],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]], 0, 1, True),
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        # Win in other rows
        ([[0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 1, True),
        ([[0, 0, 0, 0],
          [0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 1, True),
        ([[0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]], 2, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 1],
          [0, 0, 0, 0]], 2, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 0, 0]], 2, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0]], 3, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 1]], 3, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 1]], 3, 1, True),
        # Win with other piece type
        ([[0, 0, 0, 0],
          [2, 2, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, True),
        ([[0, 0, 0, 0],
          [0, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, True),
        ([[0, 0, 0, 0],
          [2, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, True),
        # Win has other type around
        ([[1, 1, 1, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[2, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        # Win isn't with asked about piece type
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 2, False),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 2, False),
        ([[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 2, False),
        ([[2, 2, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[2, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        # Win broken by non-empty
        ([[1, 1, 2, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[1, 2, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[1, 1, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 1]], 0, 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 1]], 0, 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 1, 1]], 0, 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 0, 1, False)]:

        # Attempt the function call
        try:
            for loop_row in range(len(test_board)):
                attempt += 1
                win_in_row_result = win_in_row(test_board, loop_row, test_piece)
                # Does it have the correct return type?
                if type(win_in_row_result) is not bool:
                    print(f"  Attempting to use win_in_row Test {attempt}")
                    print("The board was:")
                    pprint(test_board, width=len(test_board[0]) * 3 + 2)
                    print(f"FAILED: For row = {loop_row} piece = {test_piece}")
                    print(f"FAILED: The value returned was a {type(win_in_row_result)}, not a Boolean.")
                    failed += 1
                    if STOP_FIRST_FAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                if test_exp_result and not win_in_row_result and test_row == loop_row:
                    print(f"  Attempting to use win_in_row Test {attempt}")
                    print("The board was:")
                    pprint(test_board, width=len(test_board[0]) * 3 + 2)
                    print(f"FAILED: For row = {loop_row} piece = {test_piece}")
                    print(f"FAILED: The value returned was {win_in_row_result} when {test_exp_result} was expected.")
                    print(f"FAILED: win_in_row should say True to win_in_row {loop_row} but said False.")
                    failed += 1
                    if STOP_FIRST_FAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                elif test_exp_result and win_in_row_result and test_row != loop_row:
                    print(f"  Attempting to use win_in_row Test {attempt}")
                    print("The board was:")
                    pprint(test_board, width=len(test_board[0]) * 3 + 2)
                    print(f"FAILED: For row = {loop_row} piece = {test_piece}")
                    print(f"FAILED: The value returned was {win_in_row_result} when {test_exp_result} was expected.")
                    print(f"FAILED: win_in_row should say True to win_in_row but for {test_row} and not {loop_row}.")
                    failed += 1
                    if STOP_FIRST_FAIL:
                        return
                    else:
                        continue
                elif not test_exp_result and win_in_row_result:
                    print(f"  Attempting to use win_in_row Test {attempt}")
                    print("The board was:")
                    pprint(test_board, width=len(test_board[0]) * 3 + 2)
                    print(f"FAILED: For row = {loop_row} piece = {test_piece}")
                    print(f"FAILED: The value returned was {win_in_row_result} when {test_exp_result} was expected.")
                    print(f"FAILED: win_in_row should not returning True.")
                    failed += 1
                    if STOP_FIRST_FAIL:
                        return
                    else:
                        continue
                passed += 1

        except Exception as ex:
            print(str(ex) + "\n")
            traceback.print_exc(file=sys.stderr)
            print(f"  Attempting to use win_in_row Test {attempt}")
            print("FAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(test_board, width=len(test_board[0]) * 3 + 2)
            print()
            failed += 1
            if STOP_FIRST_FAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"test_win_in_row Failed {failed} test cases of {attempt}")
    else:
        print(f"test_win_in_row Passed all tests. <{attempt}>")

    print()
    return True


def test_win_in_column() -> bool:
    """
    Run a series of tests on the win_in_column function
    :return: True if all tests passed.  False if any test fails.
    """
    if not TEST_PART_4:
        return True
    print("Testing win_in_column...")

    # Does function exist?
    try:

        if "win_in_column" in globals() and function_exists("win_in_column"):
            print("  win_in_column function seems to exist.")
        else:
            print("  win_in_column is not a function.")
            print("Failed test_win_in_column!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  win_in_column function doesn't seem to exist.")
        print("Failed test_win_in_column!!!!!")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(win_in_column).args) != 3:
        print("  win_in_column should have 3 arguments.")
        print("Failed test_win_in_column!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(win_in_column).args != ['board', 'column', 'piece']:
        print("  win_in_column should have arguments 'board', 'column', 'piece'.")
        print("Failed test_win_in_column!!!!!")
        return False

    # Can I run the function?
    try:
        win_in_column(create_board(3, 3), 0, 1)
        print("  win_in_column(board,0,1) function execution ran without exception.")
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  An exception occurred during win_in_column(board,0, 1).")
        print("Failed test_win_in_column!!!!!")
        return False

    # Does function return something?
    if win_in_column(create_board(3, 3), 0, 1) is None:
        print("  win_in_column is returning None.")
        print("Failed test_win_in_column!!!!!")
        return False

    # Does function return right type?
    if type(win_in_column(create_board(3, 3), 0, 1)) != bool:
        print("  win_in_column should return a bool type.")
        print("Failed test_win_in_column!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_col, test_piece, test_exp_result) in [
        ([[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]], 0, 1, True),
        ([[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0],
          [0, 0, 0]], 0, 1, True),
        ([[0, 0, 0],
          [1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]], 0, 1, True),
        ([[1, 0, 0],
          [1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]], 0, 1, True),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, True),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, True),
        ([[0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, True),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, True),
        # Win in other rows
        ([[0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 1, 1, True),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0]], 1, 1, True),
        ([[0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0],
          [0, 1, 0, 0]], 1, 1, True),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 2, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 2, 1, True),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 2, 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0]], 3, 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 3, 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 3, 1, True),
        # Win with other piece type
        ([[0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, 2, True),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0]], 1, 2, True),
        ([[0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0]], 1, 2, True),
        # Win has other type around
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [2, 0, 0, 0]], 0, 1, True),
        ([[2, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, True),
        # Win isn't with asked about piece type
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0]], 0, 2, False),
        ([[0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 2, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 2, False),
        ([[2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0]], 0, 1, False),
        ([[2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0],
          [2, 0, 0, 0]], 0, 1, False),
        # Win broken by non-empty
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [2, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 0],
          [2, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 0, 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 0, 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 0, 1, False)]:

        # Attempt the function call
        try:
            for loop_col in range(len(test_board[0])):
                attempt += 1
                win_in_column_result = win_in_column(test_board, loop_col, test_piece)
                # Does it have the correct return type?
                if type(win_in_column_result) is not bool:
                    print(f"  Attempting to use win_in_column Test {attempt}")
                    print("The board was:")
                    pprint(test_board, width=len(test_board[0]) * 3 + 2)
                    print(f"FAILED: For row = {loop_col} piece = {test_piece}")
                    print(f"FAILED: The value returned was a {type(win_in_column_result)}, not a Boolean.")
                    failed += 1
                    if STOP_FIRST_FAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                elif test_exp_result and not win_in_column_result and test_col == loop_col:
                    print(f"  Attempting to use win_in_column Test {attempt}")
                    print("The board was:")
                    pprint(test_board, width=len(test_board[0]) * 3 + 2)
                    print(f"FAILED: For row = {loop_col} piece = {test_piece}")
                    print(f"FAILED: The value returned was {win_in_column_result} when {test_exp_result} was expected.")
                    print(f"FAILED: win_in_column should say True to winInCol {loop_col} but said False.")
                    failed += 1
                    if STOP_FIRST_FAIL:
                        return
                    else:
                        continue
                # Did it return the correct value
                elif test_exp_result and win_in_column_result and test_col != loop_col:
                    print(f"  Attempting to use win_in_column Test {attempt}")
                    print("The board was:")
                    pprint(test_board, width=len(test_board[0]) * 3 + 2)
                    print(f"FAILED: For row = {loop_col} piece = {test_piece}")
                    print(f"FAILED: The value returned was {win_in_column_result} when {test_exp_result} was expected.")
                    print(f"FAILED: win_in_column should say True to winInCol but for {test_col} and not {loop_col}.")
                    failed += 1
                    if STOP_FIRST_FAIL:
                        return
                    else:
                        continue
                elif not test_exp_result and win_in_column_result:
                    print(f"  Attempting to use win_in_column Test {attempt}")
                    print("The board was:")
                    pprint(test_board, width=len(test_board[0]) * 3 + 2)
                    print(f"FAILED: For row = {loop_col} piece = {test_piece}")
                    print(f"FAILED: The value returned was {win_in_column_result} when {test_exp_result} was expected.")
                    print(f"FAILED: win_in_column should not returning True.")
                    failed += 1
                    if STOP_FIRST_FAIL:
                        return
                    else:
                        continue
                passed += 1
        except Exception as ex:
            print(str(ex) + "\n")
            traceback.print_exc(file=sys.stderr)
            print(f"  Attempting to use win_in_column Test {attempt}")
            print("FAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(test_board, width=len(test_board[0]) * 3 + 2)
            print()
            failed += 1
            if STOP_FIRST_FAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"win_in_column Failed {failed} test cases of {attempt}")
    else:
        print(f"test_win_in_column Passed all tests. <{attempt}>")
    print()
    return True


def test_win_in_diagonal_backslash() -> bool:
    """
    Run a series of tests on the win_in_diagonal_backslash function
    :return: True if all tests passed.  False if any test fails.
    """
    # IS THIS TEST ON?
    if not TEST_PART_5:
        return True
    print("Testing win_in_diagonal_backslash...")

    # Does function exist?
    try:

        if "win_in_diagonal_backslash" in globals() and function_exists("win_in_diagonal_backslash"):
            print("  win_in_diagonal_backslash function seems to exist.")
        else:
            print("  win_in_diagonal_backslash is not a function.")
            print("Failed test_win_in_diagonal_backslash!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  win_in_diagonal_backslash function doesn't seem to exist.")
        print("Failed test_win_in_diagonal_backslash!!!!!")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(win_in_diagonal_backslash).args) != 2:
        print("  win_in_diagonal_backslash should have 2 arguments.")
        print("Failed test_win_in_diagonal_backslash!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(win_in_diagonal_backslash).args != ['board', 'piece']:
        print("  win_in_diagonal_backslash should have arguments 'board', 'piece'.")
        print("Failed test_win_in_diagonal_backslash!!!!!")
        return False

    # Can I run the function?
    try:
        win_in_diagonal_backslash(create_board(3, 3), 1)
        print("  The win_in_diagonal_backslash(board,1) function execution ran without exception.")
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  An exception occurred during win_in_diagonal_backslash(board, 1).")
        print("Failed test_win_in_diagonal_backslash!!!!!")
        return False

    # Does function return something?
    if win_in_diagonal_backslash(create_board(3, 3), 1) is None:
        print("  win_in_diagonal_backslash is returning None.")
        print("Failed test_win_in_diagonal_backslash!!!!!")
        return False

    # Does function return right type?
    if type(win_in_diagonal_backslash(create_board(3, 3), 1)) != bool:
        print("  win_in_diagonal_backslash should return a bool type.")
        print("Failed test_win_in_diagonal_backslash!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_piece, test_exp_result) in [
        # win in different board sizes
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 1, True),
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1],
          [0, 0, 0]], 1, True),
        ([[0, 0, 0],
          [1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 1, True),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0]], 1, True),
        ([[0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, True),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, True),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, True),
        # Win with other piece type
        ([[2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 2]], 2, True),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 2]], 2, True),
        ([[2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 0]], 2, True),
        # Win has other type around
        ([[2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 1]], 2, True),
        ([[2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 1]], 2, True),
        # Win isn't with asked about piece type
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 2, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 2, False),
        # Win broken by non-empty
        ([[1, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),

        # OTHER DIRECTION
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 1, False),
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0],
          [0, 0, 0]], 1, False),
        ([[0, 0, 0],
          [0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 1, False),
        ([[0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, False),
        # Win with other piece type
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 2, False),
        # Win has other type around
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [1, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 1],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 2, False),

        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 1, False),
        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 2, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 1, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 2, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 1, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 2, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 1, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 2, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 2, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 2, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 2, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 2, False)]:

        # Attempt the function call
        try:
            attempt += 1
            win_in_diagonal_result = win_in_diagonal_backslash(test_board, test_piece)
            # Does it have the correct return type?
            if type(win_in_diagonal_result) is not bool:
                print(f"  Attempting to use win_in_diagonal_backslash Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was a {type(win_in_diagonal_result)}, not a Boolean.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            if test_exp_result and not win_in_diagonal_result:
                print(f"  Attempting to use win_in_diagonal_backslash Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {win_in_diagonal_result} when {test_exp_result} was expected.")
                print(f"FAILED: winInDiag should've returned True.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            elif not test_exp_result and win_in_diagonal_result:
                print(f"  Attempting to use win_in_diagonal_backslash Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {win_in_diagonal_result} when {test_exp_result} was expected.")
                print(f"FAILED: winInDiag should've returned False.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as ex:
            print(str(ex) + "\n")
            traceback.print_exc(file=sys.stderr)
            print(f"  Attempting to use win_in_diagonal_backslash Test {attempt}")
            print("FAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(test_board, width=len(test_board[0]) * 3 + 2)
            print()
            failed += 1
            if STOP_FIRST_FAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"test_win_in_diagonal_backslash Failed {failed} test cases of {attempt}")
    else:
        print(f"test_win_in_diagonal_backslash Passed all tests. <{attempt}>")
    print()
    return True


def test_win_in_diagonal_forward_slash() -> bool:
    """
    Run a series of tests on the win_in_diagonal_forward_slash function
    :return: True if all tests passed.  False if any test fails.
    """
    # IS THIS TEST ON?
    if not TEST_PART_6:
        return True
    print("Testing win_in_diagonal_forward_slash...")

    # Does function exist?
    try:

        if "win_in_diagonal_forward_slash" in globals() and function_exists("win_in_diagonal_forward_slash"):
            print("  win_in_diagonal_forward_slash function seems to exist.")
        else:
            print("  win_in_diagonal_forward_slash is not a function.")
            print("Failed test_win_in_diagonal_forward_slash!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  win_in_diagonal_forward_slash function doesn't seem to exist.")
        print("Failed test_win_in_diagonal_forward_slash!!!!!")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(win_in_diagonal_forward_slash).args) != 2:
        print("  win_in_diagonal_forward_slash should have 2 arguments.")
        print("Failed test_win_in_diagonal_forward_slash!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(win_in_diagonal_forward_slash).args != ['board', 'piece']:
        print("  win_in_diagonal_forward_slash should have arguments 'board', 'piece'.")
        print("Failed test_win_in_diagonal_forward_slash!!!!!")
        return False

    # Can I run the function?
    try:
        win_in_diagonal_forward_slash(create_board(3, 3), 1)
        print("  The win_in_diagonal_forward_slash(board,1) function execution ran without exception.")
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  An exception occurred during win_in_diagonal_forward_slash(board, 1).")
        print("Failed test_win_in_diagonal_forward_slash!!!!!")
        return False

    # Does function return something?
    if win_in_diagonal_forward_slash(create_board(3, 3), 1) is None:
        print("  win_in_diagonal_forward_slash is returning None.")
        print("Failed test_win_in_diagonal_forward_slash!!!!!")
        return False

    # Does function return right type?
    if type(win_in_diagonal_forward_slash(create_board(3, 3), 1)) != bool:
        print("  win_in_diagonal_forward_slash should return a bool type.")
        print("Failed test_win_in_diagonal_forward_slash!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_piece, test_exp_result) in [
        # win in different board sizes
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 1, True),
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0],
          [0, 0, 0]], 1, True),
        ([[0, 0, 0],
          [0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 1, True),
        ([[0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0]], 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, True),
        # Win with other piece type
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 2, True),
        # Win has other type around
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [1, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 1],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 2, True),
        # Win isn't with asked about piece type
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0]], 1, False),
        # Win broken by non-empty
        ([[0, 0, 0, 1],
          [0, 0, 2, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 2, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),

        # OTHER DIRECTION
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 1, False),
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1],
          [0, 0, 0]], 1, False),
        ([[0, 0, 0],
          [1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0]], 1, False),
        ([[0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, False),
        ([[2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 2]], 2, False),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 2]], 2, False),
        ([[2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 0]], 2, False),
        ([[2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 1]], 2, False),
        ([[2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 1]], 2, False),

        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 1, False),
        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 2, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 1, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 2, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 1, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 2, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 1, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 2, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 2, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 2, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 2, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 2, False)]:

        # Attempt the function call
        try:
            attempt += 1
            win_in_diagonal_result = win_in_diagonal_forward_slash(test_board, test_piece)
            # Does it have the correct return type?
            if type(win_in_diagonal_result) is not bool:
                print(f"  Attempting to use win_in_diagonal_forward_slash Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was a {type(win_in_diagonal_result)}, not a Boolean.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            if test_exp_result and not win_in_diagonal_result:
                print(f"  Attempting to use win_in_diagonal_forward_slash Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {win_in_diagonal_result} when {test_exp_result} was expected.")
                print(f"FAILED: win_in_diagonal_forward_slash should've returned True.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            elif not test_exp_result and win_in_diagonal_result:
                print(f"  Attempting to use win_in_diagonal_forward_slash Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {win_in_diagonal_result} when {test_exp_result} was expected.")
                print(f"FAILED: win_in_diagonal_forward_slash should've returned False.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as ex:
            print(str(ex) + "\n")
            traceback.print_exc(file=sys.stderr)
            print(f"  Attempting to use win_in_diagonal_forward_slash Test {attempt}")
            print("FAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(test_board, width=len(test_board[0]) * 3 + 2)
            print()
            failed += 1
            if STOP_FIRST_FAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"win_in_diagonal_forward_slash Failed {failed} test cases of {attempt}")
    else:
        print(f"test_win_in_diagonal_forward_slash Passed all tests. <{attempt}>")
    print()
    return True


def test_won() -> bool:
    """
    Run a series of tests on the won function
    :return: True if all tests passed.  False if any test fails.
    """
    # IS THIS TEST ON?
    if not TEST_PART_7:
        return True
    print("Testing won...")

    # Does function exist?
    try:

        if "won" in globals() and function_exists("won"):
            print("  The won function seems to exist.")
        else:
            print("  won is not a function!!!!!")
            print("Failed test_won!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  won function doesn't seem to exist.")
        print("Failed test_won!!!!!")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(won).args) != 2:
        print("  won should have 2 arguments!")
        print("Failed test_won!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(won).args != ['board', 'piece']:
        print("  won should have arguments 'board', 'piece'.")
        print("Failed test_won!!!!!")
        return False

    # Can I run the function?
    try:
        won(create_board(3, 3), 1)
        print("  The win_in_row(board,1) function execution ran without exception.")
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("An exception occurred during won(board,1).")
        print("Failed test_won!!!!!")
        return False

    # Does function return something?
    if won(create_board(3, 3), 1) is None:
        print("  won is returning None.")
        print("Failed test_won!!!!!")
        return False

    # Does function return right type?
    if type(won(create_board(3, 3), 1)) != bool:
        print("  won should return a bool type.")
        print("Failed test_won!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_piece, test_exp_result) in [
        ([[1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]], 1, True),
        ([[0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]], 1, True),
        ([[0, 0, 0],
          [0, 0, 0],
          [1, 1, 1]], 1, True),
        ([[2, 2, 2],
          [0, 0, 0],
          [0, 0, 0]], 2, True),
        ([[0, 0, 0],
          [2, 2, 2],
          [0, 0, 0]], 2, True),
        ([[0, 0, 0],
          [0, 0, 0],
          [2, 2, 2]], 2, True),
        ([[1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]], 2, False),
        ([[0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]], 2, False),
        ([[0, 0, 0],
          [0, 0, 0],
          [1, 1, 1]], 2, False),
        ([[2, 2, 2],
          [0, 0, 0],
          [0, 0, 0]], 1, False),
        ([[0, 0, 0],
          [2, 2, 2],
          [0, 0, 0]], 1, False),
        ([[0, 0, 0],
          [0, 0, 0],
          [2, 2, 2]], 1, False),
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 1, True),
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 1, True),
        ([[2, 0, 0],
          [0, 2, 0],
          [0, 0, 2]], 2, True),
        ([[0, 0, 2],
          [0, 2, 0],
          [2, 0, 0]], 2, True),
        ([[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]], 2, False),
        ([[0, 0, 1],
          [0, 1, 0],
          [1, 0, 0]], 2, False),
        ([[2, 0, 0],
          [0, 2, 0],
          [0, 0, 2]], 1, False),
        ([[0, 0, 2],
          [0, 2, 0],
          [2, 0, 0]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2]], 2, False),
        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 1, False),
        ([[1, 2, 0],
          [2, 2, 1],
          [1, 1, 2]], 2, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 1, False),
        ([[1, 2, 1],
          [1, 2, 2],
          [2, 1, 0]], 2, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 1, False),
        ([[2, 1, 1],
          [1, 2, 2],
          [0, 2, 1]], 2, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 1, False),
        ([[0, 1, 2],
          [2, 2, 1],
          [1, 2, 1]], 2, False),
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [2, 2, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 1],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [2, 2, 2, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 2, 2]], 2, True),
        ([[1, 1, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 1, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [2, 2, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 2, 2, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 1],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [2, 2, 2, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 2, 2]], 1, False),
        ([[1, 1, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 1]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 1, 1]], 1, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, True),
        ([[0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0]], 2, True),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 1, True),
        ([[0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 2]], 2, True),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 2, False),
        ([[0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0],
          [0, 2, 0, 0]], 1, False),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 2, False),
        ([[0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 2],
          [0, 0, 0, 2]], 1, False),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, True),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0]], 2, True),
        ([[0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 1, True),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, True),
        ([[0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 2, True),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0]], 2, True),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 2, False),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 2, 0]], 1, False),
        ([[0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0]], 2, False),
        ([[0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 2, False),
        ([[0, 0, 2, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 2, 0],
          [0, 2, 0, 0]], 1, False),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, False),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 1]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0]], 2, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 1, False),
        ([[1, 2, 1],
          [2, 0, 2],
          [1, 2, 1],
          [0, 0, 0]], 2, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 1, False),
        ([[2, 1, 2],
          [1, 0, 1],
          [2, 1, 2],
          [0, 0, 0]], 2, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 1, False),
        ([[1, 2, 1, 0],
          [2, 0, 2, 0],
          [1, 2, 1, 0],
          [0, 0, 0, 0]], 2, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 1, False),
        ([[2, 1, 2, 0],
          [1, 0, 1, 0],
          [2, 1, 2, 0],
          [0, 0, 0, 0]], 2, False)]:

        # Attempt the function call
        try:
            attempt += 1
            won_result = won(test_board, test_piece)
            # Does it have the correct return type?
            if type(won_result) is not bool:
                print(f"  Attempting to use won Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was a {type(won_result)}, not a Boolean.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue

            # Did it return the correct value
            if test_exp_result and not won_result:
                print(f"  Attempting to use won Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {won_result} when {test_exp_result} was expected.")
                print(f"FAILED: won should've returned True.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            elif not test_exp_result and won_result:
                print(f"  Attempting to use won Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: For piece = {test_piece}")
                print(f"FAILED: The value returned was {won_result} when {test_exp_result} was expected.")
                print(f"FAILED: won should've returned False.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as ex:
            print(str(ex) + "\n")
            traceback.print_exc(file=sys.stderr)
            print(f"  Attempting to use won Test {attempt}")
            print("FAILED: An exception occurred during the attempt.")
            print("The board was:")
            pprint(test_board, width=len(test_board[0]) * 3 + 2)
            print()
            failed += 1
            if STOP_FIRST_FAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"test_won Failed {failed} test cases of {attempt}")
    else:
        print(f"test_won Passed all tests. <{attempt}>")
    print()
    return True


def test_hint() -> bool:
    """
    Run a series of tests on the hint function
    :return: True if all tests passed.  False if any test fails.
    """
    # IS THIS ON?
    if not TEST_PART_8:
        return True
    print("Testing hint...")

    # Does function exist?
    try:

        if "hint" in globals() and function_exists("hint"):
            print("  The hint function seems to exist.")
        else:
            print("  hint is not a function!!!!!")
            print("Failed test_hint!!!!!")
            return False
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  The hint function doesn't seem to exist.")
        print("Failed test_hint!!!!!")
        return False

    # Is the argument count correct
    if len(inspect.getfullargspec(hint).args) != 2:
        print("  hint should have 2 arguments.")
        print("Failed test_hint!!!!!")
        return False

    # Are argument names correct?
    if inspect.getfullargspec(hint).args != ['board', 'piece']:
        print("  hint should have arguments 'board', 'piece'.")
        print("Failed test_hint!!!!!")
        return False

    # Can I run the function?
    try:
        hint(create_board(3, 3), 1)
        print("  The hint(board,0,1) function execution ran without exception.")
    except Exception as ex:
        print(str(ex) + "\n")
        traceback.print_exc(file=sys.stderr)
        print("  An exception occurred during hint(board, 1).")
        print("Failed test_hint!!!!!")
        return False

    # Does function return something?
    if hint(create_board(3, 3), 1) is None:
        print("  hint is returning None.")
        print("Failed test_hint!!!!!")
        return False

    # Does function return right type?
    if type(hint(create_board(3, 3), 1)) != tuple or len(hint(create_board(3, 3), 1)) != 2:
        print("  hint should return a tuple size 2 example (-1, -1).")
        print("Failed test_hint!!!!!")
        return False

    passed = 0
    failed = 0
    attempt = 0
    for (test_board, test_piece, test_row, test_col) in [
        ([[1, 1, 0],
          [0, 0, 0],
          [0, 0, 0]], 1, 0, 2),
        ([[1, 1, 0],
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]], 1, 0, 2),
        ([[1, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 2),
        ([[1, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 2),
        ([[0, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 1),
        ([[0, 0, 0, 0],
          [2, 0, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, 1, 1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, 1, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 0]], 1, 2, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 0]], 1, 2, 1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [2, 0, 2, 0]], 2, 3, 1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 2]], 2, 3, 2),
        ([[1, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [2, 0, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [2, 0, 2, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 2]], 1, -1, -1),
        ([[1, 1, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 2),
        ([[1, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[1, 0, 1, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 0, 1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 0, 1]], 1, 3, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 1]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 1, 1]], 1, 3, 1),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, 0),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, 1, 0),
        ([[0, 2, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 2, 1, 1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 0]], 2, 2, 1),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 1, 1, 2),
        ([[0, 0, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 2, 1, 3),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 2]], 2, 2, 3),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 2, -1, -1),
        ([[0, 2, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 0, 0]], 1, -1, -1),
        ([[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0]], 2, -1, -1),
        ([[0, 0, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 0, 0, 0],
          [0, 0, 0, 2]], 1, -1, -1),
        ([[1, 0, 0, 0],
          [1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, 2, 0),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0]], 1, -1, -1),
        ([[1, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]], 1, 1, 0),
        ([[0, 0, 0, 1],
          [0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, 2, 3),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, -1, -1),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 1]], 1, 1, 3),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, 2, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, 1, 2),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 1, 2, 2),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 1, 1, 2),
        ([[0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, 2, 3),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 2, 0, 2),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 2, 3, 2),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 2, 0, 0]], 2, 1, 3),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 2, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 2, -1, -1),
        ([[1, 0, 0, 0],
          [0, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 1]], 2, -1, -1),
        ([[0, 0, 0, 1],
          [0, 0, 0, 0],
          [0, 1, 0, 0],
          [1, 0, 0, 0]], 2, -1, -1),
        ([[0, 2, 0, 0],
          [0, 0, 2, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 2, 0, 0],
          [2, 0, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [2, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 0, 0]], 1, -1, -1),
        ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 2, 0, 0]], 1, -1, -1)

    ]:

        # Attempt the function call
        try:
            attempt += 1
            row_result, col_result = hint(deepcopy(test_board), test_piece)
            # Does it have the correct return type?
            if type(row_result) is not int:
                print(f"  Attempting to use hint Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: The row value returned was a {type(row_result)}, not a Integer.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            if type(col_result) is not int:
                print(f"  Attempting to use hint Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(f"FAILED: The col value returned was a {type(col_result)}, not a Integer.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            # Did it return the correct value
            if test_row != row_result or test_col != col_result:
                print(f"  Attempting to use hint Test {attempt}")
                print("The board was:")
                pprint(test_board, width=len(test_board[0]) * 3 + 2)
                print(
                    f"FAILED: The value returned was {row_result},{col_result} for piece = {test_piece} when {test_row},{test_col} was expected.")
                failed += 1
                if STOP_FIRST_FAIL:
                    return
                else:
                    continue
            passed += 1
        except Exception as ex:
            print(str(ex) + "\n")
            traceback.print_exc(file=sys.stderr)
            print("FAILED: An exception occurred during the attempt.")
            print(f"  Attempting to use hint Test {attempt}")
            print("The board was:")
            pprint(test_board, width=len(test_board[0]) * 3 + 2)
            failed += 1
            if STOP_FIRST_FAIL:
                return
            else:
                continue
    if failed > 0:
        print(f"hint Failed {failed} test cases of {attempt}")
    else:
        print(f"test_hint Passed all tests. <{attempt}>")
    print()
    return True


if __name__ == '__main__':
    print("This file CPSC217S23A3.py is not designed to be executed directly.")
