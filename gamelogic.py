import os 
import time
import filehandling as fh

def check_win(board, symbole):
    return ((board[0] == symbole and board[1] == symbole and board[2] == symbole) or 
        (board[3] == symbole and board[4] == symbole and board[5] == symbole) or 
        (board[6] == symbole and board[7] == symbole and board[8] == symbole) or 
        (board[0] == symbole and board[3] == symbole and board[6] == symbole) or 
        (board[1] == symbole and board[4] == symbole and board[7] == symbole) or
        (board[2] == symbole and board[5] == symbole and board[8] == symbole) or
        (board[0] == symbole and board[4] == symbole and board[8] == symbole) or 
        (board[6] == symbole and board[4] == symbole and board[2] == symbole))

def check_draw(board):
    isDraw = True
    for s in board:
        if (s == ' '):
            isDraw = False
            break
    return isDraw

def draw_board(board):
    os.system('cls')
    print(f"| {board[0]} | {board[1]} | {board[2]} |") 
    print("|---|---|---|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|---|---|---|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")

def update_board(board, location, symbole):
    if (board[location] == ' '):
        board[location] = symbole
        return True
    else:
        return False

def get_board_location(isPlayerOne):
    location = int(input(f"Player {1 if isPlayerOne else 2}: Select your field (1-9): "))
    if (location < 1 or location > 9):
        return None
    return location

def finish_game(board, filename, message):
    os.system('cls')
    draw_board(board)
    print(message)
    fh.delete(filename)
    time.sleep(5)