"""title: library itertools
topics: 
    what is an iterator?;
    infinite iterators; 
    terminating iterators; 
    combinatoric iterators; 
reference1: 
    "Advanced Python: Itertools library - the gem of Python language"
    Farhad Malik in: FinTechExplained (medium.com archive)
reference2:
    ""
    Yong Cui in: Better Programming (Medium archive)
reference3: 
    "" John Sturtz (realpython.com)
so what? 
    way to abstract functionality into a function definition; 
    DRY principle; 
    reusability of code; 
    later changes made in one place only; 
    modularize the main program; 
    namespace separation (namespace is a region of a program in which identifiers have meaning; 
    have the same name as variables defined in other functions or even in the main program)
further reading/links: 
    (piettoon_koud > master)  ; function_decorators.py
github: 
    piettoon_koud > advanced 
dependencies:
    itertools version 2.3 and Python 3.8
"""

import itertools as it

#-----topic------------what is an iterator?-------------------------------------------top-----------
#   It is an object with a __next__ method. It also has a state which is used to remember the execution 
#   during iteration. It will always get the next item in the stream when next(iterator) is executed, or
#    raise a StopIteration error if there is no next item to be returmed
# 
#   An iterable is an object which we can loop over. It has an __iter__ method that returns an iterator
#   when iter() is called. It has a __getitem__ method that can take sequential indexes, starting at 
#   zero and raising IndexError when the indexes are no longer valid 
# 
#   Itertools is a Python module that is part of the Python 3 standard libraries. It has various functions
#   that works on iterators to produce iterators (allows us to perform iterator algebra) in a memory
#   and computationally efficient manner 
#-----topic------------what is an iterator?----------------------------------------bottom-----------


#-----topic------------infinite iterators---------------------------------------------top-----------
# itertools.count() function generates an infinite sequence of evenly spaced values
start = 10
step = 1
my_counter = it.count(start, step)
#for i in my_counter:
    #this loop will run forever
#    print(i)
print(type(my_counter))
# my_counter is an itertools.count object
# to reveal its methods ...  my_counter.__dir__()  or dir(my_counter)
# one of these methods is ...  my_counter.__next__()  or next(my_counter) which returns consecutive values
print(my_counter.__next__())
print(next(my_counter))
print(my_counter.__next__())
#
#this is equivalent to
#   def count(start=0, step=1):
#       x = start
#       while 1:
#           yield x
#           x += step
#   for i in count():
#       print(i)
#above is an infinite loop
#
#
#-----topic------------infinite iterators------------------------------------------bottom-----------


#-----topic------------terminating iterators------------------------------------------top-----------
#-----topic------------terminating iterators---------------------------------------bottom-----------

#-----topic------------combinatoric iterators-----------------------------------------top-----------
#-----topic------------combinatoric iterators--------------------------------------bottom-----------