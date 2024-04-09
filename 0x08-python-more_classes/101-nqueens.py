#!/usr/bin/python3
"""Module: N Queens.

N Queens problem solver.
"""
import sys


def error_exit(message="", code=1):
    """Exit handling.

    Args:
        message (str): the stdout message to display.
        code (int): exit code.
    """
    print(message)
    exit(code)


def test_pos(board, y):
    """Tests if a queen can be placed at the current position.

    Args:
        board (list): the chessboard.
        y (int): parameter height.
    """
    for x in range(y):
        if board[y][1] is board[x][1]:
            return False
        if abs(board[y][1] - board[x][1]) == y - x:
            return False
    return True


def rec_backtrack(board, y):
    """Backtrack of the possibilities.

    Args:
        board (list): chessboard.
        y (int): parameter height.
    """
    if y is N:
        print(board)
    else:
        for i in range(N):
            board[y][1] = i
            if test_pos(board, y):
                rec_backtrack(board, y + 1)


if len(sys.argv) is not 2:
    error_exit("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except:
    error_exit("N must be a number")

if N < 4:
    error_exit("N must be at least 4")

board = [[i, 0] for i in range(N)]
rec_backtrack(board, 0)
