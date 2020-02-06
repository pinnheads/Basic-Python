# TICTACTOE 
# from IPython.display import clear_output
# 'clear_output()' works in juypter notebook


import random
import os

# Function to display the board
# Based on the numpad of a keyboard where the numbers represent the positions of a player's marker
 
def display_board(board): # Prints and update the board at each input from the player
    os.system('clear') # To clear the output screen each time a input is taken and show the updated table  
    print('_'+board[7]+'_|_'+board[8]+'_|_'+board[9]+'_')
    print('_'+board[4]+'_|_'+board[5]+'_|_'+board[6]+'_')
    print('_'+board[1]+'_|_'+board[2]+'_|_'+board[3]+'_')

# Function to take the player markers
def player_input(): # Player chooses his marker and the second player automatically gets the remaining marker

    marker = ''
   
    while marker != 'X' and marker != 'O':  
        marker=input("Player1 choose 'X' or 'O': ").upper()
        
        Player1_marker=marker
        
        if Player1_marker=='X': # If Player 1 chooses 'X' second player gets 'O'
            Player2_marker='O'
            return ('X','O') # For later use through tuple unpacking 
            
        else:
            Player2_marker='X' 
            return ('O','X') # For later use through tuple unpacking

# Function to place the marker
def place_marker(board, marker, position):

    board[position]=marker
    
    
# Function to check for a Win
def win_check(board, mark):

	# Checking Conditions in all directions
    if ((board[1]==board[2]==board[3]==mark) or 
    (board[4]==board[5]==board[6]==mark) or 
    (board[7]==board[8]==board[9]==mark) or 
    (board[1]==board[4]==board[7]==mark) or 
    (board[2]==board[5]==board[8]==mark) or 
    (board[3]==board[6]==board[9]==mark) or 
    (board[1]==board[5]==board[9]==mark) or 
    (board[3]==board[5]==board[7]==mark)):
        return True

# Function to select a random player to go first
def choose_first():
    if random.randint(1,2)==1:
        return 'Player1'
    else:
        return 'Player2'

# Function to check whether enetred position is empty or not
def space_check(board, position):
    
    if board[position]==' ':
        return True
    else: 
        return False
        
# Function to check for a draw
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Function to ask players for the position of the maker
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position
    
    
# ASK PLAYER WHETHER THEY WANNA PLAY AGAIN    
def replay():
    return input('Do you want to play again? Enter Yes or No: ').upper().startswith('Y')
    
    
# MAIN CODE    
print('Welcome to Tic Tac Toe!')

while True:
    # Basic Working
    The_board=[' ']*10 
    Player1_marker,Player2_marker=player_input() # To get the players markers and assign it to repective players through tuple unpacking
    
    turn=choose_first() # To choose a random player to go first
    print('{} will go first'.format(turn)) #prints which player will go first
    
    play_game=input('Are you ready to play the game: Enter YES or NO- ').upper() # Asks player if ready or not and starts the game if ready 
    if play_game=='YES':
        game_on=True
    else:
        game_on=False
        
    while game_on:
        
        if turn=='Player1': # Checks if it's player 1 turn 
        
            display_board(The_board) # Prints the empty board
            
            position=player_choice(The_board) # Takes the input of player 1 from the numpad
            
            place_marker(The_board, Player1_marker, position) # Places the marker of Player 1 on board 
            
            if(win_check(The_board,Player1_marker)): # Checks for a win
                display_board(The_board)
                print('Congratulations! Player 1 you have won the game!')
                game_on = False # Breaks out of the loop
                
            else:
            
                if full_board_check(The_board): # Checks for a draw
                    display_board(The_board)
                    print('The game is a draw!')
                    break
                    
                else:
                    turn='Player2' # Turn changes if none of the conditions above are satisfied
                    
        else:
            display_board(The_board) # Prints the empty board            
            
            position=player_choice(The_board) # Takes the input of player 1 from the numpad
            
            place_marker(The_board, Player2_marker, position) # Places the marker of Player 2 on board
            
            if(win_check(The_board,Player2_marker)):
                display_board(The_board)
                print('Congratulations! Player 2 you have won the game!')
                game_on = False
                
            else:
            
                if full_board_check(The_board):
                    display_board(The_board)
                    print('The game is a draw!')
                    break
                    
                else:
                    turn='Player1'
                    
    if not replay(): # Asks player it they want to play again and if input is no breaks out of the loop
        break
