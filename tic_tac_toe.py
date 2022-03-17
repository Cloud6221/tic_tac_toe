import time
from os import system
import random


def create_board():
    '''
    Description:


    Parameters:


    Returns:


    '''
    system('cls')
    while True:
        player_input = input('Select a board size (3-20):')
        try:
            player_input = int(player_input)
        except:
            system('cls')
            print('Not a valid board size.')
            continue
        if player_input not in range(3,21):
            system('cls')
            print('Not a valid board size.')
            continue
        board_size = player_input**2
        board_state = {'board_size':player_input, 'draw_counter':board_size}
        for number in range(board_size):
            number += 1
            board_state[number] = str(number)
        board_state = create_win_conditions(board_state)

        return board_state

def create_win_conditions(board_state):
    '''
    Description:


    Parameters:


    Returns:


    '''
    winning_list = []
    winning_set = []
    board_size = board_state['board_size']

    for key, value in board_state.items():
        if key == 'board_size' or key == 'draw_counter':
            continue
        winning_set.append(value)
        if len(winning_set) == board_size:
            winning_list.append(winning_set)
            winning_set = []

    copy_winning_list = winning_list.copy()

    for index_set in range(board_size):
        for item in copy_winning_list:
            winning_set.append(item[index_set])
        winning_list.append(winning_set)
        winning_set = []

    for item in copy_winning_list:
        winning_set.append(item[copy_winning_list.index(item)])
    winning_list.append(winning_set)
    winning_set = []

    for item in copy_winning_list:
        board_size -= 1
        winning_set.append(item[board_size])
    winning_list.append(winning_set)

    board_state['winning_list'] = winning_list

    return board_state

def draw_board(board_state) :
    '''
    Description:


    Parameters:


    Returns:


    '''
    '''
    dict: The dictionary of the current board statement
    Returns a print of the board.
    dict: dictionary
    return: print of print of board
    '''
    print_counter = 1
    system('cls')
    print()
    print('  ', end='')
    for key, value in board_state.items():
        if key == 'board_size' or key == 'draw_counter' or key == 'winning_list':
            continue
        if board_state['board_size']**2 - key < board_state['board_size']:
            if print_counter < board_state['board_size']:
                if key <= 9 or value in ('X', 'O'):
                    print('  '+value+'  |', end='')
                    print_counter +=1
                    continue
                if key >= 10 and key <= 99:
                    print(' '+value+'  |', end='')
                    print_counter +=1
                    continue
                if key >= 100:
                    print(' '+value+' |', end='')
                    print_counter +=1
                    continue
            if print_counter >= board_state['board_size']:
                if key <= 9 or value in ('X', 'O'):
                    print('  '+value+'  ')
                    print_counter = 1
                    print('  ', end='')
                    continue
                if key >= 10 and key <= 99:
                    print(' '+value+'  ')
                    print_counter = 1
                    print('  ', end='')
                    continue
                if key >= 100:
                    print(' '+value+' ')
                    print_counter = 1
                    print('  ', end='')
                    continue
        else:
            if print_counter < board_state['board_size']:
                if key <= 9 or value in ('X', 'O'):
                    print('__'+value+'__|', end='')
                    print_counter +=1
                    continue
                if key >= 10 and key <= 99:
                    print('_'+value+'__|', end='')
                    print_counter +=1
                    continue
                if key >= 100:
                    print('_'+value+'_|', end='')
                    print_counter +=1
                    continue
            if  print_counter >= board_state['board_size']:
                if key <= 9 or value in ('X', 'O'):
                    print('__'+value+'__')
                    print_counter = 1
                    print('  ', end='')
                    continue
                if key >= 10 and key <= 99:
                    print('_'+value+'__')
                    print_counter = 1
                    print('  ', end='')
                    continue
                if key >= 100:
                    print('_'+value+'_')
                    print_counter = 1
                    print('  ', end='')
                    continue
    print()

def are_you_winning(board_state) :
    '''
    Description:


    Parameters:


    Returns:


    '''
    '''
    list: list of move the play has made
    return true if three in a row, else returns false
    '''
    win_counter_x = 0
    win_counter_o = 0

    for list in board_state['winning_list']:
        win_counter_x = 0
        win_counter_o = 0
        for item in list:
            item = int(item)
            if board_state[item] == 'X':
                win_counter_x += 1
                win_counter_o = 0
            if board_state[item] == 'O':
                win_counter_o += 1
                win_counter_x = 0
            if win_counter_x == board_state['board_size']:
                return True
            if win_counter_o == board_state['board_size']:
                return True
    return False

def print_win_or_draw(board_state, player):
    '''
    Description:


    Parameters:


    Returns:


    '''
    if player == 1:
        x_o_message = 'X'
    if player == 2:
        x_o_message = 'O'
    if are_you_winning(board_state) :
        draw_board(board_state)
        print(x_o_message, 'won!')
        input('Press Enter.')
        return exit()
    board_state['draw_counter'] -=1
    if board_state['draw_counter'] <= 0:
        draw_board(board_state)
        print("It's a draw!")
        input('Press Enter.')
        return exit()
    return None

def is_last_move(board_state):
    moves_left = []
    for index in range(1,board_state['board_size']**2 + 1):
        if board_state[index] in ('X', 'O'):
            continue
        else:
            moves_left.append(index)
    return moves_left


def is_valid_move(board_state, player):
    '''
    Description:


    Parameters:


    Returns:


    '''
    if player == 1:
        x_o_message = 'X'
    if player == 2:
        x_o_message = 'O'
    draw_board(board_state)
    print()
    while True:
        print("Player", str(player) + "'s Turn")
        player_input = is_last_move(board_state)
        if len(player_input) == 1:
            return int(player_input[0])
        else:
            player_input = input('Select a space for ' + x_o_message + ':')
        if player_input.lower() in ('exit', 'quit'):
            return exit()
        try:
            player_input = int(player_input)
        except:
            draw_board(board_state)
            print('Not a valid space for', x_o_message)
            continue
        if player_input not in board_state.keys() or board_state[player_input] in ('X', 'O'):
            draw_board(board_state)
            print('Not a valid space for', x_o_message)
            continue
        return player_input

def is_random_move(board_state, player):
    '''
    Description:


    Parameters:


    Returns:


    '''
    if player == 1:
        x_o_message = 'X'
    if player == 2:
        x_o_message = 'O'
    draw_board(board_state)
    print()
    while True:
        print("Player", str(player) + "'s Turn")
        print('Select a space for ' + x_o_message + ':')
        print('Player', str(player), 'is thinking...')
        time.sleep(1)
        while True:
            player_input = random.choice(range(1, board_state['board_size']**2 + 1))
            if board_state[player_input] in ('X', 'O'):
                continue
            draw_board(board_state)
            print()
            print("Player", str(player) + "'s Turn")
            print('Select a space for ' + x_o_message + ':', player_input)
            time.sleep(0.5)
            break
        return player_input



def is_hard_move(board_state, player) :
    '''
    Description:


    Parameters:


    Returns:


    '''
    if player == 1:
        x_o_message = 'X'
    if player == 2:
        x_o_message = 'O'
    draw_board(board_state)
    print()
    print("Player", str(player) + "'s Turn")
    print('Select a space for ' + x_o_message + ':')
    print('Player', str(player), 'is thinking...')
    time.sleep(1)
    if board_state['board_size'] == 3:
        if board_state[5] not in ('X', 'O'):
            return '5'
        elif board_state[5] in ('X'):
            if board_state[1] in ('X') and board_state[9] not in ('O'):
                return '9'
            elif board_state[2] in ('X') and board_state[8] not in ('O'):
                return '8'
            elif board_state[3] in ('X') and board_state[7] not in ('O'):
                return '7'
            elif board_state[4] in ('X') and board_state[6] not in ('O'):
                return '6'
            elif board_state[6] in ('X') and board_state[4] not in ('O'):
                return '4'
            elif board_state[7] in ('X') and board_state[3] not in ('O'):
                return '3'
            elif board_state[8] in ('X') and board_state[2] not in ('O'):
                return '2'
            elif board_state[9] in ('X') and board_state[1] not in ('O'):
                return '1'
        elif board_state[5] in ('O'):
            if board_state[1] in ('X') and board_state[2] in ('X') and board_state[3] not in ('O'):
                return '3'
            elif board_state[2] in ('X') and board_state[2] in ('X') and board_state[1] not in ('O'):
                return '1'
            elif board_state[1] in ('X') and board_state[3] in ('X') and board_state[2] not in ('O'):
                return '2'
            elif board_state[1] in ('X') and board_state[4] in ('X') and board_state[7] not in ('O'):
                return '7'
            elif board_state[4] in ('X') and board_state[7] in ('X') and board_state[1] not in ('O'):
                return '1'
            elif board_state[1] in ('X') and board_state[7] in ('X') and board_state[4] not in ('O'):
                return '4'
            elif board_state[3] in ('X') and board_state[6] in ('X') and board_state[9] not in ('O'):
                return '9'
            elif board_state[6] in ('X') and board_state[9] in ('X') and board_state[3] not in ('O'):
                return '3'
            elif board_state[3] in ('X') and board_state[9] in ('X') and board_state[6] not in ('O'):
                return '6'
            elif board_state[7] in ('X') and board_state[8] in ('X') and board_state[9] not in ('O'):
                return '9'
            elif board_state[8] in ('X') and board_state[9] in ('X') and board_state[7] not in ('O'):
                return '7'
            elif board_state[7] in ('X') and board_state[9] in ('X') and board_state[8] not in ('O'):
                return '8'
        while True:
            player_input = random.choice(range(1, board_state['board_size']**2 + 1))
            if board_state[player_input] in ('X', 'O'):
                continue
            return player_input


def main_menu() :
    '''
    Description:


    Parameters:


    Returns:


    '''
    system('cls')
    print('Welcome to Tic-Tac-Toe!')
    print('1. 1 Player')
    print('2. 2 Player')
    print('3. Quit')
    while True :
        player_input = input('Select an option: ')
        if player_input.lower() in ('1', '1.', '1 player'):
            sub_menu_1_player()
            continue
        elif player_input.lower() in ('2', '2.', '2 player'):
            play_game()
        elif player_input.lower() in ('3', '3.', 'exit', 'quit'):
            system('cls')
            print('Good-Bye')
            exit()
        else:
            system('cls')
            print('Welcome to Tic-Tac_Toe!')
            print('1. 1 Player')
            print('2. 2 Player')
            print('3. Quit')
            print('Invalid Input')
            continue

def sub_menu_1_player():
    '''
    Description:


    Parameters:


    Returns:


    '''
    system('cls')
    print('Select a difficulty or go back')
    print('1. Easy')
    print('2. Hard')
    print('3. Back')
    while 1 :
        player_input = input('Select an option:')
        if player_input.lower() in ('1', '1.', 'easy'):
            play_game_easy()
        elif player_input.lower() in ('2', '2.', 'hard'):
            play_game_hard()
        elif player_input.lower() in ('3', '3.', 'back'):
            return main_menu()
        else:
            system('cls')
            print('Select a difficulty or go back')
            print('1. Easy')
            print('2. Hard')
            print('3. Back')
            print('Invalid Input')
            continue

def play_game():
    '''
    Description:


    Parameters:


    Returns:


    '''
    board_state = create_board()

    while True:
        #x_move = is_valid_move(board_state, 1)
        board_state[int(is_valid_move(board_state, 1))] = 'X'
        print_win_or_draw(board_state, 1)

        #o_move = is_valid_move(board_state, 2)
        board_state[int(is_valid_move(board_state, 2))] = 'O'
        print_win_or_draw(board_state, 2)

    exit()


def play_game_easy():
    '''
    Description:


    Parameters:


    Returns:


    '''
    board_state = create_board()

    while True:
        #x_move = is_valid_move(board_state, 1)
        board_state[int(is_valid_move(board_state, 1))] = 'X'
        print_win_or_draw(board_state, 1)

        #o_move = is_random_move(board_state, 2)
        board_state[int(is_random_move(board_state, 2))] = 'O'
        print_win_or_draw(board_state, 2)

    exit()

def play_game_hard():
    '''
    Description:


    Parameters:


    Returns:


    '''
    board_state = {'board_size':3, 'draw_counter':9, 1:'1' , 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    board_state = create_win_conditions(board_state)

    while True:
        board_state[int(is_valid_move(board_state, 1))] = 'X'
        print_win_or_draw(board_state, 1)

        board_state[int(is_hard_move(board_state, 2))] = 'O'
        print_win_or_draw(board_state, 2)

    exit()









if __name__ == '__main__' :
    main_menu()
