import os
import random
import time

import chess

board = chess.Board()

while not board.is_game_over():

    print(f"It is {'white' if board.turn else 'black'}'s turn to move.")
    print(board)
    move = random.choice(list(board.legal_moves))
    board.push(move)
    time.sleep(0.5)
    os.system('clear')

print(board)
