import os
import colorama
from time import sleep


def draw_board(positions):
    board = (f"|{positions[1]}|{positions[2]}|{positions[3]}|\n"
             f"|{positions[4]}|{positions[5]}|{positions[6]}|\n"
             f"|{positions[7]}|{positions[8]}|{positions[9]}|")
    print(colorama.Fore.LIGHTWHITE_EX + board)


def check_turn(trn):
    if trn % 2 == 0:
        trn = "X"
    else:
        trn = "O"
    return trn


def check_win(position):
    # Horizontal cases
    if (positions[1] == positions[2] == positions[3]) \
            or (positions[4] == positions[5] == positions[6]) \
            or (positions[7] == position[8] == positions[9]):
        return True
    # Vertical cases
    elif (positions[1] == positions[4] == positions[7]) \
            or (positions[2] == positions[5] == positions[8]) \
            or (positions[3] == position[6] == positions[9]):
        return True
    # Diagonal cases
    elif (positions[1] == positions[5] == positions[9]) \
            or (positions[3] == positions[5] == positions[7]):
        return True
    return False


positions = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
play = True
finished = False
turn = 0

while play:
    os.system("cls")
    draw_board(positions)

    # Announce winner and restart game
    if finished:
        sleep(0.5)
        if check_turn(turn) == "O":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
        while True:
            restart = str(input(colorama.Fore.LIGHTWHITE_EX + "Play again?: (y / n): "))
            if restart == "y" or restart == "Y":
                positions = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
                os.system("cls")
                draw_board(positions)
                turn = 0
                finished = False
                break
            elif restart == "n" or restart == "N":
                print("Goodbye!")
                exit()
            else:
                print(colorama.Fore.RED + "Invalid option, please confirm your choice.")
                continue

    # Get input for player choice
    sleep(0.5)
    p_choice = input(f"Player {str(turn % 2 + 1)}'s turn\nMake your choice: ")

    # Game logic for taking turns
    if str.isdigit(p_choice) and int(p_choice) in positions:
        if not positions[int(p_choice)] in {"X", "O"}:
            positions[int(p_choice)] = check_turn(turn)
            turn += 1

        else:
            print("This position is already marked! Please try again")
            sleep(1.5)

    else:
        print("Invalid choice! Please input an available number [1-9]")
        sleep(1.5)

    # Check if there is a winner and game finished
    if check_win(positions):
        finished = True

# draw the board one last time after game is finished
os.system("cls")
draw_board(positions)

