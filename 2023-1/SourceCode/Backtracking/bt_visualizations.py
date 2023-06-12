import pygame
import sys
import os

def draw_chessboard(queen_positions):

    queen_positions = [(i,queen_positions[i]) for i in range(len(queen_positions))]

    # Set up colors
    BLACK = (107,142,35)
    WHITE = (255,248,220)
    RED = 	(0,0,0)

    # Set up the window size
    WIDTH = 480
    HEIGHT = 480

    # Calculate cell width and height
    CELL_SIZE = WIDTH // len(queen_positions)

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chessboard')

    # Main game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw the chessboard
        for row in range(len(queen_positions)):
            for col in range(len(queen_positions)):
                color = WHITE if (row + col) % 2 == 0 else BLACK
                pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                if (row, col) in queen_positions:
                    pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

        # Update the display
        pygame.display.flip()


def draw_sudoku(board):
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)

    # Dimensions
    SCREEN_WIDTH = 540
    SCREEN_HEIGHT = 600
    CELL_SIZE = 60
    GRID_SIZE = CELL_SIZE * 9

    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku Solver")

    # Load font
    font = pygame.font.Font(None, 36)
    
    screen.fill(WHITE)

    # Draw grid lines
    for x in range(10):
        if x % 3 == 0:
            pygame.draw.line(screen, BLACK, (x * CELL_SIZE, 0), (x * CELL_SIZE, GRID_SIZE), 4)
            pygame.draw.line(screen, BLACK, (0, x * CELL_SIZE), (GRID_SIZE, x * CELL_SIZE), 4)
        else:
            pygame.draw.line(screen, GRAY, (x * CELL_SIZE, 0), (x * CELL_SIZE, GRID_SIZE), 2)
            pygame.draw.line(screen, GRAY, (0, x * CELL_SIZE), (GRID_SIZE, x * CELL_SIZE), 2)

    # Draw numbers
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                number_text = font.render(str(board[row][col]), True, BLUE)
                number_rect = number_text.get_rect(
                    center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(number_text, number_rect)

    pygame.display.update()
    pygame.time.delay(10)

def draw_sudoku_txt(board):
    os.system('cls')
    horizontal_line = "+-------+-------+-------+"

    for i in range(9):
        if i % 3 == 0:
            print(horizontal_line)

        row = "| "
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "| "

            if board[i][j] == 0:
                row += "  "
            else:
                row += str(board[i][j]) + " "

        row += "|"
        print(row)

    print(horizontal_line)



