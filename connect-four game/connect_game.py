import numpy as np
import pygame
import sys

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT)) #6 rows and 7 columns
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece    #place the piece in the board at the specified row and column


def is_valid_location(board, col):
    return board[5][col] == 0    #check if the top row of column is empty


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):   #check from the bottom row to the top row of the column
        if board[r][col] == 0:
            return r
    
def print_board(board):
    print(np.flip(board, 0))   #flip the board to display it correctly


def winning_move(board, piece):
    #Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    #Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    #Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def draw_board(board):
    pass


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE
size = (width, height)
screen = pygame.display.set_mode(size)  #Set up the display window for the game

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                # Ask for Player 1 Input
            if turn == 0:
                col = int(input("Player 1 Make your Selection (0-6): "))
                if is_valid_location(board, col):
                   
                   row = get_next_open_row(board, col)
                   drop_piece(board, row, col, 1)   #Player 1 is represented by 1
                if winning_move(board, 1):
                   print("Player 1 wins!")
                   game_over = True



    # Ask for Player 2 Input
    else:
        col = int(input("Player 2 Make your Selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)   #Player 2 is represented by 2

            if winning_move(board, 2):
                print("Player 2 wins!")
                game_over = True

    print_board(board)
    turn += 1
    turn = turn % 2

