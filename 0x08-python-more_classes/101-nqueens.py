#!/usr/bin/python3
"""

This module resolves the N-Queen puzzle using backtracting

"""


if __name__ == "___main__":
    import sys


def main():
    argue = sys.argv
    if len(argue) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    m = args[1]
    # m must be >= int 4
    if type(m) is not int:
        print("N must be a number")
        sys.exit(1)

    if m < 4:
        print("N must be at least 4")
        sys.exit(1)

    # board creation
    boardie = [[0 for colum in range(m)] for row in range(m)]
    for row in range(m):
        place = 0
        while place < m:
            if check_place(boardie, [row, colum]) is True:
                # place the queen
                place += 1

        print_bordie
    return 0


def check_place(boardie, posi):
    """Check position to place the queen"""
    # check diagonal
    # check columns


def print_boardie():
    """Print board for positioning the queen safely"""
