import random


def display_board(board):
    print('\n ', board[0][0], " | ", board[0][1], " | ", board[0][2])
    print("-----------------")
    print(' ', board[1][0], " | ", board[1][1], " | ", board[1][2])
    print("-----------------")
    print(' ', board[2][0], " | ", board[2][1], " | ", board[2][2], '\n')


def get_player_input(board, player='your'):
    # Current player selects the position he want to choose. If the input is valid
    # (that position is not already occupied and it is on the table), the function
    # return the choosen position.
    option = [int(x) for x in input(f"It's {player} turn. Choose an position on the board (line, column): ").split()]
    if 1 <= option[0] <= 3 and 1 <= option[1] <= 3:
        if board[option[0] - 1][option[1] - 1] == "-":
            return (option[0] - 1) * 3 + option[1] - 1
        else:
            print("Oops, this position is already occupied.")
            return get_player_input(board, player)
    else:
        print("Oops, you entered an invalid position.")
        return get_player_input(board, player)


def check_win(board, player):
    # This function checks if the parameter player is the winner.
    for i in range(0, 3):
        # check horizontally
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # check vertically
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[2][0] == board[1][1] == board[0][2] == player:
        return True
    return False


def check_tie(board):
    # This function verifies if there is any empty space on the table and if the game could continue.
    if "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:
        return True
    return False


def switch_player(player):
    if player == "X":
        return "O"
    else:
        return "X"


def multi_player_mode(board):
    current_player = "X"
    game_running = True

    while game_running:
        display_board(board)
        inp = get_player_input(board, current_player)
        col_inp = inp % 3
        line_inp = inp // 3
        board[line_inp][col_inp] = current_player
        if check_win(board, current_player) is not False:
            game_running = False
            display_board(board)
            print(current_player, " is the WINNER!\n")
        if check_tie(board):
            game_running = False
            display_board(board)
            print("It's a tie!\n")
        current_player = switch_player(current_player)


def get_bot_move_easy(board):
    # The easy bot just randomly choose an empty position on board
    position = random.randint(0, 8)
    col_pos = position % 3
    line_pos = position // 3
    if board[line_pos][col_pos] == '-':
        return position
    else:
        return get_bot_move_easy(board)


def get_bot_move_medium(board, bot_player):
    # The medium bot checks if there is an empty winning position for it.
    # If there is not, it randomly chooses an empty position.
    for position in range(0, 9):
        col_pos = position % 3
        line_pos = position // 3
        if board[line_pos][col_pos] == '-':
            board[line_pos][col_pos] = bot_player
            if check_win(board, bot_player) is True:
                return position
            else:
                board[line_pos][col_pos] = '-'

    return get_bot_move_easy(board)


def get_bot_move_hard(board, bot_player):
    # The hard bot first checks if there is an empty winning position for it.
    # If there is not, then it checks if there is an empty winning position for the player to block it.
    # In the worst case, it randomly chooses an empty position.
    for position in range(0, 9):
        col_pos = position % 3
        line_pos = position // 3
        if board[line_pos][col_pos] == '-':
            board[line_pos][col_pos] = bot_player
            if check_win(board, bot_player) is True:
                return position
            else:
                board[line_pos][col_pos] = '-'

    for position in range(0, 9):
        col_pos = position % 3
        line_pos = position // 3
        if board[line_pos][col_pos] == '-':
            board[line_pos][col_pos] = 'X' if bot_player == 'O' else 'O'
            if check_win(board, 'X' if bot_player == 'O' else 'O') is True:
                return position
            else:
                board[line_pos][col_pos] = '-'

    return get_bot_move_easy(board)


def get_bot_difficulty():
    # The player selects the bot difficulty and the function verifies to be an valid input.
    bot_difficulty = input('Now you have to choose a difficulty for the bot (easy, medium, hard): ').lower()
    while bot_difficulty not in ('easy', 'medium', 'hard'):
        print('Oops, you entered an invalid difficulty')
        return get_bot_difficulty()
    print(f'\nYou selected to play with our {bot_difficulty} bot.')
    return bot_difficulty


def get_bot_move(board, difficulty, bot_player):
    # This function returns the position the bot is choosing based on the bot difficulty.
    if difficulty == 'easy':
        return get_bot_move_easy(board)
    elif difficulty == 'medium':
        return get_bot_move_medium(board, bot_player)
    else:
        return get_bot_move_hard(board, bot_player)


def single_player_mode(board):
    print('\nYou chose to play with our bot.')
    bot_difficulty = get_bot_difficulty()
    player = input('Now enter the symbol you would like to play with (X or O): ').upper()
    while player not in ('X', 'O'):
        print('Oops, you entered an invalid symbol.')
        player = input('Choose a symbol between X and O: ').upper()
    bot = 'X' if player == 'O' else 'O'
    display_board(board)

    while True:
        position = get_player_input(board)
        col_pos = position % 3
        line_pos = position // 3
        board[line_pos][col_pos] = player
        display_board(board)
        if check_win(board, player) is True:
            print('Hooray! You are the winner!\n')
            break
        elif check_tie(board) is True:
            print("It's a tie!")
            break

        print("Now it's bot's turn.")
        bot_move = get_bot_move(board, bot_difficulty, bot)
        col_pos = bot_move % 3
        line_pos = bot_move // 3
        board[line_pos][col_pos] = bot
        display_board(board)
        if check_win(board, bot) is True:
            print('Oof! The bot is the winner!\n')
            break
        elif check_tie(board) is True:
            print("It's a tie!")
            break


def main():
    game_board = [["-", "-", "-"],
                  ["-", "-", "-"],
                  ["-", "-", "-"]]
    print('\nWelcome to Tic Tac Toe!\n')
    print('You have to choose how you would like to play.')
    game_type = input('Enter B to play with our bot or F to play with your friend: ').lower()
    while game_type not in ('b', 'f'):
        print('Oops, you entered an invalid symbol')
        game_type = input('Enter B to play with out bot or F to play with your friend: ').lower()
    if game_type == 'f':
        multi_player_mode(game_board)
    else:
        single_player_mode(game_board)


if __name__ == '__main__':
    main()
