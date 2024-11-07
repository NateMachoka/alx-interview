#!/usr/bin/python3
"""
The N queens puzzle
"""

import sys


def print_solution(board):
    """Print the board configuration."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row] == col:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row):
    """Solve the N Queens problem using backtracking."""
    n = len(board)
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1)
            board[row] = -1  # Backtrack


def main():
    """Main entry point for the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
