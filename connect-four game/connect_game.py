import numpy as np

def create_board():
    board = np.zeros((6, 7)) #6 rows and 7 columns
    return board

board = create_board()
game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        selection = input("Player 1 Make your Selection (0-6):")


    # Ask for Player 2 Input

