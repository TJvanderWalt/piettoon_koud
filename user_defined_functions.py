"""title: user-defined python functions
summary and context: 
reference1: "Defining your own Python function" John Sturtz (realpython.com)
so what? way to abstract functionality into a function definition; DRY principle; reusability of code; 
later changes made in one place only; modularize the main program; namespace separation (variables can
be defined and used in one function, even though they have the same name as variables defined in other 
functions or even in the main program)
further reading/links: (piettoon_koud > master) built_in_functions.py ; function_decorators.py
github: piettoon_koud > master 
dependencies:
"""

def my_func(qty = 6, item = 'bananas', price = 2.49):
    print(f"{qty} {item} cost R{price}")

my_func()

#id() , len(), any()
