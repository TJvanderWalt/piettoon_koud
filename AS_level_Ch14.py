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
