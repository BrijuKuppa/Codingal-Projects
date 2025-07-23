import colorama
from colorama import init, Fore, Style
import random

init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()


def player_choice():
    choice = ""
    while choice not in ["X", "O"]:
        choice = input(f"\n{Fore.GREEN}Would you like to be 'X' or 'O'?").upper()
    if choice == "X":
        return ("X", "O")
    elif choice == "O":
        return ("O", "X")


def player_move(board, symbol):
    move = -1
    
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input(f"{Fore.CYAN}Chose a position on the board."))
            if move not in range(1, 10) or not board[move - 1].isdigit():
                print(f"{Fore.RED}That is an invalid input. Please try again.")
        except ValueError:
                print(f"{Fore.RED}That is an invalid input. Please try again.")
    board[move - 1] = symbol


def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if winning_cond(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if winning_cond(board_copy, player_symbol):
                board[i] = ai_symbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol


def winning_cond(board, symbol):
    win_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), 
    (0, 3, 6), (1, 4, 7), (2, 5, 8), 
    (0, 4, 8), (2, 4, 6)
    ]
    for i in win_conditions:
        if board[i[0]] == board[i[1]] == board[i[2]] == symbol:
            return True
    return False


def full(board):
    return all(not spot.isdigit() for spot in board)


def play():
    print(f"{Fore.LIGHTCYAN_EX}Welcome to Tik - Tak - Toe!")
    print(f"{Fore.GREEN}Here is how to play:")
    print(f"{Fore.YELLOW} - There are two players, and each person has to go once.\n - One person is 'X', and one person is 'O'. The 'X' will always go first.\n - To win the game, you have to get all the 'X' into a diagonal, horizontal, or vertical position.\n - You can't go the same place as someone else.")

    name = input(f"\n{Fore.YELLOW}First, enter your username. ")

    while True:
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        player_symbol, ai_symbol = player_choice()
        turn = "Player"
        game = True
    
        while game:
            display_board(board)
            if turn == "Player":
                player_move(board, player_symbol)
                if winning_cond(board, player_symbol):
                    display_board(board)
                    print(f"\n{Fore.GREEN}{name} has won the game!")
                    game = False
                else:
                    if full(board):
                        display_board(board)
                        print(f"\n{Fore.YELLOW}It is a tie!")
                        break
                    else:
                        turn = "AI"
            else:
                ai_move(board, ai_symbol, player_symbol)
                if winning_cond(board, ai_symbol):
                    print(f"\n{Fore.RED}AI has won the game.")
                    display_board(board)
                    game = False
                else:
                    if full(board):
                        display_board(board)
                        print(f"\n{Fore.YELLOW}It is a tie!")
                        break
                    else:
                        turn = "Player"
        repeat = input(f"{Fore.LIGHTYELLOW_EX}Do you want to play again?").lower()
        if repeat != "yes":
            print(f"{Fore.GREEN}See you later, {name}!")
            break

if __name__  == "__main__":
    play()
            