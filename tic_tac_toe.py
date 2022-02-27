import time
from os import system
import random


def create_board():
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
        board_state = {}
        board_size = player_input*player_input
        for number in range(board_size):
            number += 1
            board_state[number] = str(number)

        return board_state, player_input

def create_win_conditions(board_state, board_size):
    winning_list = []
    winning_set = []

    for value in board_state.values():
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

    return winning_list

def draw_board(board_state, board_size) :
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
        if len(board_state) - key < board_size:
            if print_counter < board_size:
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
            if print_counter >= board_size:
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
            if print_counter < board_size:
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
            if  print_counter >= board_size:
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

def are_you_winning(board_state, winning_list, board_size) :
    '''
    list: list of move the play has made
    return true if three in a row, else returns false
    '''
    win_counter_x = 0
    win_counter_o = 0

    for list in winning_list:
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
            if win_counter_x == board_size:
                return True
            if win_counter_o == board_size:
                return True
    return False

def print_win_or_draw(board_state, winning_list, board_size, draw_counter, player):
    if player == 1:
        x_o_message = 'X'
    if player == 2:
        x_o_message = 'O'
    if are_you_winning(board_state, winning_list, board_size) :
        draw_board(board_state, board_size)
        print(x_o_message, 'won!')
        input('Press Enter.')
        return exit()
    draw_counter +=1
    if draw_counter >= board_size * board_size:
        draw_board(board_state, board_size)
        print("it's a draw!")
        input('Press Enter.')
        return exit()
    return draw_counter

def is_valid_move(board_state, board_size, player):
    if player == 1:
        x_o_message = 'X'
    if player == 2:
        x_o_message = 'O'
    draw_board(board_state, board_size)
    print()
    while True:
        print("Player", str(player) + "'s Turn")
        player_input = input('Select a space for ' + x_o_message + ':')
        if player_input.lower() in ('exit', 'quit'):
            return exit()
        try:
            player_input = int(player_input)
        except:
            draw_board(board_state, board_size)
            print('Not a valid space for', x_o_message)
            continue
        if player_input not in board_state.keys() or board_state[player_input] in ('X', 'O'):
            draw_board(board_state, board_size)
            print('Not a valid space for', x_o_message)
            continue
        return player_input

def is_random_move(board_state, board_size, player):
    if player == 1:
        x_o_message = 'X'
    if player == 2:
        x_o_message = 'O'
    draw_board(board_state, board_size)
    print()
    while True:
        print("Player", str(player) + "'s Turn")
        print('Select a space for ' + x_o_message + ':')
        print('Player', str(player), 'is thinking...')
        time.sleep(1)
        while True:
            player_input = random.choice(range(1, board_size*board_size + 1))
            if board_state[player_input] in ('X', 'O'):
                continue
            draw_board(board_state, board_size)
            print()
            print("Player", str(player) + "'s Turn")
            print('Select a space for ' + x_o_message + ':', player_input)
            time.sleep(0.5)
            break
        return player_input



def hard_pick(board_state, board_size) :
    if board_size == 3:
        if board_state[5] not in ('X', 'O'):
            return '5'
        elif '5' in x_space :
            if '1' in x_space and '9' not in o_space :
                return '9'
            elif '2' in x_space and '8' not in o_space :
                return '8'
            elif '3' in x_space and '7' not in o_space :
                return '7'
            elif '4' in x_space and '6' not in o_space :
                return '6'
            elif '6' in x_space and '4' not in o_space :
                return '4'
            elif '7' in x_space and '3' not in o_space :
                return '3'
            elif '8' in x_space and '2' not in o_space :
                return '2'
            elif '9' in x_space and '1' not in o_space :
                return '1'
        elif '5' in o_space :
            if '1' in x_space and '2' in x_space and '3' not in o_space :
                return '3'
            elif '2' in x_space and '3' in x_space and '1' not in o_space :
                return '1'
            elif '1' in x_space and '3' in x_space and '2' not in o_space :
                return '2'
            elif '1' in x_space and '4' in x_space and '7' not in o_space :
                return '7'
            elif '4' in x_space and '7' in x_space and '1' not in o_space :
                return '1'
            elif '1' in x_space and '7' in x_space and '4' not in o_space :
                return '4'
            elif '3' in x_space and '6' in x_space and '9' not in o_space :
                return '9'
            elif '6' in x_space and '9' in x_space and '3' not in o_space :
                return '3'
            elif '3' in x_space and '9' in x_space and '6' not in o_space :
                return '6'
            elif '7' in x_space and '8' in x_space and '9' not in o_space :
                return '9'
            elif '8' in x_space and '9' in x_space and '7' not in o_space :
                return '7'
            elif '7' in x_space and '9' in x_space and '8' not in o_space :
                return '8'
        return random.choice(space_left)


def main_menu() :
    system('cls')
    print('Welcome to Tic-Tac_Toe!')
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
            system('cls')
            print('Welcome to Tic-Tac_Toe!')
            print('1. 1 Player')
            print('2. 2 Player')
            print('3. Quit')
            return None
        else:
            system('cls')
            print('Select a difficulty or go back')
            print('1. Easy')
            print('2. Hard')
            print('3. Back')
            print('Invalid Input')
            continue

def play_game() :
    board_state, board_size = create_board()
    winning_list = create_win_conditions(board_state, board_size)
    draw_counter = 0

    while True:
        x_move = is_valid_move(board_state, board_size, 1)
        board_state[int(x_move)] = 'X'
        draw_counter = print_win_or_draw(board_state, winning_list, board_size, draw_counter, 1)

        o_move = is_valid_move(board_state, board_size, 2)
        board_state[int(o_move)] = 'O'
        draw_counter = print_win_or_draw(board_state, winning_list, board_size, draw_counter, 2)

    exit()


def play_game_easy() :
    board_state, board_size = create_board()
    winning_list = create_win_conditions(board_state, board_size)
    draw_counter = 0

    while True:
        x_move = is_valid_move(board_state, board_size, 1)
        board_state[int(x_move)] = 'X'
        draw_counter = print_win_or_draw(board_state, winning_list, board_size, draw_counter, 1)

        o_move = is_random_move(board_state, board_size, 2)
        board_state[int(o_move)] = 'O'
        draw_counter = print_win_or_draw(board_state, winning_list, board_size, draw_counter, 2)

    exit()

def play_game_hard() :
    valid_spaces = '123456789'
    x_space = []
    o_space = []
    board_state = {1:'1' , 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    draw_counter = 9
    space_left = ['1','2','3','4','5','6','7','8','9']
    system('cls')
    draw_board(board_state)
    print()
    while draw_counter > 0 :
        while draw_counter > 0 :
            print("Player 1's Turn")
            x_input = input('Select a space for X: ')
            if x_input not in valid_spaces or x_input in x_space + o_space :
                system('cls')
                draw_board(board_state)
                print('Not a valid space for X')
                continue
            system('cls')
            x_space.append(x_input)
            space_left.remove(x_input)
            board_state[int(x_input)] = 'X'
            draw_board(board_state)
            break
        if are_you_winning(x_space) :
            print()
            print('X won!')
            break
        else:
            draw_counter -= 1
            print()
        while draw_counter > 0 :
            print("Player 2 is thinking")
            o_input = hard_pick(x_space, o_space, space_left)
            if o_input not in valid_spaces or o_input in x_space + o_space :
                system('cls')
                draw_board(board_state)
                print('Not a valid space for O')
                print(o_input)
                print(space_left)
                print(x_space)
                print(o_space)
                time.sleep(5)
                continue
            time.sleep(1)
            system('cls')
            o_space.append(o_input)
            space_left.remove(o_input)
            board_state[int(o_input)] = 'O'
            draw_board(board_state)
            break
        if are_you_winning(o_space) :
            print('O won!')
            break
        elif draw_counter > 0:
            draw_counter -= 1
            print()
    if draw_counter <= 0 :
        print("it's a draw!")
    input('Press Enter.')
    exit()









if __name__ == '__main__' :
    main_menu()
