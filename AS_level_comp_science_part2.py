"""
TITLE:
    AS level computer science: Part 2 (Python exercises) 
REFERENCE1:
    'Cambridge International AS and A Level Computer Science Coursebook' S Langfield and D Duddell
REFERENCE2:
    'Python built-in functions' (with example code) 
    https://www.programiz.com/python-programming/methods/built-in
FURTHER READING & LINKS: 
    github>piettoon_koud>as_level_comp_science_part2.py
DEPENDENCIES:
    Pythyon 3 set up on Windows
DONE:
    basic python
        #comment
        "string" or 'string'
        print("a message string containing \" ...\"  \n and \t  and end=''  ")
        continue a python statement on the next line by using \ENTER
        print("") #empty line
        use of triple, double and single quotes in the print()
        no requirement to define python MY_CONSTANTS or snake_case_variables; naming conventions; rules for valid identifiers
        concatenate (+) strings    print("partial string" + 3*"_" + "partial string" + 3*"\t")
        pseudo: INPUT   python: input() and int(input())
        pseudo: OUTPUT  python: print(comma-separated or string concatenated(+) and str() type conversion)
        print with fstring or with .format() method
        pseudo: {leftwards arrow} assignment  python: A, B = 12, 21 multiple assignment
        pseudo: use of TEMP variable  python: swap values of two variables without using TEMP
        use of relational and logic operators to set up condition for selection and repetition statements
        pseudocode: IF condition THEN ELSE ENDIF  python: if condition: [tab] else: [tab]

TO DO:
    add more examples to the identifier table (Philip)
    code example for using the pretty print function (Philip)
    correct line 79 to exactly re-produce the output of line 76 by making use of a fstring (Philip)
    Ch11 Exam-Style-Questions : Write Python code for Question 1 : Modulo 11 check digit (Philip)
"""

print("Read and understand the statements/syntax in the next lines of Python code \nand compare with the terminal \
output; also read the comment lines - i.e. lines prepended by #") #note the use of \n (continue to print on the next line) 
#and the use of \ (i.e. Python code runs over to the next line)
print("") #print empty line
print("He said 'Hello' to her") #print("He said "Hello" to her") throws an error
print('He said "Hello" to her') #combination of '  " " '   OR  "   ' '  "   is OK but NOT  "  " "  "   NOR  '   '  '   '
print("He said \"Hello\" to her") 
#OK since \ escapes the special meaning of " which is to mark the reach of a literal string, and " simply becomes
#another printable character
print("")

print("""In Python there is no requirement to define variables and/or constants before you can use them. Also, \n\
the identifiers ("names") chosen for MY_CONSTANTS and my_snake_case_variables should adhere to rules such as: \n\
\tthey may contain 0 through 9, a to z, A to Z and underscore _ \n\tthey should not start with a number, \
and \n\tcase matters""")
#note use of " " within """  """ and also \t for horizontal tab
print("")
print("Identifier table: \n" + 100*"-" + "\nIdentifier" +3*"\t" + "| Explanation")
print("counter                         | stores how many numbers have been input so far OR counts number of times round the loop")
print("next_number                     | the next number to be input")
print("running_total                   | sum of all numbers input so far")
print("average                         | calculated result from dividing running_total by counter")
print("biggest_so_far                  | stores the biggest number input so far")
print("")

print('pseudocode: \n\tINPUT "Prompt: " A')
print('pythoncode: \n\t>>>user_name = input("Please enter your username")')
print('\t>>>your_age = int(input("Please enter your age in years")')
user_name = input("\tPlease enter your username ")
your_age = int(input("\tPlease enter your age in years ")) 
#int() converts the string type (e.g. '19') resulting from input() into the integer number 19
print("")

print('pseudocode: \n\tOUTPUT "message" B')
print('pythoncode on IDLE: \n\t>>>print("Your name is", user_name, "and you are", your_age, "years old")')
print("\tYour name is", user_name, "and you are", your_age, "years old")
#a space will replace every comma in the print list
print('\t>>>print("Your name is " + user_name + " and you are " + str(your_age) + " years old")')
print("\tYour name is " + user_name + " and you are " + str(your_age) + " years old")
#in string concatenation you need to insert the spaces yourself and number types need to be converted to string types
#next, a so-called fstring will be used in the print()
#print('\tfYour name is {user_name} and you are {your_age} years old')
print("")

print("My name is John")
print("and I am 21 years old")
#the two print statements will print on subsequent lines unless this default behaviour is changed
print("My name is John", end ='')
print(" and I am 21 years old")
#two print statements print on the same line when you set end=''
print("")

print('pseudocode: \n\tA \N{leftwards arrow} 12 \n\tB \N{leftwards arrow} 21 \n\t\
TEMP \N{leftwards arrow} A \n\tA \N{leftwards arrow} B \n\tA \N{leftwards arrow} TEMP ')
print('pythoncode on IDLE: \n\t>>>A, B = 12, 21 #python allows multiple assignments in one line')
A, B = 12, 21
print(f"\tA = {A} and B = {B}")
print('\n\t>>>A, B = B, A #python trick to swap the values of two variables without using a third \
(TEMP) variable')
A, B = B, A
print("\tA = {} and B = {}".format(A, B)) #print with the help of the .format() method
print("")

print('pseudocode: \n\tIF A <> B \n\t\tTHEN OUTPUT "A is not equal to B" \n\t\tELSE \
OUTPUT "A and B are equal" \n\tENDIF')
#an important part of any selection and repetition construct is a simple logic proposition (also
#called condition) that will evaluate to either True or False. Example of simple condition that
#makes use of relational (comparison) operators is:
# pseudocode:    A<B  A>B  A=B   A<>B  A>=B  A<=B
# pythoncode:    A<B  A>B  A==B  A!=B  A>=   A<=B
print('pythoncode on IDLE: \n\t>>> if A != B: \n\t... [tab]print("A is not equal to B") \n\t... else: \
\n\t... [tab]print("A and B are equal") \n\t... [ENTER]')
if A != B:
    print("\tA is not equal to B")
else:
    print("\tA and B are equal")
print("")


#complex conditions can be formed by "joining" two or more simple conditions with AND, OR and NOT
#(called logic operators). Furthermore, one IF statement can contain another IF statement 
#(referred to as nested IF statements). Similarly, nested REPEAT statements are possible
#More about this in Part3

#**************  PYTHON CODING EXERCISES in IDLE by PHILIP ****************************
# Ch 11 of the Coursebook, Exam-Style Questions
# Question 1: Modulo-11 method to calculate a check digit for a sequence of nine digits
# Leftmost digit receives a weight of 10, next digit a weight of 9, and so on
# Calculate the sum over al nine digits of (digit * weight)
# Calculate the result of sum mod 11 (i.e. the remainder of sum divided by 11)
# Calculate the result of (11 - previous result)
# assign this result to the check digit, unless the result is equal to 10, in which case the value X 
# is assigned to the check digit; or the result is equal to 11, in which case 0 is assigned to the check digit
