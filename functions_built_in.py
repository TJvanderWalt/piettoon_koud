"""title: built-in python functions
topics: 
    any()
    filter()
    id()
    len()
    map()
    max()
    object.method() vs function(object)
    reduce()
    sort() and sorted() 
    type()
currying;
reference1: 
further reading/links: 
github: piettoon_koud > master 
dependencies:
"""

#-----topic------------any()-------------------------------------------------------------top--------
#takes an iterable as its argument and returns True if any of the items in the iterable are truthy
# and False otherwise
print(any(['bar' == 'baz', len('foo') == 4, 'qux' in {'foo', 'bar', 'baz'}]), "\n") #prints False
print(any([False, True, False]), "\n")  #prints True
#-----topic------------any()----------------------------------------------------------bottom--------


#-----topic------------filter()----------------------------------------------------------top--------
#-----topic------------filter()-------------------------------------------------------bottom--------

#-----topic------------id()--------------------------------------------------------------top--------
#returns the argument object's unique integer identifier
s = "foobar"
print(id(s), "\n")
#-----topic------------id()-----------------------------------------------------------bottom--------


#-----topic------------len()-------------------------------------------------------------top--------
#returns the length of the argument passed to it
a = ['foo', 'bar', 'baz', 'qux']
print(len(a), "\n") #prints 4
#-----topic------------len()----------------------------------------------------------bottom--------



#-----topic------------map()-------------------------------------------------------------top--------
#from a list of numbers [1, 2, 3, 4, 5] another list of their squares can be produced
#the map object from the map() function is an iterator that can be fed to a lambda function to 
# calculate the squares, and finally these squares are made into a list  
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares, "\n")
#A BETTER PRACTICE might be to use list comprehensions, instead of lambda functions
cubes = [x**3 for x in numbers]
print(cubes, "\n")
#-----topic------------map()----------------------------------------------------------bottom--------

#-----topic------------filter()----------------------------------------------------------top--------
#-----topic------------filter()-------------------------------------------------------bottom--------

#-----topic------------filter()----------------------------------------------------------top--------
#-----topic------------filter()-------------------------------------------------------bottom--------





















