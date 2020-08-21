'''This module accompanies Cambridge International AS and A Level Computer Science Coursebook
by Sylvia Langfield and Dave Duddell (pdf downloadable for free from ???)

Ch12: Stepwise refinement and decomposing a problem into sub-tasks (procedure/function) p. 155 - 160
      Concept of a program module  function1...function2...mainfunction
      split the workload / maintenance / debugging
Ch14: Structured Programming p.212 - Functions and procedures

in pseudocode:
PROCEDURE <procedureIdentifier>()  // this is the procedure header
    <statement(s)>                // these statements are the procedure body
ENDPROCEDURE

CALL <procedureIdentifier>()

in Python:
void function must be defined before the main program; function is only called in the main program
when you want to execute the statements in the function
def my_function():
    name = input("Please enter your name")
    print(f"Your name is {name}")

#main function
my_function()
print("We welcome you as a student in computer science")


'''

#Task 14.01 (Implement the pseudocode from worked example 12.02 on p.159)
#review/update structured English and identifier table p.156-7
#review/update pseudocode (also code snippet REPEAT ... UNTIL to control inputs) p157
#for i in range(len(alist)))  /  for i in alist / for i, j in enumerate(alist)
#dir(alist)  /  alist.__dir__()  look for __iter__  --> for i in (iterable)



symb=input("Enter a symbol")
num=int(input("Enter an odd number, being the number of symbols in the base of the pyramid"))
symbstr=symb * num
emptystr=' ' * num
left=num//2
right = num//2 + 1

while left != 0:
    printstr = emptystr[:left] + symbstr[left:right] + emptystr[right:]
    print(printstr)
    left-=1
    right+=1


#print a hollow pyramid
symb=input("Enter a symbol")
num=int(input("Enter an odd number, being the number of symbols in the base of the pyramid"))
num_leading_spaces=num//2
print(' ' * num_leading_spaces + symb)
num_middle_spaces=0
num_leading_spaces-=1
while num_leading_spaces > 0:
    num_middle_spaces+=2
    print(' ' * num_leading_spaces + symb + ' ' * num_middle_spaces + symb)
    num_leading_spaces-=1
print(symb * num)


#Task 14.01  Print a pyramid 
#UNCOMMENT MAIN() TO RUN
def InputMaxNumberOfSymbols():
    global MaxNumberOfSymbols
    MaxNumberOfSymbols = 0
    while MaxNumberOfSymbols % 2 == 0:
        MaxNumberOfSymbols = int(input("Enter number of symbols: "))

def SetValues():
    global symbol, MaxNumberOfSymbols, NumberOfSpaces, NumberOfSymbols
    symbol = input("Enter a symbol: ")
    InputMaxNumberOfSymbols()
    NumberOfSpaces = int(((MaxNumberOfSymbols - 1) / 2) + 1)
    NumberOfSymbols =  1

def OutputSpacesAndSymbols():
    global NumberOfSpaces
    print(' ' * (NumberOfSpaces - len(str(symbol))) +  str(symbol * NumberOfSymbols))

def AdjustValueForNextRow():
    global NumberOfSpaces, NumberOfSymbols
    NumberOfSpaces -= 1
    NumberOfSymbols += 2
    
def main():
    SetValues()
    while NumberOfSymbols <= MaxNumberOfSymbols:
        OutputSpacesAndSymbols()
        AdjustValueForNextRow()
#main()


#Connect 4 Game
#UNCOMMENT MAIN TO RUN
import pprint

def InitialiseBoard(): 
    global Board
    Board = [["*" for column in (range(7))] for row in range(6)]

def SetUpGame():
    global ThisPlayer, GameFinished
    ThisPlayer = 'O'
    GameFinished = False

def OutputBoard():
        pprint.pprint(Board, width=40)

def ThisPlayerMakesMove():
    global ValidColumn, ValidRow, ThisPlayer
    ValidColumn = ThisPlayerChoosesColumn()
    ValidRow = FindNextFreePositionInColumn()
    Board[ValidRow][ValidColumn] = ThisPlayer

def ThisPlayerChoosesColumn():
    global ColumnNumber 
    boolResult = False
    print("It is ", ThisPlayer, "'s turn.")
    while boolResult == False:
        ColumnNumber = int(input("Please enter a valid column number: "))
        ColumnNumber -= 1
        boolResult = ColumnNumberValid()
    return ColumnNumber

def ColumnNumberValid():
    Valid = False
    if ColumnNumber >= 0 and ColumnNumber <= 6:
        if Board[0][ColumnNumber] == '*':
            Valid = True
    return Valid

def FindNextFreePositionInColumn():
    ThisRow = 5
    while Board[ThisRow][ValidColumn] != '*':
        ThisRow -= 1
    return ThisRow

def CheckIfThisPlayerHasWon():
    global GameFinished, WinnerFound
    WinnerFound = False
    CheckHorizontalLineInValidRow()
    if WinnerFound == False:
        CheckVerticalLineInValidColumn()
    if WinnerFound == False:
        CheckDiagonalLineInValidColumn()
    if WinnerFound == True:
        GameFinished = True
        print(ThisPlayer, " is the winner.")
    else:
        CheckForFullBoard()

def CheckDiagonalLineInValidColumn():
    global WinnerFound
    if ValidRow == 0 or ValidRow == 1 or ValidRow == 2:
        if ValidColumn == 0 or ValidColumn == 1 or ValidColumn == 2:     
            if Board[ValidRow][ValidColumn] == ThisPlayer and Board[ValidRow + 1][ValidColumn + 1] == ThisPlayer and\
                 Board[ValidRow + 2][ValidColumn + 2] == ThisPlayer and Board[ValidRow + 3][ValidColumn + 3] == ThisPlayer:
                WinnerFound = True
        elif ValidColumn == 4 or ValidColumn == 5 or ValidColumn == 6:
            if Board[ValidRow][ValidColumn] == ThisPlayer and Board[ValidRow + 1][ValidColumn - 1] == ThisPlayer and\
                 Board[ValidRow + 2][ValidColumn - 2] == ThisPlayer and Board[ValidRow + 3][ValidColumn - 3] == ThisPlayer:
                WinnerFound = True         
        elif ValidColumn == 3:
            if Board[ValidRow][ValidColumn] == ThisPlayer and Board[ValidRow + 1][ValidColumn + 1] == ThisPlayer and\
                 Board[ValidRow + 2][ValidColumn + 2] == ThisPlayer and Board[ValidRow + 3][ValidColumn + 3] == ThisPlayer or\
                      Board[ValidRow][ValidColumn] == ThisPlayer and Board[ValidRow + 1][ValidColumn - 1] == ThisPlayer and\
                           Board[ValidRow + 2][ValidColumn - 2] == ThisPlayer and Board[ValidRow + 3][ValidColumn - 3] == ThisPlayer:
                WinnerFound = True

    elif ValidRow == 3 or ValidRow == 4 or ValidRow == 5:
        if ValidColumn == 0 or ValidColumn == 1 or ValidColumn == 2:
            if Board[ValidRow][ValidColumn] == ThisPlayer and Board[ValidRow - 1][ValidColumn + 1] == ThisPlayer and\
                 Board[ValidRow - 2][ValidColumn + 2] == ThisPlayer and Board[ValidRow - 3][ValidColumn + 3] == ThisPlayer:
                WinnerFound = True
        elif ValidColumn == 4 or ValidColumn == 5 or ValidColumn == 6:
            if Board[ValidRow][ValidColumn] == ThisPlayer and Board[ValidRow - 1][ValidColumn - 1] == ThisPlayer and\
                 Board[ValidRow - 2][ValidColumn - 2] == ThisPlayer and Board[ValidRow - 3][ValidColumn - 3] == ThisPlayer:
                WinnerFound = True
        elif ValidColumn == 3:
            if Board[ValidRow][ValidColumn] == ThisPlayer and Board[ValidRow - 1][ValidColumn + 1] == ThisPlayer and\
                 Board[ValidRow - 2][ValidColumn + 2] == ThisPlayer and Board[ValidRow - 3][ValidColumn + 3] == ThisPlayer or\
                      Board[ValidRow][ValidColumn] == ThisPlayer and Board[ValidRow - 1][ValidColumn - 1] == ThisPlayer and\
                           Board[ValidRow - 2][ValidColumn - 2] == ThisPlayer and Board[ValidRow - 3][ValidColumn - 3] == ThisPlayer:
                WinnerFound = True

def CheckHorizontalLineInValidRow():
    global WinnerFound
    for i in range(0, 5):
        if Board[ValidRow][i] == ThisPlayer and\
             Board[ValidRow][i + 1] == ThisPlayer and\
                  Board[ValidRow][i + 2] == ThisPlayer and\
                       Board[ValidRow][i + 3] == ThisPlayer:
            WinnerFound = True
        
def CheckVerticalLineInValidColumn():
    global WinnerFound
    if ValidRow == 0 or ValidRow == 1 or ValidRow == 2:
        if Board[ValidRow][ValidColumn] == ThisPlayer and\
             Board[ValidRow + 1][ValidColumn] == ThisPlayer and\
                  Board[ValidRow + 2][ValidColumn] == ThisPlayer and\
                       Board[ValidRow + 3][ValidColumn] == ThisPlayer:
            WinnerFound = True

def CheckForFullBoard():
    global GameFinished
    BlankFound = False
    ThisRow = 0
    while ThisRow == 6 or BlankFound == False:
        ThisColumn = 0
        ThisRow += 1
        while ThisColumn == 7 or BlankFound == False:
            ThisColumn += 1
            if Board[ThisRow][ThisColumn] == '*':
                BlankFound = True
    if BlankFound == False:
        print("It is a draw")
        GameFinished = True
    
def SwapThisPlayer():
    global ThisPlayer
    if ThisPlayer == 'O':
        ThisPlayer = 'X'
    else:
        ThisPlayer = 'O'

# Main (connect 4)
"""Replay = 'Y'
while Replay == 'Y':
    InitialiseBoard()
    SetUpGame()
    OutputBoard()
    while GameFinished == False:
        ThisPlayerMakesMove()
        OutputBoard()
        CheckIfThisPlayerHasWon()
        if GameFinished == False:
            SwapThisPlayer()
    Replay = input("Want to play again? Y/N : ")"""



#Random Number Tally
#UNCOMMENT MAIN TO RUN
import random
import time

NoOfNos = 1000

def initialise_tally():
    global tally
    tally = []

def random_number_gen():
    global RandomList
    num_range = 20
    RandomList = random.choices(range(1,num_range + 1), k = NoOfNos)

def sort_list():
    global RandomList
    for passnum in range(len(RandomList)-1,0,-1):
        for i in range(passnum):
            if RandomList[i]>RandomList[i+1]:
                temp = RandomList[i]
                RandomList[i] = RandomList[i+1]
                RandomList[i+1] = temp

def update_tally():
    global tally
    RandomList.append(0)
    num = 1
    for i in range(NoOfNos):
        if RandomList[i] == RandomList[i+1]:
            num += 1
        else:
            percent = round(((num/NoOfNos) * 100), 1)
            tally.append(percent)
            num = 1

def output_tally():
    nums = [i for i in range(1,21)]
    print(nums)
    print(tally)

"""
initialise_tally()
random_number_gen()
print(time.process_time())
sort_list()
print(time.process_time())
update_tally()
output_tally()"""
