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
    'Python built-in functions' (with example code) 
    https://www.programiz.com/python-programming/methods/built-in
reference2:
    "Built-in functions" https://docs.python.org/3/library/functions.html
further reading/links: 
github: piettoon_koud > master 
dependencies:
DONE:
    math functions (7):
        abs()
        divmod()
        max()
        min()
        pow()
        round()     round(-15.5555, 2) #prints -15.56 (i.e. 2 digits after the decimal points)
        sum()
    type conversion functions (13):
        ascii()
        bin()
        bool()
        chr()       chr(68) #prints 'D'
        complex()
        float()     float('75.43') #prints 75.43
        hex()
        int()       int(-15.8) #truncates to -15
                    int('5') #prints 5
        oct()
        ord()       ord('D') #prints 68
        repr()
        str()
        type()
TO DO:
    iterable and iterator functions (13):
        all()
        any()
        enumerate()
        filter()
        iter()
        len()   len("Peter") #prints 5
        map()
        next()
        range()
        reversed()
        slice()
        sorted()
        zip()

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


#-----topic------------formatted output--------------------------------------------------top--------
print("N1:{0:>10}|N2:{1:^10}|N3:{2:<10}|${3:.2f}".format(N1,Q,N,Price))

#-----topic------------formatted output-----------------------------------------------bottom--------


















