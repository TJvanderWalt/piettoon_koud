"""title: user-defined python functions
topics: 
    regular functions; 
    lambda functions; 
    closures; 
    function decorators; 
    currying;
reference1: 
    "Python functions: Lambdas, Closures, Decorators, and Currying"
    Yong Cui in: Better Programming (Medium archive)
reference2:
    "The top 4 misuses of lambdas in python"
    Yong Cui in: Better Programming (Medium archive)
reference3: 
    "Defining your own Python function" John Sturtz (realpython.com)
so what? 
    way to abstract functionality into a function definition; 
    DRY principle; 
    reusability of code; 
    later changes made in one place only; 
    modularize the main program; 
    namespace separation (namespace is a region of a program in which identifiers have meaning; 
     variables can be defined and used in one function, even though they
     have the same name as variables defined in other functions or even in the main program)
further reading/links: 
    (piettoon_koud > master) built_in_functions.py ; function_decorators.py
github: 
    piettoon_koud > master 
dependencies:
    none
"""

#-----topic------------regular functions (with default arguments)---------------------top-----------

def add_up(num_1, num_2):          #declare function with def keyword
    '''example regular function''' #function docstring
    print("regular function was called")
    added_up = num_1 + num_2
    return added_up
first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))
two_numbers_summed = add_up(first_number, second_number) 
#order and number of args in the call should match order and number in the def
#call function and assign the return value
print(f"Sum of {first_number} and {second_number} is {two_numbers_summed}\n")

def my_func(qty=6, item='bananas', price=2.49):
#keywords arguments should match in number, but the order is flexible
#when both positional and keyword args are present, all the positional args must come first
    '''default values for keyword arguments'''
    print(f"{qty} {item} cost R{price}\n")
my_func(item='oranges') #kwargs not specified in the call, take on their default values from def

#-----topic------------regular functions (with default arguments)---------------------bottom--------



#-----topic------------Lambda functions (and their misuses)------------------------------top--------

#lambda functions are small, anonymous one-time inline functions with the syntax
# lambda arguments: expression
# they take zero or multiple arguments
# they are MOST SUITABLE WHEN A BRIEF, SINGLE-USE FUNCTION IS NEEDED

#Best Practice no1: think about built-in functions first, before writing your own lambdas
pets = ['dog', 'turtle', 'bird', 'fish', 'kitty']
number_tuples = [(4, 5, 7), (3, 1, 2), (9, 4, 1)]
sorted_pets = sorted(pets, key=lambda x: len(x), reverse=True) #misuse of lambda; simply use    sorted(pets, key=len)
sorted_tuples = sorted(number_tuples, key=max) 
#correct use of built-in functions; misuse of lambdas would be   sorted(number_tuples, key=lambda x: max(x))
print(sorted_pets, "\n")
print(sorted_tuples, "\n")

#Best Practice n02: write a regular function instead of a lambda when the function is to be used
# or put another way, do not assign lambdas to variables that can be called
print(23 + (lambda e, f: e**f)(2, 3), "\n") #prints 31; lambda was not assigned to a variable prior
base_raised_to_power = lambda b, e: b**e #lambda will be used once
print(100 + base_raised_to_power(10, 3), "\n") #prints 1100; NOT A BEST PRACTICE to open up lambdas for multiple use
# multiple times (i.e. when the function may be called many times, possibly even with forbidden arguments)
# def divide_two_numbers_fun(x, y): return x / y 
#above function, suitable for multiple use, wqs defined in a single line
#calling this function with (3,0) leads to ... ZeroDivisionError ... in divide_two_numbers_fun 
# divide_two_numbers = lambda a, b: a / b 
#assigning lambdas (intended for single use) to a variable is NOT A BEST PRACTICE since divide_two_numbers(3, 0)
# leads to ... ZeroDivisionError ... in <lambda> which is not useful for debugging when many lambdas are defined
# and share the sama anonymous name <lambda>
 
#Best Practice no3: consider replacing higher-order functions using lambdas, with list comprehensions
# example of higher-order functions include map() filter() and reduce()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares, "\n")
#A BETTER PRACTICE might be to use list comprehensions, instead of lambda functions
cubes = [x**3 for x in numbers]
print(cubes, "\n")

#Best Practice no4: rather write a regular function (i.e. spanning many lines) if the expression
# of a lambda is too cumbersome (readability and maintainability of code)

#-----topic------------Lambda functions (and their misuses)---------------------------bottom--------



#-----topic------------Closure functions ------------------------------------------------top--------

#the three key elements to creating closures in Python are (i)declare a nested function within the
# scope of the outer function; the binding of non-local variables outside the scope of the nested
# function; return the nested function to output the closure function
#THUS, THE OUTER FUNCTION DOES AN INITIAL PIECE OF WORK (INCLUDING DECLARING SOME VARIABLES) AND RETURNS
# ANOTHER FUNCTION WHICH, WHEN CALLED, BUILDS ONTO THIS INITIAL WORK TO THEN FINISH THE REST
# OF THE WORK (INCLUDING MULTIPLE UPDATES TO VARIABLES OF THE FIRST FUNCTION)
def make_an_incrementer(step): #outer function
    multiple = 0
    def well_made_incrementer(): #nested (inner) function declared within the scope of the outer function
        nonlocal multiple 
        #step is a free variable outside the scope of the nested function and in order for it to be modified
        # it does need the nonlocal keyword; step is another free variable and although it can be used by the
        # inner function, but is not modified by it, it does not need the nonlocal keyword
        multiple += step
        return multiple
    return well_made_incrementer #return the nested function to output the closure function

increment_in_fives = make_an_incrementer(5)
multiples = []
for i in range(1, 12, 2):
    multiples.append(i*increment_in_fives()) #increment_in_fives() is called six times during the loop
print(multiples, "\n")
called_once_more = increment_in_fives() #increment_in_fives() called and assigned once more
for i in range(10):
    multiples.append(i*called_once_more)
print(multiples, "\n")
print(increment_in_fives.__code__.co_freevars) 
#prints the free vars of the closure function assigned to increment_in_fives
print(increment_in_fives.__closure__)
print(increment_in_fives.__closure__[0].cell_contents)
print(increment_in_fives.__closure__[1].cell_contents)

#-----topic------------Closure functions ------------------------------------------------bottom-----



#-----topic------------function decorators--------------------------------------------------top-----

#decorators are functions that extend the behaviour of other functions without explicitly modifying them

def triple_repeat_wrapper(func): 
    #func is the calling function that will be indicated by @ as being wrapped
    #triple_repeat_wrapper is not the wrapper itself - it is only the function that will produce the actual wrapper
    # i.e. by defining and returning the actual wrapper
    def wrapper():
        print(f"Wrapper does some pre-work before calling func {func.__name__}")
        func()
        func()
        func()
        print(f"Wrapper does some post-work after calling func {func.__name__}")
    return wrapper

@triple_repeat_wrapper
#telling the interpreter that the function we are about to define will be wrapped by the decorator function
#thus, on calling hooray(), instead of executing it, the wrapper will be executed
def hooray():
    print("Hooray! Hooray!")

hooray() #in effect this becomes a call to wrapper()

#-----topic------------function decorators-----------------------------------------------bottom-----



#-----topic------------Currying ------------------------------------------------------------top-----

#Currying (after mathematician Haskell Curry) refers to creating new functions from existing functions
# by applying partial arguments (also termed partial functions)
# the add_up() function above takes two arguments; a new function with only one argument can be created
#since a default value is set for the other argument
add_to_seven = lambda x: add_up(7, x)
print("\n" + str(add_to_seven(23)) + "\n") 

#-----topic------------Currying ---------------------------------------------------------bottom-----
