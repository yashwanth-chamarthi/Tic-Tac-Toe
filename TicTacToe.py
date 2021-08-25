import random

def tic_tac_toe():

    def display_board(board):   # prints board format 
        print('\n'*100)
        print(board[1],'|',board[2],'|',board[3])
        print('---------')
        print(board[4],'|',board[5],'|',board[6])
        print('---------')
        print(board[7],'|',board[8],'|',board[9])
        pass

    def player_input():   # takes player input
        marker=''
        while marker not in ('x','o'):
            marker=input('please select x or o\t:')
        
        if marker == 'x':
            return ('x','o')
        else:
            return ('o','x')

    def place_marker(board, marker, position):  # places marker at the given position in the board
        board[position]=marker

    def win_check(board, mark):  # check the board if anyone has won already 
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
        (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
        (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
        (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
        (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
        (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
        (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
        (board[9] == mark and board[5] == mark and board[1] == mark))


    def choose_first():   # returns randomly which player goes first
        if random.randint(0,1)==0:
            return 'player 2'
        else:
            return 'player 1'

    def space_check(board, position):  # checks if the given position is empty or not
        return board[position]==' '
 
    def full_board_check(board):  # checks if the board is full or not
        for n in range(1,10):
            if space_check(board,n):
                return False
        return True

    def player_choice(board):  # takes the position given by the player
        position = 0
        while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
            position = int(input('enter a value in (0-9): '))
        return position

    def replay():   #checks for replay
        game=''
        while game not in ('y','n'):  
            game=input('do you want to continue playing y or n')
            if game=='y':
                return True
            else:
                return False
        pass

    while True:  
        the_board=[' ']*10
        player1_marker,player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first')
        play_game = input('Are you ready to play? Enter Yes or No.')
        if play_game =='Yes' or 'yes':
            game_on = True
        else:
            game_on = False
        while game_on:
            if turn =='player 1':
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,player1_marker,position)
                if win_check(the_board,player1_marker):
                    display_board(the_board)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'player 2'
            else:
                display_board(the_board)
                position = player_choice(the_board)
                place_marker(the_board,player2_marker, position)

                if win_check(the_board,player2_marker):
                    display_board(the_board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'player 1'
        if not replay():
            break

tic_tac_toe()              