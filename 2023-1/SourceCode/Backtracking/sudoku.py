import pygame
from bt_visualizations import draw_sudoku, draw_sudoku_txt

def is_valid(board, row, col, num):
    # Check if the number is already present in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is already present in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already present in the 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        draw_sudoku_txt(board)                      

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0
                        draw_sudoku_txt(board)
                        
                return False

    return True


# Example usage
if __name__ == '__main__':

    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(board):
        print("Sudoku solved:")
        draw_sudoku_txt(board)
    else:
        print("No solution exists for the given Sudoku.")   

