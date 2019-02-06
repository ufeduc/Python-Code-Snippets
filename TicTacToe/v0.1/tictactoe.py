# tictactoe v0.1 - ufirat117 - 2/7/2019 - 12:40 AM
import sys

def display(list):
    print(" {}  |  {}  |  {}".format(list[1], list[2], list[3]))
    print("---------------")
    print(" {}  |  {}  |  {}".format(list[4], list[5], list[6]))
    print("---------------")
    print(" {}  |  {}  |  {}".format(list[7], list[8], list[9]))

def get_input(xo):
    position = input("Which position would you like to make {} (1-9): ".format(xo))
    if position in "123456789":
        return int(position)
    else:
        print("{} is the cheater".format(xo))
        sys.exit()

def tictactoe():
    display_list = ["None", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    xo_list      = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

    for xo in xo_list:
        position_input = get_input(xo)
        if display_list[position_input] == " ":
            display_list.pop(position_input)
            display_list.insert(position_input, xo)

        elif display_list[position_input] != " ":
            print("{} is the cheater".format(xo))
            sys.exit()

        if display_list[1] == display_list[2] == display_list[3] and (display_list[1] == "X" or display_list[1] == "O") or\
           display_list[1] == display_list[5] == display_list[9] and (display_list[1] == "X" or display_list[1] == "O") or\
           display_list[1] == display_list[4] == display_list[7] and (display_list[1] == "X" or display_list[1] == "O") or\
           display_list[7] == display_list[5] == display_list[3] and (display_list[7] == "X" or display_list[7] == "O") or\
           display_list[7] == display_list[8] == display_list[9] and (display_list[7] == "X" or display_list[7] == "O") or\
           display_list[2] == display_list[5] == display_list[8] and (display_list[2] == "X" or display_list[2] == "O") or\
           display_list[3] == display_list[6] == display_list[9] and (display_list[3] == "X" or display_list[3] == "O") or\
           display_list[4] == display_list[5] == display_list[6] and (display_list[4] == "X" or display_list[4] == "O"):
            print("Well Done Winner is {}".format(xo))
            if input("Do You Wish To Play Again (Y-N): ").lower() == "y":
                tictactoe()
            print("Have a Nice Day!")
            sys.exit()

        display(display_list)

tictactoe()
