import os
import time
import filehandling as fh
import gamelogic as gl

def game(filename, isLoaded):
    isPlayerOne = True
    board = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
    
    # load game
    if isLoaded:
        load = fh.load(filename)
        if (load is None):
            os.system('cls')
            print('No saved game')
            time.sleep(2)
            return 
        board = load['board']
        isPlayerOne = load['isPlayerOne']
    
    while (True):
        # draw the board to the screen 
        gl.draw_board(board)

        try:
            # get field location from the player 
            location = gl.get_board_location(isPlayerOne)
            if (location is None):
                continue
        except (IOError, ValueError):
            continue
        except KeyboardInterrupt:
            saving = input('Do you want to save the game (y/n)? ')
            if saving == 'y':
                fh.save(filename, {"board": board, "isPlayerOne": isPlayerOne})
            break
        
        # get the symbole for the current player 
        symbole = 'X' if isPlayerOne else 'O'
        
        # update the game board 
        if (not gl.update_board(board, location - 1, symbole)):
            continue
        
        # check if game is a draw 
        if (gl.check_draw(board)):
            gl.finish_game(board, filename, "It is a draw")
            break
        
        # check if current player has won 
        if (gl.check_win(board, symbole)):
            gl.finish_game(board, filename, f"Player {1 if isPlayerOne else 2} has won the game")
            break
            
        # change current player 
        isPlayerOne = not isPlayerOne
        
def main():
    filename = 'game.json'
    
    while(True):
        os.system('cls')
        print('(1) New game')
        print('(2) Load game')
        print('(3) Quit')
        
        choice = int(input('What do you want to do? '))
        if (choice == 1):
            game(filename, False)
        elif(choice == 2):
            game(filename, True)
        elif (choice == 3):
            break
    
if __name__ == '__main__':
    main()