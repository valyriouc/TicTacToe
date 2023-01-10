import os

board = [
    ' ', ' ', ' ',
    ' ', ' ', ' ',
    ' ', ' ', ' '
]

def draw_board():
    os.system('cls')
    print(f"| {board[0]} | {board[1]} | {board[2]} |") 
    print("|---|---|---|")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("|---|---|---|")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")

def update_board(location, symbole):
    if (board[location] == ' '):
        board[location] = symbole

def check_board(symbole):
    if ((board[0] == symbole and board[1] == symbole and board[2] == symbole) or 
        (board[3] == symbole and board[4] == symbole and board[5] == symbole) or 
        (board[6] == symbole and board[7] == symbole and board[8] == symbole) or 
        (board[0] == symbole and board[3] == symbole and board[6] == symbole) or 
        (board[1] == symbole and board[4] == symbole and board[7] == symbole) or
        (board[2] == symbole and board[5] == symbole and board[8] == symbole) or
        (board[0] == symbole and board[4] == symbole and board[8] == symbole) or 
        (board[6] == symbole and board[4] == symbole and board[2] == symbole)):
        return True
    else:
        return False
        
def main():
    isPlayerOne = True
    while(True):
        draw_board()
        try: 
            number = int(input('Where do you want to place your symbole(1-9): '))
            if (number < 1 or number > 9):
                continue
            
            symbole = 'X' if isPlayerOne else 'O'
            update_board(number - 1, symbole)
            
            if (check_board(symbole)):
                draw_board()
                print(f"Player {1 if isPlayerOne else 0} has won the game")
                break
            isPlayerOne = not isPlayerOne
        except IOError:
            continue
    
if __name__ == '__main__':
    main()