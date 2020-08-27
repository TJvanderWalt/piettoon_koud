"""title: python keywords
topics: 
    value keywords: True, False, None; 
    operator keywords: and, or, not, in, is; 
    control flow keywords: if, elif, else; 
    iteration keywords: for, while, break, continue, else; 
    structure keywords: def, class, with, as, pass, lambda;
    returning keywords: return, yield;
    import keywords: import, from, as
    exception-handling keywords: try, except, raise, finally, else, assert;
    asynchronous programming keywords: async, await;
    variable handling keywords: del, global, local;
reference1: 
    "Python keywords: an introduction" Chad Hansen (realpython.com)
reference2:
    ""
    Yong Cui in: Better Programming (Medium.com archive)
reference3: 
    "" John Sturtz (realpython.com)
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


#-----topic------------value keywords: True, False, None-----------------------------top-----------
'''In python, True and False are written in uppercase
The truthiness of a value is tested by the Boolean evaluation bool() of the value
Truthy means any value that evaluates to True in the Boolean context
Falsy means any value that evaluates to False in the Boolean context
    bool("cat")    # non-empty strings are truthy
    bool(12.3)     # any non-zero numbers are truthy
    bool(['a'])    # any non-empty lists are truthy
    bool(0.0)      # the number zero is falsy
    bool([])       # empty lists are falsy
    bool("")       # empty strings are falsy, as well as {} and set()
    bool(False)    # falsy
'''
x = True 
y = "True"
z = False
print(type(x)) # <class 'bool'>
print(type(y)) # <class 'str'>
print(x is True) # prints True
print(y is True) # prints False
print(y is False) # prints False
print(z is False) # prints True
print(bool(y) is True) # prints True since a non-empty string is truthy
if x is True: print("x is actually True") # don't do this to compare truthiness
if x: print("x is truthy") # do this to compare truthiness

'''The keyword None represents no value
It is also the default value returned by a function if it doesn't have a return statement
'''
def func():
    print("hello")
x = func()
print(x) # prints None
print("")
#-----topic------------value keywords: True, False, None--------------------------bottom-----------


#-----topic------------operator keywords: and, or, not, in, is------------------------top-----------
'''The use of and in the next line will result in a truthy result only if both expressions are truthy
    <expression1> and <expression2> 
The result will not necessarily be True or False since the use of and will return <expression1> if
it is falsy, and if it is truthy, then <expression2> is returned. This return value can be passed
to bool() to get an explicit True or False, or it should be used in a conditional if statement
    ((1+2 == 3) and ('A'*2)) is "AA"        # this evaluates to True
    ((1+2 == 3) and ('A'*2)) is True        # this evaluates to False
    bool(1+2==3 and 'A'*2) is True          # this evaluates to True
Instead of using and, the python ternary expression can achieve the same result:
    x = (1+2==3) and ('A'*2)
    x = (1+2==3) if not (1+2==3) else ('A'*2)
'''
if(1+2==3 and 'A'*2):
    print(True)  #prints True

'''The use of or in the next line will return the first operand if it is truthy, otherwise returns
the second operand (again: operands are not converted to True/False but their truthiness determines
the result of or)
    <expression1> or <expression2>
Instead of using or, a ternary expression can achieve the same result:
'''
((1+2 != 3) or ('A'*2)) is True  #evaluates to False 
x = (1+2 != 3) if (1+2 != 3) else ('A'*2)
print(x)  #prints "AA"

'''The not keyword flips the meaning of result. It will return the explicit Boolean value (True, False)
and then return the opposite
'''
val = ""  #falsy
not val   #truthy
val = 5   #truthy
(not val) is False #evaluates to True 


#-----topic------------operator keywords: and, or, not, in, is---------------------bottom-----------


#-----topic------------control flow keywords: if, elif, else--------------------------top-----------
#-----topic------------control flow keywords: if, elif, else-----------------------bottom-----------

#-----topic------------iteration keywords: for, while, break, continue, else----------top-----------
#-----topic------------iteration keywords: for, while, break, continue, else-------bottom-----------

#-----topic------------structure keywords: def, class, with, as, pass, lambda---------top-----------
#-----topic------------structure keywords: def, class, with, as, pass, lambda------bottom-----------

#-----topic------------import keywords: import, from, as------------------------------top-----------
#-----topic------------import keywords: import, from, as---------------------------bottom-----------

#-----topic-----exception-handling keywords: try, except, raise, finally, else, assert-----------top
#-----topic-----exception-handling keywords: try, except, raise, finally, else, assert--------bottom

#-----topic------------asynchronous programming keywords: async, await----------------top-----------
#-----topic------------asynchronous programming keywords: async, await-------------bottom-----------

#-----topic------------variable handling keywords: del, global, local-----------------top-----------
#-----topic------------variable handling keywords: del, global, local--------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------
