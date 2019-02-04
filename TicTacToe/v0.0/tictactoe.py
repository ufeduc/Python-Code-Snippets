# creator ufirat117

import sys

# getting input
def getInput():
    flag= True
    while flag:
        #making a right choice
        choiceFlag= True
        while choiceFlag:
            choice= input("X-O: ")
            if choice == 'X' or choice == 'x' or choice == 'O' or choice == 'o':
                choiceFlag= False
        #making a right position
        posFlag= True
        while posFlag:
            pos= input("what pos u want to make {}: ".format(choice.upper()))
            if pos in '123456789':
                posFlag= False
        #for the getting out of while loop
        if choiceFlag == False and posFlag == False:
            flag= False

    return choice.upper(), int(pos)

# table list
def creatingTableList(choice,pos,liste,counter,chaseList):
    flag= True
    while flag:
        if liste[pos] == ' ' and (choice != chaseList[counter-1]):
            liste.pop(pos) #erasing position for the choice
            liste.insert(pos,choice) #replace with choice
            chaseList.append(choice)
            flag= False

        else:
            print("u are cheater ~{}~ and u lose this game!!!".format(choice))
            sys.exit()

#create table
def table(liste):
    liste= liste
    print(" {} | {} | {} ".format(liste[1],liste[2],liste[3]))
    print("-----------")
    print(" {} | {} | {} ".format(liste[4],liste[5],liste[6]))
    print("-----------")
    print(" {} | {} | {} ".format(liste[7],liste[8],liste[9]))

#gameover function
def gameOver(choice):
    print("winner is {}".format(choice))
    print("Hope you enjoy!")

    flag= True
    while flag:
        yn= input("do you want to play again (Y-N)?: ")

        if yn[0] == 'Y' or yn[0] == 'y':
            flag= False
            tictactoe()
        elif yn[0] == 'N' or yn[0] == 'n':
            flag= False
            sys.exit()#exit console
        else:
            print("its just a yes or no question as you can see!!!")
            flag=True

def tictactoe():
    chaseList=['NONE']# for the cheaters :))
    counter=1
    liste=['NONE',' ',' ',' ',' ',' ',' ',' ',' ',' ','NONE']
    while counter<11:
        choice,pos= getInput()
        creatingTableList(choice,pos,liste,counter,chaseList)
        counter+=1
        table(liste)
        if (liste[1] == liste[2] == liste[3] == 'X' or\
            liste[1] == liste[2] == liste[3] == 'O' or\
            liste[1] == liste[4] == liste[7] == 'X' or\
            liste[1] == liste[4] == liste[7] == 'O' or\
            liste[1] == liste[5] == liste[9] == 'X' or\
            liste[1] == liste[5] == liste[9] == 'O' or\
            liste[4] == liste[5] == liste[6] == 'X' or\
            liste[4] == liste[5] == liste[6] == 'O' or\
            liste[7] == liste[8] == liste[9] == 'X' or\
            liste[7] == liste[8] == liste[9] == 'O' or\
            liste[3] == liste[6] == liste[9] == 'X' or\
            liste[3] == liste[6] == liste[9] == 'O' or\
            liste[3] == liste[5] == liste[7] == 'X' or\
            liste[3] == liste[5] == liste[7] == 'O' or\
            liste[2] == liste[5] == liste[8] == 'X' or\
            liste[2] == liste[5] == liste[8] == 'O'):
            gameOver(choice)

if __name__ == "__main__": tictactoe()
