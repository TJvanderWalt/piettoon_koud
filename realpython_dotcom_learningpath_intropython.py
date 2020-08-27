"""title: Introduction to Python (learning path on realpython.com)
topics:
    Python3 development set-up;
    basic python data types
        integers,
        floating-point numbers,
        complex numbers,
        strings (escape sequences, raw strings, triple quoted
        strings),
        boolean type (True/False/"truthiness");
    built-in functions ()
reference1:
    'Introduction to Python' learning path in realpython.com
reference2:
    'Python built-in functions' (with example code) 
    https://www.programiz.com/python-programming/methods/built-in
so what?
    To learn python syntax; basics
further reading/links: 
    Python3 cheat sheet; 
github:
    github>piettoon_koud>functions_built_in.py
dependencies:
    Pythyon 3 set up on Windows
DONE:
    math functions (7):
        abs()
        divmod()
        max()
        min()
        pow()
        round()
        sum()
    type conversion functions (13):
        ascii()
        bin()
        bool()
        chr()
        complex()
        float()
        hex()
        int()
        oct()
        ord()
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
        len()
        map()
        next()
        range()
        reversed()
        slice()
        sorted()
        zip()

"""

#-----topic------------basic python data types----------------------------------------top-----------

print("Basic data types: Integers")
print(10)    #base 10 (by default); no limit on its maximum length
print(0b10 ) #base 2 (binary)
print(0o10)  #base 8 (octal)
print(0x10)  #base 16 (hexadecimal)
my_int_var = int()
print(type(my_int_var))
my_int_var = int(input("Please enter an integer: "))
print(10*my_int_var)
print("")

print("Basic data types: Floating-point numbers")
print(4.2)   #floating-point number
print(type(4.2))
print(.2)
print(4.)
print(.4e7)  #scientific notation; use 'e' or 'E'
print(1.8e308) #infinite (largest float number is 1.79e308)
print(1e-325)  #smallest number near zero 5e-324
my_float_var = float()
print(type(my_float_var))
print("")

print("Basic data types: Complex numbers")
print(2+3j) #complex number
print(type(2+3j))
print("")

print("Basic data types: Strings")
print("hello, world!")
print('bye world!')
print("")   #empty string
#pair of double quotes or pair of single quotes can be used for a string literal
print('He wrote: "Hello world" on his computer') 
#single quote(s) allowed within double quotes, and vice versa
print("\n") 
#instead of printing \n these combination of characters get the special meaning of new-line
print('a\nb\nc') # \n newline characters causes this to print over several lines
print('a\
    b\
    c')          # \ ignores ENTER (i.e. code can be written over several lines)
print('a\n\
b\n\
    c')
print("c:\\users\\student") #escape \ with double \\
print("hello \tworld")      #tab character
#print('\a')                #sounds a bell (audible)
print('\141')               #character with octal value 141
print('\x61')               #character with hex value 61
print('a\141\x61')          #prints aaa
print('\u2192 \N{rightwards arrow}') 
#unicode 16-bit hex value and character from Unicode database with given name
print("")
print("""foo'bar""")        #single and/or double quote(s) allowed within triple quotes
print("foo'bar")            #single quote allowed within double quotes, and vice versa
print('foo\'bar')           #escape the special meaning of the single quote in the middle
print(r'This   poetry on c:\users')
#raw string ignores special meaning of \ and simply prints it
print("""within triple quotes
you can print single and double quotes,
and even print over several lines
without the need to prepend '\' first""") #escape sequences still work in triple quotes

#some of the sixty-eight built-in functions of Python 3.6+
print("")
print("math functions")
a_list = [100, 102, 0.5]
b_tuple = ()
print("abs(-3.4) =", abs(-3.4))     #absolute value (or magnitude for a complex number)
print("divmod(19,3) =", divmod(19, 3)) 
#returns a tuple (quotient, remainder) of integer/float division
print("alternative to divmod(19,3) is (19//3, 19%3) =", (19//3, 19%3)) 
#alternative to divmod for int division
print("")
print("max() function")
print("")
print(max([1, 2, 340, 4, 25] + a_list, key=lambda x: pow(x, -1))) 
#Returns largest of given arguments or items in an iterable(s) 
# iterables are passed to the key = function and comparison is based on its return values
print(min((56, 3, 34))) 
#smallest of given arguments or items in an iterable
print(min(b_tuple), default=100)
#default = value if iterable is empty
print(pow(-3, 3))
print((-3)**3)           #alternative to pow()
print(round(23.456, 2)) 
#round floating-point number to specified number of digits behind decimal point
print(sum([1, 2, 3, 4])) #sums ite→ms of an iterable
print('')

print('type conversion functions')
print("Take two steps \u2192 and one step \N{leftwards arrow}")
print(ord('\u2192')) #returns integer representation of a character (left arrow)
print(ord('\N{leftwards arrow}')) #returns integer representation of right arrow character
print(chr(8594),chr(8592)) #returns string of character given by (unicode) integer argument
print(ascii("Take two steps " + chr(8594) + " and one step " + chr(8592)))
#returns a printable string representation of an object (non-printable characters escaped by \)
print(bin(1234)) #converts integer to a binary string
print(bool(3==3)) #converts an argument to a Boolen value
print(complex(2,3)) #complex number constructed from arguments
print(float("123")) #float number constructed from a string integer number
print(float(123)) #float number constructed from an integer
print(int("123")) #integer number from a string
print(int(123.5)) #integer from a number

#-----topic------------basic python data types-------------------------------------bottom-----------



#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------
