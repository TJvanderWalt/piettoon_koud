"""title: python lists and strings and arrays
topics: 
    basic construction of a list or string; 
    string character conversion methods;

    list comprehensions;
    creation of 1D and 2D arrays/lists and shallow lists;
    check for an empty list; 
    indexing and reverse indexing; 
    slicing;
    append/insert items;
    iteration;
    sorting;
    reverse lists;
    check element's presence (membership);
    update items;
    delete items;
    copy lists;
    count specific items (finding the most common item in a list);
    checking for uniqueness;
    concatenate lists;
    randomize the items;
    get a random item;
    find an item's index;
    check relationships between lists;
    hashability;
    filtering lists with the Filter() function or with list comprehensions;
    modifying lists with the Map() function or with list comprehensions;
    combining lists with the Zip() function;
    flatten a list of lists;
    built-in functions applied to lists max() min() len() sum()
reference1: 
    "8 Advanced python list techniques you should know"
    Nik Piepenbreier in: Towards Data Science (Medium.com)
reference2:
    "20 Things to know to master lists in python"
    Yong Cui in: Better Programming (Medium.com)
reference3:
    "Using 2D arrays/lists the right way"
    https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
reference4: 
    "A complete walk-through in Python for beginners"
    Felix Antony in: Towards Data Science (Medium.com)
so what? 
    better understand the most common ordered collection data type in python; 
    lists can store any types (integers, floats, strings, custom class instances) as their elements
    (and even a mixture of all of them); 
    lists are mutable (we can add, change, remove items from lists);
    lists correspond to array-data types in other languages
further reading/links: 
    (piettoon_koud > master) list_comprehensions.py; functions_lambda.py; library_itertools.py;
github: 
    piettoon_koud > master 
dependencies:
    none
DONE:

TO DO:

"""


#-----topic------------basic construction of a list or string-------------------------top-----------
#remove the next two '''
'''
my_string = 'Quote of the day' #can also use double/triple quotes
print(my_string, '\n')
string_over_several_lines = '''A string
over
three lines'''
print(string_over_several_lines, "\n")
empty_list = []  #create an empty list
integer_list = [2, 3, 5]
number_list = list((2, 3.2, 1.5)) #list created from a tuple
integer_list = list(range(10)) #list created from a range
letter_list = list('hello') #list created from a string
print(empty_list, number_list, integer_list, letter_list)
'''
#-----topic------------basic construction of a list or string----------------------bottom-----------


#-----topic------------string methods-------------------------------------------------top-----------
#remove next two '''
'''
#CHARACTER CONVERSION METHODS-----------------------------------------------------------------------
string = "i love python"
print(string.capitalize()) #converts first letter of string to upper case

string = "hApPy CoDinG"
print(string.casefold()) #converts all uppercase characters to lower case

string="hAPPY cODING"
print(string.swapcase()) #convert uppercase to lower case and lower case to uppercase

string="Hello Python"
print(string.upper()) #capitalize all characters in a string
print(string.lower()) #converts entire string into lowercase letters

string="hello python"
print(string.title()) #converts first character of all words in string

#TYPE CHECKING METHODS------------------------------------------------------------------------------------
string = "hello"
print(string.isalpha()) #True

string = "1234'
print(string.isnumeric()) #True

string = "str123"
print(string.isalnum()) #True

string1 = "HELLO"
string2 = "python"
print(string1.isupper()) #True
print(string2.islower()) #True

string1 = "var_3"
string2 = "2var"
print(string1.isidentifier()) #True since it meets the rules of valid identifier names
print(string2.isidentifier()) #False since identifier names may not start with numbers

string = "   "
print(string.isspace()) #True since all characters are white spaces

string = "Hello Python"
string.istitle()) #True

#SUB-STRING METHODS----------------------------------------------------------------------------------------
string="I am learning Python"
print(string.count("a")) #outputs 2

string="Happy Coding"
print(string.startswith("Hap") #True

string = "Happy COding"
print(string.endswith("ing")) #True

string="I love Python" 
#index() and find() return the index of the first occurrence of substring in string
print(string.index("o")) #outputs 3; creates an exception if substring not found in string
print(string.find("o")) #outputs 3; outputs -1 if substring not found in string
#rindex() and rfind() return the index of the last occurrence of a substring in string
print(string.rindex("o")) #outputs 11
print(string.rfind("o")) #outputs 11

string="I love Java"
print(string.replace("Java","Python")) #I love Python

#ALIGNMENT METHODS----------------------------------------------------------------------
string="python"
print(string.center(20)) #centered within the width passed
print(string.ljust(20)) #justify to the left end of the given width
print(string.rjust(20)) #justify to the right end of the given width

string="Python \tProgramming"
print(string) #tab will have the default length
print(string.expandtabs(5)) #customize the length of tabs in a string



'''
#-----topic------------string methods----------------------------------------------bottom-----------


#-----topic------------list comprehensions--------------------------------------------top-----------
# syntax is  [expression for x in iterable]
# see list_comprehensions.py for further details
#remove the next two '''
'''
letter_dict = {'a': 0, 'B': 1, 'c': 2, 'd': 3} #dictionary of key:value pairs
squares_list = [x*x for x in letter_dict.values()]
keys_list = [x.lower() for x in letter_dict.keys()]
list_of_lists = [list(x) for x in letter_dict.items()]
print('\n', squares_list, keys_list, list_of_lists)
'''
#-----topic------------list comprehensions-----------------------------------------bottom-----------


#-----topic------------creation of 1D and 2D arrays/lists and shallow lists-----------top-----------
#remove the next two '''

#creating a 1D array of size N and initialize it with 0's by method1: using * operator
N = 5
my1Darr = [0]*N  
print("\nmy1Darray: ", my1Darr) #output [0, 0, 0, 0, 0]

#creating a 1D array of size N and initialize it with 0's by method2: list comprehensions
N = 5
arr1D = [0 for i in range(N)] 
print("1D array: ", arr1D)      #output [0, 0, 0, 0, 0]

#creating a 1D array of size N and store values entered by the user: method3 - looping
N = int(input("How many elements in this 1D array? "))
arr1D = []
for i in range(N):
    arr1D.append(int(input("Please enter a number: "))) 
print(arr1D)

#creating a 2D array of size 3x5 and initialize it with 0's by method1: using * operator
rows, columns = (3,5)
my2Darr = [[0]*columns]*rows #output [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
print("my2Darray: ", my2Darr)
#change the first element of the first row to 1 and print the array
my2Darr[0][0] = 1
print("array when changing element my2Darr[0][0] = 1:\n")
for row in my2Darr:
    print(row)
print("Not what we expected! See explanation in reference3\n")

#creating a 2D array of size 3x5 and initialize it with 0's by method2: list comprehensions
rows, cols = (3, 5)
arr2D = [[0 for i in range(cols)] for j in range(rows)]
print("arr2D: " + str(arr2D))
#change the first element of the first row to 1 and print the array
arr2D[0][0] = 1
print("array when changing element arr2D[0][0] = 1:\n")
for row in arr2D:
    print(row)
print("Now it is what we expected! See explanation in reference3\n")

#creating a 2D array of size 3x5 and initialize it with 0's by method3: looping
rows, cols = (3,5)
arr = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    arr.append(row)
print("array of size 3x5:", arr)
#change the first element of the first row to 1 and print the array
arr[0][0] = 1
print("array when changing element arr[0][0] = 1:\n")
for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end=" ")
    print("\r")
print("Again what we expected! See explanation in reference3\n")

#creating a 2D array of size 3x5 and initialize it with 0's by method3: looping another way
rows, cols = (3,5)
myArr = []
row = []
for i in range(cols):
    row.append(0)
for j in range(rows):
        myArr.append(row)
print("array of size 3x5:", myArr)
#change the first element of the first row to 1 and print the array
myArr[0][0] = 1
print("array when changing element myArr[0][0] = 1:\n")
for row in myArr:
    print(row)
print("Again not what we expected! See explanation in reference3\n")

#Storing user input data in a 2D array of size MxN: use of the looping method
#use pprint to print
import pprint as pp
matrix=[]
M = int(input("Enter number of rows: "))
N = int(input("Enter number of columns: "))
for i in range(M):
    data = input(f"Please enter {N} values separated by spaces: ")
    data_list = data.split() #produces a list of strings
    data_list = [int(i) for i in data_list] #produces a list of integers
    matrix.append(data_list)
print("2D array of size MxN and populated with data: ", matrix, "\n")
pretty_object = pp.PrettyPrinter(1,30)
pretty_object.pprint(matrix)
#now to transpose this array/matrix (i.e. every element [i][j] in matrix becomes the element [j][i]
# in matrix_transposed and the original NxM matrix becomes a MxN matrix) we cannot use a loop
# and use matrix[j][i] = matrix[i][j] since non-square matrix will produce index errors
matrix_transposed=[list(i) for i in zip(*matrix)]
print("Transposed matrix: ", matrix_transposed)
#-----topic------------creation of 1D and 2D arrays/lists abd shallow lists--------bottom-----------


#-----topic------------check for an empty list----------------------------------------top-----------
#remove the next two '''
'''
# in python, empty lists are falsy when explicitly evaluated by bool()
# >>>bool(empty_list) == False
# >>>True
#empty lists can also be implicitly evaluated by if
#this is the PREFERRED METHOD to check for emptiness
if not empty_list:
    print("\nList is empty")
#alternatively check the length of the list
not_empty_list = [2, 3, 4]
if len(not_empty_list) > 0:
    print("\nThe list is not empty, based on its len() check")
#alternatively compare tone list with []
if not_empty_list != []:
    print("\nList is not equal to an empty list []")    
'''
#-----topic------------check for an empty list-------------------------------------bottom-----------

#-----topic------------indexing and reverse indexing----------------------------------top-----------
#remove the next two '''
number_list = [11, 12, 13, 14, 15, 16, 17]  
# from left-to-right the indices run from 0 to 6
# from right-to-left the indices run from -1 to -7
third_element = number_list[2]
sixth_element = number_list[5]  #alternatively it is the second element from the right
second_last_element = number_list[-2]
print("\n" + str(third_element) +" " + str(sixth_element == second_last_element))
'''
#-----topic------------indexing and reverse indexing-------------------------------bottom-----------

#-----topic------------slicing--------------------------------------------------------top-----------
#remove the next two '''
'''
long_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
long_list[:5] #first five elements (end index is not included)
long_list[:] #all elements (beginning to end, both included)
long_list[5:] #elements six to the end (start index included, end element included)
long_list[5:9] #elements six to nine (start index included, end index not included)
long_list[::3] #start element included, and thereafter every third element
long_list[3:-2] #start index included (element four), end index (second last element) not included
long_list[::-1] #full list, in reverse order 
'''
#-----topic------------slicing-----------------------------------------------------bottom-----------

#-----topic------------append/insert items--------------------------------------------top-----------
beginning_list = [13, 15, 17, 19, 21, 23]
beginning_list.insert(3, 11) #inline insert (returns None)
#in old list, element 19 at index 3 moves to the right to make place for new element 11
#inline insert --> new_list = beginning_list.insert(3, 11) will assign None to new_list
print("\n" + str(beginning_list))
beginning_list.append(25) #add element 25 at the end; inline (returns None)
print("\n" + str(beginning_list))
beginning_list.extend(range(4)) 
#add each element of an iterable (0, 1, 2, 3) at the end; inline (returns None)
first_list = [1, 2, 3]
second_list = ['one', 'two', 'three']
first_list.extend(second_list) 
#first list extended with each element of an iterable (i.e. second list); inline (returns None)
#-----topic------------append/insert items-----------------------------------------bottom-----------

#-----topic------------iteration------------------------------------------------------top-----------
#-----topic------------iteration---------------------------------------------------bottom-----------

#-----topic------------sorting--------------------------------------------------------top-----------
#-----topic------------sorting-----------------------------------------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------

#-----topic------------regular functions (with default arguments)---------------------top-----------
#-----topic------------regular functions (with default arguments)------------------bottom-----------
'''