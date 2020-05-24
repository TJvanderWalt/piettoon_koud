""" TOPIC: function_decorators (Part2)

SUMMARY & CONTEXT: *scope of variables (global, local, nonlocal), *closures, function decorators

REFERENCE-1: "Python function decorators - a brief tutorial" by Mark A. Brennan in: The Startup

REFERENCE-2:* "Closures and decorators in Python" by Reza Bagheri in: Towards Data Science

SO WHAT? Decorators are a powerful tool in Python which are implemented using closures. They allow programmers to 
modify the behaviour of a function without permanently modifying it (like in dynamic coding environments)

FURTHER READING/LINKS: Python 3.X "global" and "nonlocal" statement; class decorators; search realpython.com and 
Medium app and Corey Schafer; 

DEPENDENCIES: Decorators are part of the Python standard library 

GITHUB: piettoon_koud(master branch)
"""

import math
from math import sin

print("\nuser_defined_functions.py",2*"\N{leftwards arrow} ",10*" ","function_decorators_part1.py","\N{leftwards arrow}\n")

print("""THE SCOPE of a variable refers to the area in which you can see or access that variable - it cannot be \n\
accessed outside its scope. The scope of a variable is determined by where it is assigned in the source code:\n\t\
global scope - is defined outside all functions and can be accessed by all functions in the file\n\t\
local scope - defined inside a function and can only be accessed inside the function in which it was defined\n\t\
nonlocal scope - when a variable is assigned in an enclosing function, it is nonlocal to its nested functions.")\n\
If you reassign a global variable in a function, any changes to the local variable inside the function will not \n\
affect the global variable. If you want to change a global variable from inside a function, you have to use the \n\
"global" keyword in Python for that. In nested functions, the local variables of the outer function are said to be \n\
nonlocal to its inner function. The inner function can access the nonlocal variables but cannot change them. Reassigning \n\
them simply creates a new local variable with the same name in the inner function, and does not affect the nonlocal \n\
variable. To make a change to a nonlocal variable in a nested function, you must use the "nonlocal" keyword ).""")

print("")
print("""A CLOSURE is an inner function that remembers the nonlocal variables in the enclosing scopes (i.e. state\n\
of the outer function) even if these nonlocal variables are no longer in memory (since the outer function has "finished"\n\
and gone out of scope). To define a closure we need an inner function that:\
\n\tis returned by the outer function;\
\n\tshould capture some of the nonlocal variables of the outer function - by accessing those variables or defining them as "nonlocal"\n\
\tor having a nested closure that needs to capture them. \n\
After defining it, you need to call the outer function to return the closure\n\n\
In the interactive Python environment\n\
>>> def f(x):                        \n\
>>>\tz = 2                           \n\
>>>\tdef g(y):                       \n\
>>>\t\treturn x*z + y                \n\
>>>\treturn g                        \n\
>>> a = 5                            \n\
>>> b = 1                            \n\
>>> h = f(a)                         \n\
>>> h.__name__  #returns 'g'         \n\
>>> h.__code__.co_freevars    #shows which free variables ('x', 'z') are captured by the inner function   \n\
>>> h.__closure__             #shows if it's a closure (None if not)                                      \n\
>>> print(f"{h.__code__.co_freevars[0]} = {h.__closure__[0].cell_contents}")                              \n\
>>> h(b)                      #outputs 11
""")
def f(x):
    z = 2
    def g(y):
        return x*z + y
    return g
a = 5
b = 1
h = f(a)
print(h.__name__)
print(h.__code__.co_freevars)
print(h.__closure__)
print(f"{h.__code__.co_freevars[0]} = {h.__closure__[0].cell_contents}")
print(h(b))
print("""\nAlso note that a closure is not called directly - therefore (anonymous) lambda functions can be used\n\
>>> def f(x):                                                \n\
>>>\tz=2                                                     \n\
>>>\treturn lambda y: z*x + y                                \n\
>>> a = 5                                                    \n\
>>> b = 1                                                    \n\
>>> f(a)(b)      #output 11                                  \n\
""")
def f(x):
    z = 2
    return lambda y: x*z+y
a = 5
b = 1
print(f(a)(b))

print("""\nApplications for closures - to combine g(y) and f(x) into one function h(x) = g(f(x))\n\
In the interactive python environment                      \n\
>>> import math                                            \n\
>>> from math import sin                                   \n\
>>> unshifted_lst = [x for x in range(30, 240, 30)]        \n\
>>> def sin_curve(degrees_lst):                            \n\
>>> \tsin_lst = [round(sin(x*math.pi/180),2) for x in degrees_lst]                                     \n\
>>> \treturn sin_lst                                       \n\
>>> def add_degrees(b4shift_lst, y=0):                     \n\
>>> \treturn [x + y for x in b4shift_lst]                  \n\
>>> def compose(g, f):                                     \n\
>>> \tdef h(*args, **kwargs):                              \n\
>>> \t\treturn g(f(*args, **kwargs))                       \n\
>>> \treturn h                                             \n\
>>> print("unshifted_sin_curve : ", end='')                \n\
>>> for i, j in zip(unshifted_lst, sin_curve(unshifted_lst)):   \n\
>>> \tprint((i, j), end='')                                \n\
>>> print("shifted_sin_curve :", 12*" ", end='')         \n\
>>> for i, j in zip(unshifted_lst, compose(sin_curve, add_degrees)(unshifted_lst, 30)):   \n\
>>> \tprint((i, j), end='')                                \n\
>>> print("shifted 30 degrees to the left with respect to unshifted sin curve")         \n\
""")
unshifted_lst = [x for x in range(30, 240, 30)]
def sin_curve(degrees_lst):
    """calculate the sin of a list of input values (in degrees) and return the sin values in a list"""                                  
    sin_lst = [round(sin(x*math.pi/180), 2) for x in degrees_lst]
    return sin_lst
def add_degrees(b4shift_lst, y=0):  
    #an input list of values, after adding the shift y (default=0), returns an output list
    return [x + y for x in b4shift_lst]
def compose(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h

print("unshifted_sin_curve : ", end='')
for i, j in zip(unshifted_lst, sin_curve(unshifted_lst)):
    print((i, j), end='')
print("\nshifted_sin_curve :            ", end='')
for i, j in zip(unshifted_lst, compose(sin_curve, add_degrees)(unshifted_lst, 30)):
    print((i, j), end='') 
print("\nshifted 30 degrees to the left with respect to unshifted sin curve")





print("")
print("""A decorator is a function (or "callable") that takes another function as argument (the \
decorated function) \nand returns another (wrapper) function. Decorators typically call their decorated \nfunctions, but \
they don't have to - they could completely swap behaviour. They may modify the arguments being passed \
to their decorated function; they may save and modify the decorated function's return value; or they may add \
additional behaviour either before or after invoking the decorated function. Decorators provide an easy way""")




def permutation(a_list): 
    """this outer function does the first part of the work e.g. produce permut_big_list of all possible ways to
    pick 3 numbers (which may be the same) from the numbers in a_list"""
    permut_small_list = [] #list of three numbers picked
    permut_big_list = []   #list of lists
    for first_number in a_list:
        for second_number in a_list:
            for third_number in a_list:
                permut_small_list.append(first_number)
                permut_small_list.append(second_number)
                permut_small_list.append(third_number)
                copy_list = permut_small_list.copy()
                permut_big_list.append(copy_list)
                permut_small_list.clear() #this would also clear out small_list within big_list if it were not
                #for a copy of small_list that had been appended to big_list
    def base_number(base): 
        """inner function defined within the outer function; this inner function (having access to the work done
        by the outer function) will then do additional work where the outer function left off""" 
        for small_list in permut_big_list: #permut_big_list is free of the outer (i.e. enclosing) function's scope -
        #to the extent that the inner function has access to the state (including permut_big_list) of the outer
        #function (i.e. closure)
            denary = 0
            for num in small_list:
                if num%10 >= base or num//10 >= base: #with base number = 8 (say) num=x or num=xx with x limited
                    #to the digits 0 through 7 (num=7 and num=15 are allowed, for example, but num=9 is not allowed)
                    break
                denary = denary + num%10 + base*(num//10)
            if denary == 30:
                return f"{small_list} {base}"
    return base_number #returns a function that will continue the work where the first function left off



my_list = [1, 3, 5, 7, 9, 11, 13, 15] #note: only numbers allowed, no letters are used

riddle = permutation(my_list) #calls outer function to do the first part of some work and to return a 
#further function that will then complete the rest of the work
for i in range(1, 11): #without the option to use letters, base 10 is the upper limit
    print(riddle(i)) #call on the further function to complete the rest of the work