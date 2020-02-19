from __future__ import print_function
from IPython.display import clear_output
import random 


def display_board(board):
    clear_output()
    print (board[1] +'|'+ board[2] +'|'+ board[3])
    print (board[4] +'|'+ board[5] +'|'+ board[6])
    print (board[7] +'|'+ board[8] +'|'+ board[9])
    

def player_input(marker):      
     marker = ''
     while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O?').upper()
     if marker == 'X':
      return ('X', 'O')
     else:
      return ('O', 'X')
        
def place_marker(board,marker,position):
    
    
    board[position] = marker

def winCheck(board, mark):
    
 if (board[7]  ==  board[8] ==  board[9] == mark) or \
        (board[4] ==  board[5] ==  board[6] == mark) or \
        (board[1] ==  board[2] ==  board[3] == mark) or \
        (board[7] ==  board[4] ==  board[1] == mark) or \
        (board[8] ==  board[5] ==  board[2] == mark) or \
        (board[9] ==  board[6] ==  board[3] == mark) or \
        (board[1] ==  board[5] ==  board[9] == mark) or \
        (board[3] ==  board[5] ==  board[7] == mark):
        return True
 else:
        return False
    
def boardSpaceAvailable(board , position):
    return board[position] == ' '
  
def fullBoard(board):
    for x in range(0,10):
        if boardSpaceAvailable(board, x) == ' ':
           return False
       
def startingPlayer():
    
    flip = random.randint(0,1)
    if (flip == 1):
        return 'Player 1 starts'
    else:
        return 'Player 2 starts'

def position_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not boardSpaceAvailable(board,position):
        position = int(input("chose a position(1 - 9)"))
        
    return position 

def replay():
    input("play again? Y or N)")
    choice = ' '
    return choice == 'Y'

print("Welcome to TicTacToe")

while True :
    the_board = [' ']*10
    player1_marker, player2_marker = player_input(" ")
    turn = startingPlayer()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(the_board)
            position = position_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if winCheck(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if fullBoard(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(the_board)
            position = position_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if winCheck(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if fullBoard(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
    
    
    


    
