from colorama import Fore, Style
import colorama

colorama.init(autoreset=True)

board = {
    '7': ' ' , '8': ' ' , '9': ' ' ,
    '4': ' ' , '5': ' ' , '6': ' ' ,
    '1': ' ' , '2': ' ' , '3': ' ' 
}

board_keys = []

print(f"{Fore.BLUE}Welcome to, Tic-Tac-Toe!\n")
print(f"{Fore.GREEN}Here is how to play:")
print(f"{Fore.YELLOW} - There are two players, and each person has to go once.\n - One person is 'X', and one person is 'O'. The 'X' will always go first.\n - To win the game, you have to get all the 'X' into a diagonal, horizontal, or vertical position.\n - You can't go the same place as someone else.")

for i in board:
    board_keys.append(i)

def printboard():
    print(f"\n")
    print(board['7'] + " " + " " + " " + '|' + board['8'] + " " + " " + " " + '|' + board['9'])
    print('----+----+----')
    print(board['4'] + " " + " " + " " + '|' + board['5'] + " " + " " + " " + '|' + board['6'])
    print('----+----+----')
    print(board['1'] + " " + " " + " " + '|' + board['2'] + " " + " " + " " + '|' + board['3'])
    print(f"\n")

def game():
    turn = "X"
    count = 0

    for i in range(10):
        printboard()

        move = input(f"{Fore.CYAN}It is '{turn}'s turn! Where would it like to go? (Enter a number 1-9)")

        if board[move] == ' ':
            board[move] = turn
            printboard
            count += 1
        
        else:
            print(f"{Fore.RED}That place has been taken. Please chose an empty area on the board.")
            continue

        if count >= 5:
            if board["7"] == board["8"] == board["9"] != " ":
                print(f"{Fore.GREEN}Nice, {turn} has won the game!")
                printboard
                break 
            elif board["4"] == board["5"] == board["6"] != " ":
                print(f"{Fore.GREEN}Nice, {turn} has won the game!")
                printboard
                break
            elif board["1"] == board["2"] == board["3"] != " ":
                print(f"{Fore.GREEN}Nice, {turn} has won the game!")
                printboard
                break
            elif board["1"] == board["4"] == board["7"] != " ":
                print(f"{Fore.GREEN}Nice, {turn} has won the game!")
                printboard
                break
            elif board["2"] == board["5"] == board["8"] != " ":
                print(f"{Fore.GREEN}Nice, {turn} has won the game!")
                printboard
                break
            elif board["3"] == board["6"] == board["9"] != " ":
                print(f"{Fore.GREEN}Nice, {turn} has won the game!")
                printboard
                break
            elif board["7"] == board["5"] == board["3"] != " ":
                print(f"{Fore.GREEN}Nice, {turn} has won the game!")
                printboard
                break
            elif board["1"] == board["5"] == board["9"] != " ":
                print(f"{Fore.GREEN}Nice, {turn} has won the game!")
                printboard
                break

        if count == 9:
            print(f"{Fore.YELLOW}Oh! Seems like the game is a tie. Starting the game again...")
            for key in board_keys:
                board[key] = " "
            game()

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart = input(f"{Fore.RED}Would you like to start over?").lower().strip()
    if restart == "yes":
        for key in board_keys:
            board[key] = " "

        print(f"{Fore.GREEN}Okay! Starting the game again...")
        game()
    elif restart == "no":
        print(f"{Fore.RED}Alright! Exiting application...")
    else:
        print(f"{Fore.RED}I didn't quite understand that. Exiting application...")

if __name__ == "__main__":
    game()