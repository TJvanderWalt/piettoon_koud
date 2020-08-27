'''This module accompanies Cambridge International AS and A Level Computer Science Coursebook
by Sylvia Langfield and Dave Duddell (pdf downloadable for free from www.gceguide.xyz)

Ch12: Stepwise refinement : break bigger problem into smaller, more detailed steps tp produce a 
        solution in terms of the four basic constructs: sequence, assignment, selection and
        repetition  p.155-158

      Modular design : break bigger problem into sub-tasks (procedure/function), leading to the    
         concept of program modules  function1...function2...mainProgram ; 
         procedure: sequence of steps that is given an identifier and can be called to perform a sub-task;
         function: sequence of steps that is given an identifier and returns a (single) value; the function
                   call is part of an expression or assignment;
         local variables are accessible only in the (single) module in which they are declared/initialised;
         global variables are accessible from all modules (throughout the solution); p.159-167
         
         structure charts gives a graphical representation of the modular structure of a solution, showing the
                   interrelations between sub-tasks and the parameters (values passed) between a calling module
                   and the model being called. From the structure charts, the equivalent pseudocode can be derived p.167-171

Ch14: Structured Programming - Functions and procedures  p.212
      passing parameters by reference: args are updated in-place
      passing parameters by value: args are not updated in-place
      pyhthon passes by object???
Ch13: 1D and 2D arrays p.198-200
      No declaration - only initialisation via
        list comprehensions  OR
        * operator   OR
        loops   OR
      !!!  import array as arr
      !!! Numpy arrays
        my1Darr = arr.array('i', [1, 2, 3])  #all elements limited to the same datatype; 'd' for floats
        my1Darr.append(4)
        my1Darr.insert(1, 100)
        for i in range(len(my1Darr)):
            print(my1Darr[i], end='')   OR
        for i in my1Darr:
            print(i, end='') #[1, 100, 2,3,4]
Ch11: Working with arrays p.144
'''

#using global variables in combination with procedures (i.e. no return values)
#remove the next two '''
'''
def my_procedure():       #definition of void function happens before main program; however, it is only
                          #executed once CALLED in the main program
    global global_var1
    global_var1 += 'b'

#main program starts here
global_var1 = 'a'  #global since it is declared in the main program (outside any procedure/function)
print("global_var1 before CALL is: ", global_var1)  #prints 'a'
my_procedure() #make the procedure CALL
print("global_var1 after CALL is: ", global_var1) #prints 'ab' after adjustment that happens 
                                                  #in my_procedure
my_procedure() #make the procedure CALL again
print("global_var1 is changed again: ", global_var1) #prints 'abb'
'''

#use local variables in combination with functions (i.e. with return values)
#remove the next two ''' 
'''
def my_function(param1):  #definition of fruitful function happens before main program; however, it is only
                          #executed once CALLED in the main program
    myVar = param1        #local since it is not preceded by a global statement
    myVar += 1
    print("myVar inside the function, and already updated, is: ", myVar) #prints '14'
    return myVar

#main program starts here
myVar = 13  #global since it is declared in the main program (outside any procedure/function)
            #(myVar correspond to arg1) corresponds to param1
print("myVar in main program, before making the call: " , myVar) #prints 13
result = my_function(myVar)  #make the function CALL
print("myVar in main program, after making the CALL but before assignment of result: ", myVar) 
#still prints 13; no automatic update between param1 and (arg1 = myVar) like what you would get
#with call by reference. This corresponds closer to call by value
myVar = result
print("myVar in main program after CALL and assignment of result is: ", myVar) #prints 14
myVar = my_function(myVar) #make the CALL and assignment of result in one step
print("myVar after another adjustment done by calling my_function and assigning the result: ", myVar) #prints 15
'''

#Task 14.01 (Implement the pseudocode from worked example 12.02 on p.159)
#remove the next two '''
'''
def SetValues():
    symbol = input("Enter a symbol character which the pyramid will be built from: ")
    MaxNumberOfSymbols = InputMaxNumberOfSymbols()
    NumberOfSpaces = MaxNumberOfSymbols // 2
    NumberOfSymbols = 1
    return symbol, MaxNumberOfSymbols, NumberOfSpaces, NumberOfSymbols

def InputMaxNumberOfSymbols():
    MaxNumberOfSymbols = 0
    while MaxNumberOfSymbols % 2 != 1:
        MaxNumberOfSymbols = int(input("Please enter an odd number for the number of symbols to appear in the last row: "))
    return MaxNumberOfSymbols

<<<<<<< HEAD
def OutputSpaces(NumberOfSpaces):
    for _ in range(NumberOfSpaces):
        print(' ', end='')

def OutputSymbols(NumberOfSymbols, symbol):
    for _ in range(NumberOfSymbols):
        print(symbol, end='')
    print('\n', end='')
=======
symb=input("Enter a symbol")
num=int(input("Enter an odd number, being the number of symbols in the base of the pyramid"))
symbstr=symb * num
emptystr=' ' * num
left=num//2
right = num//2 + 1
>>>>>>> 9015d879936943216218b5c3a3a4181d25a8adda

def AdjustValuesForNextRow(NumberOfSpaces, NumberOfSymbols):
    NumberOfSpaces -= 1
    NumberOfSymbols += 2
    return NumberOfSpaces, NumberOfSymbols

#main program
symbol, MaxNumberOfSymbols, NumberOfSpaces, NumberOfSymbols = SetValues()
while NumberOfSymbols <= MaxNumberOfSymbols:
    OutputSpaces(NumberOfSpaces)
    OutputSymbols(NumberOfSymbols, symbol)
    NumberOfSpaces, NumberOfSymbols = AdjustValuesForNextRow(NumberOfSpaces, NumberOfSymbols)
'''

#print a hollow pyramid (without using functions, resulting in fewer lines of code??)
#remove the next two '''
'''
print("")
symb=input("Enter a symbol: ")
num=int(input("Enter an odd number, being the number of symbols in the base of the pyramid: "))
num_leading_spaces=num//2
print(' ' * num_leading_spaces + symb)
num_middle_spaces=0
num_leading_spaces-=1
while num_leading_spaces > 0:
    num_middle_spaces+=2
    print(' ' * num_leading_spaces + symb + ' ' * num_middle_spaces + symb)
    num_leading_spaces-=1
print(symb * num)
<<<<<<< HEAD
'''

#task 12.04 (structure chart for a number guessing game) p.169
#remove the next two '''
'''
import random
def generate_secret_number():
    secret_number=random.randint(1,10)
    return secret_number

def input_guess(number_of_guesses):
    guess=int(input("Please enter your guess: integer between 1 and 10, both included: "))
    number_of_guesses+=1
    return number_of_guesses, guess

def output_message(secret_number, guess, number_of_guesses):
    if guess != secret_number:
        output_consolation()
    else:
        output_congratulation(number_of_guesses)

def output_consolation():
    print("You exhausted your number of guesses. Sorry")

def output_congratulation(number_of_guesses):
    print(f"Congratulations. You used only {number_of_guesses -1} guesses")

#Number Guessing Game
print('')
secret_number = generate_secret_number()
number_of_guesses = 1
guess = 0
while not (secret_number == guess or number_of_guesses > 3):
    number_of_guesses, guess = input_guess(number_of_guesses)
output_message(secret_number, guess, number_of_guesses)
'''

#task 12.05 (structure chart for user login) p.169
#remove the next two '''
'''
list_of_userids = ["tjaart01", "philip03"]
list_of_pws = ["Tj@$%67", "Ph&*90"]

def input_user_id():
    user_id = input("Please enter your userid")
    return user_id.lower()

def check_userid(user_id):
    return list_of_userids.index(user_id)

def saved_pws(index):
    return list_of_pws[index]

def input_pw():
    entered_pw = input("Please enter your pw")
    return entered_pw

def success_message():
    print("You logged in successfully")

def warning_message():
    print("You exhausted your atempts to log in. Please speak to your password administrator")

def output(saved_pw, entered_pw):
    if saved_pw == entered_pw:
        success_message()
    else:
        warning_message()

#user_logon
user_id = input_user_id()
index = check_userid(user_id)
saved_pw = saved_pws(index)
entered_pw = ' '
attempts = 1
while not (saved_pw == entered_pw or attempts > 3):
    entered_pw = input_pw()
    attempts += 1
output(saved_pw, entered_pw)
'''

#connect4 (sub-tasks) p.160
#delete next two '''
'''
def InitialiseBoard():
    global board
    rows, cols = (6,7)
    board=[['*  ' for i in range(cols)] for j in range(rows)] #empty position on board indicated by *
    #from the player's perspective, columns are numbered 1 to 7 starting from left; from 
    # Python's perspective the column numbers run from 0 through 6 and the row numbers
    # run from 0 through 5 starting at the top of the board

def SetUpGame():
    global GameFinished, ThisPlayer
    GameFinished = False
    ThisPlayer = 'o  '  #player 'O' always start
    
def OutputBoard():
    for row in range(6):
        for column in range(7):
            print(board[row][column], end='')
        print('\n\n', end='')

def ColumnNumberValid():
    global ColumnNumber
    Valid = False
    if 0 <= ColumnNumber <= 6:
        if board[0][ColumnNumber] == '*  ':
            Valid = True
    return Valid

def ThisPlayerChoosesColumn():
    global ColumnNumber
    print(f"Player {ThisPlayer}'s turn")
    #Valid=False
    ColumnNumber = 7 #remove
    while not ColumnNumberValid(): #Valid==False:
        ColumnNumber=int(input("Enter a valid column number"))
        ColumnNumber -= 1
        #Valid = ColumnNumberValid()
    return ColumnNumber

def FindNextFreePositionInColumn():
    global ValidColumn
    ThisRow=5
    while board[ThisRow][ValidColumn] != '*  ':
        ThisRow -= 1
    return ThisRow

def ThisPlayerMakesMove():
    global ValidColumn, ValidRow, board
    ValidColumn = ThisPlayerChoosesColumn()
    ValidRow = FindNextFreePositionInColumn()
    board[ValidRow][ValidColumn]=ThisPlayer

def CheckForFullBoard():
    global GameFinished
    BlankFound = False
    GameFinished = False
    ThisRow = 5
    while ThisRow >= 0 and BlankFound==False:
        ThisColumn = 6
        while ThisColumn >= 0 and BlankFound == False:
            if board[ThisRow][ThisColumn] == '*  ':
                BlankFound = True
            ThisColumn -= 1
        ThisRow -= 1
    if BlankFound == False:
        print("It is a draw")
        GameFinished = True

def CheckHorizontalLineInValidRow():
    global WinnerFound
    for i in range(0,4):
        if ((board[ValidRow][i] == ThisPlayer) and (board[ValidRow][i+1] == ThisPlayer) and (board[ValidRow][i+2] == ThisPlayer) and (board[ValidRow][i+3] == ThisPlayer)):
            WinnerFound = True

def CheckVerticalLineInValidColumn():
    global WinnerFound
    for i in range(3,6):
        if ((board[i][ValidColumn] == ThisPlayer) and (board[i-1][ValidColumn] == ThisPlayer) and (board[i-2][ValidColumn] == ThisPlayer) and (board[i-3][ValidColumn] == ThisPlayer)):
            WinnerFound = True    

def CheckDiagonals():
    global WinnerFound
    row_bot_index = 5 - ValidRow
    row_top_index = ValidRow - 0
    col_left_index = ValidColumn - 0
    col_right_index =  6 - ValidColumn
    lb_index = row_bot_index if row_bot_index < col_left_index else col_left_index
    lb_index = -lb_index if lb_index < 3 else -3
    rt_index = row_top_index if row_top_index < col_right_index else col_right_index
    rt_index = rt_index if rt_index < 3 else 3
    for i in range(lb_index,rt_index-3+1):
        if ((board[ValidRow-i][ValidColumn+i] == ThisPlayer) and (board[ValidRow-i-1][ValidColumn+i+1] == ThisPlayer) and (board[ValidRow-i-2][ValidColumn+i+2] == ThisPlayer) and (board[ValidRow-i-3][ValidColumn+i+3] == ThisPlayer)):
            WinnerFound = True
            break
    lt_index = row_top_index if row_top_index < col_left_index else col_left_index
    lt_index = -lt_index if lt_index < 3 else -3
    rb_index = row_bot_index if row_bot_index < col_right_index else col_right_index
    rb_index = rb_index if rb_index < 3 else 3
    for i in range(lt_index,rb_index-3+1):
        if ((board[ValidRow+i][ValidColumn+i] == ThisPlayer) and (board[ValidRow+i+1][ValidColumn+i+1] == ThisPlayer) and (board[ValidRow+i+2][ValidColumn+i+2] == ThisPlayer) and (board[ValidRow+i+3][ValidColumn+i+3] == ThisPlayer)):
            WinnerFound = True
            break

def CheckIfThisPlayerHasWon():
    global GameFinished, WinnerFound
    GameFinished = False
=======


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
>>>>>>> 9015d879936943216218b5c3a3a4181d25a8adda
    WinnerFound = False
    CheckHorizontalLineInValidRow()
    if WinnerFound == False:
        CheckVerticalLineInValidColumn()
    if WinnerFound == False:
<<<<<<< HEAD
        CheckDiagonals()
    if WinnerFound == True:
        GameFinished = True
        print(f"{ThisPlayer} is the winner")
    else:
        CheckForFullBoard()

def SwapThisPlayer():
    global ThisPlayer
    if ThisPlayer == 'x  ':
        ThisPlayer = 'o  '
    else:
        ThisPlayer = 'x  '

#main program starts here
InitialiseBoard()
SetUpGame()
OutputBoard()
while GameFinished == False:
    ThisPlayerMakesMove()
    OutputBoard() 
    CheckIfThisPlayerHasWon()
    if GameFinished == False:
        SwapThisPlayer()
'''

#Ch12: Exam-style Questions
#Question1 : Frequency of random number generator
#using local variables and parameters (and functions with return statements)
#remove next two '''
'''
import random

def initialiseTally():
    Tally=[0 for i in range(1,21)]
    return Tally

def generateRandomNumber():
    RandomNumber = random.randint(1,20)
    return RandomNumber

def updateTally(Tally, RandomNumber):
    for i in range(1,21):
        if RandomNumber == i:
            Tally[i-1]+=1
    return Tally

def outputTally(Tally):
    for i in range(1,21):
        print(i, Tally[i-1])

NumberOfTests=0
Tally=initialiseTally()
while NumberOfTests < 1001:
    RandomNumber=generateRandomNumber()
    updatedTally=updateTally(Tally, RandomNumber)
    NumberOfTests+=1
outputTally(updatedTally)
'''

#Ch12: Exam-style Questions
#Question1 : Frequency of random number generator
#using global variables (no args/parameters and no return statements)
#remove next two '''
'''
import random

def initialiseTally():
    global Tally
    Tally=[0 for i in range(1,21)]
    
def generateRandomNumber():
    global RandomNumber
    RandomNumber = random.randint(1,20)
    
def updateTally():
    global Tally
    Tally[RandomNumber-1]+=1

def outputTally():
    for i in range(1,21):
        print(i, Tally[i-1])

NumberOfTests=0
initialiseTally()
while NumberOfTests < 1001:
    generateRandomNumber()
    updateTally()
    NumberOfTests+=1
outputTally()


#Ch12: Exam-style Questions
#Question2 : Memory game
#using global variables (neither parameters nor return statements)
#remove next two '''
'''
import random
import time

def SetUpEmptyGrid():
    global Grid
    Grid=[[0 for i in range(2)] for j in range(2)]#2-->8

def RandomlyDistributeCards():
    global Grid
    for number in range(1,3):#3-->33
        GetEmptyGridPosition()
        Grid[x][y] = number
        GetEmptyGridPosition()
        Grid[x][y] = number


def GetEmptyGridPosition():
    global x,y
    x = random.randint(0,1)#1-->7
    y = random.randint(0,1)#
    while Grid[x][y] != 0:
        x = random.randint(0,1)#
        y = random.randint(0,1)#


def SetUpPlayers():
    global Points, ThisPlayer
    Points = [0,0]
    ThisPlayer = 1


def GetPlayersCoordinates():
        global x1, y1, x2, y2
        x1, y1 = input(f"Player {ThisPlayer} enter two values separated by a space(s)").split()
        x1 = int(x1)
        y1 = int(y1)
        while Grid[int(x1)][int(y1)] == 0:
            x1, y1 = input(f"Player {ThisPlayer} enter two values separated by a space(s)").split()
            x1 = int(x1)
            y1 = int(y1)
        x2, y2 = input(f"Player {ThisPlayer} enter two values separated by a space(s)").split()
        x2 = int(x2)
        y2 = int(y2)
        while Grid[int(x2)][int(y2)] == 0 or (x1,y1)==(x2,y2):
            x2, y2 = input("Enter two values separated by a space(s)").split()
            x2 = int(x2)
            y2 = int(y2)

def DisplayGrid():
    for i in range(2):#2-->8
        for j in range(2):#
            if (i,j) == (x1,y1):
                print(Grid[x1][y1], end='')
            elif (i,j) == (x2, y2):
                print(Grid[x2][y2], end='')
            elif Grid[i][j] == 0:
                print(0, end='')
            else:
                print('?', end='')
        print("\r")
                


def TestForMatch():
    global Points
    if Grid[x1][y1] == Grid[x2][y2]:
        Grid[x1][y1] = Grid[x2][y2] = 0
        Points[ThisPlayer-1] += 1
        time.sleep(3)
        print("\n")
        DisplayGrid()
    else:
        SwapPlayers()

def SwapPlayers():
    global ThisPlayer
    if ThisPlayer == 1:
        ThisPlayer = 2
    else:
        ThisPlayer = 1
        


def TestForEndGame():
    global GameEnd
    if Points[0] + Points[1] == 2:#2-->32
        GameEnd = True

def OutputResults():
    if Points[0] > Points[1]:
        print("Winner is player 1")
    else:
        print("Winner is player 2")



#main program starts here
SetUpEmptyGrid()
RandomlyDistributeCards()
SetUpPlayers()
GameEnd = False
while GameEnd == False:
    GetPlayersCoordinates()
    DisplayGrid()
    TestForMatch()
    TestForEndGame()
OutputResults()
'''
=======
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
>>>>>>> 9015d879936943216218b5c3a3a4181d25a8adda
