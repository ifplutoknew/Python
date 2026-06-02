import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT)) #6 rows and 7 columns
    return board

def drop_piece():
    pass

def is_valid_location(board, col):
    return board[5][col] == 0    #check if the top row of column is empty


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):   #check from the bottom row to the top row of the column
        if board[r][col] == 0:
            return r
    


board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6): "))


    # Ask for Player 2 Input
    else:
        col = int(input("Player 2 Make your Selection (0-6): "))
    
    turn += 1
    turn = turn % 2

